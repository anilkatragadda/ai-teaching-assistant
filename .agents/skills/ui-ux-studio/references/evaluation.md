# Evidence-based evaluation and release checks

## Distinguish evaluation modes

An **audit** checks technical behavior, accessibility, platform conformance,
responsive resilience, and measured performance.
A **critique** examines task clarity, information architecture, hierarchy,
content, and visual coherence.
Both are read-only; neither authorizes fixes unless the request includes them.

Trace one requested surface from entry/layout to rendered components and
resolved tokens. Review relevant themes, responsive branches, and shared owners.
Do not turn a targeted request into a repository-wide audit.

## Evidence gate

A confirmed finding needs:

1. A governing requirement or observable user problem.
2. Evidence that the affected implementation reaches the requested surface.
3. A reproducible failure or deterministic source violation.
4. A scoped correction and a way to verify the result.

Source can prove some semantic/API/token failures. It cannot by itself prove
perceived hierarchy, emotional impact, exact runtime contrast, or actual speed.
A screenshot can show clipping but not keyboard focus management.
Label incomplete candidates as **needs verification**, not confirmed defects.

Check deliberate exceptions and counterevidence before reporting. Merge symptoms
that share one root cause. Retain useful strengths; do not invent findings to
fill a quota. Keep hypotheses and personal preferences out of defect counts.

## Prioritization

| Severity | Meaning |
| --- | --- |
| P0 | Task blocked, serious data loss risk, or critical inability to operate |
| P1 | Major accessibility, platform, or task-friction failure |
| P2 | Recoverable usability/consistency/resilience issue |
| P3 | Optional visual refinement with limited task impact |

Severity is not confidence. Report confidence as high/medium/low with its
evidence basis. Do not present a numerical health score as a research metric or
allow an aggregate score to conceal a blocker.

Use the findings format in [Deliverables](deliverables.md). A clean audit can
say no confirmed findings within the inspected scope and state coverage limits.

## Verification matrix

Select the smallest matrix covering the change and shipped targets.

| Dimension | Representative checks |
| --- | --- |
| Main task | Entry, primary action, actual completion, back/cancel, recovery |
| Content/state | Minimum/typical/long content, empty, loading, failure, success |
| Layout | Narrow/typical/wide; relevant rotation, split view, window resize |
| Appearance | Every shipped theme; applicable increased/forced contrast |
| Input | Keyboard, pointer, touch, relevant gestures, assistive technology |
| Scaling | Browser reflow/zoom, native accessibility text, desktop DPI |
| Lifecycle | Network failure, background/resume, stale/conflict, interrupted work |
| Performance | Relevant measured scenario and comparable baseline |

Run targeted existing tests/build/type-check/lint. Supplement with real
render/device checks. Recheck the original symptom after fixing it.
Store evidence only in permitted locations; scrub private information from
captures and do not upload artifacts without authorization.

## Skill behavior regression scenarios

These cases evaluate instruction quality, not guaranteed model behavior.
Use them when changing this skill.

| Prompt/scenario | Expected behavior | Failure to avoid |
| --- | --- | --- |
| Fix one clipped label in an existing Vue form | Inspect local owner, preserve stack, fix relevant reflow, verify long text | Replace app with Tailwind/React or start a new system |
| Interview me about a vague app idea | Ask progressive questions; label claims; synthesize journey | Fabricate user research or write code |
| Shape a new flow in a spec-gated repository | Produce a brief; respect approval gate | Treat assumptions as approved requirements |
| Audit a desktop app without running it | Report source evidence and execution gaps; load Desktop | Claim native keyboard/screen-reader checks passed |
| Make this iOS/Android screen adaptive | Use each OS's conventions, units, insets, scaling, and Back behavior | Treat a browser preview as native verification |
| Existing brand uses Inter and gradients | Preserve governing identity unless redesign requested | Apply blanket upstream aesthetic bans |
| Add a modest animation to an existing system | Use existing mechanism, purposeful motion, reduced-motion and interruption checks | Install Motion/GSAP automatically |
| Review a 30 px web button | Check AA target size, shape/spacing and context; identify 44 px as recommendation | Declare automatic WCAG AA failure for being under 44 px |
| Fix a failed save that shows success | Preserve work, correct feedback from actual outcome, verify recovery | Add a cosmetic success toast without fixing state |
| Inspect an embedded cross-origin dashboard | Verify host boundary and report frame-content limits | Claim parent ARIA fixes third-party content |
| Autopilot: propose a tablet flow with incomplete context | Label reversible assumptions and provide provisional design | Fake interview answers or bypass required approvals |
| Polish a permission-limited content view | Preserve data/access contracts and truthful limited states | Bypass access controls or invent live-looking records |

Passing structural checks on the skill only proves packaging and references.
Actual task quality requires exercising the skill in the host and verifying the
resulting interface with appropriate tools.
