# GitHub Branch Protection & Approval Rules

To enforce that the `main` branch is protected and can **only be modified via a Pull Request approved by you**, configure the following settings on GitHub.

---

## 1. Quick Setup via GitHub Web UI

1. Navigate to: **[github.com/anilkatragadda/ai-teaching-assistant/settings/branches](https://github.com/anilkatragadda/ai-teaching-assistant/settings/branches)**
2. Click **Add branch protection rule** (or **Add rule** under Rulesets).
3. In **Branch name pattern**, enter: `main`
4. Configure the following protection checkboxes:

### A. Pull Request & Approval Enforcement
- [x] **Require a pull request before merging**
- [x] **Require approvals**
  - Set **Required number of approvals before merging** to **`1`**
- [x] **Require review from Code Owners**
  *(Enforces [`.github/CODEOWNERS`](.github/CODEOWNERS) so that `@anilkatragadda` must explicitly approve every PR).*
- [x] **Dismiss stale pull request approvals when new commits are pushed**
  *(Ensures any new changes added to a PR require a fresh review).*

### B. CI Quality & Security Gates
- [x] **Require status checks to pass before merging**
- [x] **Require branches to be up to date before merging**
- In the search box under "Status checks that are required", select:
  1. `LLM Wiki & Specs Integrity` (from `ci.yml`)
  2. `Unit, Component & Integration Tests` (from `ci.yml`)
  3. `Production Build Verification` (from `ci.yml`)
  4. `Secret & Token Detection (Gitleaks)` (from `security.yml`)

### C. Admin & History Protections
- [x] **Do not allow bypassing the above settings**
  *(Applies the rule strictly to everyone, ensuring accidental direct pushes never land on `main`).*
- [x] **Require linear history** *(Optional, recommended: keeps git log clean and free of merge bubbles).*

5. Click **Create** or **Save changes**.

---

## 2. Enforcement Matrix

| Gate | Local Verification | CI / GitHub Verification | Merge Blocker? |
|---|---|---|---|
| **Secret Scanning** | `.githooks/pre-commit` regex scan | `security.yml` Gitleaks action | ⛔ Hard Block |
| **Wiki Integrity** | `python3 scripts/validate_wiki.py` | `ci.yml` llm-wiki-validate | ⛔ Hard Block |
| **Unit & Integration Tests** | `.githooks/pre-commit` test runner | `ci.yml` test runner | ⛔ Hard Block |
| **Production Build** | Local build (optional) | `ci.yml` build job | ⛔ Hard Block |
| **Owner Approval** | — | `@anilkatragadda` approval via `.github/CODEOWNERS` | ⛔ Hard Block |
