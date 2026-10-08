# Interaction, content, and production resilience

## Navigation and information architecture

Organize destinations by user goals, not backend service names. Make location,
selected state, back behavior, and task exit predictable. Use links for
navigation and buttons for actions on web; native navigation on native apps.

Keep deep links and browser/system history meaningful. Preserve filters,
scroll position, selection, and drafts when returning if the product contract
requires it. Scope shortcuts and gestures; do not steal platform conventions.
Offer visible alternatives to hover, swipe, drag, long press, or shortcuts.

## Forms and task feedback

Use persistent labels, appropriate input types, autocomplete, and clear units.
State requirements before submission. Allow paste, password managers, and
accessible authentication. Preserve entered values through validation/network
failure; distinguish invalid input from service failure.

Show field errors near their fields and associate them programmatically.
For multiple errors, use a navigable summary when appropriate; focus after
submission should help recovery, not unexpectedly jump during typing.
Explain disabled actions when the reason is not obvious.

Distinguish queued, pending, saved, failed, and cancelled. Do not display success
before the relevant operation succeeds. Prevent duplicate consequential
submissions; do not disable unrelated navigation while one operation is pending.
Use optimistic updates only with a justified contract and visible rollback.

## State inventory

Include only applicable states, but do not omit material failures.

| State | User question | Required design response |
| --- | --- | --- |
| Loading | Is anything happening? | Honest progress, stable space, relevant cancellation |
| Empty/new | How do I start? | Explain purpose and one useful first action |
| Empty/filter | Why did results disappear? | Show active criteria and a reset path |
| Error | What failed, and what can I do? | Specific failure, preserved work, appropriate recovery |
| Success | Did it complete? | Confirm the actual result without unnecessary interruption |
| Permission-limited | Why is this unavailable? | Safe explanation and an approved access path |
| Offline | Is my work saved? | Explicit local/remote status and synchronization policy |
| Stale/conflicted | Is this current? | Freshness and a conflict-resolution path |
| Interrupted | Can I continue? | Restore meaningful state or explain what was lost |

Avoid blanket retries. Authentication, authorization, validation, conflicts,
rate limits, and server failures need different recovery. Do not expose
sensitive backend details in copy.

## Consequential actions

Prefer undo for safely reversible actions when supported. Use explicit,
consequence-specific confirmation for irreversible or high-impact actions.
Do not require a modal for every deletion or style all warnings as emergencies.
Keep safe exit/cancel available; protect unsaved work without trapping users.

For multi-step flows, show meaningful progress, back/edit paths, and a review
step when consequences warrant it. Never hide pricing, consent, permissions,
or material consequences behind visual tricks.

## Onboarding and copy

Let people achieve a useful outcome quickly. Ask for permissions when their
benefit is clear and the capability is needed; honor denial gracefully.
Allow skipping nonessential tours and expose later help.

Write controls as actions, messages as facts, and errors as problem plus
recovery. Avoid technical status codes as the only explanation. Keep essential
feedback persistent enough to act upon; a disappearing toast is not an adequate
sole record of a failed payment, save, or export.

## Content resilience and localization

Use real or explicitly labeled fixture content. Exercise long names, long
identifiers, URLs, missing values, zero, negative values, large numbers, many
items, and translated text. Distinguish unknown data from zero.

Allow essential content to wrap. Truncation needs an operable full-value path
for keyboard, pointer, touch, and assistive technology users; a hover tooltip
alone is insufficient. Wrapping/balancing enhancements must degrade naturally.

Use locale-aware dates, numbers, currency, time zones, and pluralization.
Avoid concatenated translated sentences. Test right-to-left layout where
supported; mirror directional affordances when meaningful, not all symbols.
Do not treat pseudo-localization as proof of translation quality.

## Tables, charts, and analytics

Choose the visualization from the question: trend, comparison, distribution,
composition, relationship, or exact lookup. Do not use charts as decoration.
Show units, period, freshness, uncertainty, and provenance where relevant.
Never invent data to make a live-looking dashboard convincing.

Use labels, patterns, shapes, and accessible summaries, not color alone.
Provide a table/text alternative when appropriate. Keep tooltips available
without precision pointing; ensure legends and filters are operable.
Explain missing data and partial loading separately from empty results.

For dense grids, use correct header/sort/selection semantics, stable row
identity, predictable focus, and clear bulk-selection scope. Virtualization
must preserve navigation, semantics, and meaningful announcements.
