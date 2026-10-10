# Discovery and experience shaping

Load for fuzzy ideas, new flows, changing feedback, or an explicit interview.
Do not turn a precise repair request into a lengthy discovery exercise.

## Gather evidence without steering the answer

First read the supplied brief, current product behavior, and permitted research.
Restate the user job briefly, then choose two to four questions that reduce the
largest uncertainty. Prefer concrete recent experiences over speculative
feature wish lists.

| Uncertainty | Useful question |
| --- | --- |
| User and role | Who performs this task, and who approves or receives its result? |
| Trigger | Describe the last time this need occurred. What started it? |
| Current workflow | What happened from start to finish, including workarounds? |
| Friction | Where did time, confidence, or information get lost? |
| Outcome | What tells the person that the task is complete and trustworthy? |
| Environment | Which devices, interruptions, network conditions, or policies matter? |
| Content | What real data, files, labels, and ranges must the interface handle? |
| Risk | What happens if someone makes a mistake, cancels, or loses connectivity? |

Use the host's structured question tool when available. Summarize each answer
round before continuing. Do not repeat settled questions or ask users to select
CSS values before understanding the problem.

In unattended work, infer only reversible details, label them as assumptions,
and proceed with a provisional design. Unknown safety, authorization, or
approval decisions remain explicit blockers to dependent implementation.

## Maintain an evidence ledger

| Label | Meaning | Example |
| --- | --- | --- |
| Observed | Directly inspected behavior or supplied research artifact | A tested form loses its draft after a server error |
| Reported | A participant or stakeholder stated it | A user says exporting takes too long |
| Inferred | Interpretation of evidence | The export status may be difficult to discover |
| Proposed | A solution or testable hypothesis | Show progress next to the export action |
| Unknown | Missing material information | Whether exports continue after logout |

One interview can establish that person's reported experience, not prevalence
across a population. Never fabricate participants, quotes, sample sizes,
personas, usability sessions, or research results.

## Map the task before the screen

Record trigger, prerequisites, main steps, feedback, completion, and recovery.
At each step identify the user's question, system response, friction, and
opportunity. Include role/permission differences and interruptions when material.

Define one primary outcome. Examples: complete the task without assistance;
find the correct record without losing filters; understand whether a save is
pending or complete. Numerical success targets need a baseline or must be
labeled proposed; do not invent improvements.

Use problem statements of the form:

```text
For [user in context], [current friction] prevents [desired outcome].
Evidence: [source and confidence].
Opportunity: [change to explore].
Validation: [task and observable measure].
```

## Shape without prematurely implementing

Specify information architecture, navigation, task sequence, content hierarchy,
required states, and acceptance criteria. Use a low-fidelity description or
wireframe before a visual treatment when interaction is unsettled.

For uncertain concepts, propose a lightweight validation method: task-based
prototype testing, comprehension checks, or observation of the existing
workflow. State what evidence could disprove the hypothesis.

Discovery ends with a synthesis, not an automatic backlog or PRD.
Shape ends with a brief, not application code. Move to implementation only
when requested and any applicable repository approvals exist.

## Update rather than restart

For new feedback, identify what changed in user, goal, context, journey, or risk.
Preserve supported findings; retract disproved assumptions. Describe the
resulting design consequence and remaining questions. See
[Deliverables](deliverables.md) for compact output formats.
