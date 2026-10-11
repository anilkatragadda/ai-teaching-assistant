# Universal Documentation Invariant (Lineage, Purpose, Usability)

Every document in this repository (`SCOPE`, `ARN`, `ADR`, `UI`, `PRD`, `OAS`, `TASK`, `REL`) must satisfy these standards:

1. **Clear Purpose**: Every document exists to inform a concrete engineering or product decision. If a document has no active consumer or purpose, do not create it.
2. **Strict Bidirectional Lineage**:
   - Every document must declare its `upstream` parent and `downstream` children in machine-readable YAML frontmatter.
   - Every document must include Section 0 with clickable GitHub-style links (`file://`).
3. **No Redundancy**:
   - Never duplicate technology choices across docs (defer to `ADR-###`).
   - Never duplicate API schemas in prose (defer to `OAS-###`).
   - Never duplicate user stories in architecture notes (defer to `PRD-###`).
4. **Consistency & Structure**:
   - Follow standard ID prefixing (`PREFIX-###-<slug>.md`).
   - Keep prose concise, active, and measurable (ASD-STE100 style). No AI fluff or filler narratives.
5. **Master Index Registration**:
   - Every created or updated artifact must be registered in [`docs/INDEX.md`](file:///Users/anilkatragadda/Documents/code/ai-teaching-assistant/docs/INDEX.md).
   - All docs must pass validation via `python3 scripts/validate_wiki.py`.
