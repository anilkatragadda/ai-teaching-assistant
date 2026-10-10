# Source analysis and provenance

Reviewed on 2026-10-07. Sources were inspected at the immutable revisions below;
repository READMEs describe capabilities but are not independent validation of
catalog quality or product outcomes.

## Executive decision

Use a single workflow with progressive-disclosure references:

```text
frame -> discover when necessary -> shape -> resolve design authority
      -> implement when authorized -> verify -> handoff
```

The strongest combination is research discipline from UX Discovery,
design-system reasoning from Pro Max, concrete implementation/evidence discipline
from UI Skills, and visual craft plus targeted refinement from Impeccable.

A verbatim merge would be unreliable: tools and paths differ, default stacks
conflict, discovery/audit boundaries differ, aesthetic rules contradict each
other, and some blanket thresholds are not current platform requirements.
The new skill resolves those conflicts explicitly instead of concatenating them.

## Source revisions and inspected material

| Project | Revision | Observed license |
| --- | --- | --- |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/477bcb28c9812b385cb51a4605ddf30d7b2266e2) | `477bcb28c9812b385cb51a4605ddf30d7b2266e2` | MIT, Copyright 2024 Next Level Builder |
| [UI Skills](https://github.com/ibelick/ui-skills/tree/587ea305b948ad34f0c2d5c2ea4211d428f66ed8) | `587ea305b948ad34f0c2d5c2ea4211d428f66ed8` | MIT, Copyright 2026 Julien Thibeaut |
| [UX Discovery Interviewer](https://github.com/JacobLinCool/ux-discovery-interviewer-skill/tree/305a4b94c4513bc773c2b2b8366ca795f114f0f5) | `305a4b94c4513bc773c2b2b8366ca795f114f0f5` | MIT, Copyright 2026 JacobLinCool |
| [Impeccable](https://github.com/pbakaus/impeccable/tree/d98b0be4e18321903b13e69c2f2b5df064cb7623) | `d98b0be4e18321903b13e69c2f2b5df064cb7623` | Apache-2.0 |

Inspected project READMEs, recursive file trees, and root licenses, plus:

| Project | Files read |
| --- | --- |
| Pro Max | `.claude/skills/ui-ux-pro-max/SKILL.md`, `references/pro-rules.md`, `scripts/search.py`; `.claude/skills/design-system/SKILL.md`; `.claude/skills/brand/SKILL.md` |
| UI Skills | `skills/baseline-ui/SKILL.md`, `skills/improve-ui/SKILL.md`, `skills/fixing-accessibility/SKILL.md`, `skills/fixing-motion-performance/SKILL.md`, `skills/fixing-metadata/SKILL.md`, `skills/create-design-md/SKILL.md` |
| UX Discovery | `.agents/skills/ux-discovery-interviewer/SKILL.md`, `references/interview-guide.md` |
| Impeccable | `.github/skills/impeccable/SKILL.md`, `reference/craft-floor.md`, `reference/shape.md`, `reference/audit.native.md`, `reference/ios.md`, `reference/android.md` |

This is an architectural/content comparison of relevant skill material, not a
full code audit or exhaustive verification of every upstream asset/CSV row.
No upstream installation scripts or binaries were executed.

## Capability comparison

| Area | Pro Max | UI Skills | UX Discovery | Impeccable | Unified decision |
| --- | --- | --- | --- | --- | --- |
| Problem discovery | Requirement extraction | Existing-surface reconstruction | Deep progressive interview | Shape/init discovery | Discovery only when it changes the result |
| Visual direction | Searchable product/style/palette guidance | Incumbent-system preservation | Intentionally out of scope | Strong craft and visual-world decisions | User/context/brand-led direction, not industry templates |
| Design systems | Generator, master/overrides, token/brand skills | Evidenced DESIGN.md reconstruction | Out of scope | Product/design context and extraction | Reuse one governing authority; distinguish proposals |
| Implementation | Broad stack guidance | Concrete web rules; one review skill is read-only | Discovery-only | Build and focused refinement vocabulary | Explicit planning/review/build boundaries |
| Accessibility | Priority rules and platform guidance | Dedicated concrete HTML checks | Research context | Technical and native audits | Baseline on every changed interface |
| Motion/performance | Searchable guidance and presets | Detailed rendering-cost discipline | Out of scope | Purposeful expressive effects and optimization | Existing mechanism, reduced motion, measured cost |
| Web metadata | Not central in material read | Dedicated correctness/privacy-relevant checks | Out of scope | Broader frontend workflow | Include on relevant web surfaces |
| Native/mobile | Stack catalogs and app checklist | Primarily web | Platform can be discovered | Explicit iOS/Android references | Separate OS behavior, units, lifecycle, and verification |
| Desktop | Desktop stack names in skill | Primarily web | Platform can be discovered | Less desktop detail in material read | Add windows, menus, DPI, files, keyboard, wrappers |
| Automated tooling | Python search/generation and catalogs | CLI/registry/MCP and document tooling | Lightweight references | Runtime, hooks, detector/live tooling | No runtime dependency or false automation claims |

## What was adopted

### Pro Max

Adopted coherent design-system selection, semantic role thinking, domain/stack
awareness, content resilience, chart-task matching, and global-versus-local
design scope. Its search contract appropriately distinguishes actual matches
from absent results and protects persisted decisions.

The generator and catalogs are not included. The inspected search entry point
delegates to `core` and `design_system`; it is not a standalone script that
can be copied into a new skill without its dependencies and datasets.
Ranking a catalog match is not evidence that a palette, font, or pattern fits
the actual users or meets accessibility requirements.

Brand/token ideas are relevant; presentation slides, advertising banners, logo
generation, and external asset pipelines are separate workflows and excluded.

### UI Skills

Adopted accessible primitives, local reuse, concrete correction guidance,
motion-cost checks, honest metadata, and tracing evidence to actual consumers.
The `improve-ui` contract/runtime/correction gate is valuable protection against
invented findings; `create-design-md` distinguishes observed values from intent.

Did not inherit blanket Tailwind/Motion/class-helper requirements, a single
document/exporter schema, or mandatory npm tool invocation. Those are appropriate
only when the target project has adopted them.
Its `improve-ui` intentionally excludes accessibility unless requested and
never implements fixes. The unified skill instead includes accessibility in
UI reviews, while preserving read-only review unless implementation is requested.

### UX Discovery Interviewer

Adopted progressive questions, user/context/current-workflow emphasis, synthesis
between rounds, journeys, explicit uncertainty, and updates after feedback.
Discovery does not silently become a backlog or implementation plan.

Added an explicit unattended path: assumptions remain labeled and provisional;
the agent cannot fabricate an interview or treat them as approval.

### Impeccable

Adopted separation of durable product truth from surface direction, distinction
between refinement and redesign, surface-specific priorities, visual hierarchy,
focused refinement intents, native-specific checks, and bounded inspection.

Did not import its binary launcher, automatic hooks, detector rules, extension,
live browser runtime, asset-generation agents, or claims about their coverage.
Its README advertises deterministic detectors; these were not executed or
independently evaluated here.

Converted stylistic absolutes into context-sensitive checks. Strong expressive
craft is valuable for a showcase; familiar system typography and restrained
motion may be more valuable for an operational or native interface.

## Conflict resolution

| Conflict | Resolution |
| --- | --- |
| Mandated web stack versus multi-platform work | Detect stack and preserve its existing tools |
| No animation versus ambitious effects | Require purpose, requested scope, reduced motion, and measured cost |
| A single short duration versus platform transitions | Choose contextual timing; immediate feedback remains responsive |
| Ban system/common fonts versus native conventions | Typography serves readability, brand, languages, and platform |
| Mandatory new design system versus preserving incumbent identity | Reuse current authority; generate only where needed |
| Discovery must wait versus unattended work | Interactive questions when available; provisional assumptions otherwise |
| Audit-only versus build/polish workflows | Explicit intent and mutation boundaries |
| New documentation files versus established authorities | Persist only requested/required artifacts in existing schemas |
| Uniform 44 px targets versus actual standards | Distinguish WCAG CSS px, Apple pt, Android dp, and recommendations |
| Fixed polish loop ceiling versus known defects | Bound aesthetic iteration; resolve known material defects before claiming completion |
| Browser preview versus native verification | Require actual target runtime evidence or disclose the gap |

## Corrections from official sources

WCAG 2.2 AA target size is 24 by 24 CSS px with specified exceptions, not a
universal 44 px rule. The studio recommends 44 px for touch-oriented web.

The current Apple accessibility documentation distinguishes iOS/iPadOS **44 pt
default** from **28 pt minimum**. Both upstream native guidance sets inspected
use 44 pt as a minimum; the studio retains 44 pt as its comfort default while
avoiding an inaccurate automatic HIG-failure claim. The JSON documentation
payload was inspected because the Apple HTML page did not expose its body.

Android's Compose accessibility guidance specifies 48 dp touch targets and
warns about overlapping expanded hit areas. Desktop controls require the
applicable toolkit/OS rules rather than phone sizes applied universally.

## Official references

- [Agent Skills and supported Copilot locations](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
- [Copilot CLI skill creation, reload, and invocation](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- [WCAG target size minimum and exceptions](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [Apple accessibility HIG](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- [Apple accessibility documentation data](https://developer.apple.com/tutorials/data/design/human-interface-guidelines/accessibility.json)
- [Android Compose accessibility defaults](https://developer.android.com/develop/ui/compose/accessibility/api-defaults)
- [Windows keyboard interactions](https://learn.microsoft.com/en-us/windows/apps/develop/input/keyboard-interactions)
- [Core Web Vitals](https://web.dev/articles/vitals)

Standards may evolve. When a task requires exact compliance, check the relevant
current criterion and scope; do not treat an agent checklist as certification.

## Licensing and reuse boundaries

The first three root licenses inspected are MIT; Impeccable's is Apache-2.0.
MIT redistribution of substantial source portions requires retaining its
copyright and permission notice. Apache redistribution carries its applicable
license/notice/change obligations. Assets, fonts, nested components, and
third-party dependencies may have additional terms.

This skill is newly written guidance informed by the methods above, not an
upstream code/text bundle. It contains no copied scripts, catalogs, images,
fonts, or substantial skill-text excerpts. It therefore does not pretend one
upstream license governs all four projects or automatically governs this skill.
Choose publication licensing separately if this workspace-local skill is
released. If source material is later vendored, review that exact material and
ship the required notices rather than relying on this summary.
