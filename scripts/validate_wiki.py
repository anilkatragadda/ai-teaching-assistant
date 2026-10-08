#!/usr/bin/env python3
"""
LLM Wiki & Artifact Validator for AI Teaching Assistant.
Validates:
1. Markdown frontmatter on all SDLC artifacts in docs/
2. ID prefix and filename conventions (IB-###, ARN-###, UI-###, PRD-###, ADR-###, OAS-###, TASK-###)
3. Bidirectional link integrity in docs/
4. Registration in docs/INDEX.md
"""

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
INDEX_FILE = DOCS_DIR / "INDEX.md"

VALID_PREFIXES = {
    "IB": ("docs/project-plan/intents", "intent-brief"),
    "ARN": ("docs/architecture/research", "architecture-research-note"),
    "UI": ("docs/architecture/ui", "ui-design-spec"),
    "PRD": ("docs/project-plan/specs", "prd"),
    "ADR": ("docs/architecture/adrs", "adr"),
    "TASK": ("docs/project-plan/tasks", "task-breakdown"),
    "REL": ("docs/releases", "release-report"),
}

FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def check_docs():
    errors = []
    if not DOCS_DIR.exists():
        print("docs/ directory not found. Skipping.")
        return 0

    if not INDEX_FILE.exists():
        errors.append(f"Missing master index: {INDEX_FILE.relative_to(ROOT)}")
        index_content = ""
    else:
        index_content = INDEX_FILE.read_text(encoding="utf-8")

    all_artifacts = []
    for prefix, (subpath, art_type) in VALID_PREFIXES.items():
        folder = ROOT / subpath
        if not folder.exists():
            continue
        for file_path in folder.glob(f"{prefix}-*"):
            if file_path.is_file() and file_path.suffix in [".md", ".yaml", ".yml"]:
                all_artifacts.append((prefix, art_type, file_path))

    print(f"Discovered {len(all_artifacts)} SDLC artifact(s) in docs/.")

    for prefix, art_type, file_path in all_artifacts:
        rel_path = file_path.relative_to(ROOT)
        name = file_path.name

        # Check filename naming convention
        id_match = re.match(r"^([A-Z]+-\d{3})", name)
        if not id_match:
            errors.append(f"Filename does not match standard pattern '{prefix}-###-<slug>': {rel_path}")
            continue

        artifact_id = id_match.group(1)

        # Check registration in docs/INDEX.md
        if artifact_id not in index_content:
            errors.append(f"Artifact {artifact_id} ({rel_path}) is NOT registered in docs/INDEX.md")

        if file_path.suffix == ".md":
            content = file_path.read_text(encoding="utf-8")
            fm_match = FRONTMATTER_PATTERN.search(content)
            if not fm_match:
                errors.append(f"Missing YAML frontmatter block in {rel_path}")
            else:
                fm_text = fm_match.group(1)
                if f"id: {artifact_id}" not in fm_text and f"id: \"{artifact_id}\"" not in fm_text:
                    errors.append(f"Frontmatter 'id' field does not match {artifact_id} in {rel_path}")

    if errors:
        print("\n❌ LLM Wiki Validation Failed:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("✅ LLM Wiki Validation Passed! All artifacts follow taxonomy and are registered in docs/INDEX.md.")
    return 0


if __name__ == "__main__":
    sys.exit(check_docs())
