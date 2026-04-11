#!/usr/bin/env python3
"""逐篇抓取 arXiv abs 页中的 v1 提交日期。"""

from __future__ import annotations

import argparse
import csv
import re
import time
import urllib.request
from datetime import datetime
from pathlib import Path


SUBMISSION_PATTERN = re.compile(
    r"\[v1\].*?(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),\s+(\d{1,2}\s+\w+\s+\d{4})",
    re.S,
)


def fetch_html(arxiv_id: str) -> str:
    request = urllib.request.Request(
        f"https://arxiv.org/abs/{arxiv_id}",
        headers={"User-Agent": "fhx-nips-2026/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="ignore")


def parse_date(html: str) -> str:
    match = SUBMISSION_PATTERN.search(html)
    if not match:
        raise ValueError("v1 submission date not found")
    raw_date = match.group(1)
    return datetime.strptime(raw_date, "%d %b %Y").strftime("%Y-%m-%d")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--sleep", type=float, default=1.5)
    args = parser.parse_args()

    rows = list(csv.DictReader(args.input_csv.open("r", encoding="utf-8")))
    output_rows = []
    for row in rows:
        arxiv_id = row["arxiv_id"].strip()
        if not arxiv_id:
            row["abs_date"] = ""
            row["abs_status"] = "missing_id"
            output_rows.append(row)
            continue

        html = fetch_html(arxiv_id)
        row["abs_date"] = parse_date(html)
        row["abs_status"] = "ok"
        output_rows.append(row)
        time.sleep(args.sleep)

    with args.output.open("w", encoding="utf-8", newline="") as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=output_rows[0].keys())
        writer.writeheader()
        writer.writerows(output_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
