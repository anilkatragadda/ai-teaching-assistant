---
id: ADR-001
title: "Core Technology Stack, Selective Video Harness, and Rendering Pipeline"
type: adr
status: accepted
created: 2026-10-10
updated: 2026-10-10
upstream:
  - "docs/architecture/research/ARN-001-competitive-differentiation-and-moat.md"
  - "docs/project-plan/SCOPE.md"
downstream: []
tags:
  - tech-stack
  - fastify
  - manim
  - video-rendering
  - sympy
  - decision-harness
  - architecture
---

# ADR-001: Core Technology Stack, Selective Video Harness, and Rendering Pipeline

## 0. Artifact Lineage & Traceability
- **Upstream Scope Anchor:** [`docs/project-plan/SCOPE.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/SCOPE.md) (`SCOPE-001`)
- **Upstream Research Note:** [`docs/architecture/research/ARN-001-competitive-differentiation-and-moat.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/research/ARN-001-competitive-differentiation-and-moat.md) (`ARN-001`)

---

## 1. Context and Problem Statement

To provide low-friction homework assistance without falling into the "thin wrapper" trap or running unbounded compute costs, the platform requires an architecture that balances:
1. **Low Interactive Latency:** Fast real-time dialogue (SSE streaming text $\le 3\text{s}$) matching a student's short attention span.
2. **Selective Video Triggering:** Video rendering takes 20–90 seconds and consumes compute. Not every image requires a video; videos must be reserved strictly for deep conceptual explanations.
3. **Deterministic Mathematical Accuracy:** Eliminating hallucinations by verifying mathematical ground truth via symbolic computation (SymPy CAS) **before** generating Socratic guidance.
4. **Execution Safety at Scale:** Ensuring rendering workers run parameterized, audited templates rather than arbitrary, un-sandboxed LLM-generated code.
5. **COPPA / FERPA Compliance:** Isolating child data and enforcing zero-retention policies.

---

## 2. Decision & Architecture Overview

We adopt a decoupled, event-driven multi-service architecture with a **Pre-Generation Symbolic Verification Gate** and a **Selective Video Decision Harness**:

```text
┌─────────────────┐       ┌────────────────────────┐       ┌─────────────────┐
│   Mobile App    │       │   Web / Desktop Canvas │       │   Parent Mobile │
│ (React Native)  │       │     (React Native)     │       │     (Expo)      │
└────────┬────────┘       └───────────┬────────────┘       └────────┬────────┘
         │ Upload Worksheet (Presigned S3) │ Real-time SSE / Sync   │ Parent Approvals
         ▼                            ▼                            ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                    API Gateway & Orchestration (Fastify)                   │
│        • Fastify (TypeScript) on AWS ECS Fargate                           │
│        • Auth0 / Cognito with Verifiable Parental Consent (COPPA)          │
│        • Aurora PostgreSQL (Jobs, sessions) + Redis (Rate limits/cache)    │
└─────────────────────────────────────┬──────────────────────────────────────┘
                                      │
                                      ▼
                    ┌───────────────────────────────────┐
                    │      Vision OCR & Extraction      │
                    │   • Extracts equations & text     │
                    └─────────────────┬─────────────────┘
                                      │
                                      ▼
                    ┌───────────────────────────────────┐
                    │  Pre-Gen SymPy CAS Verification   │
                    │   • Computes symbolic truth       │
                    │   • Validates question solvability│
                    └─────────────────┬─────────────────┘
                                      │ Verified ground truth
                                      ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                  LLM Socratic Engine & Decision Harness                    │
│   • Streams real-time Socratic hints via SSE (< 3s)                        │
│   • Evaluates: Does this problem require a Conceptual Video Explainer?      │
│     - Simple procedural step? ──▶ Stream text only                         │
│     - Deep conceptual hurdle? ──▶ Generate Storyboard JSON                 │
└─────────────────────────────────────┬──────────────────────────────────────┘
                                      │ Storyboard JSON (if triggered)
                                      ▼
                    ┌───────────────────────────────────┐
                    │    Zod Schema Validation Gate     │
                    │   • Strict schema_version check   │
                    └─────────────────┬─────────────────┘
                                      │ Validated payload
                                      ▼
                    ┌───────────────────────────────────┐
                    │       AWS SQS Queue + DLQ         │
                    └─────────────────┬─────────────────┘
                                      │ Worker pull
                                      ▼
                    ┌───────────────────────────────────┐
                    │   Isolated Python Render Pool     │
                    │   • Parameterized Manim templates │
                    │   • Pinned LaTeX, FFmpeg, fonts   │
                    │   • Managed TTS audio narration   │
                    └─────────────────┬─────────────────┘
                                      │ MP4 output
                                      ▼
                    ┌───────────────────────────────────┐
                    │       S3 + CloudFront CDN         │
                    │   • Delivers video asynchronously │
                    │   • Notifies app via push / SSE   │
                    └───────────────────────────────────┘
```

---

## 3. Core Architectural Invariants

### 3.1 The Video Decision Harness: Solving the Author's Challenge
Not every uploaded image or question needs an animated video. Generating video indiscriminately introduces severe queue lag, compute exhaustion, and poor UX.

**Video Trigger Invariant:** The decision harness activates video generation **only** when all three conditions are satisfied:
1. **Pedagogical Intent:** The response requires explaining an **underlying mental model or concept** (e.g., *why* fraction denominators must match, geometric area decomposition, place-value regrouping), NOT for procedural calculations (e.g., $14 \times 3$, single-step arithmetic).
2. **Student State:** The student has encountered a repeated roadblock ($\ge 2$ failed attempts on isomorphic steps), or the parent/student explicitly clicks *"Explain Visually"*.
3. **Template Match:** A validated, parameterized template exists in the template registry for the concept.

### 3.2 Resolving the Behavioral Trap (The 90-Second Latency Problem)
Because Manim video rendering takes 20–90 seconds while a student's attention span is 3–10 seconds:
- **Text / Audio SSE is the Real-Time Tutor:** Delivers immediate guidance ($\le 3\text{s}$) so the student never sits waiting at a blocked screen.
- **Video is the Asynchronous Anchor:**
  - Delivered via an in-canvas notification banner when ready (*"Visual explanation ready — tap to watch"*).
  - Automatically embedded in the **Parent End-of-Session Summary** as an educational highlight of concepts covered.

### 3.3 Pre-Generation SymPy Truth Grounding
To prevent the LLM from outputting mathematically flawed hints or videos:
1. The extracted problem statement is processed by **SymPy** before LLM prompt assembly.
2. The exact symbolic solution, intermediate factorization, and roots are injected into the LLM system prompt as verified grounding truth.
3. If SymPy cannot solve or verify the problem (or OCR confidence is below $85\%$), the system abstains from generating a video and alerts the student to confirm the problem statement.

### 3.4 Parameterized Templates, Never LLM-Generated Code
The Python rendering workers execute **fixed, audited Manim scene templates** (15–30 core math models: number line, fraction bar, area model, coordinate transformation).
- Workers receive sanitized parameters (floats, strings, LaTeX labels).
- **Prohibited:** Arbitrary LLM-generated Python code (`exec`/`eval` is forbidden).
- If no template matches, the system gracefully falls back to Tier 2 or Tier 3.

### 3.5 Three-Tier Visual Scaffolding Cascade
```text
Tier 1: Full Manim Video (Rendered when conceptual template matches and criteria met)
  │ (No template match or low queue capacity)
  ▼
Tier 2: Static Visual Scaffolding (Instant SVG, Matplotlib, or KaTeX diagram < 500ms)
  │ (Non-visual problem)
  ▼
Tier 3: Structured Socratic Text Dialogue (Immediate step-by-step guidance)
```

### 3.6 Canonicalized Deduplication Caching
In elementary and middle school homework, up to $80\%$ of curriculum problems are identical or isomorphic:
- The Redis and S3 cache is keyed by **Canonical Problem Representation**:
  $$\text{CacheKey} = \text{hash}(\text{normalized\_equation}, \text{concept\_id}, \text{grade\_level})$$
- When a match is found in the cache, the CloudFront video URL is returned in $< 100\text{ms}$, bypassing SQS and Fargate compute entirely.

### 3.7 Golden-Frame Regression Testing
All templates are guarded by golden-frame test suites in CI:
- Fixed test storyboards are rendered during builds.
- Key frames are compared against baseline PNGs with a pixel-diff tolerance $\le 0.1\%$.

---

## 4. Consequences and Trade-Offs

### Positive
- **Predictable Compute Costs:** Selective triggering and canonical caching keep monthly compute costs within sustainable subscription margins ($\le \$2.50$/student/month).
- **Zero RCE Attack Surface:** Strict parameter injection eliminates malicious code execution.
- **Zero Mathematical Hallucinations:** SymPy CAS grounds all explanations in symbolic fact.
- **Responsive UX:** Students receive immediate text dialogue; slow video renders do not block homework flow.

### Trade-Offs
- **Asynchronous Delivery:** Video arrives after the initial text turn; the UI must gracefully notify students without disrupting their concentration.
- **Template Authoring Overhead:** Engineering must curate 15–30 robust templates for Grades 3–6 before launching video capabilities.
