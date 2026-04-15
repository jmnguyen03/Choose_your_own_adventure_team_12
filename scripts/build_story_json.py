#!/usr/bin/env python3
"""Build a single JSON story map from page text files and Mermaid graph."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

EDGE_RE = re.compile(r"\bP(\d+)\s*-->\s*P(\d+)\b")
NODE_RE = re.compile(r"^\s*P(\d+)\s*\[")
PAGE_FILE_RE = re.compile(r"^(\d+)-CoT\.txt$")
PAGE_HEADER_RE = re.compile(r"^\s*Page\s+\d+\s*$", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build output/story.json from OCR pages and Mermaid graph.")
    parser.add_argument(
        "--pages-dir",
        type=Path,
        default=Path("output/cot-pages-ocr-v2"),
        help="Directory containing page text files.",
    )
    parser.add_argument(
        "--graph",
        type=Path,
        default=Path("output/cot-story-graph.mmd"),
        help="Mermaid graph file.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output/story.json"),
        help="Output JSON file path.",
    )
    parser.add_argument(
        "--start-page",
        type=int,
        default=2,
        help="Expected story start page (default: 2).",
    )
    return parser.parse_args()


def parse_graph(graph_path: Path) -> tuple[set[int], dict[int, list[int]]]:
    nodes: set[int] = set()
    edges: dict[int, list[int]] = {}

    for raw_line in graph_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        node_match = NODE_RE.match(line)
        if node_match:
            nodes.add(int(node_match.group(1)))

        edge_match = EDGE_RE.search(line)
        if not edge_match:
            continue

        src = int(edge_match.group(1))
        dst = int(edge_match.group(2))
        nodes.add(src)
        nodes.add(dst)
        edges.setdefault(src, [])
        if dst not in edges[src]:
            edges[src].append(dst)

    for node in nodes:
        edges.setdefault(node, [])

    return nodes, edges


def clean_page_text(text: str) -> str:
    lines = text.splitlines()
    if lines and PAGE_HEADER_RE.match(lines[0]):
        lines = lines[1:]
        if lines and not lines[0].strip():
            lines = lines[1:]
    return "\n".join(lines).strip()


def parse_page_texts(pages_dir: Path) -> dict[int, str]:
    page_texts: dict[int, str] = {}

    for path in sorted(pages_dir.glob("*-CoT.txt")):
        match = PAGE_FILE_RE.match(path.name)
        if not match:
            continue
        page_num = int(match.group(1))
        raw_text = path.read_text(encoding="utf-8")
        page_texts[page_num] = clean_page_text(raw_text)

    return page_texts


def build_story_map(
    page_texts: dict[int, str], nodes: set[int], edges: dict[int, list[int]], start_page: int
) -> dict[str, dict[str, object]]:
    all_pages = sorted(nodes | set(page_texts.keys()))
    if start_page not in all_pages:
        raise RuntimeError(f"Start page {start_page} is missing from graph and page files.")

    story: dict[str, dict[str, object]] = {}

    for page in all_pages:
        choices = [
            {"text": f"Turn to page {dst}", "page": str(dst)}
            for dst in edges.get(page, [])
        ]
        story[str(page)] = {
            "text": page_texts.get(page, ""),
            "choices": choices,
        }

    return story


def main() -> None:
    args = parse_args()

    if not args.pages_dir.exists():
        raise FileNotFoundError(f"Pages directory not found: {args.pages_dir}")
    if not args.graph.exists():
        raise FileNotFoundError(f"Graph file not found: {args.graph}")

    page_texts = parse_page_texts(args.pages_dir)
    nodes, edges = parse_graph(args.graph)
    story = build_story_map(page_texts, nodes, edges, args.start_page)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(story, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Pages loaded: {len(page_texts)}")
    print(f"Graph nodes: {len(nodes)}")
    print(f"Start page: {args.start_page}")
    print(f"Wrote: {args.output}")


if __name__ == "__main__":
    main()
