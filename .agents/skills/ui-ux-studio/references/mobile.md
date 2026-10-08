# Mobile and adaptive native apps

Apply to native iOS/iPadOS and Android, including React Native and Flutter.
Mobile web uses [Web](web.md), not native controls copied into HTML.
Share brand and task semantics, but preserve the shipped OS's expected behavior.

## Platform-specific behavior

| Concern | iOS/iPadOS | Android |
| --- | --- | --- |
| Navigation | Platform navigation stacks, tabs, sheets; preserve system back affordances | Back button/gesture and predictive Back where supported; appropriate navigation bar/rail/drawer |
| Typography | Semantic text styles and Dynamic Type; scaled custom fonts when justified | Material/type-system roles and scalable sp text |
| Color/theme | Semantic system colors and materials where appropriate | Material color roles; dynamic color only when it fits, with static fallback |
| Controls | Platform control semantics and familiar actions | Material/platform controls and familiar actions |
| Icons | Consistent platform-aware family, often SF Symbols | Consistent platform-aware family, often Material Symbols |
| Tap targets | Studio default at least 44 by 44 pt | At least 48 by 48 dp |
| Accessibility | VoiceOver, Reduce Motion, larger text, increased contrast | TalkBack, font scale, animation/accessibility settings |

Do not enforce a universal icon library or identical navigation shell across
OSes. A common cross-platform design system still owes users OS gestures,
insets, accessibility, and expected interaction semantics.
Current Apple HIG distinguishes default and minimum control sizes; do not
report every sub-44 pt target as an automatic HIG violation. Use the studio's
44 pt comfort default unless a justified approved platform control governs.

## Insets, keyboard, and input

Keep actionable content clear of cutouts, status/navigation bars, home
indicators, and the IME. Decorative backgrounds may extend edge-to-edge while
content respects insets. Avoid double-counted inset padding.

Focus the appropriate field and keep it visible when the keyboard opens.
Use relevant keyboard types/autofill, return-key actions, and a reliable
dismissal path. Never depend on hover. Ensure gesture recognizers do not block
system Back, scrolling, or nested control interaction.

## Adapt beyond phones

Use window/size-class information rather than a hardcoded physical device
assumption. Adapt navigation and master/detail composition to tablets,
foldables, split-screen, rotation, and resizable windows where supported.
Avoid stretching a narrow phone column across a large display or placing
essential controls across a fold hinge.

Maintain meaningful reading widths and touch reach. Make selection, filters,
and current detail survive a layout transition when the task contract requires.
Honor an intentional orientation restriction rather than removing it blindly.

## Lifecycle and trust

Design for background/resume, process recreation, interrupted login, denied
permissions, connectivity loss, and unfinished drafts. State whether work is
local, syncing, failed, or safely stored. Do not claim offline support without
a real data/synchronization implementation.

Request permissions at a relevant moment, explain their benefit, and provide
usable denial/revocation states. Do not fabricate platform permission strings
or introduce new permission scope as a cosmetic change.

Keep notifications, haptics, and badges meaningful and configurable where
appropriate. Avoid unnecessary vibration or persistent promotional interruption.

## Implementation and performance

Use the detected framework's accessibility, navigation, insets, and lifecycle
APIs. Prefer existing platform primitives over hand-built approximations.
Measure list virtualization, image decoding, launch work, recomposition/rendering,
and gesture responsiveness using appropriate native tooling.

Match frame-time budgets to device refresh rate: approximately 16.7 ms at 60 Hz
and 8.3 ms at 120 Hz. These are diagnostic frame budgets, not a universal
promise that all work must complete within one frame.

## Verification

Build and run the actual target app. Inspect a representative phone, tablet
if shipped, both appearances if supported, large accessibility text, keyboard,
Back/dismissal, errors, and interrupted lifecycle.

Use simulator/emulator captures for native visual evidence, not a responsive
browser preview. Run assistive technology checks on the actual platform.
Identify the selected device; do not change a shared device's global settings
without permission, and restore any settings changed for testing.
Emulator screenshots do not establish hardware gesture or performance quality.
