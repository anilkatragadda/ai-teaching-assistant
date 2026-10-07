# Clarity Guide for Educational AI & Documentation

This reference defines how the principles of **[Clarity](https://github.com/addyosmani/clarity)** apply specifically to the **AI Teaching Assistant** platform: its student interactions, course knowledge base, and software architecture.

---

## 1. Core Principles in Education

In education, generic AI writing ("slop") is not just a stylistic problem — it actively damages learning. When a tutor is vague, polite, and hedge-heavy, students become confused and lose trust.

```text
Bad Tutor:   "Great job trying that! Perhaps you might want to look into your logic somewhere in that loop, as it could potentially cause issues."
Clear Tutor: "Look at line 14: when `i` reaches `len(items)`, what does `items[i]` evaluate to in Python?"
```

### The 4 Grounding Tests

1. **Be specific enough to be wrong**:
   Never use vague placeholders ("a potential error", "some dependencies"). Name the function, the parameter, the error code, and the line.
2. **Refuse to invent specifics**:
   If a student's question is missing essential data (e.g., error logs, compiler version, expected output), **ask the student** (`ask-author`) rather than guessing or fabricating an explanation.
3. **No fluent emptiness**:
   Cut robotic conversational padding ("I'd be thrilled to help you explore this fascinating topic!"). Deliver immediate pedagogical value.
4. **Diagnostic questioning over vague hints**:
   Socratic teaching is an **interview**: anchor questions to concrete evidence so the student diagnoses their own misconception.

---

## 2. Writing Rubrics & Knowledge Base (`docs/knowledge_base/`)

When creating curriculum, assignment rubrics, and conceptual guides:

| Rule | Guideline | Bad Example | Good Example |
|---|---|---|---|
| **Prerequisites First** | State required knowledge before introducing advanced topics. | "In this advanced lab we will explore Dijkstra's algorithm." | "Prerequisites: Adjacency lists (Module 3.2), Priority queues (Module 4.1)." |
| **Observable Criteria** | Rubric items must be measurable by another human grader without ambiguity. | "Student writes clean, good code." | "Zero memory leaks detected by Valgrind; all public functions have type annotations." |
| **Concrete Failure States** | List the 3 most common misconceptions and how to recognize them. | "Common mistakes may occur." | "Failure mode: Modifying list during iteration raises `RuntimeError`." |

---

## 3. Engineering Documentation & ADRs (`docs/architecture/`)

Apply Clarity's `references/medium.md` for technical documentation:

1. **Trade-offs over cheerleading**: State what is sacrificed in an architecture decision (e.g., "Choosing client-side embedding search increases bundle size by 1.8MB but eliminates backend inference latency").
2. **Explicit boundaries**: Define what the service or module *does not* do.
3. **Omit throat-clearing**: Never open a spec with "This document aims to provide an in-depth, comprehensive overview...". State the claim and system objective in sentence one.

---

## 4. Linting Diagnostics

Run Clarity's diagnostic script on draft documentation or system prompts:

```bash
python3 .agents/skills/clarity/scripts/strip_markdown.py docs/knowledge_base/rubric.md | \
python3 .agents/skills/clarity/scripts/prose_stats.py -
```

This identifies:
- **Excessive hedging** (`possibly`, `tends to`, `it appears that`)
- **Sentence length monotony** (plodding cadence that tires student attention)
- **Passive and non-attributive assertions**
