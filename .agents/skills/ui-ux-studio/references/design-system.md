# Design direction, brand, and reusable systems

## Discover governing owners

Read accepted design/brand documentation, current tokens/themes, component
primitives, and the requested surface's actual consumers. Prove relationships
through imports, configuration, composition, or computed styles. Similar names
and repeated literals alone do not establish a shared design contract.

Record current owner, source, scope, themes, variants, and explicit exceptions.
Do not promote accidental styling into a canonical rule. Missing `DESIGN.md`
does not make an established application greenfield.

For documentation-only requests, report current evidence. For a new system,
label new decisions as proposed until accepted. Never replace existing accepted
rules merely because another system is more fashionable.

## Choose direction from the use scene

| Surface/job | Prioritize | Suitable structural starting point | Common failure |
| --- | --- | --- | --- |
| Repeated operational work | Scanability, speed, predictable state | Task toolbar, filters, results, contextual details | Spacious marketing cards hiding critical data |
| Comparison/decision | Comparable evidence and transparent tradeoffs | Consistent comparison fields and a clear next step | Decorative claims without decision support |
| Reading/learning | Comprehension and orientation | Content hierarchy, readable measure, in-page navigation | Wide paragraphs and competing calls to action |
| Creation/editing | Workspace continuity and recovery | Canvas/editor, tools, properties, saved-state feedback | Modals interrupting every edit |
| Mobile field task | Reachability and interruption tolerance | Short task steps, clear progress, resumable draft | Hover-only actions and fragile connectivity assumptions |
| Catalog/commerce | Findability and purchase confidence | Search/filter, comparable items, detail, checkout | Fake scarcity or hidden cost |
| Showcase/exploration | Content character and discovery | Artifact-led composition with restrained navigation | Effects overpowering the work |

These are hypotheses, not automatic templates. Industry does not determine
palette, typeface, light/dark appearance, or layout.

For useful variants, keep product truth and task flow constant. Change at most
a few meaningful axes: hierarchy/composition, density, visual character, or
motion emphasis. Explain user benefit, tradeoff, accessibility, performance,
and implementation cost. Do not generate twenty arbitrary themes.

## Token architecture

Reuse the repository's schema. When creating a new system, distinguish:

| Layer | Responsibility | Illustrative role |
| --- | --- | --- |
| Primitive | Raw values and scales | Neutral color step, spacing increment |
| Semantic | Purpose across themes/platforms | Content-primary, surface-raised, action-danger |
| Component | Specific interaction needs | Button-primary-background, field-error-border |

The names above are examples, not assertions about existing tokens.
Use semantic roles in consumers; resolve roles independently for light, dark,
increased-contrast, and disabled states. Avoid cyclic aliases and preserve
type-safe token definitions. Prefer existing platform colors/material roles
where they supply system adaptation.

Maintain roles for typography, spacing, radius, elevation, icon size, motion,
layering, and focus. Do not introduce a token for every one-off literal.
Use the existing design-token export standard if present; do not invent a
tool-specific YAML format or claim exporter compatibility without validation.

## Generative Prototyping & Token Extraction (Google Stitch)

When using **Google Stitch** (`stitch.withgoogle.com`, Stitch MCP `https://stitch.googleapis.com/mcp`, or `@_davideast/stitch-mcp`) for generative UI and vibe design:
1. **Prompt for Tone & Structure:** Specify the pedagogical context (e.g. Socratic tutor, split-pane coding canvas, quiet distraction-free focus, accessible light/dark themes).
2. **Extract to Semantic Tokens:** Map Stitch's raw hex values and typographic scales into our 3-tier token architecture (`Primitive -> Semantic -> Component`).
3. **Validate Craft & Contrast:** Verify contrast ratios before accepting any Stitch palette. Generative palettes frequently fail WCAG AA contrast (4.5:1 for text, 3:1 for large text/icons). Adjust lightness/saturation to ensure compliance.
4. **Zero Proprietary Lock-in:** Translate Stitch outputs into clean, accessible web components (vanilla CSS custom properties, React/TypeScript) native to this repository.

## Typography and color

Choose fonts for readability, language coverage, licensing, platform fidelity,
brand, and loading cost. System fonts and common fonts can be the right choice;
novelty is not a requirement. Use role-based type scales and scalable units.
Allow fallbacks without destroying layout; test real localized copy.

Give colors semantic jobs. Separate brand/accent from success, warning, error,
selection, and focus. Check every meaningful foreground/background pair,
including overlays and interaction states. Never choose color by stereotype or
assume a palette is accessible before measuring it.

Define data-visualization palettes separately from action/status colors.
Provide non-color distinctions for categories and states.

## Component contracts

For each reusable component, capture purpose, variants, content rules,
accessibility semantics, keyboard/touch behavior, focus ownership, and applicable
default/hover/pressed/focused/selected/disabled/loading/error states.
Define responsive behavior and realistic content boundaries.

Reuse an existing primitive when it fits. Extract a shared owner only when
multiple real consumers need the same semantics and behavior, not simply because
two rectangles look similar. Do not mix incompatible primitive libraries inside
one interaction surface or hand-roll complex focus management unnecessarily.

## Platform mapping

Keep brand and semantic intent consistent; adapt composition and controls.
CSS px, Apple pt, Android dp, and Android text sp are not interchangeable.
Map typography and colors to system roles where appropriate; share state
models and content contracts without forcing identical navigation everywhere.

## Assets and voice

Use approved logos, real product imagery, and an internally consistent icon
family. Verify asset/font rights, localization needs, responsive sizes, and
meaningful text alternatives. Do not automatically fetch stock imagery or
infer endorsement from a logo.

Define voice through useful examples: action label, help text, empty state,
error, and confirmation. Preserve facts and domain terminology. Avoid
unsupported promises, discriminatory assumptions, and manipulative urgency.

For persisted system documentation, use the existing authoritative destination
and schema. See [Deliverables](deliverables.md); do not create competing
`MASTER.md`, `DESIGN.md`, and token files for the same authority.
