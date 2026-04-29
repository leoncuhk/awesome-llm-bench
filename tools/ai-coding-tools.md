# AI Coding Tools Landscape

A hand-curated reference table of AI **CLI / IDE / agent** tools that ship code in production. Manually maintained — not auto-synced. Last reviewed: **2026-04-29**.

## What we track

For each tool: form factor, who's behind it, license/pricing, the underlying model strategy, distinguishing features, and update cadence. We deliberately skip:
- Vaporware demos with no shipping artifact
- Generic "ChatGPT wrappers" with no original engineering
- Tools that are abandoned (no commit in 6+ months) — moved to [Archive](#archive)

## Selection criteria

A tool earns a row if it meets at least 3 of these:
1. Verifiable user count (>10k MAU, public GitHub stars >5k, or paying customer count)
2. Distinct technical contribution (custom agent loop, tooling layer, eval, harness)
3. Active maintenance (commit / release in the past 60 days)
4. Used by named teams in production
5. Original UX or workflow innovation

---

## CLI Agents

| Tool | Provider | License | Underlying model | Pricing | Killer feature | Update cadence |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| [Claude Code](https://www.anthropic.com/claude-code) | Anthropic | Closed source, official | Claude family (Opus/Sonnet/Haiku) | Subscription (Pro $20/mo, Max $100-200/mo) + API | Sub-agents, hooks, MCP, slash commands, skills | Weekly |
| [Codex CLI](https://github.com/openai/codex) | OpenAI | Apache 2.0 | GPT-5 family | API only | Official OpenAI agent CLI, sandboxed exec | Weekly |
| [Aider](https://aider.chat) | Paul Gauthier (independent) | Apache 2.0 | Any (BYOK: Claude, GPT, Gemini, local) | Free + your API costs | Git-native diffs, repo-map, voice mode | Weekly |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Google | Apache 2.0 | Gemini 2.5 / 3.0 | Generous free tier + API | Built-in Google Search grounding | Bi-weekly |

## IDE-Native (forks & extensions)

| Tool | Provider | License | Underlying model | Pricing | Killer feature | Update cadence |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| [Cursor](https://cursor.com) | Anysphere | Closed source | Multi-model (own Composer + Claude/GPT) | $20-40/mo + API | Composer multi-file edit, fast Tab completion | Bi-weekly |
| [Windsurf](https://windsurf.com) | Codeium (acquired by OpenAI 2025) | Closed source | Multi-model | $15-60/mo | Cascade flow, supercomplete | Bi-weekly |
| [Zed AI](https://zed.dev) | Zed Industries | Closed source | Multi-model | Subscription + API | Built into fastest editor (Rust) | Weekly |
| [GitHub Copilot](https://github.com/features/copilot) | GitHub / Microsoft | Closed source | OpenAI + Anthropic + own | $10-39/mo | Largest deployment, best IDE coverage | Monthly |
| [JetBrains AI Assistant](https://www.jetbrains.com/ai/) | JetBrains | Closed source | Multi-model | $10/mo | Deep IntelliJ integration | Monthly |

## Open-Source IDE Extensions (BYOK)

| Tool | Provider | License | IDE | Pricing | Killer feature | Update cadence |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| [Cline](https://cline.bot) | Cline Bot Inc. | Apache 2.0 | VS Code | Free, BYOK | Plan/Act modes, MCP, browser use | Weekly |
| [Roo Code](https://roocode.com) | Open source community | Apache 2.0 | VS Code | Free, BYOK | Cline fork with custom agent modes | Weekly |
| [Continue](https://continue.dev) | Continue Dev Inc. | Apache 2.0 | VS Code, JetBrains | Free, BYOK | Custom assistants, slash commands, autocomplete | Weekly |
| [Kilo Code](https://kilocode.ai) | Kilo Code | Apache 2.0 | VS Code | Free + paid plans | Roo/Cline fork with shared budget | Weekly |
| [Tabby](https://tabby.tabbyml.com) | Tabby ML | Apache 2.0 | VS Code, JetBrains | Free self-host | Self-hosted, open weights friendly | Bi-weekly |

## Cloud / Async Agents

| Tool | Provider | License | Underlying model | Pricing | Killer feature | Update cadence |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| [Devin](https://devin.ai) | Cognition | Closed source | Multi-model | $500/mo team | Long-running autonomous agent, browser+shell | Monthly |
| [Replit Agent](https://replit.com/ai) | Replit | Closed source | Claude (primarily) | Subscription | End-to-end app generation in browser | Monthly |
| [Lovable](https://lovable.dev) | Lovable AB | Closed source | Multi-model | Subscription | Vibe-coding for full-stack apps | Bi-weekly |
| [Bolt.new](https://bolt.new) | StackBlitz | Closed source | Claude / GPT | Subscription | In-browser WebContainer, instant preview | Bi-weekly |

## Code Search & Codebase Q&A

| Tool | Provider | License | Underlying model | Pricing | Killer feature | Update cadence |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| [Sourcegraph Cody](https://sourcegraph.com/cody) | Sourcegraph | Closed source (commercial) | Multi-model | $9-19/mo | Code graph context, repo-scale awareness | Bi-weekly |
| [Greptile](https://greptile.com) | Greptile | Closed source | Multi-model | Custom | Codebase Q&A, PR review | Monthly |
| [Tabnine](https://tabnine.com) | Tabnine | Closed source | Own + multi | $9-39/mo | Privacy-first, on-prem option, fine-tuning on your code | Monthly |

---

## Selection guide

**If you live in a terminal:** Claude Code (with subscription), Aider (BYOK / open), Codex CLI (OpenAI shop).

**If you want a full IDE:** Cursor (most polished), Windsurf (Cascade flow), Zed AI (fastest), JetBrains AI (if you're already there).

**If you're VS Code-loyal and budget-conscious:** Cline / Roo Code / Continue (BYOK, you control the model).

**If you want autonomous async work:** Devin, Replit Agent (background tasks while you do other things).

**If you have privacy/compliance constraints:** Tabby (open self-host), Tabnine (on-prem option), Continue with local models.

## How to choose

1. **Where do you write code today?** Pick the tool that lives there. Workflow continuity beats marginal model quality.
2. **Are you OK paying per-token?** If yes, BYOK tools (Aider, Cline) give you the latest models on day-1. If no, subscription tools amortize.
3. **How autonomous do you want it?** Spectrum: tab-complete (Copilot) → instructed agent (Cursor Composer, Cline) → background agent (Devin). More autonomy = more verification work.
4. **Code privacy?** Read each tool's data-handling page. Some retain prompts, some don't. On-prem options exist if you need them.

## Archive

Tools removed from the main table due to inactivity (no release in 6+ months) or shutdown. Kept here for reference:

*(none yet — will populate as tools age out)*

---

## Contributing

Add a tool by editing this file. Include: name, provider, license, model strategy, pricing summary, the **one specific** thing it does well, and update cadence (check the GitHub repo's last commit / release).

**Removal**: tools that haven't shipped in 6 months move to Archive. Tools that have shut down get a strikethrough and a note.

PRs adding new tools should explain in the description which of the [selection criteria](#selection-criteria) the tool meets.
