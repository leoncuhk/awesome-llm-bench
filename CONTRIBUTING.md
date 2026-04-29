# Contributing

Thanks for your interest. This list stays useful only if it stays curated and honest. Contributions in three categories:

## 1. Add a benchmark

1. Find the benchmark on [benchlm.ai/benchmarks](https://benchlm.ai/benchmarks). Note the camelCase slug in the URL (e.g., `mmlu`, `aimE2025`).
2. Verify benchlm.ai has it as **`Current`** or **`Refreshing`** state — not `Display only`. Display-only benchmarks have incomplete public snapshots and will mislead readers.
3. Add an entry to `scripts/benchmarks.yaml`:
   ```yaml
   - slug: <camelCaseSlug>
     display: <Human-readable name>
     zh: <中文名>
     category: Agentic | Coding | Reasoning | Knowledge | Multimodal | Tool Use | Math
     blurb: One-line English description.
     blurb_zh: 一行中文描述。
   ```
4. Run `python scripts/fetch_benchmark.py --slug <camelCaseSlug>` to confirm the parser produces 10 entries. If it returns fewer, file an issue with the slug — likely a parser edge case.
5. Add the corresponding section in both `README.md` and `README.zh-CN.md` with the `<!-- AUTO:START slug=... lang=... -->` markers.
6. Run `python scripts/render_readme.py` to fill the table.

## 2. Update the AI coding tools landscape

Edit `tools/ai-coding-tools.md`. Bar is high — the tool must meet at least 3 of the [selection criteria](tools/ai-coding-tools.md#selection-criteria) listed in that file.

If you add a tool, include:
- The **one specific** thing it does well (not a generic "AI assistant for code")
- Verifiable update cadence (check the GitHub repo or changelog)
- Pricing model

## 3. Translation

For `README.zh-CN.md`, please match the structure of `README.md` exactly — same section order, same hierarchy. The auto-render script keeps the leaderboard tables in sync; the prose around them is hand-written.

## What we don't accept

- **Re-rankings or de-attribution.** This is a mirror of benchlm.ai with attribution. Don't PR a reordering or removal of source links.
- **Scraping more than Top 10.** Respect benchlm.ai's reach — go to their site for the full data.
- **Adding "Display only" benchmarks** without resolution. Use issues to flag interest; we'll add them when benchlm.ai promotes them.
- **Vendor-promotional rows.** Tools listed must be evaluated by their real shipping artifacts, not press releases.

## Reporting issues

- **Parse failure**: slug + date + the URL.
- **Stale data**: GitHub Actions logs first, then issue if you suspect a parser regression.
- **Disagreement with benchlm.ai's methodology**: that's a benchlm.ai issue, not ours. Reach out to them. We mirror; we don't re-eval.

## Local development

```bash
git clone https://github.com/leoncuhk/awesome-llm-bench.git
cd awesome-llm-bench
pip install -r scripts/requirements.txt

# Fetch one benchmark
python scripts/fetch_benchmark.py --slug sweVerified

# Fetch all
python scripts/fetch_benchmark.py --all

# Re-render READMEs from data/
python scripts/render_readme.py
```
