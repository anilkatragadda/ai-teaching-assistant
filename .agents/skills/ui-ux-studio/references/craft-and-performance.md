# Visual craft, motion, and measured performance

Refinement preserves the incumbent world. A redesign needs explicit scope.
Read the rendered composition, not just utility-class names.

## Craft checks

| Area | Evaluate | Prefer |
| --- | --- | --- |
| Hierarchy | Can the user find the task and primary action? | Distinct prominence, clear grouping, restrained competing emphasis |
| Layout | Do structure and alignment match content relationships? | Intrinsic layouts, purposeful grouping, predictable rhythm |
| Typography | Can real content be read and scanned? | Coherent roles, scalable text, robust wrapping, tabular numerals for numeric comparison |
| Color | Does each color have a job and adequate contrast? | Semantic roles and independently tested themes |
| Density | Is enough task context visible without overload? | Density appropriate to expertise, input, and frequency |
| Elevation | Does depth explain layering or interaction? | Consistent system elevation rather than arbitrary halos |
| Icons/imagery | Is meaning clear and visual language consistent? | Approved, appropriate assets and a coherent icon family |
| Content | Are claims, labels, and data trustworthy? | Real product language and honest state |

Avoid generic decoration used instead of structure: unnecessary nested cards,
arbitrary gradients, meaningless metrics, excessive badges, or repeated
entrance effects. These are evidence prompts, not bans. Cards, system fonts,
gradients, black, gray, and native springs can all be justified.

For `bolder`/`quieter`, adjust a few expressive axes while preserving task
priority and accessibility. For `distill`, remove redundancy before removing
needed help or recovery. For `delight`, enhance completion or orientation
without delaying work. Never replace factual copy to fit a visual concept.

## Motion contract

Before adding motion, name its purpose: feedback, continuity, changed state,
orientation, or explicitly requested expression. Do not add animation merely
to advertise effort. Existing system transitions may already be enough.

Choose durations/easing for distance, component, platform, and user settings.
Immediate feedback must not wait for a decorative sequence. There is no single
200 ms limit appropriate to all platforms and transitions.

Prefer transform/opacity for web animation, but do not assume all such effects
are free. Verify layer/memory cost. Small bounded paint/layout animations can
be acceptable when justified and measured; avoid continuous expensive work on
large surfaces, animated blur backdrops, and interleaved layout reads/writes.

Use one compatible animation mechanism for the interaction. Batch measurement;
scope temporary layer hints; stop work when offscreen/backgrounded. Respect
reduced motion and keep content usable if animation or an optional API fails.

Test interruption: rapid clicks, route changes, reversal, cancellation, and
unmounting. Final state, accessibility state, focus, and visible content must
remain correct. An animation is not the authority for business state.

## Measure performance

For web, useful default field goals are LCP <= 2.5 seconds, INP <= 200 ms, and
CLS <= 0.1 at the 75th percentile, segmented by mobile/desktop.
These are Core Web Vitals targets, not proof from one local run.
Use real-user evidence where available and permitted; label laboratory results
as lab measurements.

For native/desktop, use platform launch, frame, UI-thread, memory, and energy
measurements. Do not apply browser Core Web Vitals to an entire native app.
Define dataset, device, network, and scenario so before/after results compare.

Identify the cause before optimizing: image decoding, unbounded lists, expensive
re-rendering/recomposition, blocking work, layout thrash, or unnecessary loading.
Use existing caches, asynchronous APIs, and virtualization patterns. Avoid
speculative memoization or a new library without evidence.

## Bounded refinement

Inspect representative layouts/states together. Fix verified root problems in
one coherent batch, then recheck changed behavior. Stop when requested outcomes
and material defects are addressed; optional visual taste is not a reason to
keep rewriting.

If visual tools are unavailable, do not claim hierarchy or delight was verified
from source. Record specific source issues and visual questions separately.
