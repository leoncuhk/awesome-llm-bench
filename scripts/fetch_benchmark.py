#!/usr/bin/env python3
"""Fetch a benchlm.ai benchmark page and extract Top 10 leaderboard entries.

Usage:
    python fetch_benchmark.py --slug sweVerified
    python fetch_benchmark.py --all     # iterate scripts/benchmarks.yaml

Writes data/<slug>.json with structure:
    {
      "slug": "sweVerified",
      "display": "SWE-bench Verified",
      "category": "Coding",
      "source_url": "https://benchlm.ai/benchmarks/sweVerified",
      "fetched_at": "2026-04-29T10:00:00Z",
      "updated_at": "2026-04-28",
      "total_models": 43,
      "top10": [
        {"rank": 1, "model": "Claude Mythos Preview",
         "provider": "Anthropic", "license": "Closed",
         "score": 93.9, "model_url": "/models/claude-mythos-preview"},
        ...
      ]
    }
"""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
CONFIG = ROOT / "scripts" / "benchmarks.yaml"

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/131.0.0.0 Safari/537.36")


def load_config() -> list[dict]:
    text = CONFIG.read_text(encoding="utf-8")
    items: list[dict] = []
    cur: dict | None = None
    for line in text.splitlines():
        s = line.rstrip()
        if not s or s.lstrip().startswith("#"):
            continue
        if s.startswith("benchmarks:"):
            continue
        if s.startswith("  - "):
            if cur:
                items.append(cur)
            cur = {}
            key, _, val = s[4:].partition(": ")
            cur[key.strip()] = val.strip()
        elif s.startswith("    ") and cur is not None:
            key, _, val = s.strip().partition(": ")
            cur[key.strip()] = val.strip()
    if cur:
        items.append(cur)
    return items


def fetch_html(url: str, timeout: int = 20) -> str:
    headers = {
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml",
        "Accept-Language": "en-US,en;q=0.9",
    }
    req = Request(url, headers=headers)
    ctx = ssl.create_default_context()
    with urlopen(req, timeout=timeout, context=ctx) as resp:
        raw = resp.read()
        if resp.headers.get("Content-Encoding") == "gzip":
            import gzip
            raw = gzip.decompress(raw)
        charset = resp.headers.get_content_charset() or "utf-8"
        return raw.decode(charset, errors="replace")


def html_to_markdown(html_raw: str) -> str:
    """Convert HTML to plain Markdown using html2text (preserve links)."""
    import html2text
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0
    return h.handle(html_raw)


# Regex for the leaderboard rows in the rendered Markdown.
# Pattern looks like:
#     1
#     [Claude Mythos Preview](/models/claude-mythos-preview)
#     AnthropicClosed
#     93.9%
ENTRY_RE = re.compile(
    r"^(\d+)\s*\n+\s*\[([^\]]+)\]\(([^)]+)\)\s*\n+\s*"
    r"([A-Za-z][A-Za-z0-9 .&+\-/]*?)(Closed|Open)\s*\n+\s*"
    r"(\d+(?:\.\d+)?)\s*%",
    re.MULTILINE,
)

# "Updated April 28, 2026" or "updated April 28, 2026"
UPDATED_RE = re.compile(r"[Uu]pdated\s+([A-Z][a-z]+\s+\d{1,2},\s+\d{4})")
# "Leaderboard (43 models)" or "43 models"
COUNT_RE = re.compile(r"(\d+)\s+models")


def parse_top10(md: str) -> tuple[list[dict], str | None, int | None]:
    entries: list[dict] = []
    seen_ranks: set[int] = set()
    for m in ENTRY_RE.finditer(md):
        rank = int(m.group(1))
        if rank in seen_ranks:
            continue
        seen_ranks.add(rank)
        provider = m.group(4).strip()
        entries.append({
            "rank": rank,
            "model": m.group(2).strip(),
            "model_url": m.group(3).strip(),
            "provider": provider,
            "license": m.group(5).strip(),
            "score": float(m.group(6)),
        })
        if rank >= 10:
            break
    entries.sort(key=lambda e: e["rank"])
    top10 = entries[:10]

    upd = UPDATED_RE.search(md)
    updated_at = None
    if upd:
        try:
            d = datetime.strptime(upd.group(1), "%B %d, %Y")
            updated_at = d.strftime("%Y-%m-%d")
        except ValueError:
            updated_at = upd.group(1)

    cnt = COUNT_RE.search(md)
    total = int(cnt.group(1)) if cnt else None

    return top10, updated_at, total


def fetch_one(item: dict) -> dict:
    slug = item["slug"]
    url = f"https://benchlm.ai/benchmarks/{slug}"
    html_raw = fetch_html(url)
    md = html_to_markdown(html_raw)
    top10, updated_at, total = parse_top10(md)
    if not top10:
        raise RuntimeError(f"Could not parse leaderboard from {url}")
    return {
        "slug": slug,
        "display": item.get("display", slug),
        "zh": item.get("zh", ""),
        "category": item.get("category", ""),
        "blurb": item.get("blurb", ""),
        "blurb_zh": item.get("blurb_zh", ""),
        "source_url": url,
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "updated_at": updated_at,
        "total_models": total,
        "top10": top10,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", help="single slug to fetch")
    ap.add_argument("--all", action="store_true", help="fetch all in benchmarks.yaml")
    ap.add_argument("--sleep", type=float, default=1.5,
                    help="seconds between requests when --all")
    args = ap.parse_args()

    DATA_DIR.mkdir(exist_ok=True)
    items = load_config()

    if args.slug:
        items = [i for i in items if i["slug"] == args.slug]
        if not items:
            print(f"Unknown slug: {args.slug}", file=sys.stderr)
            return 1
    elif not args.all:
        ap.print_help()
        return 1

    failures: list[str] = []
    for i, item in enumerate(items):
        slug = item["slug"]
        try:
            result = fetch_one(item)
            out = DATA_DIR / f"{slug}.json"
            out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                           encoding="utf-8")
            n = len(result["top10"])
            print(f"[OK] {slug}: top {n}, updated {result['updated_at']}")
        except Exception as exc:
            print(f"[FAIL] {slug}: {exc}", file=sys.stderr)
            failures.append(slug)
        if args.all and i < len(items) - 1:
            time.sleep(args.sleep)

    return 0 if not failures else 2


if __name__ == "__main__":
    raise SystemExit(main())
