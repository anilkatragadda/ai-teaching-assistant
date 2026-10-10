# Deliverable contracts

Use the smallest format that makes the result actionable. Do not create files
by default. When persistence is requested, use the repository's established
destination and format; do not overwrite approved specs or accepted decisions.
These are output shapes, not mandatory document filenames.

## Discovery synthesis

```text
User/job/context:
Current workflow and reported friction:
Evidence and confidence:
Journey: trigger -> key steps -> completion -> recovery
Opportunities linked to friction:
Assumptions and unknowns:
Next validation activity or focused interview questions:
```

Separate reported facts from hypotheses. Do not default to a backlog.

## Design Brief (`UI-###`)

When persisting a UI/UX specification, save as `docs/architecture/ui/UI-###-<slug>.md`:

```markdown
---
id: UI-###
title: "UI/UX Design Spec: [Feature / Surface Name]"
type: ui-design-spec
status: proposed
created: YYYY-MM-DD
updated: YYYY-MM-DD
upstream:
  - "docs/project-plan/intents/IB-###-<slug>.md"
downstream:
  - "docs/project-plan/specs/PRD-###-<slug>.md"
  - "docs/project-plan/tasks/TASK-###-<slug>.md"
tags:
  - [ui, ux, design-system, accessibility]
---

# UI-###: UI/UX Design Spec — [Feature / Surface Name]

## 0. Artifact Lineage & Traceability
- **Upstream Intent Brief:** [`IB-###-<slug>.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/intents/IB-###-<slug>.md)
- **Supporting Research Note:** [`ARN-###-<slug>.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/architecture/research/ARN-###-<slug>.md)
- **Target Downstream Spec:** [`PRD-###-<slug>.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/project-plan/specs/PRD-###-<slug>.md)

## 1. Context & Scope
- **Target surface, platform(s), stack:** [e.g., Student Workspace, Web, React/TypeScript]
- **User job & primary outcome:** [Clear pedagogical goal]
- **Governing design/spec sources:** [Links to existing design system or ADRs]
- **Prototyping Source (if any):** [e.g., Google Stitch prototype URL / token export]

## 2. Experience & Screen Topology
- **Flow & Information Hierarchy:** [Step-by-step user journey]
- **Component & State Inventory:** [Loading, empty, error, active, success states]
- **Content Ranges & Localization:** [Min/typical/max lengths, Socratic feedback bounds]

## 3. Design System & Visual Tokens
- **Chosen Visual Direction:** [Rationale for aesthetics, cognitive load reduction]
- **Token Mappings:** [Semantic colors, typography, spacing, radius, elevation]
- **Reusable Component Owners:** [Existing or proposed primitives]

## 4. Accessibility & Platform Invariants
- **WCAG 2.1 AA Checklist:** [Contrast ratios, keyboard focus ring, screen-reader text]
- **Platform Conventions:** [Touch targets, safe areas, responsive breakpoints]

## 5. Acceptance Criteria & Verification
- **Testable Criteria:** [Observable UI states that must pass]
- **Verification Plan:** [Automated checks, Chrome DevTools audit, keyboard test]
- **Out of Scope & Deferred:** [What is intentionally deferred]
```

## Design-system proposal or documented baseline

```text
Status: observed baseline / proposed change / accepted decision
Scope and governing sources:
Visual principles tied to user context:
Token roles and existing definitions:
Theme/platform mappings:
Typography, spacing, elevation, icon, and motion roles:
Component semantics, variants, states, and content limits:
Exceptions and migration impact:
Validation and open decisions:
```

For observed documentation, include only evidence-supported rules.
For new designs, mark proposals separately and validate proposed pairs/scales.
Preserve the project's machine-readable schema if it has one.

## Audit or critique

State inspected surface, evidence type, coverage, and limitations, then:

| Severity | Finding / user impact | Evidence | Confidence | Correction | Verification |
| --- | --- | --- | --- | --- | --- |
| P1 | Specific observable problem | File:line, route/state, capture or reproduction | High/medium/low and basis | Exact scoped change | Test or device check |

Use one row per root cause. Source line citations need real current locations.
Include strengths briefly and separate unverified candidates from findings.
Do not write application code during a read-only review.

## Implementation handoff

Lead with the delivered behavior and meaningful design change. Name changed
surfaces or artifacts when useful. State material assumptions, placeholders,
unresolved issues, and unavailable verification. Do not equate a successful
build with verified UX.

Keep detailed test/evidence records in the repository's normal reporting format
when requested. Do not create extra planning/report files as a side effect of
a narrow implementation.

## Acceptance-criteria examples

| Need | Observable criterion |
| --- | --- |
| Reliable form recovery | A failed request keeps entered values, shows the failure, and allows a successful retry without duplicate submission |
| Keyboard-operable dialog | Open, complete, cancel, and return focus using the keyboard; focus never escapes into inert background |
| Robust text | Essential labels remain readable at supported narrow width and text scale with long localized content |
| Adaptive mobile flow | Phone/tablet composition keeps navigation and current task state; keyboard does not cover the active field |
| Desktop editing | Primary action is reachable via visible UI and keyboard; unsaved close and undo follow the approved contract |
| Honest chart | Units, period, missing data, and legend are understandable without relying on color alone |

## Minimum evidence record

When evidence is needed, record target, revision if available, tool/device,
layout/scale/theme, state/input path, expected outcome, observed outcome,
artifact location, and remaining limitations.
Do not expose credentials, personal information, or confidential content in
captures or reports.
