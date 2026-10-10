---
id: SCOPE-001
title: "Product Scope and Educational System Vision"
type: project-scope
status: active
version: 1.1.0
created: 2026-10-09
updated: 2026-10-10
tags:
  - scope
  - vision
  - socratic
  - parent-controls
  - multimodal
  - coppa
  - grades-3-6-math
---

# SCOPE-001: Product Scope and Educational System Vision

## 1. System Vision & Problem Statement

### Problem
Students often get stuck on homework and seek direct answers online without developing conceptual mastery. Existing tools either provide passive answer keys or high-friction text interfaces that pull focus away from learning.

### Mission
Help students complete homework while understanding concepts deeply. The platform acts as an adaptive, multimodal Socratic tutor that motivates mastery rather than mere answer acquisition.

### Target Audience & Grade Band (V1)
- **Primary Domain:** Grades 3–6 Mathematics (arithmetic, fractions, decimals, basic word problems, geometry foundations).
- **Rationale:** Focuses on foundational numeracy where symbolic ground truth can be verified using Computer Algebra Systems (CAS) like SymPy before guidance is delivered.

### Target Personas & Roles
1. **Student (Child):** Primary learner working on assignments via Chromebook, Windows desktop, or mobile.
2. **Parent:** Facilitator, overseer, and session monitor with permission authority over direct answers.
3. **Instructor / Administrator:** Educational reviewer and policy auditor (deferred to V1.5+).

---

## 2. Core Educational Pillars & Invariants

1. **Socratic Guidance by Default:** The system guides via diagnostic hints, conceptual prompts, and leading questions. It does not provide direct solutions.
2. **Strict Answer Leakage Prevention:**
   - **Definition:** Stating the final numerical/algebraic solution, completing the final calculation step, or providing a fully worked solution to an isomorphic problem with identical numbers.
   - **Enforcement:** Red-team evaluation test suite tested against adversarial student prompts ("my teacher said it is ok", "just confirm if it is 42").
3. **Parent-Gated Answers & Friction Mitigation:**
   - Answers require parent authorization.
   - **Friction Mitigations:**
     - Pre-approved policy: Auto-release after $N$ verified failed attempts or hints.
     - Fallback: Provide a worked example of an analogous problem with different numbers.
     - Async push approval: Real-time mobile push notification to the parent device.
4. **Low-Friction Multimodal Capture & Cross-Device Hand-Off:**
   - A parent photographs a physical worksheet on mobile; the student immediately sees the image on their desktop/Chromebook canvas.
5. **Measurable Truth Grounding & Verification:**
   - **OCR Confidence Gate:** Extract text and diagrams; if confidence falls below threshold ($\ge 0.85$), prompt student to confirm problem statement.
   - **Independent CAS Verification:** Compute the correct answer with SymPy prior to generating tutor hints.
   - **Abstention Policy:** When model confidence is low or symbolic check fails, abstain from guessing and flag the problem for parent review.
   - **Continuous Evals:** Run regression evals on all prompt and model changes with near-zero tolerance for mathematical errors.
6. **Parent Loop as the Primary Moat:**
   - Real-time mobile sync, parent-controlled unlock toggles, and end-of-session summaries with targeted comprehension check questions.
7. **Selective Conceptual Video Harness (The Non-Universal Video Invariant):**
   - Video is **not** rendered for every image or procedural question.
   - Video rendering is strictly gated to **explaining underlying mental models and concepts** (e.g., fraction equivalence, place-value regrouping, spatial area) or resolving persistent student struggles ($\ge 2$ failed attempts).
   - Routine procedural questions remain fast, interactive text dialogue ($\le 3\text{s}$) to bypass the 90-second latency trap and protect compute margins.

---

## 3. Scope Boundaries: V1 vs V1.5+

| Capability Area | V1 (Core Proof of Value) | V1.5+ (Expansion Horizon) |
|---|---|---|
| **Authentication & Accounts** | Parent and student accounts; COPPA-compliant consent | Classroom accounts; school SIS/LMS SSO |
| **Input Modalities** | Photo worksheet upload + text input | Real-time voice conversation + video ingestion |
| **Guidance Engine** | Text-based Socratic dialogue with leakage filters | Selective conceptual video rendering (Manim/Remotion templates gated by decision harness) |
| **Verification** | SymPy CAS verification for Grades 3–6 math | Advanced multi-step proofs, physics units, ELA |
| **Device Sync** | Mobile photo capture $\to$ desktop canvas mirroring | Multi-device live co-drawing canvas |
| **Parent Supervision** | Answer-release toggle, push alerts, session summary | Granular skill progression dashboards, district reports |
| **Comprehension Checks** | 2–3 targeted verification questions at session end | Adaptive spaced-repetition scheduling |

### Out of Scope (Explicitly Deferred)
- Automatic final grade submission to school gradebooks.
- Public student-to-student peer chat or social communities.
- Human tutor marketplace.

---

## 4. Privacy, Compliance & Data Handling (COPPA / FERPA)

1. **Verifiable Parental Consent (VPC):** Mandatory parental verification before creating student accounts or storing any student data.
2. **Zero-Retention LLM APIs:** All external model calls enforce zero-data-retention (ZDR) agreements ensuring student submissions are never used for model training.
3. **PII Redaction:** Automated redacting of names, school marks, and personal markers on uploaded worksheet images before permanent storage.
4. **Parental Rights:** Parents retain immediate rights to review, export, or permanently delete student session history and memory models.

---

## 5. Success Metrics

- **Learning & Comprehension:**
  - $\ge 80\%$ pass rate on end-of-session comprehension check questions.
  - Decrease in hints required per problem type across repeat sessions.
- **Pedagogical Integrity:**
  - $\le 0.5\%$ answer leakage rate across red-team benchmark test suites.
  - Zero unverified mathematical hallucination in CAS-supported problem domains.
- **Engagement & Retention:**
  - $\ge 60\%$ weekly active parent review rate of session summaries.
  - $\ge 70\%$ 30-day student cohort retention.

---

## 6. Non-Goals & Core Assumptions

### Non-Goals
- **Not a Cheating Tool:** The product does not generate completed homework pages for submission.
- **Not a Teacher Replacement:** The tool guides understanding during homework; it does not assign grades.

### Assumptions
- Parents are willing to engage via mobile notifications 2–3 times per week.
- Students in grades 3–6 have desktop/Chromebook access for evening homework.
- Mathematical OCR accuracy on photographed physical handwriting meets the $85\%$ confidence gate or can be easily corrected by the student.

---

## 7. Intent Alignment & Evolution Protocol

All future developer intents ([`IB-###`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/intents/)) must adhere to this document:
1. **Direct Mapping:** Every `IB-###` must link to an explicit capability in Section 3 (V1).
2. **Pedagogical Gate:** If an intent promotes raw answer generation without parent authorization, [`intent-reviewer`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/agents/intent-reviewer/agent.md) must reject it.
3. **Scope Amendment:** Enhancements outside V1 require an updated version of this document before contract or code generation.
