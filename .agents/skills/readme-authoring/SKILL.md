---
name: readme-authoring
description: Authors appealing, informative, and concise root README.md files. Use when creating or refreshing the project's public README, establishing open-source presentation standards, or structuring quickstart, architecture overview, and documentation navigation without emoji bloat or redundant licensing sections.
---

# README Authoring Skill

## Overview

A project's `README.md` is its front door. Great open-source and enterprise READMEs are appealing, informative, concise, and immediately answer three questions:
1. **What is this?** (A clear 1–2 sentence elevator pitch with purpose and target user)
2. **Why does it matter?** (Core capabilities, pedagogical/architectural differentiation, and key invariants)
3. **How do I run or explore it?** (Quickstart, local commands, and pointers to the documentation index)

---

## When to Use

- Creating the initial `README.md` for the repository.
- Refreshing the `README.md` as the project reaches new milestones (MVP 1, MVP 2, Beta).
- Aligning repository presentation with modern open-source standards.

**When NOT to use:**
- Writing architectural decisions (use `documentation-and-adrs`).
- Writing task checklists (use `planning-and-task-breakdown`).
- Writing release notes (use `clarity`).

---

## Core Guidelines & Style Rules

1. **Concise & Direct:** Keep explanations tight and to the point. Avoid fluff and corporate buzzwords.
2. **Restrained Emoji Usage:** Never sprinkle random emojis on every line or bullet point. Use icons only when they serve visual scanning (e.g., status tables, architecture gates).
3. **No Redundant Sections:**
   - **Do NOT** include sections like "LICENSE", "CONTRIBUTING", "CODE_OF_CONDUCT", or "CHANGELOG" if separate files exist for them at root. Mention them in a compact one-line footer if needed.
4. **Use GitHub Admonition Syntax:**
   - Highlight prerequisites, important architectural bounds, or tips using GFM admonitions:
     ```markdown
     > [!IMPORTANT]
     > Crucial requirement or invariant

     > [!TIP]
     > Helpful command or shortcut
     ```
5. **Header & Branding:**
   - If a project logo or icon exists, center it or place it prominently at the top with a clear subtitle.
6. **Architecture & Visual Overview:**
   - Provide a clean ASCII diagram or Mermaid workflow showing how components connect.
7. **Document Navigation:**
   - Link directly to the Master Traceability Matrix in [`docs/INDEX.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/INDEX.md) and core ADRs.

---

## Reference Archetypes

Draw inspiration from:
- `Azure-Samples/serverless-chat-langchainjs`: Clean feature callouts, architecture flow, and clear local run instructions.
- `Azure-Samples/serverless-recipes-javascript`: Minimalist, table-driven navigation of capabilities.
- `sinedied/run-on-output` & `sinedied/smoke`: Punchy CLI/service overviews with zero wasted prose and clean command snippets.

---

## Standard README Template

```markdown
# AI Teaching Assistant

> Adaptive, Socratic math homework tutor for Grades 3–6 with deterministic symbolic verification and parent supervisory controls.

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![AI-SDLC](https://img.shields.io/badge/AI--SDLC-Gated-success.svg)](AGENTS.md)

---

## Overview

Students often get stuck on homework and seek direct answers without developing conceptual understanding. **AI Teaching Assistant** bridges this gap by providing real-time, adaptive Socratic guidance while strictly preventing answer leakage.

The platform grounds every problem in deterministic mathematical truth via **SymPy Computer Algebra System (CAS)** before hints are generated, and provides parents with supervisory control over answer unlocks and session summaries.

> [!IMPORTANT]
> **Strict Answer Leakage Invariant:** The system guides via diagnostic hints and conceptual models. It does not provide final numerical calculations or complete solutions without verified parent authorization.

---

## Key Features

- **Socratic Dialogue Engine:** Real-time hint streaming ($\le 3\text{s}$ SSE) designed for short student attention spans.
- **Deterministic Truth Grounding:** Pre-generation symbolic verification with SymPy eliminates mathematical hallucination.
- **Parent-Gated Answer Unlocks:** Direct answers require parental approval; includes automatic analogous problem fallbacks.
- **Selective Visual Explanations:** Static diagrams and gated Manim animations reserved strictly for foundational conceptual hurdles.
- **COPPA / FERPA Compliant:** Zero data retention on external model calls and automated student PII redaction.

---

## Architecture & How It Works

```text
Student Worksheet (Photo / Text)
       │
       ▼
[Vision OCR / Extraction] (Confidence Gate ≥ 85%)
       │
       ▼
[SymPy Symbolic CAS] ──▶ Computes exact mathematical ground truth
       │
       ▼
[Fastify Socratic Engine] ──▶ Streams hints via SSE (< 3s)
       │
       ├── Red-Team Answer Leakage Filter (≤ 0.5% leakage)
       └── Parent Notification & Answer Release Gate
```

---

## Progressive Deployment

Per [ADR-002](docs/architecture/adrs/ADR-002-progressive-deployment-plan.md), the system deploys progressively:
1. **Phase 1 (MVP 1 — $0 Cost):** Local Apple Silicon Mac mini running Fastify, local Docker (PostgreSQL 16 + Redis 7), and Cloudflare Tunnel for mobile testing.
2. **Phase 2 (MVP 2 — Lean Cloud):** AWS ECS Fargate tasks in public subnets with RDS PostgreSQL and SQS queue.
3. **Phase 3 (Enterprise):** Hardened multi-AZ VPC with automated worker autoscaling and WAF.

---

## Quickstart (Local Development)

### Prerequisites
- Node.js 20+
- Python 3.11+ (with `sympy`)
- Docker & Docker Compose

### 1. Clone & Install
```bash
git clone https://github.com/your-org/ai-teaching-assistant.git
cd ai-teaching-assistant
npm install
```

### 2. Start Local Services
```bash
docker compose up -d
```

### 3. Run Development Server
```bash
npm run dev
```

---

## Documentation & Knowledge Graph

This repository follows an **Intent-Driven AI-SDLC** where all architectural and product decisions are tracked in a bidirectional knowledge graph:

| Artifact | Purpose | Directory |
|---|---|---|
| **System Scope** | Product vision and target grade bands | [`docs/project-plan/SCOPE.md`](docs/project-plan/SCOPE.md) |
| **Master Index** | Central artifact graph and traceability matrix | [`docs/INDEX.md`](docs/INDEX.md) |
| **ADRs** | Core stack & deployment decisions | [`docs/architecture/adrs/`](docs/architecture/adrs/) |
| **Specs & PRDs** | Functional requirements and user stories | [`docs/project-plan/specs/`](docs/project-plan/specs/) |
| **Agent Rules** | AI pairing and SDLC governance | [`AGENTS.md`](AGENTS.md) |
```
