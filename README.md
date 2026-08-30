<div align="center">
  <img src="banner.svg" width="880" alt="djm — SigRank SignalAF" />
</div>

<br/>

<div align="center">

[![X](https://img.shields.io/badge/%40burnmydays-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/burnmydays)
[![signalaf.com](https://img.shields.io/badge/signalaf.com-c4923a?style=for-the-badge&logoColor=white)](https://signalaf.com)
[![sigeconomy.com](https://img.shields.io/badge/sigeconomy.com-1a1a2e?style=for-the-badge&logoColor=white)](https://sigeconomy.com)
[![mos2es.org](https://img.shields.io/badge/mos2es.org-0a0a0a?style=for-the-badge&logoColor=white)](https://mos2es.org)
[![signomy.xyz](https://img.shields.io/badge/signomy.xyz-2d4a3e?style=for-the-badge&logoColor=white)](https://signomy.xyz)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0002--9904--5390-A6CE39?style=for-the-badge&logo=orcid&logoColor=white)](https://orcid.org/0009-0002-9904-5390)
[![npm](https://img.shields.io/badge/npm-sigrank-CB3837?style=for-the-badge&logo=npm&logoColor=white)](https://www.npmjs.com/package/sigrank)

</div>

---

<div align="center">
  <img src="metrics.svg" width="640" alt="GitHub metrics" />
</div>

---

## The architecture

```
MO§ES™  →  Upsilon  →  SigRank | SignalAF
  │           │            │
  │           │            ├── signalaf.com — public leaderboard + proof surface
  │           │            ├── sigeconomy.com — competitive operator-ranking arena
  │           │            └── npx sigrank — CLI + MCP + TUI
  │           │
  │           └── Enterprise measurement engine (content-free token telemetry)
  │
  ├── mos2es.org — governance framework + methodology
  ├── enterprise.mos2es.org — enterprise B2B pilot
  ├── mcp.mos2es.org — MCP server
  └── signomy.xyz — governed agent marketplace
```

**MO§ES™ is the governance framework. Upsilon is the measurement engine. SigRank is the public proof surface. SignalAF is the distribution brand.**

Content-free telemetry: four token pillars (INPUT, OUTPUT, CACHE READ, CACHE WRITE). No prompts. No outputs. No PII. Just counts.

> **Currently shipping:** 1,498 seeded operators on the SigRank board. 50 users. `sigrank@1.0.8` on npm. 41 AI evaluation pages live across mos2es.org, signalaf.com, and sigeconomy.com. Enterprise B2B pilot in progress.

---

## What I'm building

### 🏆 SigRank SignalAF
AI operator evaluation — measures how effectively humans use AI, not how good the AI is.

*The first leaderboard that ranks the operator, not the model. Yield (Υ) = (cache_read × output) / input².*

| Surface | URL | What |
|---------|-----|------|
| Leaderboard | [signalaf.com](https://signalaf.com) | Public rankings, score calculator, methodology |
| SigEconomy | [sigeconomy.com](https://sigeconomy.com) | Competitive operator-ranking arena (Cloudflare Workers) |
| CLI + MCP | `npx sigrank` | On-device token scanner, TUI dashboard, 20+ MCP tools |
| VS Code | [extension](https://github.com/SunrisesIllNeverSee/sigrank-vscode) | Inline Yield measurement in your editor |

[![app](https://img.shields.io/badge/app-Next.js-black?style=flat-square&logo=next.js)](https://github.com/SunrisesIllNeverSee/sigrank-app)
[![MCP](https://img.shields.io/badge/MCP-npm-red?style=flat-square&logo=npm)](https://github.com/SunrisesIllNeverSee/sigrank-mcp)
[![VS Code](https://img.shields.io/badge/VS%20Code-extension-blue?style=flat-square&logo=visual-studio-code)](https://github.com/SunrisesIllNeverSee/sigrank-vscode)
[![SigArena](https://img.shields.io/badge/sigeconomy.com-Cloudflare-F38020?style=flat-square&logo=cloudflare)](https://github.com/SunrisesIllNeverSee/sigarena)

---

### 🎯 signa
Interactive coaching agent that reads your token logs, builds a taste profile, and coaches your cascade.

*The metabolic panel to SigRank's calorie counter.*

[Repository](https://github.com/SunrisesIllNeverSee/signa) · `npx signa`

---

### ⚖️ Commitment Theory
Meaning is measurable. A Conservation Law for Commitment in Language — falsifiable, empirically tested, patent pending.

*34-paper research program. If a "may" becomes a "shall" during compression, we catch it.*

[Foundational law](https://github.com/SunrisesIllNeverSee/commitment-conservation) · [Full program](https://github.com/SunrisesIllNeverSee/Commitment_Theory)
CC-BY-4.0 · [Zenodo DOI](https://doi.org/10.5281/zenodo.20029607)

[![ORCID](https://img.shields.io/badge/ORCID-0009--0002--9904--5390-green?style=flat-square&logo=orcid)](https://orcid.org/0009-0002-9904-5390)

---

### 🏛️ MO§ES™
Governance framework for AI operator evaluation. Content-free telemetry, provenance labels, developmental measurement.

*The architecture is sovereign. The artifacts are licensable. The core that produces them is never for sale.*

| Surface | URL | What |
|---------|-----|------|
| Governance | [mos2es.org](https://mos2es.org) | Methodology, concepts, AI evaluation pages |
| Enterprise | [enterprise.mos2es.org](https://enterprise.mos2es.org) | B2B pilot platform |
| MCP | [mcp.mos2es.org](https://mcp.mos2es.org) | MO§ES™ MCP server |

[![promo](https://img.shields.io/badge/promo-Cloudflare-F38020?style=flat-square&logo=cloudflare)](https://github.com/SunrisesIllNeverSee/Moses_Enterprise_B2BPilot_)
[![site](https://img.shields.io/badge/site-mos2es.org-black?style=flat-square)](https://mos2es.org)

---

### 🤖 Signomy
Governed AI agent marketplace with constitutional governance baked into the HTTP layer.

*Multi-homing breaks network effects. The compounding advantage is the non-portable provenance chain.*

[signomy.xyz](https://signomy.xyz) · [Repository](https://github.com/SunrisesIllNeverSee/agent-universe)

---

## The ecosystem

| | Project | What it does | |
|:---:|---------|-------------|:---:|
| 🏆 | **[SigRank](https://signalaf.com)** | AI operator leaderboard — measures what you do, not what you claim | `npx sigrank` |
| 📊 | **[SigEconomy](https://sigeconomy.com)** | Competitive operator-ranking arena — satellite leaderboard | Live |
| 🔌 | **[sigrank-mcp](https://www.npmjs.com/package/sigrank)** | MCP server + CLI + TUI dashboard — 20+ tools any agent can call | `npm i -g sigrank` |
| 🎯 | **[signa](https://github.com/SunrisesIllNeverSee/signa)** | Interactive coaching agent — reads your logs, builds a taste profile | `npx signa` |
| 📈 | **[fundscore](https://www.npmjs.com/package/fundscore)** | Investor-readiness repo scorer | `npx fundscore` |
| ⚖️ | **[Commitment Theory](https://github.com/SunrisesIllNeverSee/Commitment_Theory)** | 34-paper research program on the conservation law | CC-BY-4.0 |
| 🏛️ | **[MO§ES™](https://mos2es.org)** | Governance framework for AI operator evaluation | Patent pending |
| 🤖 | **[Signomy](https://signomy.xyz)** | Governed agent marketplace with bounty board | Live |
| 🏢 | **[Application Hub](https://mos2es.xyz)** | Founder-first application infrastructure | Live |

---

## The receipts

| | |
|---|---|
| 📄 **4 patent filings** | 63/877,177 · 63/883,018 · 19/426,028 · 63/991,282 |
| 🏷️ **MO§ES™ trademark** | TM 99408355, IC 042 |
| 🔬 **Zenodo DOIs** | [10.5281/zenodo.20029607](https://doi.org/10.5281/zenodo.20029607) · [10.5281/zenodo.19105225](https://doi.org/10.5281/zenodo.19105225) · [10.5281/zenodo.20031715](https://doi.org/10.5281/zenodo.20031715) |
| 🎓 **ORCID** | [0009-0002-9904-5390](https://orcid.org/0009-0002-9904-5390) |
| 🏢 **Entity** | Ello Cello LLC |
| 📊 **Operators ranked** | 1,498 seeded operators + 50 users on the SigRank board |
| 🌐 **Live domains** | signalaf.com · sigeconomy.com · mos2es.org · signomy.xyz · mos2es.xyz |
| 🧪 **Coherence stress test** | 41% baseline → 80–85% measured (5-phase, rival AI architectures) |
| 🎙️ **Live demos** | [KASSA voice AI](https://sunrisesillneversee.github.io/KASSA/demo/commitment_kernel_demo_v7.html) · [Signomy](https://signomy.xyz) |
| 📰 **Public record** | Grok stress thread (339 exchanges, 13 days) · Stanford submission |

---

<div align="center">

**The record is the moat.**

`C(T(S)) ≈ C(S)` · `Υ = (cache_read × output) / input²`

</div>

---

<div align="center">
  <sub>Last updated: September 2026</sub>
</div>
