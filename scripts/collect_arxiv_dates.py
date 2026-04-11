#!/usr/bin/env python3
"""从论文列表 markdown 中提取条目，并批量查询 arXiv 首发日期。"""

from __future__ import annotations

import argparse
import csv
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


ARXIV_API = "https://export.arxiv.org/api/query"
ENTRY_PATTERN = re.compile(
    r"^(\d+)\.\s+(\d{4}-\d{2}(?:-\d{2})?)\s+\|\s+(.*?)\s+\|\s+(\d{4}-\d{2}(?:-\d{2})?)\s+\|\s+(https?://\S+)$"
)
ARXIV_ID_PATTERN = re.compile(r"([0-9]{4}\.[0-9]{4,5})(?:v\d+)?")


@dataclass(frozen=True)
class PaperEntry:
    index: int
    title: str
    recorded_date: str
    url: str
    arxiv_id: str | None


def parse_entries(path: Path) -> list[PaperEntry]:
    entries: list[PaperEntry] = []
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        match = ENTRY_PATTERN.match(raw_line.strip())
        if not match:
            continue
        index, _display_date, title, recorded_date, url = match.groups()
        arxiv_match = ARXIV_ID_PATTERN.search(url)
        entries.append(
            PaperEntry(
                index=int(index),
                title=title.strip(),
                recorded_date=recorded_date,
                url=url,
                arxiv_id=arxiv_match.group(1) if arxiv_match else None,
            )
        )
    return entries


def fetch_url(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "fhx-nips-2026/1.0"})
    delay_seconds = 1.0
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            if exc.code != 429 or attempt == 4:
                raise
            time.sleep(delay_seconds)
            delay_seconds *= 2
    raise RuntimeError("unreachable")


def fetch_arxiv_by_ids(arxiv_ids: list[str]) -> dict[str, str]:
    if not arxiv_ids:
        return {}
    query = urllib.parse.urlencode({"id_list": ",".join(arxiv_ids), "max_results": len(arxiv_ids)})
    xml_text = fetch_url(f"{ARXIV_API}?{query}")
    root = ET.fromstring(xml_text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    results: dict[str, str] = {}
    for entry in root.findall("atom:entry", ns):
        paper_id = entry.findtext("atom:id", default="", namespaces=ns).rsplit("/", 1)[-1]
        paper_id = paper_id.split("v", 1)[0]
        published = entry.findtext("atom:published", default="", namespaces=ns)
        if paper_id and published:
            results[paper_id] = published[:10]
    return results


def fetch_arxiv_by_title(title: str) -> tuple[str | None, str | None]:
    # 用标题检索时，先限制结果数，再做严格标题匹配，避免误配。
    query = urllib.parse.urlencode(
        {
            "search_query": f'ti:"{title}"',
            "start": 0,
            "max_results": 5,
        }
    )
    xml_text = fetch_url(f"{ARXIV_API}?{query}")
    root = ET.fromstring(xml_text)
    ns = {"atom": "http://www.w3.org/2005/Atom"}
    normalized_target = normalize_title(title)
    for entry in root.findall("atom:entry", ns):
        candidate_title = entry.findtext("atom:title", default="", namespaces=ns)
        candidate_id = entry.findtext("atom:id", default="", namespaces=ns).rsplit("/", 1)[-1]
        published = entry.findtext("atom:published", default="", namespaces=ns)
        if normalize_title(candidate_title) == normalized_target and published:
            return candidate_id.split("v", 1)[0], published[:10]
    return None, None


def normalize_title(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_markdown", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--skip-title-lookup", action="store_true")
    args = parser.parse_args()

    entries = parse_entries(args.input_markdown)
    arxiv_ids = sorted({entry.arxiv_id for entry in entries if entry.arxiv_id})

    resolved_dates: dict[str, str] = {}
    batch_size = 20
    for start in range(0, len(arxiv_ids), batch_size):
        batch = arxiv_ids[start : start + batch_size]
        resolved_dates.update(fetch_arxiv_by_ids(batch))
        time.sleep(0.5)

    rows: list[dict[str, str]] = []
    for entry in entries:
        resolved_id = entry.arxiv_id
        resolved_date = resolved_dates.get(entry.arxiv_id or "", "")
        status = "id_match" if resolved_date else "needs_title_lookup"
        if not resolved_date and not args.skip_title_lookup:
            lookup_id, lookup_date = fetch_arxiv_by_title(entry.title)
            if lookup_date:
                resolved_id = lookup_id
                resolved_date = lookup_date
                status = "title_match"
            else:
                status = "not_found"
            time.sleep(0.5)
        elif not resolved_date and args.skip_title_lookup:
            status = "not_found"

        rows.append(
            {
                "index": str(entry.index),
                "title": entry.title,
                "recorded_date": entry.recorded_date,
                "resolved_date": resolved_date,
                "arxiv_id": resolved_id or "",
                "url": entry.url,
                "status": status,
            }
        )

    with args.output.open("w", encoding="utf-8", newline="") as file_obj:
        writer = csv.DictWriter(
            file_obj,
            fieldnames=[
                "index",
                "title",
                "recorded_date",
                "resolved_date",
                "arxiv_id",
                "url",
                "status",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    unresolved = [row for row in rows if row["status"] == "not_found"]
    print(f"entries={len(rows)} unresolved={len(unresolved)}", file=sys.stderr)
    for row in unresolved:
        print(f"UNRESOLVED\t{row['title']}\t{row['url']}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
