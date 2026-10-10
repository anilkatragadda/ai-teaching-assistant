# AI Teaching Assistant — LLM Wiki & Artifact Index

Welcome to the **LLM Wiki Knowledge Graph** for the AI Teaching Assistant project. 

This repository uses an **Intent-Driven AI-SDLC** where high-level developer intents ("vibe coding") are autonomously transformed into production-ready software across rigorous engineering gates. Every gate produces an explicitly typed, uniquely numbered, bidirectionally linked markdown or schema artifact.

- **System Scope & Vision Anchor:** [`docs/project-plan/SCOPE.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/SCOPE.md) (`SCOPE-001`)

---

## 1. Artifact Taxonomy & Naming Conventions

Every artifact follows a strict ID namespace and file naming format:

| Prefix | Artifact Type | Standard Directory | Naming Pattern | Downstream Consumer / Agent |
|---|---|---|---|---|
| **`IB`** | **Intent Brief** | [`docs/project-plan/intents/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/intents/) | `IB-###-<slug>.md` | `architecture-explorer`, `ui-ux-designer`, `spec-driven-development` |
| **`ARN`** | **Architecture Research Note** | [`docs/architecture/research/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/research/) | `ARN-###-<slug>.md` | `intent-reviewer`, `documentation-and-adrs` |
| **`UI`** | **UI/UX Design Spec** | [`docs/architecture/ui/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/ui/) | `UI-###-<slug>.md` | `ui-ux-designer`, `ui-ux-studio`, `spec-driven-development` |
| **`PRD`** | **Requirements & Spec** | [`docs/project-plan/specs/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/specs/) | `PRD-###-<slug>.md` | `api-and-interface-design`, `planning-and-task-breakdown` |
| **`ADR`** | **Architecture Decision Record** | [`docs/architecture/adrs/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/) | `ADR-###-<slug>.md` | All engineering agents |
| **`OAS`** | **OpenAPI Service Contract** | [`docs/open-api/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/open-api/) | `OAS-###-<slug>.yaml` | Backend engineers, frontend callers, `test-engineer` |
| **`TASK`** | **Task Implementation Breakdown** | [`docs/project-plan/tasks/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/tasks/) | `TASK-###-<slug>.md` | Implementation agents (`test-engineer`, coder) |
| **`REL`** | **Release & Verification Report** | [`docs/releases/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/releases/) | `REL-###-<slug>.md` | Release gatekeeper, `clarity` |

---

## 2. Bidirectional Graph Traversal & Frontmatter Standard

To allow LLMs and human engineers to navigate seamlessly up and down the dependency graph without hallucinating paths, **every artifact must contain a structured YAML frontmatter block**:

```yaml
---
id: ARN-001
title: "Session Storage & Student Authentication Architecture"
type: architecture-research-note
status: accepted # draft | proposed | accepted | superseded | implemented
created: 2026-10-06
updated: 2026-10-06
upstream:
  - "docs/project-plan/intents/IB-001-student-session-auth.md"
downstream:
  - "docs/architecture/adrs/ADR-001-http-only-cookie-auth.md"
  - "docs/project-plan/specs/PRD-001-student-session-auth.md"
tags:
  - auth
  - sessions
  - jwt
  - ferpa
---
```

### Traceability Block Standard
Immediately beneath the H1 title of every document, include clickable GitHub-style file links:

```markdown
## 0. Artifact Lineage & Traceability
- **Upstream:** [Link to parent artifact]
- **Downstream:** [Links to child artifacts]
- **Related ADRs / Contracts:** [Links to architecture or OpenAPI specs]
```

---

## 3. The Master Traceability Matrix

When a new artifact is created or advances through the gates, update this central table:

| Intent (`IB`) | Research Note (`ARN`) | UI Design (`UI`) | Spec / PRD (`PRD`) | ADR (`ADR`) | OpenAPI Contract (`OAS`) | Task Plan (`TASK`) | Status |
|---|---|---|---|---|---|---|---|
| — | [`ARN-001`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/research/ARN-001-competitive-differentiation-and-moat.md) | — | — | [`ADR-001`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/ADR-001-core-tech-stack-and-video-rendering.md)<br>[`ADR-002`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/ADR-002-progressive-deployment-plan.md) | — | — | Accepted |



---

## 4. How Agents Traverse this Wiki

1. **Context Seeding**: When starting any task, agents inspect [`docs/INDEX.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/INDEX.md) to discover existing concepts, decisions, and related artifacts.
2. **Upstream Verification**: Before implementing code, agents verify that a valid `PRD-###`, `ADR-###`, or `OAS-###` exists and is marked `accepted`.
3. **Graph Registration**: Upon generating an `IB`, `ARN`, `PRD`, `ADR`, `OAS`, or `TASK`, the authoring agent **must** append or update the row in this index file.
