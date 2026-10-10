# AI Teaching Assistant — Development Guidelines (AI-SDLC)

This repository follows an **Intent-Driven AI Software Development Life Cycle (AI-SDLC)**. 

The developer provides high-level **Intent** ("vibe coding"), and the agent ecosystem autonomously guides it through rigorous engineering gates: Technical Exploration, Requirements, Architecture, Contracts, Tests, Code, Audits, and Docs.

---

## 1. The Intent-Driven AI SDLC Workflow

Every non-trivial feature or architectural change proceeds through these sequential gates:

```text
[Developer Intent] 
       │
       ▼
Gate 0: INTENT REVIEW & TECHNICAL EXPLORATION (intent-reviewer + architecture-explorer)
       │  Context seeding, deep domain research, curated options, scope boundary definition
       ▼
Gate 1: REQUIREMENTS & SPEC (spec-driven-development)
       │  Write PRD with user stories & acceptance criteria in docs/project-plan/
       ▼
Gate 1.5: UI/UX & DESIGN ARCHITECTURE (ui-ux-designer + ui-ux-studio)
       │  Screen flows, Google Stitch vibe prototyping, accessible design tokens in docs/architecture/ui/
       ▼
Gate 2: ARCHITECTURE & CONTRACTS (api-and-interface-design + documentation-and-adrs)
       │  Define OpenAPI specs in docs/open-api/ and ADRs in docs/architecture/
       ▼
Gate 3: TASK BREAKDOWN (planning-and-task-breakdown)
       │  Deconstruct into ordered, testable, independent units of work
       ▼
Gate 4: TEST-DRIVEN IMPLEMENTATION (test-engineer + test-driven-development)
       │  Write failing tests first (red-green-refactor loop)
       ▼
Gate 5: DUAL-AXIS AUDIT (security-auditor + code-reviewer)
       │  Scan OWASP/LLM vulnerabilities + 6-axis code quality review
       ▼
Gate 6: POLISH & RELEASE (clarity)
          Generate release notes, verify documentation, and finalize PR
```

---

## 2. SDLC Role & Subagent Roster

The workspace tools and subagents in `.agents/` map directly to the SDLC stages:

| SDLC Phase | Persona / Agent | Purpose |
|---|---|---|
| **Phase 0: Technical Exploration** | [`architecture-explorer`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/agents/architecture-explorer.md) | Seeds app context from `docs/`, researches complex technical domains (Auth, JWT, RAG, Sessions), and produces curated option matrices. |
| **Phase 0: Intent Ingestion** | [`intent-reviewer`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/agents/intent-reviewer/agent.md) | Interrogates developer prompts, guides developers along recommended technical paths, and outputs the structured Intent Brief. |
| **Phase 1: Requirements & Specs** | Primary Agent with [`spec-driven-development`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/spec-driven-development/SKILL.md) | Authors PRDs in `docs/project-plan/specs/` and decomposes into capability maps. |
| **Phase 1.5: UI/UX & Design Architecture** | [`ui-ux-designer`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/agents/ui-ux-designer.md) with [`ui-ux-studio`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/ui-ux-studio/SKILL.md) | Translates `IB-###` into screen flows, accessible component systems, and Google Stitch prototypes in `docs/architecture/ui/`. |
| **Phase 2: Architecture & Contracts** | Primary Agent with [`api-and-interface-design`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/api-and-interface-design/SKILL.md) & [`documentation-and-adrs`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/documentation-and-adrs/SKILL.md) | Authors typed OpenAPI contracts in `docs/open-api/` and ADRs in `docs/architecture/adrs/`. |
| **Phase 4: QA & Test Harness** | [`test-engineer`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/agents/test-engineer.md) | Writes unit/integration tests and prompt eval benchmarks before application logic is written. |
| **Phase 5: Security Audit** | [`security-auditor`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/agents/security-auditor.md) | Validates input bounds, auth/authz, student data protection (FERPA/COPPA), and prompt safety. |
| **Phase 5: Code Quality Review** | [`code-reviewer`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/agents/code-reviewer.md) | Conducts pre-merge review across correctness, readability, architecture, and clarity. |
| **Phase 6: Prose & Docs Polish** | [`clarity`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/clarity/SKILL.md) | Ensures user-facing guides, API docs, and release notes are concrete and free of AI filler. |

---

## 3. Skill-Driven Execution Model

| Developer Intent | Required Skill | Workflow Summary |
|---|---|---|
| **Ideate & Refine Concept** | [`idea-refine`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/idea-refine/SKILL.md) | Expand and stress-test raw product ideas through structured divergence and convergence. |
| **Intent Interview & Guidance** | [`interview-me`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/interview-me/SKILL.md) | Ask one targeted question at a time with opinionated recommendations attached. |
| **UI/UX Discovery, Design & Polish** | [`ui-ux-studio`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/ui-ux-studio/SKILL.md) | Full-lifecycle UI discovery, design briefs, Google Stitch prototyping, WCAG AA, and platform adaptation. |
| **Frontend Component Engineering** | [`frontend-ui-engineering`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/frontend-ui-engineering/SKILL.md) | Build production-grade, accessible components with composition, colocated tests, and clean state. |
| **Verify Official Framework Patterns** | [`source-driven-development`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/source-driven-development/SKILL.md) | Ground technical choices in authoritative framework documentation rather than stale memory. |
| **Educational Prose & Spec Review** | [`clarity`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/clarity/SKILL.md) | Review student-facing prose, rubrics, and specs to eliminate generic AI filler. |
| **Requirements & PRD Drafting** | [`spec-driven-development`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/spec-driven-development/SKILL.md) | Draft a specification with objectives and acceptance criteria before writing code. |
| **API & Service Contracts** | [`api-and-interface-design`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/api-and-interface-design/SKILL.md) | Design stable, typed schemas in `docs/open-api/` following Hyrum's Law. |
| **Task Planning & Breakdown** | [`planning-and-task-breakdown`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/planning-and-task-breakdown/SKILL.md) | Deconstruct milestones into sequenced, testable units of work. |
| **Logic Implementation & Bugfixes** | [`test-driven-development`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/test-driven-development/SKILL.md) | Follow red-green-refactor; write failing tests to prove bugs before fixing. |
| **Security & Privacy Hardening** | [`security-and-hardening`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/security-and-hardening/SKILL.md) | Audit input boundaries, sanitize student PII, and prevent prompt injection. |
| **Pre-merge Review & Polish** | [`code-review-and-quality`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/code-review-and-quality/SKILL.md) | Review changes across correctness, readability, architecture, security, performance, and clarity. |
| **Bug Diagnosis & Recovery** | [`debugging-and-error-recovery`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/debugging-and-error-recovery/SKILL.md) | Trace root causes methodically using reproduction steps and log analysis. |
| **Architectural Decisions (ADRs)** | [`documentation-and-adrs`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/documentation-and-adrs/SKILL.md) | Record architectural choices in `docs/architecture/` with context, trade-offs, and consequences. |
| **Prompt Tuning & Context** | [`context-engineering`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/context-engineering/SKILL.md) | Optimize agent and model prompt windows, tokens, and system instructions. |

---

## 4. LLM Wiki Architecture & Living Knowledge Graph

All artifacts generated across the SDLC form a connected, bidirectional **LLM Wiki Knowledge Graph** anchored at [`docs/INDEX.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/INDEX.md).

### 4.1 Artifact Taxonomy & Naming Conventions

Every artifact must follow this strict prefix, folder, and naming convention:

| Prefix | Artifact Type | Standard Directory | Naming Pattern | Author / Ingesting Agent |
|---|---|---|---|---|
| **`IB`** | **Intent Brief** | [`docs/project-plan/intents/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/intents/) | `IB-###-<slug>.md` | [`intent-reviewer`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/agents/intent-reviewer/agent.md) |
| **`ARN`** | **Architecture Research Note** | [`docs/architecture/research/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/research/) | `ARN-###-<slug>.md` | [`architecture-explorer`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/agents/architecture-explorer.md) |
| **`UI`** | **UI/UX Design Spec** | [`docs/architecture/ui/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/ui/) | `UI-###-<slug>.md` | [`ui-ux-designer`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/agents/ui-ux-designer.md) |
| **`PRD`** | **Requirements & Spec** | [`docs/project-plan/specs/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/specs/) | `PRD-###-<slug>.md` | [`spec-driven-development`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/spec-driven-development/SKILL.md) |
| **`ADR`** | **Architecture Decision Record** | [`docs/architecture/adrs/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/) | `ADR-###-<slug>.md` | [`documentation-and-adrs`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/documentation-and-adrs/SKILL.md) |
| **`OAS`** | **OpenAPI Service Contract** | [`docs/open-api/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/open-api/) | `OAS-###-<slug>.yaml` | [`api-and-interface-design`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/api-and-interface-design/SKILL.md) |
| **`TASK`** | **Task Implementation Breakdown** | [`docs/project-plan/tasks/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/tasks/) | `TASK-###-<slug>.md` | [`planning-and-task-breakdown`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/planning-and-task-breakdown/SKILL.md) |
| **`REL`** | **Release & Verification Report** | [`docs/releases/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/releases/) | `REL-###-<slug>.md` | [`clarity`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/clarity/SKILL.md) |

### 4.2 Machine-Readable Frontmatter Standard

Every markdown artifact must begin with a YAML frontmatter block for automated graph traversal:

```yaml
---
id: [PREFIX]-[###]
title: "[Human readable title]"
type: [intent-brief | architecture-research-note | prd | adr | task-breakdown]
status: [draft | proposed | accepted | superseded | implemented]
created: YYYY-MM-DD
updated: YYYY-MM-DD
upstream:
  - "docs/[relative-path-to-upstream-artifact]"
downstream:
  - "docs/[relative-path-to-downstream-artifact]"
tags: [tag1, tag2]
---
```

### 4.3 Human & LLM Traceability Block

Every artifact must include a visible Section 0 block immediately after the main heading:

```markdown
## 0. Artifact Lineage & Traceability
- **Upstream Intent Brief:** [`IB-###-<slug>.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/intents/IB-###-<slug>.md)
- **Supporting Research Note:** [`ARN-###-<slug>.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/research/ARN-###-<slug>.md)
- **Downstream ADR:** [`ADR-###-<slug>.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/ADR-###-<slug>.md)
- **Downstream Spec:** [`PRD-###-<slug>.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/specs/PRD-###-<slug>.md)
```

---

## 5. Engineering Invariants & Guardrails

1. **Curated Guidance Over Blank-Slate Questions**: When developers encounter deep technical topics (Auth, JWT, Sessions, Vector RAG), `architecture-explorer` and `intent-reviewer` must provide opinionated recommendations with trade-offs rather than forcing developers to invent solutions.
2. **Bidirectional Lineage & Wiki Registration**: Every artifact MUST link back to its upstream parent (e.g., `ARN` links to `IB`, `ADR` links to `ARN` or `PRD`), define its downstream targets, and register its entry in [`docs/INDEX.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/INDEX.md).
3. **No Code Without a Contract**: Never generate backend endpoints or frontend callers without an agreed schema or OpenAPI spec in `docs/open-api/`.
4. **Red Before Green (TDD)**: Every bugfix or new feature must start with a failing test written by or verified by `test-engineer`.
5. **No Fluent Emptiness (Clarity Standard)**: Documentation and prompts must name exact functions, error states, and measurable bounds. Never invent specifics (`ask-author` when in doubt).
6. **Student Privacy by Design**: Never log student conversations, tokens, or PII without anonymization; never commit API keys or credentials.
