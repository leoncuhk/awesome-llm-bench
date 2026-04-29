#!/usr/bin/env python3
"""Render leaderboard tables from data/*.json into README.md and README.zh-CN.md.

Markers in the README files:
    <!-- AUTO:START slug=sweVerified lang=en -->
    ...auto-generated content...
    <!-- AUTO:END slug=sweVerified -->

The script also updates a global "Last sync" line:
    <!-- LAST_SYNC -->Last sync: 2026-04-29 (UTC)<!-- /LAST_SYNC -->
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
README_EN = ROOT / "README.md"
README_ZH = ROOT / "README.zh-CN.md"


def load_all() -> list[dict]:
    items = []
    for p in sorted(DATA_DIR.glob("*.json")):
        with p.open(encoding="utf-8") as f:
            items.append(json.load(f))
    return items


def render_table(data: dict, lang: str) -> str:
    head_en = "| Rank | Model | Provider | License | Score |\n| :-: | :-- | :-- | :-: | --: |"
    head_zh = "| 排名 | 模型 | 提供商 | 开闭源 | 分数 |\n| :-: | :-- | :-- | :-: | --: |"
    head = head_en if lang == "en" else head_zh
    rows: list[str] = []
    for e in data["top10"]:
        url = e["model_url"]
        if url.startswith("/"):
            url = "https://benchlm.ai" + url
        model_link = f"[{e['model']}]({url})"
        score = f"{e['score']:.1f}%"
        rows.append(
            f"| {e['rank']} | {model_link} | {e['provider']} | "
            f"{e['license']} | {score} |"
        )
    table = head + "\n" + "\n".join(rows)

    updated = data.get("updated_at") or "unknown"
    total = data.get("total_models") or "?"
    src = data["source_url"]
    if lang == "en":
        meta = (f"\n\n*Source: [{src}]({src}) · "
                f"Updated {updated} · Total models: {total}*")
    else:
        meta = (f"\n\n*来源: [{src}]({src}) · "
                f"更新于 {updated} · 共 {total} 个模型*")
    return table + meta


def make_block(slug: str, lang: str, body: str) -> str:
    start = f"<!-- AUTO:START slug={slug} lang={lang} -->"
    end = f"<!-- AUTO:END slug={slug} -->"
    return f"{start}\n{body}\n{end}"


def replace_block(text: str, slug: str, lang: str, body: str) -> str:
    pat = re.compile(
        rf"<!-- AUTO:START slug={re.escape(slug)} lang={lang} -->.*?"
        rf"<!-- AUTO:END slug={re.escape(slug)} -->",
        re.DOTALL,
    )
    new_block = make_block(slug, lang, body)
    if pat.search(text):
        return pat.sub(new_block, text)
    print(f"[warn] no marker for slug={slug} lang={lang} in README", file=sys.stderr)
    return text


def update_last_sync(text: str, lang: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if lang == "en":
        body = f"Last sync: **{now}** (UTC, daily auto-update)"
    else:
        body = f"最近同步: **{now}** (UTC,每日自动更新)"
    pat = re.compile(r"<!-- LAST_SYNC -->.*?<!-- /LAST_SYNC -->", re.DOTALL)
    new = f"<!-- LAST_SYNC -->{body}<!-- /LAST_SYNC -->"
    if pat.search(text):
        return pat.sub(new, text)
    return text


def render(readme: Path, lang: str, items: list[dict]) -> bool:
    if not readme.exists():
        print(f"[warn] {readme} does not exist; skipping {lang}", file=sys.stderr)
        return False
    text = readme.read_text(encoding="utf-8")
    original = text
    for data in items:
        body = render_table(data, lang)
        text = replace_block(text, data["slug"], lang, body)
    text = update_last_sync(text, lang)
    if text != original:
        readme.write_text(text, encoding="utf-8")
        print(f"[OK] updated {readme.name}")
        return True
    print(f"[skip] {readme.name} unchanged")
    return False


def main() -> int:
    items = load_all()
    if not items:
        print("No data/*.json found. Run fetch_benchmark.py --all first.",
              file=sys.stderr)
        return 1
    render(README_EN, "en", items)
    render(README_ZH, "zh", items)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
