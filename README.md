<div align="center">

# Awesome LLM Bench

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Sync Leaderboards](https://github.com/leoncuhk/awesome-llm-bench/actions/workflows/sync.yml/badge.svg)](https://github.com/leoncuhk/awesome-llm-bench/actions/workflows/sync.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![中文](https://img.shields.io/badge/lang-中文-red.svg)](README.zh-CN.md)

**A curated, auto-synced mirror of the most reliable LLM leaderboards and AI coding-tool dynamics.**

<!-- LAST_SYNC -->Last sync: **2026-04-29** (UTC, daily auto-update)<!-- /LAST_SYNC -->

*Top 10 only · Updated daily · Sourced from [benchlm.ai](https://benchlm.ai)*

</div>

---

## Why this list?

The LLM evaluation landscape is noisy. LMArena reflects user preference, not capability; vendor-published numbers are cherry-picked; aggregate boards lag months behind frontier model releases. This repository mirrors **[benchlm.ai](https://benchlm.ai)** — the most reliable, frequently-updated, methodologically-honest aggregator we have found — and distills the **Top 10** of each high-signal benchmark for fast scanning.

**What you get:**
- Top 10 of 7 high-signal benchmarks across **Agentic / Coding / Reasoning / Knowledge**
- Curated AI **CLI / IDE tool** landscape (Claude Code, Cursor, Cline, Aider, ...)
- Auto-synced daily via GitHub Actions; historical data preserved as JSON in [`data/`](data/)
- English (this file) + [中文版](README.zh-CN.md)

**What this is not:** an evaluation, a re-ranking, or a replacement for benchlm.ai. We are a mirror with attribution. For full leaderboards (43+ models per benchmark), pricing, methodology, and dashboards, **always go to [benchlm.ai](https://benchlm.ai)** — they do the hard work.

## Contents

- [Top 10 Leaderboards](#top-10-leaderboards)
  - [Agentic](#agentic) · [Coding](#coding) · [Reasoning](#reasoning) · [Knowledge](#knowledge)
- [AI Coding Tools Landscape](#ai-coding-tools-landscape)
- [Methodology Notes](#methodology-notes)
- [Limitations & Honest Caveats](#limitations--honest-caveats)
- [How to Read These Numbers](#how-to-read-these-numbers)
- [Contributing](#contributing)
- [License](#license)

---

## Top 10 Leaderboards

### Agentic

#### Terminal-Bench 2.0
> Multi-step terminal/CLI workflows — inspect, run, edit, recover from errors.

<!-- AUTO:START slug=terminalBench2 lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 82.7% |
| 2 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 69.4% |
| 3 | [MiMo-V2.5-Pro](https://benchlm.ai/models/mimo-v2-5-pro) | Xiaomi | Closed | 68.4% |
| 4 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 67.9% |
| 5 | [Kimi 2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 66.7% |
| 6 | [MiMo-V2.5](https://benchlm.ai/models/mimo-v2-5) | Xiaomi | Closed | 65.8% |
| 7 | [Qwen 3.6 Max (preview)](https://benchlm.ai/models/qwen-3-6-max-preview) | Alibaba | Closed | 65.4% |
| 8 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 63.3% |
| 9 | [Composer 2](https://benchlm.ai/models/composer-2) | Cursor | Closed | 61.7% |
| 10 | [Qwen3.6-27B](https://benchlm.ai/models/qwen3-6-27b) | Alibaba | Open | 59.3% |

*Source: [https://benchlm.ai/benchmarks/terminalBench2](https://benchlm.ai/benchmarks/terminalBench2) · Updated 2026-04-28 · Total models: 17*
<!-- AUTO:END slug=terminalBench2 -->

#### OSWorld-Verified
> Computer-use tasks in desktop GUIs — navigation, editing, workflow completion.

<!-- AUTO:START slug=osWorldVerified lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 79.6% |
| 2 | [Holo3-122B-A10B](https://benchlm.ai/models/holo3-122b-a10b) | H Company | Closed | 78.8% |
| 3 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 78.7% |
| 4 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 78.0% |
| 5 | [Holo3-35B-A3B](https://benchlm.ai/models/holo3-35b-a3b) | H Company | Open | 77.8% |
| 6 | [GPT-5.4](https://benchlm.ai/models/gpt-5-4) | OpenAI | Closed | 75.0% |
| 7 | [Kimi 2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 73.1% |
| 8 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 72.7% |
| 9 | [Claude Sonnet 4.6](https://benchlm.ai/models/claude-sonnet-4-6) | Anthropic | Closed | 72.5% |
| 10 | [GPT-5.4 mini](https://benchlm.ai/models/gpt-5-4-mini) | OpenAI | Closed | 72.1% |

*Source: [https://benchlm.ai/benchmarks/osWorldVerified](https://benchlm.ai/benchmarks/osWorldVerified) · Updated 2026-04-28 · Total models: 18*
<!-- AUTO:END slug=osWorldVerified -->

#### BrowseComp
> Web-research agents — search, inspect sources, return correct answers.

<!-- AUTO:START slug=browseComp lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.5 Pro](https://benchlm.ai/models/gpt-5-5-pro) | OpenAI | Closed | 90.1% |
| 2 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 89.3% |
| 3 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 86.9% |
| 4 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 84.4% |
| 5 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 83.7% |
| 6 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 83.4% |
| 7 | [Kimi 2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 83.2% |
| 8 | [GPT-5.4](https://benchlm.ai/models/gpt-5-4) | OpenAI | Closed | 82.7% |
| 9 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 80.4% |
| 10 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 79.3% |

*Source: [https://benchlm.ai/benchmarks/browseComp](https://benchlm.ai/benchmarks/browseComp) · Updated 2026-04-28 · Total models: 21*
<!-- AUTO:END slug=browseComp -->

### Coding

#### SWE-bench Verified
> Real GitHub issues in popular Python repos. The gold standard for AI coding agents.

<!-- AUTO:START slug=sweVerified lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 93.9% |
| 2 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 87.6% |
| 3 | [GPT-5.3 Codex](https://benchlm.ai/models/gpt-5-3-codex) | OpenAI | Closed | 85.0% |
| 4 | [Claude Opus 4.5](https://benchlm.ai/models/claude-opus-4-5) | Anthropic | Closed | 80.9% |
| 5 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 80.8% |
| 6 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 80.6% |
| 7 | [Kimi 2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 80.2% |
| 8 | [GPT-5.2](https://benchlm.ai/models/gpt-5-2) | OpenAI | Closed | 80.0% |
| 9 | [Claude Sonnet 4.6](https://benchlm.ai/models/claude-sonnet-4-6) | Anthropic | Closed | 79.6% |
| 10 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 79.4% |

*Source: [https://benchlm.ai/benchmarks/sweVerified](https://benchlm.ai/benchmarks/sweVerified) · Updated 2026-04-28 · Total models: 43*
<!-- AUTO:END slug=sweVerified -->

#### LiveCodeBench
> Contamination-free code generation, fresh problems sampled continuously.

<!-- AUTO:START slug=liveCodeBench lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 93.5% |
| 2 | [DeepSeek V4 Flash (Max)](https://benchlm.ai/models/deepseek-v4-flash-max) | DeepSeek | Open | 91.6% |
| 3 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 89.8% |
| 4 | [Kimi 2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 89.6% |
| 5 | [DeepSeek V4 Flash (High)](https://benchlm.ai/models/deepseek-v4-flash-high) | DeepSeek | Open | 88.4% |
| 6 | [Kimi K2.5](https://benchlm.ai/models/kimi-k2-5) | Moonshot AI | Open | 85.0% |
| 7 | [GLM-4.7](https://benchlm.ai/models/glm-4-7) | Z.AI | Open | 84.9% |
| 8 | [Qwen3.6-27B](https://benchlm.ai/models/qwen3-6-27b) | Alibaba | Open | 83.9% |
| 9 | [Qwen3.6-35B-A3B](https://benchlm.ai/models/qwen3-6-35b-a3b) | Alibaba | Open | 80.4% |
| 10 | [Nemotron 3 Nano Omni 30B A3B](https://benchlm.ai/models/nemotron-3-nano-omni-30b-a3b) | NVIDIA | Open | 63.2% |

*Source: [https://benchlm.ai/benchmarks/liveCodeBench](https://benchlm.ai/benchmarks/liveCodeBench) · Updated 2026-04-28 · Total models: 13*
<!-- AUTO:END slug=liveCodeBench -->

### Reasoning

#### ARC-AGI-2
> Abstraction and reasoning grid puzzles — frontier general intelligence test.

<!-- AUTO:START slug=arcAgi2 lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 85.0% |
| 2 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 83.3% |
| 3 | [Gemini 3.1 Pro](https://benchlm.ai/models/gemini-3-1-pro) | Google | Closed | 77.1% |
| 4 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 75.8% |
| 5 | [Grok 4.20](https://benchlm.ai/models/grok-4-20-beta) | xAI | Closed | 53.3% |
| 6 | [GPT-5.2](https://benchlm.ai/models/gpt-5-2) | OpenAI | Closed | 52.9% |
| 7 | [Gemini 3 Pro Deep Think](https://benchlm.ai/models/gemini-3-pro-deep-think) | Google | Closed | 45.1% |
| 8 | [Muse Spark](https://benchlm.ai/models/muse-spark) | Meta | Closed | 42.5% |
| 9 | [Gemini 3 Pro](https://benchlm.ai/models/gemini-3-pro) | Google | Closed | 31.1% |
| 10 | [Claude Sonnet 4.5](https://benchlm.ai/models/claude-sonnet-4-5) | Anthropic | Closed | 13.6% |

*Source: [https://benchlm.ai/benchmarks/arcAgi2](https://benchlm.ai/benchmarks/arcAgi2) · Updated 2026-04-28 · Total models: 10*
<!-- AUTO:END slug=arcAgi2 -->

### Knowledge

#### Humanity's Last Exam (HLE)
> Expert-level questions across all academic domains, designed to be hard.

<!-- AUTO:START slug=hle lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos Preview](https://benchlm.ai/models/claude-mythos-preview) | Anthropic | Closed | 64.7% |
| 2 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 58.7% |
| 3 | [GPT-5.5 Pro](https://benchlm.ai/models/gpt-5-5-pro) | OpenAI | Closed | 57.2% |
| 4 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 54.7% |
| 5 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 53.0% |
| 6 | [GLM-5.1](https://benchlm.ai/models/glm-5-1) | Z.AI | Open | 52.3% |
| 7 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 52.2% |
| 8 | [GPT-5.4](https://benchlm.ai/models/gpt-5-4) | OpenAI | Closed | 52.1% |
| 9 | [GLM-5](https://benchlm.ai/models/glm-5) | Z.AI | Open | 50.4% |
| 10 | [Muse Spark](https://benchlm.ai/models/muse-spark) | Meta | Closed | 50.4% |

*Source: [https://benchlm.ai/benchmarks/hle](https://benchlm.ai/benchmarks/hle) · Updated 2026-04-28 · Total models: 31*
<!-- AUTO:END slug=hle -->

---

## AI Coding Tools Landscape

A hand-curated list of the AI CLI/IDE tools that practitioners actually ship code with. See [tools/ai-coding-tools.md](tools/ai-coding-tools.md) for the full table with notes, update cadence, and feature flags.

| Tool | Form factor | Provider | Pricing model | Notes |
| :-- | :-- | :-- | :-- | :-- |
| [Claude Code](https://www.anthropic.com/claude-code) | CLI + IDE plugins | Anthropic | Subscription (Pro/Max) + API | Deep agent loop, hooks, sub-agents, slash commands |
| [Cursor](https://cursor.com) | IDE (VS Code fork) | Anysphere | Subscription + API | Composer mode, Tab completion, multi-model |
| [Windsurf](https://windsurf.com) | IDE (VS Code fork) | Codeium | Subscription + API | Cascade flow, multi-file edits |
| [Cline](https://cline.bot) | VS Code extension | Open source | BYOK | Plan/Act modes, MCP support |
| [Roo Code](https://roocode.com) | VS Code extension | Open source | BYOK | Cline fork with custom modes |
| [Aider](https://aider.chat) | CLI | Open source | BYOK | Git-native, mature, model-agnostic |
| [Codex CLI](https://github.com/openai/codex) | CLI | OpenAI | API | Official OpenAI agent CLI |
| [Continue](https://continue.dev) | VS Code / JetBrains | Open source | BYOK | Customizable assistants |
| [Zed AI](https://zed.dev) | IDE | Zed | Subscription + API | Built-in to fast Rust editor |
| [GitHub Copilot](https://github.com/features/copilot) | IDE plugins + CLI | GitHub/MS | Subscription | Most-deployed assistant |
| [Sourcegraph Cody](https://sourcegraph.com/cody) | IDE plugins | Sourcegraph | Subscription | Codebase-aware (graph context) |
| [Replit Agent](https://replit.com/ai) | Cloud IDE | Replit | Subscription | End-to-end app generation |
| [Devin](https://devin.ai) | Cloud agent | Cognition | Subscription | Autonomous SWE agent |
| [Tabnine](https://tabnine.com) | IDE plugins | Tabnine | Subscription | On-prem / privacy-first option |

---

## Methodology Notes

**How benchlm.ai ranks models.** They use weighted category scores: Agentic 22%, Coding 20%, Reasoning 17%, Multimodal 12%, Knowledge 12%, Multilingual 7%, Instruction Following 5%, Math 5%. Each benchmark within a category contributes a sub-weight (e.g., SWE-bench Verified is 13% of the Coding category). Benchmarks are tagged with **freshness state** (`Current` / `Refreshing` / `Display only`) so you can tell at a glance whether a number is still load-bearing or stale. See the [BenchLM methodology page](https://benchlm.ai/methodology) for the full scoring policy.

**Why we mirror them rather than build our own.** Maintaining a leaderboard well is a full-time job: source verification, freshness audits, contamination checks, eval-script versioning, methodology disclosures. benchlm.ai does this seriously. We add value by (a) distilling to Top 10 for quick scanning, (b) pairing with the AI tools landscape they don't track, and (c) providing a Chinese version.

**Update cadence.** A GitHub Actions workflow fetches the source pages daily at 02:00 UTC, parses the leaderboard, and commits to [`data/`](data/) only when something changes. The commit message names what changed (e.g., `chore(sync): SWE-Verified leader changed from X to Y`).

## Limitations & Honest Caveats

- **benchlm.ai is also an aggregator with judgment calls** — category weights are subjective, benchmark inclusion is editorial. We mirror their judgment because it's the best we've found, not because it's objective truth.
- **"Display only" benchmarks** (GAIA, BFCL v4, FrontierMath, ...) are intentionally excluded from this mirror until they have full verified leaderboards on benchlm.ai. Including partial snapshots would mislead.
- **Benchmark contamination** is a real and growing problem. Even SWE-bench Verified isn't immune — model providers have visibility into the issues. Treat any single benchmark with skepticism; consensus across multiple is the signal.
- **Model identity drift** — vendors silently update models behind the same name. A score from 2026-01 and a score from 2026-04 for "GPT-5.3" may not be the same model.
- **Vendor self-reports vs. independent eval** — benchlm.ai is moving toward independent verification but legacy rows may still be vendor-reported. They expose this via the freshness tag; we surface it in the JSON but not yet in the table.

## How to Read These Numbers

1. **Don't compare across benchmarks.** A 93% on SWE-Verified and a 64% on HLE are not on the same scale. Each benchmark has its own ceiling.
2. **Look at the spread.** When the top 10 are clustered within 2–3 points, the benchmark is saturating — small differences are noise. When the top is 10+ points above mid-tier, the leader is genuinely ahead.
3. **Filter by license** if open-source matters to you. The table shows `Closed` / `Open` for each row.
4. **Check the date** in the source link. Benchmarks refresh asynchronously; a 2025-vintage benchmark may not reflect the latest models.
5. **For your own use case, run your own eval.** Public benchmarks measure averages on someone else's tasks. Your task is your task.

## Contributing

PRs welcome for:
- **Adding a benchmark**: edit [`scripts/benchmarks.yaml`](scripts/benchmarks.yaml) with the camelCase slug used by benchlm.ai (e.g., `mmlu`, `aimE2025`). Re-run `python scripts/fetch_benchmark.py --slug <new>` to verify the parser handles it.
- **Updating the AI tools landscape**: edit [`tools/ai-coding-tools.md`](tools/ai-coding-tools.md). Keep the bar high — only tools with meaningful adoption.
- **Translation fixes** for [`README.zh-CN.md`](README.zh-CN.md).
- **Reporting a parse failure** as an issue with the slug and the date.

Please **do not** PR re-rankings, removed attribution, or scraped content beyond the Top 10.

## Related

- 📊 [benchlm.ai](https://benchlm.ai) — the canonical source (go here for full leaderboards)
- 🧪 [Awesome Quant AI](https://github.com/leoncuhk/awesome-quant-ai) — sister list, focused on quant + AI
- 🤖 [Artificial Analysis](https://artificialanalysis.ai/) — alternative aggregator (price/perf focus)
- 🏟 [LMArena](https://lmarena.ai/) — pairwise human preference (different signal, not capability)

## License

MIT for the curation, code, and original commentary. The leaderboard data is mirrored from benchlm.ai with attribution; consult their site for their data terms.

---

<div align="center">
<sub>Maintained by <a href="https://github.com/leoncuhk">@leoncuhk</a> · Sister project to <a href="https://github.com/leoncuhk/awesome-quant-ai">awesome-quant-ai</a></sub>
</div>
