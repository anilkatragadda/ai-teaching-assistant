---
name: requirements-authoring
description: Authors simple, consistent, and traceable Product Requirements Documents (PRDs). Use during Phase 1 of the SDLC to translate Intent Briefs (IB) into verifiable functional requirements, user stories, acceptance criteria, and compliance bounds in docs/project-plan/specs/ before contracts or implementation.
---

# Requirements Authoring & PRD Gate

Grounded in the repository-wide documentation invariants ([`.agents/rules/documentation.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/rules/documentation.md)), this skill enforces **usable, consistent, and lean requirements engineering**:
- **Every requirement has a purpose**: Directly linked to a validated user problem in an Intent Brief (`IB-###`).
- **Strict bidirectional lineage**: Traces upstream to business intent and downstream to OpenAPI contracts (`OAS-###`), architecture decisions (`ADR-###`), and testable tasks (`TASK-###`).
- **Measurable acceptance criteria**: Written in testable terms (Given-When-Then) so engineers and automated evaluators know exactly when a feature is done.
- **Zero redundancy**: Does not duplicate architecture diagrams (belongs in ADRs) or API schemas (belongs in OAS). Focuses purely on *what* the system must do and *why*.

---

## When to Use

- Translating an approved Intent Brief ([`IB-###`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/intents/)) into a formal PRD (`PRD-###`).
- Defining user personas, workflows, and role permissions (e.g., student vs. parent).
- Specifying functional and non-functional requirements with testable acceptance criteria.
- Setting explicit pedagogical invariants and privacy bounds (e.g., COPPA, FERPA, zero answer leakage).

**When NOT to use:**
- Writing technical implementation details, build commands, or folder structures (use `spec-driven-development` and `planning-and-task-breakdown`).
- Defining REST/SSE payload schemas (use `api-and-interface-design`).
- Recording technology choices or infrastructure plans (use `documentation-and-adrs`).

---

## The Core Principles: Simple, Consistent, Usable

1. **No Orphan Documentation**: Every PRD must declare its upstream `IB-###` and downstream targets. If a document has no consumer, do not write it.
2. **Atomic Requirement IDs**: Number functional requirements (`FR-001`, `FR-002`) and non-functional requirements (`NFR-001`). This enables direct citation in pull requests, tests, and API schemas.
3. **Measurable Over Narrative**: Avoid vague adjectives ("fast", "intuitive", "helpful"). Specify quantitative thresholds ("SSE initial token $\le 3\text{s}$", "OCR confidence $\ge 85\%$", "answer leakage rate $\le 0.5\%$").
4. **Explicit Anti-Goals (Out of Scope)**: Clearly state what the system will *not* do in this release to prevent scope bloat.
5. **Single Accountable Owner**: Every PRD must identify a named owner responsible for clarifying edge cases and approving acceptance criteria. An unowned requirement is an abandoned requirement.
6. **Living Artifact Registration**: Every authored PRD must be registered in the Master Traceability Matrix in [`docs/INDEX.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/INDEX.md).

---

## File Naming & Directory Convention

All PRDs must be saved in:
`docs/project-plan/specs/PRD-###-<slug>.md`
*(e.g., `docs/project-plan/specs/PRD-001-core-socratic-tutor.md`)*

---

## Standard PRD Template

```markdown
---
id: PRD-###
title: "PRD: [Feature / System Name]"
type: prd
status: proposed # proposed | accepted | superseded | implemented
owner: "[Product Architect / Lead Engineer]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
upstream:
  - "docs/project-plan/intents/IB-###-<slug>.md"
downstream:
  - "docs/architecture/adrs/ADR-###-<slug>.md"
  - "docs/open-api/OAS-###-<slug>.yaml"
  - "docs/project-plan/tasks/TASK-###-<slug>.md"
tags:
  - [tag1]
  - [tag2]
---

# PRD-###: [Feature / System Name]

## 0. Artifact Lineage & Traceability
- **Owner / Champion:** [Product Architect / Role]
- **Upstream Intent Brief:** [\`IB-###-<slug>.md\`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/intents/IB-###-<slug>.md)
- **Upstream Scope Anchor:** [\`SCOPE.md\`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/SCOPE.md)
- **Downstream Contracts:** [\`OAS-###-<slug>.yaml\`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/open-api/)
- **Downstream ADRs:** [\`ADR-###-<slug>.md\`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/)
- **Downstream Tasks:** [\`TASK-###-<slug>.md\`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/tasks/)

---

## 1. Problem Statement & Objective
- **Objective:** [One concise paragraph stating what is being delivered and the measurable outcome.]
- **Target Personas:**
  - **Persona 1 (e.g. Student):** [Role, device context, constraints]
  - **Persona 2 (e.g. Parent):** [Supervisory authority, notifications]

---

## 2. User Stories & Acceptance Criteria (Gherkin)

### US-001: [Story Title]
**As a** [role],  
**I want to** [action],  
**So that** [benefit].

- **Scenario 1: [Happy Path]**
  - **Given** [pre-condition]
  - **When** [user action]
  - **Then** [expected result]
- **Scenario 2: [Edge / Failure Case]**
  - **Given** [pre-condition]
  - **When** [trigger event]
  - **Then** [recovery or error response]

---

## 3. Functional Requirements (FR)

| Req ID | Title | Description | Priority | Downstream Verification |
|---|---|---|---|---|
| **FR-001** | [Feature Name] | [Exact behavioral requirement] | P0 / P1 / P2 | [E2E test / Contract test / Unit test] |
| **FR-002** | [Feature Name] | [Exact behavioral requirement] | P0 / P1 / P2 | [E2E test / Contract test / Unit test] |

---

## 4. Non-Functional Requirements (NFR)

| Req ID | Category | Target Metric / Constraint | Verification Method |
|---|---|---|---|
| **NFR-001** | Latency | Time to first token SSE $\le 3\text{s}$ | Load testing benchmark |
| **NFR-002** | Pedagogical Safety | Direct answer leakage $\le 0.5\%$ | Red-team eval test suite |
| **NFR-003** | Privacy | COPPA Zero Data Retention on external LLM calls | Network egress audit |

---

## 5. Pedagogical Invariants & Business Rules
1. **Rule 1:** [e.g., Socratic guidance by default; no direct numerical answers without parent approval.]
2. **Rule 2:** [e.g., Ground truth must be solved by SymPy prior to hint generation.]
3. **Rule 3:** [e.g., Abstain and prompt user when OCR confidence $< 85\%$.]

---

## 6. Out of Scope (Explicit Anti-Goals)
- [Feature deliberately deferred to later phases]
- [Workflow explicitly excluded to maintain focus]

---

## 7. Requirement-to-Artifact Traceability Matrix

| Requirement | Downstream OAS Contract | Downstream ADR | Target Test Suite |
|---|---|---|---|
| **FR-001** | `POST /api/sessions/{id}/messages` | `ADR-001` | `tests/api/messages.test.ts` |
| **FR-002** | `POST /api/sessions/{id}/unlock` | `ADR-001` | `tests/auth/parent-gate.test.ts` |
| **NFR-002** | System Prompt Guardrail | `ARN-001` | `tests/evals/leakage.eval.ts` |
```

---

## Execution Checklist

Before marking any PRD as `accepted`:
- [ ] Every user story has at least one happy path and one failure scenario.
- [ ] Every functional requirement has a unique `FR-###` ID and a designated verification method.
- [ ] Performance, safety, and compliance targets have explicit numerical bounds (`NFR-###`).
- [ ] Explicit anti-goals are documented in Section 6.
- [ ] Upstream `IB-###` is linked and downstream targets are identified.
- [ ] Registered in [`docs/INDEX.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/INDEX.md).
