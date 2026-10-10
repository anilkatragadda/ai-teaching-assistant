# Web, responsive interfaces, and PWAs

## Platform and architecture

Detect the actual framework and version, render mode, routing, component library,
styles, and test tools. Preserve established browser semantics and component
APIs. Do not introduce React/Tailwind into an unrelated stack.
Use progressive enhancement and stable server/client rendering where relevant.
Never hide a hydration/state failure behind a cosmetic change.

## Responsive composition

Choose breakpoints from content and available space, not device names alone.
Recompose toolbars, navigation, tables, and details instead of shrinking them.
Use readable maximum widths, fluid gutters, and intrinsic sizing.

Test 320 CSS px reflow, representative small phone, tablet, desktop, and wide
layouts when applicable. Include zoom, long localized text, and coarse pointers.
Essential two-dimensional tables/maps may need localized scrolling with clear
affordances; avoid unintended whole-page horizontal scrolling.

Use dynamic viewport behavior and safe-area insets where necessary, with
appropriate fallbacks for supported browsers. Keep focus and content clear of
sticky headers, fixed actions, on-screen keyboards, and browser chrome.
Do not blanket-replace every full-height container without inspecting its job.

## Browser behavior

Use real URLs for navigation, meaningful document titles, expected Back/Forward,
and operable deep links. Preserve standard open-in-new-tab and modified-click
behavior. Avoid fake links, unwanted scroll resets, and hover-only controls.

Keep form labels, native validation strategy, focus, dialog semantics, and
accessible component behavior coherent. A browser screenshot is insufficient
to verify these interactions.

For embedded dashboards or third-party iframes, test frame titles, loading/error
feedback, keyboard entry/exit, sizing, and approved authentication flows.
Do not pretend parent-page ARIA fixes the contents of a cross-origin frame.
Respect existing token/privacy contracts and display unavailable verification.

## Metadata and discoverability

For searchable/shareable surfaces, follow the framework's existing metadata
owner. Verify unique titles, relevant descriptions, canonical URLs, and
consistent Open Graph/share URLs and assets. Use valid language metadata.
Structured data must match real rendered content, not invented claims.

Private/staging surfaces need deliberate indexing policy, but `noindex` and
robots directives are **not access control**. Do not put private account
content into public metadata or social images. Test public previews only when
authorized; do not upload private URLs to external inspection services.

For PWAs, verify manifest/icons, installed-window behavior, update UX, and
explicit offline/synchronization states if these capabilities are in scope.
Do not add a service worker as an incidental visual refinement.

## Performance and verification

Reserve media space, use appropriately sized responsive images, prioritize
critical content, and avoid lazy-loading the likely LCP image by default.
Use existing loading, cache, and code-splitting patterns. Virtualize only where
scale warrants it and keyboard/assistive behavior remains intact.

Use the browser/devtools or existing end-to-end runner for representative
layouts, states, keyboard paths, and network failure. Check supported browser
engines where the change involves compatibility-sensitive APIs.
See [Craft and performance](craft-and-performance.md) for metrics and motion.
