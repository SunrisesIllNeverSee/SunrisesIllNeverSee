<div align="center">
  <img src="banner.svg" width="880" alt="AI measurement, commitment, and governance" />

  **Measure the operator. Preserve the commitment. Govern the execution.**

  I build systems for understanding how people operate AI, reusing what they know, and making agent execution accountable.

  [SignalAF](https://signalaf.com) · [AQUA](https://aquaidp.xyz) · [Signomy](https://signomy.xyz) · [MO§ES](https://github.com/SunrisesIllNeverSee/MOS2ES)
</div>

## Start here

### 🏆 SignalAF / SigRank — AI operator intelligence

**Benchmark the people operating AI, not the models themselves.** SignalAF publishes an AI operator leaderboard, detailed profiles, head-to-head Compare views, and a Hall of Signal. SigRank turns locally available token-use metadata into inspectable operator metrics.

- [Explore the live leaderboard](https://signalaf.com) · [Compare operators](https://signalaf.com/compare) · [Hall of Signal](https://signalaf.com/hall)
- [Web app source](https://github.com/SunrisesIllNeverSee/sigrank-app) · [CLI + MCP source](https://github.com/SunrisesIllNeverSee/sigrank-mcp) · [Methodology](https://signalaf.com/methodology)

```bash
npx sigrank
```

[![npm](https://img.shields.io/npm/v/sigrank.svg?style=flat-square)](https://www.npmjs.com/package/sigrank) [![SigRank MCP](https://img.shields.io/badge/CLI_%2B_MCP-source-c4923a?style=flat-square)](https://github.com/SunrisesIllNeverSee/sigrank-mcp)

**Privacy and interpretation:** the four measured pillars are input, output, cache write, and cache read. Ranked telemetry does not require prompts, replies, or source code. Signed submissions include device, identity, platform, and report metadata; [read the exact privacy boundaries](https://github.com/SunrisesIllNeverSee/sigrank-mcp#privacy). These metrics describe token-processing patterns, **not** intelligence, model quality, work quality, or business outcomes.

### 🗂️ AQUA — reusable application intelligence

Stop rebuilding the same answers for every accelerator, grant, job, fellowship, or school application. AQUA archives applications, organizes questions, reuses approved answers, and assembles drafts for human review.

- [AQUA website](https://aquaidp.xyz) · [Application Hub source](https://github.com/SunrisesIllNeverSee/application-hub) · [Claude plugin](https://github.com/SunrisesIllNeverSee/aqua-idp-claude)
- Local-first encrypted answer vault and bring-your-own-key workflows; approvals remain user-controlled.
- A portable application/question graph is designed for reuse across different application programs.

### 🤖 Signomy / CIVITAE — governed agent operations

An agent marketplace and runtime for registration, teams, missions, roles, and audit-chain provenance, with MO§ES governance integrated into execution.

[Explore Signomy](https://signomy.xyz) · [Agent-universe source](https://github.com/SunrisesIllNeverSee/agent-universe)

---

## Research, protocols, and governance

| Work | Purpose | Explore |
| --- | --- | --- |
| **Commitment Theory** | Study whether obligations, permissions, and prohibitions survive transformations in language and system behavior. | [Theory](https://github.com/SunrisesIllNeverSee/Commitment_Theory) · [Conservation research](https://github.com/SunrisesIllNeverSee/commitment-conservation) |
| **MO§ES™** | Specify and test execution-time governance, constraints, provenance, and verifiable decisions. | [Architecture](https://github.com/SunrisesIllNeverSee/MOS2ES) · [Governance](https://github.com/SunrisesIllNeverSee/moses-governance) |
| **Upsilon / SigRank measurement** | Derive interpretable operator metrics from token usage, including Yield, Leverage, and Velocity. | [Methodology](https://signalaf.com/methodology) · [Implementation](https://github.com/SunrisesIllNeverSee/sigrank-mcp) |
| **TTEOP** | Define a vendor-neutral token-telemetry interchange and conformance model. Currently an **experimental draft**, not a finalized industry standard. | [Specification](https://github.com/SunrisesIllNeverSee/tteop-spec) |

**System relationship:** token telemetry feeds Upsilon and SigRank; SignalAF presents operator results. Commitment Theory studies what must be preserved when information changes; MO§ES develops enforcement and governance mechanisms. Signomy and enterprise pilot work explore those mechanisms in agent workflows.

The working research constraint is `C(T(S)) ≈ C(S)`. The token-cascade Yield metric is `Υ = (cache_read × output) / input²`. Both require the definitions, applicability limits, and evidence in their respective repositories; neither is a universal measure of AI performance.

## Additional tools

- [signaf](https://github.com/SunrisesIllNeverSee/signa) — local token-cascade coaching experiments.
- [SigRank for VS Code](https://github.com/SunrisesIllNeverSee/sigrank-vscode) — token metrics and leaderboard integration inside the editor.
- [fundscore](https://github.com/SunrisesIllNeverSee/fundscore) — investor-readiness scoring for repositories.
- [SignalAF Analyst for Claude](https://github.com/SunrisesIllNeverSee/signalaf-analyst-claude) — read-only exploration of public board data.

## Connect

SignalAF questions or collaboration: **[hello@signalaf.com](mailto:hello@signalaf.com)** · [X / @burnmydays](https://x.com/burnmydays)

[![ORCID](https://img.shields.io/badge/Research-ORCID-A6CE39?style=flat-square&logo=orcid)](https://orcid.org/0009-0002-9904-5390)

<details>
<summary>GitHub activity</summary>

<div align="center">
  <img src="metrics.svg" width="640" alt="GitHub activity and repository metrics" />
</div>

</details>

<div align="center"><sub>Public project guide · Updated October 24, 2026 · Live results and package versions are linked rather than copied as fixed counts.</sub></div>
