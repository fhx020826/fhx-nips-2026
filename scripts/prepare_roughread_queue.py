#!/usr/bin/env python3
"""
从论文列表 markdown 中抽取顺序粗读队列，并可输出单篇 scaffold。

用途：
1. 统一从“完整论文列表”中抽取顺序队列，避免后续人工复制标题。
2. 支持按 index / batch 取出待粗读论文，便于后续批量并行推进。
3. 为后续“事实层抓取 -> 模板填充”流水线提供稳定输入。
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


LINE_RE = re.compile(
    r"^\s*(\d+)\.\s+(.*?)\s+\|\s+(\d{4}-\d{2}-\d{2})\s+\|\s+(https?://\S+)\s*$"
)


def parse_entries(path: Path) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        match = LINE_RE.match(line)
        if not match:
            continue
        rank, title, date, url = match.groups()
        entries.append(
            {
                "rank": int(rank),
                "title": title.strip(),
                "date": date,
                "url": url,
            }
        )
    return entries


def make_short_name(title: str) -> str:
    head = title.split(":")[0].strip()
    return head.replace("$", "")


def render_scaffold(entry: dict[str, Any]) -> str:
    short_name = make_short_name(entry["title"])
    return f"""## {short_name}

### 1）基本信息

**标题**
{entry["title"]}

**任务身份**
{{待填写}}

**arXiv v1 日期**
{entry["date"]}

**录用情况**
{{待填写}}

**作者 / 机构**
{{待填写}}

**项目 / 代码 / 模型 / 数据**
- 项目页：
- 代码：
- 模型：
- 数据：

**引用情况**
{{待填写，可选}}

**证据来源**
- paper: {entry["url"]}
- arXiv:
- project:
- code:
- venue / OpenReview / publisher:
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        default="/home/hxfeng/fhx-nips-2026/docs/paper_list_feishu_strict.md",
        help="输入 markdown 列表文件",
    )
    parser.add_argument("--index", type=int, default=None, help="输出第几篇（1-based）")
    parser.add_argument("--batch-size", type=int, default=1, help="输出连续多少篇")
    parser.add_argument(
        "--format",
        choices=["json", "jsonl", "md"],
        default="json",
        help="输出格式",
    )
    args = parser.parse_args()

    path = Path(args.input)
    entries = parse_entries(path)
    if args.index is not None:
        start = max(args.index - 1, 0)
        end = start + max(args.batch_size, 1)
        entries = entries[start:end]

    if args.format == "json":
        print(json.dumps(entries, ensure_ascii=False, indent=2))
        return

    if args.format == "jsonl":
        for entry in entries:
            print(json.dumps(entry, ensure_ascii=False))
        return

    for idx, entry in enumerate(entries):
        if idx:
            print("\n---\n")
        print(render_scaffold(entry))


if __name__ == "__main__":
    main()
