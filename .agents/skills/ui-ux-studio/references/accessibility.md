# Accessibility requirements and verification

Treat accessibility as part of completing the user task, not a separate polish
option. For web, target WCAG 2.2 AA unless the repository requires a stronger
standard. For native, apply platform accessibility APIs and user settings.
These checks are not exhaustive and do not constitute certification.

## Quantitative checks

| Check | Requirement or guidance | Qualification |
| --- | --- | --- |
| Web normal text | Contrast at least 4.5:1 | Evaluate actual rendered background, including overlays |
| Web large text | Contrast at least 3:1 | WCAG large text: at least 18 pt regular or 14 pt bold, roughly 24/18.67 CSS px |
| Meaningful web graphics/control indicators | At least 3:1 against adjacent colors | Apply WCAG non-text contrast scope/exceptions; not every decorative border |
| Web pointer targets | At least 24 by 24 CSS px under WCAG 2.2 AA | Criterion 2.5.8 has spacing, inline, equivalent, user-agent, and essential exceptions |
| Touch-friendly web targets | Aim for at least 44 by 44 CSS px | Recommended studio default; not a claim that AA universally mandates 44 px |
| iOS/iPadOS touch targets | Prefer at least 44 by 44 pt | Studio comfort default; current Apple HIG distinguishes 44 pt default from 28 pt minimum |
| Android touch targets | At least 48 by 48 dp | Verify actual hit region and avoid overlapping expanded areas |
| Web resize/reflow | Text resize to 200%; reflow at 320 CSS px width | Respect WCAG scope/exceptions for essential two-dimensional content |

Do not convert pt or dp directly into a universal CSS target size. Prefer
normal-text contrast for ordinary UI text on native platforms; verify the
applicable platform standard before applying large-text exceptions.
Inactive controls and purely decorative elements have contrast exceptions;
still make their purpose and unavailability understandable.

## Semantics and assistive technology

Prefer semantic native controls before ARIA/custom accessibility roles.
Every control needs a meaningful name and appropriate role/state/value.
Keep accessible names consistent with visible labels for speech input.
Decorative imagery is hidden or has empty alternatives; meaningful content
gets context-appropriate alternatives. Do not duplicate adjacent spoken labels.

Use structured headings, landmarks, lists, and table headers on web.
Ensure semantic reading order matches the task; visual CSS reordering must
not produce a contradictory focus or reading sequence.

For status/progress, announce meaningful changes without flooding live regions.
Critical errors need persistent, discoverable content, not just an announcement.
Use appropriate language metadata and caption/transcript support for media.

## Keyboard and focus

Complete the main task without a pointer. Use predictable Tab order and widget
arrow-key behavior from established platform patterns. No positive `tabindex`.
Custom shortcuts must not interfere with text editing, assistive technology,
or browser/OS conventions; support remapping/disablement where relevant.

Focus must be visible and not hidden by sticky UI. Modal dialogs need meaningful
initial focus, contained focus, a dismissal path where appropriate, and sensible
focus restoration. Nonmodal popovers should not receive a modal focus trap.
After deletion or navigation, move focus to a logical surviving location.

Provide alternatives to drag, swipe, complex gestures, and hover-only content.
Touch targets must remain distinct when hit areas are expanded.

## Text, motion, and user settings

Respect Dynamic Type, Android font scale, desktop display scaling, browser zoom,
and user text-spacing overrides without losing essential information.
Avoid fixed-height text containers and disabling zoom.

Honor reduced motion, increased contrast, and forced-color settings where
applicable. Do not erase system focus indicators. Nonessential animation may
be removed; necessary transitions may use a reduced alternative.
Auto-updating/rotating content needs applicable pause/stop controls.
Avoid flashing hazards and autoplaying audio.

## Forms and authentication

Labels, hints, required status, errors, and constraints must be programmatically
available. Expose invalid state only when meaningful. Allow password managers
and paste; do not make memorization or puzzle-solving the only login path.
Avoid unnecessary repeated data entry within the same process.
Do not announce every keystroke or move focus on each validation change.

## Verify, do not infer

Use an available automated checker, then manually exercise keyboard paths,
focus transitions, text enlargement, and the target screen reader.
For native apps, use VoiceOver, TalkBack, Narrator, or the platform accessibility
inspector as appropriate. Record source-only checks separately from execution.

Measure contrast against computed/composited colors rather than an isolated
palette. Measure hit regions rather than just visible icon size.
Check main flows and errors in every shipped theme and materially different
layout. Automated results or screenshots alone cannot prove WCAG conformance.

Standards and platform references are linked in
[Source analysis](source-analysis.md). Check current guidance when auditing a
specific compliance requirement; do not cite this checklist as the standard.
