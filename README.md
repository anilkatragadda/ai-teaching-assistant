# AI Teaching Assistant

> Adaptive, Socratic math homework tutor for Grades 3–6 with deterministic symbolic verification and parent supervisory controls.

[![License](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![AI-SDLC](https://img.shields.io/badge/AI--SDLC-Gated-success.svg)](AGENTS.md)
[![Phase](https://img.shields.io/badge/Deployment-Phase%201%20(Local%20Mac%20mini)-informational.svg)](docs/architecture/adrs/ADR-002-progressive-deployment-plan.md)

---

## Overview

Students often get stuck on homework and seek direct answers without developing conceptual understanding. **AI Teaching Assistant** bridges this gap by providing real-time, adaptive Socratic guidance while strictly preventing answer leakage.

The platform grounds every problem in deterministic mathematical truth via **SymPy Computer Algebra System (CAS)** before hints are generated, and provides parents with supervisory control over answer unlocks and session summaries.

> [!IMPORTANT]
> **Strict Answer Leakage Invariant:** The system guides via diagnostic hints and conceptual models. It does not provide final numerical calculations or complete solutions without verified parent authorization ($\le 0.5\%$ leakage threshold).

---

## Key Features

- **Socratic Dialogue Engine:** Real-time hint streaming ($\le 3\text{s}$ SSE) designed for short student attention spans.
- **Deterministic Truth Grounding:** Pre-generation symbolic verification with SymPy eliminates mathematical hallucinations.
- **Parent-Gated Answer Unlocks:** Direct answers require parental approval; includes automatic analogous problem fallbacks.
- **Selective Visual Scaffolding:** Static diagrams and gated Manim animations reserved strictly for foundational conceptual hurdles.
- **COPPA & FERPA Compliant:** Zero data retention on external model calls and automated student PII redaction.

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

Per [ADR-002](docs/architecture/adrs/ADR-002-progressive-deployment-plan.md), the system deploys progressively to optimize costs and prevent premature cloud spend:

1. **Phase 1 (MVP 1 — $0 Cost):** Local Apple Silicon Mac mini running Fastify, local Docker (`PostgreSQL 16` + `Redis 7`), and Cloudflare Tunnel for mobile testing.
2. **Phase 2 (MVP 2 — Lean Cloud, ~$15–$25/mo):** AWS ECS Fargate tasks in public subnets (zero NAT Gateways) with RDS PostgreSQL and SQS queue.
3. **Phase 3 (Enterprise):** Hardened multi-AZ VPC with automated worker autoscaling, WAF, and formal compliance audits.

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
| **Intent Briefs** | Scoped feature intents (`IB-###`) | [`docs/project-plan/intents/`](docs/project-plan/intents/) |
| **ADRs** | Core stack & deployment decisions (`ADR-###`) | [`docs/architecture/adrs/`](docs/architecture/adrs/) |
| **PRDs** | Functional requirements and user stories (`PRD-###`) | [`docs/project-plan/specs/`](docs/project-plan/specs/) |
| **Tech Specs** | Technical scaffolding & implementation plans (`TECH-###`) | [`docs/architecture/specs/`](docs/architecture/specs/) |
| **Agent Rules** | AI pairing and SDLC governance | [`AGENTS.md`](AGENTS.md) |
