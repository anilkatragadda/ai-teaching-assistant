---
name: spec-driven-development
description: Authors Technical Specifications and Phased Implementation Plans (TECH-###). Use during Gate 2.5 of the SDLC to translate approved PRDs, ADRs, and OpenAPI contracts into technical scaffolding, exact commands, directory layouts, and milestone to-dos in docs/architecture/specs/ before breaking into atomic tasks.
---

# Technical Spec & Phased Implementation Planning (Gate 2.5)

## Overview

A Product Requirements Document (`PRD-###`) defines *what* to build and *why*.  
An Architecture Decision Record (`ADR-###`) defines *key trade-offs*.  
An OpenAPI Contract (`OAS-###`) defines *API schemas*.

Before jumping straight into code, software engineering requires a **Technical Specification & Implementation Plan (`TECH-###`)**:
1. **Technical Scaffolding:** Exact build/test commands, file placements, and code style patterns.
2. **Execution Boundaries:** What the developer/agent may do freely vs. what requires approval.
3. **Phased Implementation Plan (Milestone To-Dos):** The macro execution roadmap (e.g., Phase 1: DB & Migrations, Phase 2: SymPy Solver Engine, Phase 3: Fastify SSE Stream).

These milestone to-dos are then converted by `planning-and-task-breakdown` into atomic tasks (`TASK-###`), where each task contains granular checklist to-dos executed via Test-Driven Development (TDD).

---

## The 3-Level Progression (From Plan to Code)

```text
Level 1: Milestone To-Dos (TECH-###)
   │  "Phase 1: Database schemas and seed data"
   │  "Phase 2: SymPy verification solver service"
   ▼
Level 2: Atomic Tasks (TASK-###)
   │  "TASK-001: Implement SymPy solver subprocess wrapper"
   │  "TASK-002: Add OCR confidence threshold check"
   ▼
Level 3: Execution To-Dos (Within each Task)
      [ ] 1. Write failing unit test (Red)
      [ ] 2. Implement core function (Green)
      [ ] 3. Verify passing suite and lint (Refactor)
```

---

## File Naming & Directory Convention

All Technical Specs must be saved in:
`docs/architecture/specs/TECH-###-<slug>.md`  
*(e.g., `docs/architecture/specs/TECH-001-core-socratic-engine.md`)*

---

## Standard Technical Spec Template (`TECH-###`)

```markdown
---
id: TECH-###
title: "Technical Spec: [Feature / System Name]"
type: tech-spec
status: proposed # proposed | accepted | implemented
created: YYYY-MM-DD
updated: YYYY-MM-DD
upstream:
  - "docs/project-plan/specs/PRD-###-<slug>.md"
  - "docs/architecture/adrs/ADR-###-<slug>.md"
  - "docs/open-api/OAS-###-<slug>.yaml"
downstream:
  - "docs/project-plan/tasks/TASK-###-<slug>.md"
tags:
  - tech-spec
  - implementation-plan
---

# TECH-###: Technical Spec & Implementation Plan — [Feature Name]

## 0. Artifact Lineage & Traceability
- **Upstream PRD:** [\`PRD-###-<slug>.md\`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/specs/)
- **Upstream ADRs:** [\`ADR-###-<slug>.md\`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/adrs/)
- **Upstream OpenAPI Contract:** [\`OAS-###-<slug>.yaml\`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/open-api/)
- **Target Downstream Tasks:** [\`TASK-###-<slug>.md\`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/tasks/)

---

## 1. Technical Stack & Dependencies
- **Runtime & Language:** Node.js 20+ (TypeScript 5.x) / Python 3.11+
- **Frameworks:** Fastify, Zod, SymPy, Prisma / Kysely
- **Infrastructure Services:** PostgreSQL 16 (Docker), Redis 7 (Docker)

---

## 2. Executable Commands
\`\`\`bash
# Build
npm run build

# Test
npm test
npm run test:evals

# Lint & Format
npm run lint
npm run format

# Dev Server
npm run dev
\`\`\`

---

## 3. Directory Layout & Module Structure
\`\`\`text
src/
├── api/             # Fastify routes, plugins, controllers
│   ├── routes/      # Endpoints mapped to OAS-###
│   └── sse/         # SSE streaming handlers
├── domain/          # Pure business logic and invariants
│   ├── socratic/    # Hint generators, pedagogical prompts
│   └── sympy/       # CAS validation solver wrapper
├── infra/           # Database, Redis client, external APIs
└── types/           # Generated and shared TypeScript types
tests/
├── unit/            # Isolated unit tests
├── integration/     # Fastify route and DB integration tests
└── evals/           # Pedagogical and answer leakage evaluations
\`\`\`

---

## 4. Code Style & Reference Pattern
One real code snippet demonstrating standard error handling, typing, and validation:

\`\`\`typescript
import { z } from "zod";
import { FastifyReply, FastifyRequest } from "fastify";

export async function handleSocraticTurn(req: FastifyRequest, reply: FastifyReply) {
  // Validate against Zod schema mapped from OAS contract
  const body = turnRequestSchema.parse(req.body);

  // Ground truth check before streaming
  const truth = await sympySolver.solve(body.equation);
  if (!truth.solvable) {
    return reply.status(422).send({ error: "Equation cannot be verified symbolically." });
  }

  // Stream hints via SSE
  reply.raw.setHeader("Content-Type", "text/event-stream");
  for await (const chunk of hintGenerator.stream(body, truth)) {
    reply.raw.write(\`data: \${JSON.stringify(chunk)}\\n\\n\`);
  }
}
\`\`\`

---

## 5. Testing Strategy & Execution Boundaries

### Testing Pyramid
- **Unit Tests:** Fast, isolated tests for SymPy wrappers and leakage filters ($\ge 90\%$ coverage).
- **Integration Tests:** Fastify endpoint integration against test PostgreSQL and Redis instances.
- **Eval Benchmarks:** Red-team leakage benchmark ($\le 0.5\%$ leakage).

### Boundaries
- **Always:** Run test suites before PR; validate inputs with Zod; check SymPy truth before generating hints.
- **Ask First:** Adding third-party dependencies; altering database migrations; changing CI config.
- **Never:** Commit plaintext API keys; output direct solutions without parent unlock; use \`eval\`/\`exec\` on dynamic code.

---

## 6. Phased Implementation Plan (Milestone To-Dos)

### Milestone 1: Local Infrastructure & DB Setup
- [ ] 1.1 Docker Compose for PostgreSQL 16 and Redis 7
- [ ] 1.2 Prisma/Kysely database migration for sessions and messages
- [ ] 1.3 Fastify server initialization with health check endpoint

### Milestone 2: SymPy Symbolic Verification Service
- [ ] 2.1 Python SymPy execution wrapper with timeout and memory sandbox
- [ ] 2.2 TypeScript bridge service calling SymPy solver
- [ ] 2.3 Solvability and root extraction test suite

### Milestone 3: Socratic Dialogue & SSE Hint Streaming
- [ ] 3.1 Socratic prompt engine with answer leakage guardrails
- [ ] 3.2 Fastify SSE streaming endpoint matching OAS contract
- [ ] 3.3 Leakage eval benchmark suite

### Milestone 4: Parent Authorization Gate & Session Summary
- [ ] 4.1 Parent answer unlock toggle endpoint
- [ ] 4.2 End-of-session comprehension check question generator
- [ ] 4.3 Cloudflare Tunnel configuration for mobile testing

---

## 7. Downstream Task Mapping

The milestones above decompose into numbered task files authored by \`planning-and-task-breakdown\`:
- Milestone 1 $\to$ \`docs/project-plan/tasks/TASK-001-infra-db.md\`
- Milestone 2 $\to$ \`docs/project-plan/tasks/TASK-002-sympy-solver.md\`
- Milestone 3 $\to$ \`docs/project-plan/tasks/TASK-003-socratic-stream.md\`
- Milestone 4 $\to$ \`docs/project-plan/tasks/TASK-004-parent-gate.md\`
```

---

## Execution Checklist

Before advancing from Gate 2.5 to Gate 3 (Task Breakdown):
- [ ] Upstream `PRD-###`, `ADR-###`, and `OAS-###` are accepted.
- [ ] Executable commands are verified to run without interactive prompts.
- [ ] Directory layout and code style patterns are established.
- [ ] The Phased Implementation Plan has clear milestone to-dos.
- [ ] Registered in [`docs/INDEX.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/INDEX.md).
