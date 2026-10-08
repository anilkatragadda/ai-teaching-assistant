# UI/UX Studio

A single, original agent skill for discovery through delivery across web,
mobile, and desktop. It combines the useful methods from the four requested
projects without importing their conflicting defaults or runtime dependencies.

## Installed location

The canonical workspace copy is [`.agents/skills/ui-ux-studio/`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/skills/ui-ux-studio/). It integrates directly with the Antigravity agent ecosystem and pairs with the [`ui-ux-designer`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/.agents/agents/ui-ux-designer.md) subagent.

Example invocations:

```text
Use the ui-ux-studio skill to critique the current student workspace layout.
Use the ui-ux-studio skill to shape a mobile onboarding flow and produce UI-001 design spec.
Use the ui-ux-studio skill to extract and formalize our CSS design tokens.
Use the ui-ux-studio skill with Google Stitch to explore visual directions for the Socratic dialogue panel.
```

## Portability

Copy the **entire** `ui-ux-studio` directory, including `references/`, into one
skill location appropriate to the target host:

| Host/scope | Destination |
| --- | --- |
| Copilot project | `<project>/.github/skills/ui-ux-studio/` |
| Copilot personal | `~/.copilot/skills/ui-ux-studio/` |
| Claude Code project | `<project>/.claude/skills/ui-ux-studio/` |
| Codex project | `<project>/.agents/skills/ui-ux-studio/` |

Choose one canonical location per host/project; avoid duplicate copies in
directories the same host scans. A session opened directly in a child repo may
need its own project copy or an explicitly added skill location. Workspace
placement is not a guarantee that every tool scans parent directories.

No installer, Python runtime, npm package, API key, hook, remote registry, or
upstream binary is required. Normal browser/device/testing tools are still
needed to verify implemented interfaces.

## Project independence

The skill is product- and project-independent. It does not include the host
workspace's architecture, service names, infrastructure settings, brand, or
specification pipeline. It follows the target project's documented constraints
only when they apply. The installed location is described above for convenience;
it is not a requirement for use elsewhere.

## Included capabilities

| Area | Coverage |
| --- | --- |
| Discovery | Progressive questions, evidence labels, journeys, hypotheses, success criteria |
| Design systems | Brand context, semantic tokens, themes, component states, platform mappings |
| Interaction | Navigation, forms, feedback, destructive actions, onboarding, recovery, i18n |
| Visual craft | Hierarchy, typography, color, layout, density, imagery, icons, purposeful motion |
| Web | Responsive/PWA behavior, browser semantics, embedded UI, metadata, performance |
| Mobile | iOS and Android conventions, safe areas, keyboard, text scaling, tablets/foldables |
| Desktop | Keyboard workflows, menus, windows, DPI, native integration, accessible wrappers |
| Evaluation | Read-only audits/critique, severity, evidence, scoped fixes, verification matrix |

References are loaded on demand rather than all at once.

## Deliberate exclusions

This is an instruction-and-reference skill, not a bundle of upstream software.
It does **not** include Pro Max's CSV catalogs/BM25 generator, Impeccable's
detectors/browser extension/live-variant engine, or UI Skills' registry/MCP
server. It does not claim their catalog counts or automated detection features.
Their dependencies and licensing obligations would need separate review before
vendoring them.

It also excludes slide generation, advertising banners, logo-generation
pipelines, automatic asset downloads, and unsolicited experimental effects.
These are separate tasks, not prerequisites for designing a product interface.

## Analysis and attribution

Read [Source analysis](references/source-analysis.md) for the comparison,
immutable source revisions, adopted methods, rejected rules, platform gaps,
license observations, and official standards.

All guidance here is newly authored. No upstream scripts, catalogs, assets, or
substantial source text are redistributed. Upstream licenses are recorded as
provenance, not assigned to this newly authored skill; publication licensing
remains a workspace-owner decision.

## Evaluation examples

[Evaluation](references/evaluation.md) includes regression scenarios for skill
behavior. These specify expected decisions, not a claim that a model will
always comply. Validate real UI changes with the target project's own tools.
