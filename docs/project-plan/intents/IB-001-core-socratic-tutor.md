---
id: IB-001
title: "Intent Brief: Core Socratic Math Tutor and Symbolic Truth Engine"
type: intent-brief
status: accepted
created: 2026-10-10
updated: 2026-10-10
upstream:
  - "docs/project-plan/SCOPE.md"
downstream:
  - "docs/architecture/research/ARN-001-competitive-differentiation-and-moat.md"
  - "docs/architecture/adrs/ADR-001-core-tech-stack-and-video-rendering.md"
  - "docs/architecture/adrs/ADR-002-progressive-deployment-plan.md"
  - "docs/project-plan/specs/PRD-001-core-socratic-tutor.md"
tags:
  - socratic
  - sympy
  - grades-3-6-math
  - parent-controls
  - fastify
  - local-mac-mini
---

# IB-001: Intent Brief — Core Socratic Math Tutor and Symbolic Truth Engine

## 0. Artifact Lineage & Traceability
- **Upstream Scope Anchor:** [`docs/project-plan/SCOPE.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/SCOPE.md) (`SCOPE-001`)
- **Supporting Architecture Research:** [`docs/architecture/research/ARN-001-competitive-differentiation-and-moat.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/research/ARN-001-competitive-differentiation-and-moat.md) (`ARN-001`)
- **Supporting Architecture Records:**
  - [`docs/architecture/adrs/ADR-001-core-tech-stack-and-video-rendering.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/ADR-001-core-tech-stack-and-video-rendering.md) (`ADR-001`)
  - [`docs/architecture/adrs/ADR-002-progressive-deployment-plan.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/ADR-002-progressive-deployment-plan.md) (`ADR-002`)
- **Target Downstream Spec:** [`docs/project-plan/specs/PRD-001-core-socratic-tutor.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/specs/PRD-001-core-socratic-tutor.md) (`PRD-001`)
- **Target Downstream API Contract:** [`docs/open-api/OAS-001-socratic-tutor-api.yaml`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/open-api/OAS-001-socratic-tutor-api.yaml) (`OAS-001`)

---

## 1. Validated Problem Statement
- **Goal:** Help Grades 3–6 students work through math homework conceptually without leaking direct answers, while providing parents supervisory control and comprehension verification.
- **Target User & Context:** Primary learner is a Grade 3–6 student working on homework assignments via desktop canvas or tablet. Secondary user is a parent who authorizes answer releases, receives real-time alerts, and reviews session summaries.

---

## 2. Technical Direction (Curated Path)
- **Selected Architecture:** Fastify (TypeScript) API with Server-Sent Events (SSE) streaming, backed by SymPy CAS for pre-generation symbolic truth verification and PostgreSQL/Redis running locally on Apple Silicon (ADR-002 Phase 1 MVP).
- **Supporting Research Note:** [`ARN-001`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/research/ARN-001-competitive-differentiation-and-moat.md)
- **Supporting Decisions:** [`ADR-001`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/ADR-001-core-tech-stack-and-video-rendering.md), [`ADR-002`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/ADR-002-progressive-deployment-plan.md)
- **Rationale:** Fastify delivers low interactive latency ($\le 3\text{s}$ SSE). SymPy CAS eliminates mathematical hallucinations prior to prompt assembly. Phase 1 Mac mini execution enables $0 baseline hosting cost during MVP validation.
- **Key Trade-offs Accepted:** Video rendering pool is deferred to Phase 2; Tier 2 (static KaTeX / SVG diagrams) and Tier 3 (text Socratic dialogue) serve as MVP visual scaffolding.

---

## 3. Scope Boundaries

### IN SCOPE (V1 / MVP 1)
1. **Worksheet & Text Ingestion:** Student submits problem image or typed equation with an OCR confidence gate ($\ge 85\%$).
2. **Pre-Generation SymPy Truth Check:** Validates mathematical solvability and generates ground truth before prompt assembly.
3. **Socratic Guidance Stream:** Fastify SSE streaming hints, diagnostic prompts, and conceptual questions ($\le 3\text{s}$ latency).
4. **Answer Leakage Filter:** Red-team evaluation invariant ensuring the final calculation or answer is never output directly ($\le 0.5\%$ leakage).
5. **Parent Release Gate:** Direct answers require explicit parent unlock (or fallback analogous problem).
6. **End-of-Session Comprehension Check:** 2–3 targeted verification questions to measure mastery.
7. **Local Execution Environment:** Docker Compose (PostgreSQL 16, Redis 7) and Cloudflare Tunnel for secure remote mobile testing.

### OUT OF SCOPE (Deferred to V1.5+ / Cloud Phases)
1. Automated Manim video render worker cluster (deferred to ADR-002 Phase 2).
2. Live bidirectional voice streaming (deferred to V1.5).
3. School LMS / SIS gradebook sync.
4. Multi-student classroom dashboards.

---

## 4. Critical Invariants & Failure States
- **Data & State Management:** Sessions and message history stored in PostgreSQL; rate limiting and token states cached in Redis.
- **Symbolic Abstention Policy:** If SymPy fails to verify the equation or OCR confidence $< 85\%$, the system abstains from hint generation and requests student/parent confirmation.
- **Privacy & COPPA:** Zero data retention on external model calls; no student PII persisted in cleartext.

---

## 5. Downstream SDLC Execution Plan
1. **Spec Step:** Invoke `spec-driven-development` to author [`docs/project-plan/specs/PRD-001-core-socratic-tutor.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/specs/PRD-001-core-socratic-tutor.md).
2. **Contract Step:** Define API schemas in [`docs/open-api/OAS-001-socratic-tutor-api.yaml`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/open-api/OAS-001-socratic-tutor-api.yaml) via `api-and-interface-design`.
3. **Task Step:** Run `planning-and-task-breakdown` to create ordered tasks in `docs/project-plan/tasks/`.
4. **Registry:** Register `IB-001` in [`docs/INDEX.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/INDEX.md).
