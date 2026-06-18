<div align="center">

# Awesome LLM Bench

Top 10 of the most reliable LLM leaderboards, auto-synced daily.

[![Sync](https://github.com/leoncuhk/awesome-llm-bench/actions/workflows/sync.yml/badge.svg)](https://github.com/leoncuhk/awesome-llm-bench/actions/workflows/sync.yml)
[![License](https://img.shields.io/badge/license-MIT-000.svg)](LICENSE)
[![中文](https://img.shields.io/badge/lang-中文-000.svg)](README.zh-CN.md)

<!-- LAST_SYNC -->Last sync: **2026-06-18** (UTC, daily auto-update)<!-- /LAST_SYNC -->

</div>

<br>

> **Data source:** [benchlm.ai](https://benchlm.ai). For the full leaderboards (43+ models per benchmark), pricing dashboards, and methodology, please visit the canonical site. This repository is a Top-10 mirror with attribution, not a replacement.

<br>

## About

The LLM evaluation landscape is noisy. LMArena measures preference, not capability; vendor-published numbers are cherry-picked; most aggregators lag months behind frontier model releases. [benchlm.ai](https://benchlm.ai) is the most honest, frequently-updated aggregator I have found. This repository distills the **Top 10** of each high-signal benchmark for fast scanning, paired with a curated AI coding-tools landscape that benchlm.ai does not cover.

<br>

---

## Contents

**Coding** — [SWE-bench Verified](#swe-bench-verified) · [LiveCodeBench](#livecodebench)  
**Agentic** — [Terminal-Bench 2.0](#terminal-bench-20) · [OSWorld-Verified](#osworld-verified) · [BrowseComp](#browsecomp)  
**Reasoning** — [ARC-AGI-2](#arc-agi-2)  
**Knowledge** — [Humanity's Last Exam](#humanitys-last-exam)  
**Tools** — [AI Coding Tools Landscape](#ai-coding-tools-landscape)  
**Reference** — [How to read](#how-to-read-these-numbers) · [Caveats](#caveats) · [Attribution](#data-source-and-attribution)

<br>

---

## Coding

### SWE-bench Verified

Real GitHub issues from popular Python repositories (Django, Flask, scikit-learn). Human-verified subset of SWE-bench. The gold standard for AI coding agents.

<!-- AUTO:START slug=sweVerified lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos 5](https://benchlm.ai/models/claude-mythos-5) | Anthropic | Closed | 95.5% |
| 2 | [Claude Fable 5](https://benchlm.ai/models/claude-fable) | Anthropic | Closed | 95.0% |
| 3 | [Claude Opus 4.8](https://benchlm.ai/models/claude-opus-4-8) | Anthropic | Closed | 88.6% |
| 4 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 87.6% |
| 5 | [GPT-5.3 Codex](https://benchlm.ai/models/gpt-5-3-codex) | OpenAI | Closed | 85.0% |
| 6 | [Claude Opus 4.5](https://benchlm.ai/models/claude-opus-4-5) | Anthropic | Closed | 80.9% |
| 7 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 80.8% |
| 8 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 80.6% |
| 9 | [MiniMax M3](https://benchlm.ai/models/minimax-m3) | MiniMax | Open | 80.5% |
| 10 | [Qwen3.7 Max](https://benchlm.ai/models/qwen3-7-max) | Alibaba | Closed | 80.4% |

*Source: [https://benchlm.ai/benchmarks/sweVerified](https://benchlm.ai/benchmarks/sweVerified) · Updated 2026-06-16 · Total models: 53*
<!-- AUTO:END slug=sweVerified -->

### LiveCodeBench

Contamination-free code generation. Fresh problems are sampled continuously, mitigating training-data leakage.

<!-- AUTO:START slug=liveCodeBench lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 93.5% |
| 2 | [Qwen3.7 Max](https://benchlm.ai/models/qwen3-7-max) | Alibaba | Closed | 91.6% |
| 3 | [DeepSeek V4 Flash (Max)](https://benchlm.ai/models/deepseek-v4-flash-max) | DeepSeek | Open | 91.6% |
| 4 | [DeepSeek V4 Pro (High)](https://benchlm.ai/models/deepseek-v4-pro-high) | DeepSeek | Open | 89.8% |
| 5 | [Qwen3.7 Plus](https://benchlm.ai/models/qwen3-7-plus) | Alibaba | Closed | 89.6% |
| 6 | [Kimi K2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 89.6% |
| 7 | [Nemotron 3 Ultra](https://benchlm.ai/models/nemotron-3-ultra) | NVIDIA | Open | 89.0% |
| 8 | [DeepSeek V4 Flash (High)](https://benchlm.ai/models/deepseek-v4-flash-high) | DeepSeek | Open | 88.4% |
| 9 | [MAI-Thinking-1](https://benchlm.ai/models/mai-thinking-1) | Microsoft | Closed | 87.7% |
| 10 | [Kimi K2.5](https://benchlm.ai/models/kimi-k2-5) | Moonshot AI | Open | 85.0% |

*Source: [https://benchlm.ai/benchmarks/liveCodeBench](https://benchlm.ai/benchmarks/liveCodeBench) · Updated 2026-06-16 · Total models: 20*
<!-- AUTO:END slug=liveCodeBench -->

<br>

---

## Agentic

### Terminal-Bench 2.0

Multi-step terminal and CLI workflows. Models inspect files, run commands, edit code, and recover from errors over interactive sessions.

<!-- AUTO:START slug=terminalBench2 lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos 5](https://benchlm.ai/models/claude-mythos-5) | Anthropic | Closed | 88.0% |
| 2 | [Claude Fable 5](https://benchlm.ai/models/claude-fable) | Anthropic | Closed | 84.3% |
| 3 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 82.0% |
| 4 | [GLM-5.2](https://benchlm.ai/models/glm-5-2) | Z.AI | Open | 81.0% |
| 5 | [Gemini 3.5 Flash](https://benchlm.ai/models/gemini-3-5-flash) | Google | Closed | 76.2% |
| 6 | [Claude Opus 4.8](https://benchlm.ai/models/claude-opus-4-8) | Anthropic | Closed | 74.6% |
| 7 | [Qwen3.7 Plus](https://benchlm.ai/models/qwen3-7-plus) | Alibaba | Closed | 70.3% |
| 8 | [Qwen3.7 Max](https://benchlm.ai/models/qwen3-7-max) | Alibaba | Closed | 69.7% |
| 9 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 69.4% |
| 10 | [Composer 2.5](https://benchlm.ai/models/composer-2-5) | Cursor | Closed | 69.3% |

*Source: [https://benchlm.ai/benchmarks/terminalBench2](https://benchlm.ai/benchmarks/terminalBench2) · Updated 2026-06-16 · Total models: 30*
<!-- AUTO:END slug=terminalBench2 -->

### OSWorld-Verified

Computer-use tasks in desktop GUIs. Navigation, editing, and complex multi-step workflows.

<!-- AUTO:START slug=osWorldVerified lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos 5](https://benchlm.ai/models/claude-mythos-5) | Anthropic | Closed | 85.0% |
| 2 | [Claude Fable 5](https://benchlm.ai/models/claude-fable) | Anthropic | Closed | 85.0% |
| 3 | [Claude Opus 4.8](https://benchlm.ai/models/claude-opus-4-8) | Anthropic | Closed | 83.4% |
| 4 | [Holo3-35B-A3B](https://benchlm.ai/models/holo3-35b-a3b) | H Company | Open | 82.6% |
| 5 | [Holo3-122B-A10B](https://benchlm.ai/models/holo3-122b-a10b) | H Company | Closed | 78.8% |
| 6 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 78.7% |
| 7 | [Gemini 3.5 Flash](https://benchlm.ai/models/gemini-3-5-flash) | Google | Closed | 78.4% |
| 8 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 78.0% |
| 9 | [GPT-5.4](https://benchlm.ai/models/gpt-5-4) | OpenAI | Closed | 75.0% |
| 10 | [Qwen3.7 Plus](https://benchlm.ai/models/qwen3-7-plus) | Alibaba | Closed | 73.3% |

*Source: [https://benchlm.ai/benchmarks/osWorldVerified](https://benchlm.ai/benchmarks/osWorldVerified) · Updated 2026-06-16 · Total models: 23*
<!-- AUTO:END slug=osWorldVerified -->

### BrowseComp

Web-research agents. Models search, inspect sources, gather evidence, and return correct answers to research-oriented questions.

<!-- AUTO:START slug=browseComp lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.5 Pro](https://benchlm.ai/models/gpt-5-5-pro) | OpenAI | Closed | 90.1% |
| 2 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 89.3% |
| 3 | [Claude Mythos 5](https://benchlm.ai/models/claude-mythos-5) | Anthropic | Closed | 88.0% |
| 4 | [Claude Fable 5](https://benchlm.ai/models/claude-fable) | Anthropic | Closed | 86.9% |
| 5 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 84.4% |
| 6 | [Claude Opus 4.8](https://benchlm.ai/models/claude-opus-4-8) | Anthropic | Closed | 84.3% |
| 7 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 83.7% |
| 8 | [MiniMax M3](https://benchlm.ai/models/minimax-m3) | MiniMax | Open | 83.5% |
| 9 | [DeepSeek V4 Pro (Max)](https://benchlm.ai/models/deepseek-v4-pro-max) | DeepSeek | Open | 83.4% |
| 10 | [Kimi K2.6](https://benchlm.ai/models/kimi-2-6) | Moonshot AI | Open | 83.2% |

*Source: [https://benchlm.ai/benchmarks/browseComp](https://benchlm.ai/benchmarks/browseComp) · Updated 2026-06-16 · Total models: 26*
<!-- AUTO:END slug=browseComp -->

<br>

---

## Reasoning

### ARC-AGI-2

Abstraction and reasoning grid puzzles. A frontier general-intelligence test where humans solve nearly all tasks but models struggle.

<!-- AUTO:START slug=arcAgi2 lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 85.0% |
| 2 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 83.3% |
| 3 | [Gemini 3.1 Pro](https://benchlm.ai/models/gemini-3-1-pro) | Google | Closed | 77.1% |
| 4 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 75.8% |
| 5 | [Gemini 3.5 Flash](https://benchlm.ai/models/gemini-3-5-flash) | Google | Closed | 72.1% |
| 6 | [Grok 4.20](https://benchlm.ai/models/grok-4-20-beta) | xAI | Closed | 53.3% |
| 7 | [GPT-5.2](https://benchlm.ai/models/gpt-5-2) | OpenAI | Closed | 52.9% |
| 8 | [Gemini 3 Pro Deep Think](https://benchlm.ai/models/gemini-3-pro-deep-think) | Google | Closed | 45.1% |
| 9 | [Muse Spark](https://benchlm.ai/models/muse-spark) | Meta | Closed | 42.5% |
| 10 | [Gemini 3 Pro](https://benchlm.ai/models/gemini-3-pro) | Google | Closed | 31.1% |

*Source: [https://benchlm.ai/benchmarks/arcAgi2](https://benchlm.ai/benchmarks/arcAgi2) · Updated 2026-06-16 · Total models: 11*
<!-- AUTO:END slug=arcAgi2 -->

<br>

---

## Knowledge

### Humanity's Last Exam

Expert-level questions across all academic domains. Designed to be hard for frontier models.

<!-- AUTO:START slug=hle lang=en -->
| Rank | Model | Provider | License | Score |
| :-: | :-- | :-- | :-: | --: |
| 1 | [Claude Mythos 5](https://benchlm.ai/models/claude-mythos-5) | Anthropic | Closed | 64.5% |
| 2 | [Claude Fable 5](https://benchlm.ai/models/claude-fable) | Anthropic | Closed | 64.5% |
| 3 | [GPT-5.4 Pro](https://benchlm.ai/models/gpt-5-4-pro) | OpenAI | Closed | 58.7% |
| 4 | [Claude Opus 4.8](https://benchlm.ai/models/claude-opus-4-8) | Anthropic | Closed | 57.9% |
| 5 | [GPT-5.5 Pro](https://benchlm.ai/models/gpt-5-5-pro) | OpenAI | Closed | 57.2% |
| 6 | [GLM-5.2](https://benchlm.ai/models/glm-5-2) | Z.AI | Open | 54.7% |
| 7 | [Claude Opus 4.7 (Adaptive)](https://benchlm.ai/models/claude-opus-4-7-adaptive) | Anthropic | Closed | 54.7% |
| 8 | [Claude Opus 4.6](https://benchlm.ai/models/claude-opus-4-6) | Anthropic | Closed | 53.0% |
| 9 | [GLM-5.1](https://benchlm.ai/models/glm-5-1) | Z.AI | Open | 52.3% |
| 10 | [GPT-5.5](https://benchlm.ai/models/gpt-5-5) | OpenAI | Closed | 52.2% |

*Source: [https://benchlm.ai/benchmarks/hle](https://benchlm.ai/benchmarks/hle) · Updated 2026-06-16 · Total models: 40*
<!-- AUTO:END slug=hle -->

<br>

---

## AI Coding Tools Landscape

The tools practitioners actually ship code with. Selection bar is high — only tools with verifiable adoption and active maintenance. Full table with criteria, pricing, and update cadence: [tools/ai-coding-tools.md](tools/ai-coding-tools.md).

#### CLI agents

| Tool | Provider | Distinguishing capability |
| :-- | :-- | :-- |
| [Claude Code](https://www.anthropic.com/claude-code) | Anthropic | Sub-agents, hooks, MCP, slash commands, skills |
| [Codex CLI](https://github.com/openai/codex) | OpenAI | Official agent CLI with sandboxed execution |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Google | Native Search grounding, generous free tier |
| [Aider](https://aider.chat) | Open source | Git-native diffs, repo-map, model-agnostic |

#### IDE-native

| Tool | Provider | Distinguishing capability |
| :-- | :-- | :-- |
| [Cursor](https://cursor.com) | Anysphere | Composer multi-file edit, fastest Tab completion |
| [Windsurf](https://windsurf.com) | Codeium / OpenAI | Cascade flow, supercomplete |
| [Zed AI](https://zed.dev) | Zed Industries | Built into the fastest editor (Rust) |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub | Largest deployment, broadest IDE coverage |

#### VS Code extensions (open source, BYOK)

| Tool | Provider | Distinguishing capability |
| :-- | :-- | :-- |
| [Cline](https://cline.bot) | Open source | Plan/Act modes, MCP, browser use |
| [Roo Code](https://roocode.com) | Open source | Cline fork with custom agent modes |
| [Continue](https://continue.dev) | Open source | Customizable assistants and slash commands |

#### Cloud agents and codebase Q&A

| Tool | Provider | Distinguishing capability |
| :-- | :-- | :-- |
| [Devin](https://devin.ai) | Cognition | Long-running autonomous SWE agent |
| [Replit Agent](https://replit.com/ai) | Replit | End-to-end app generation in browser |
| [Sourcegraph Cody](https://sourcegraph.com/cody) | Sourcegraph | Code-graph context, repo-scale awareness |

<br>

---

## How to read these numbers

- **Do not compare across benchmarks.** Different scales, different ceilings.
- **Look at the spread.** Top 10 within 2–3 points means saturation; differences are noise. A 10+ point lead means the leader is genuinely ahead.
- **Check the date.** Each table links back to the source page; benchmarks refresh asynchronously.
- **For your own use case, run your own evaluation.** Public benchmarks measure averages on someone else's tasks.

## Caveats

- benchlm.ai is also an aggregator with judgment calls (category weights, inclusion criteria). I mirror their judgment because it is the best I have found, not because it is objective truth.
- Benchmark contamination is real and growing. Treat any single benchmark with skepticism — consensus across multiple is the signal.
- Model identity drift: vendors silently update models behind the same name. Scores from different dates are not strictly comparable.

## Data source and attribution

All leaderboard data is mirrored from [benchlm.ai](https://benchlm.ai) with full attribution. Each table links back to the canonical page. Excluded by design: benchmarks tagged "Display only" on benchlm.ai itself (GAIA, BFCL v4, FrontierMath, …) — they have incomplete public snapshots and including them would mislead.

For full leaderboards, pricing, methodology, dashboards, and category weights, please visit [benchlm.ai](https://benchlm.ai).

<br>

---

## Update cadence

A GitHub Actions workflow runs daily at 02:00 UTC, fetches the source pages, parses the leaderboard, and commits to `data/` and the README sections only when something has changed. The commit message names what changed. See [`.github/workflows/sync.yml`](.github/workflows/sync.yml).

## Contributing

PRs welcome — see [CONTRIBUTING.md](CONTRIBUTING.md). Add a benchmark by editing `scripts/benchmarks.yaml`; add a tool by editing `tools/ai-coding-tools.md`. Keep the bar high: only `Current` or `Refreshing` benchmarks on benchlm.ai, only tools with real adoption.

## Related

- [benchlm.ai](https://benchlm.ai) — canonical source
- [Awesome Quant AI](https://github.com/leoncuhk/awesome-quant-ai) — sister list
- [Artificial Analysis](https://artificialanalysis.ai/) — alternative aggregator (price/perf focus)
- [LMArena](https://lmarena.ai/) — pairwise human preference

## License

[MIT](LICENSE) for the curation, code, and original commentary. Leaderboard data is mirrored from benchlm.ai — see their terms for data use.

<br>

<div align="center">
<sub>Maintained by <a href="https://github.com/leoncuhk">@leoncuhk</a> · Sister project: <a href="https://github.com/leoncuhk/awesome-quant-ai">awesome-quant-ai</a></sub>
</div>
