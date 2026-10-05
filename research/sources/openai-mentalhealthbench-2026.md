# Source Record: MentalHealthBench (September 2026)

- **Record ID:** SRC-LIVED-EVAL-003
- **Record status:** Partly verified for reported methods and cohort comparison
- **Protocol version:** [0.6-draft](../research-protocol.md), unadopted
- **Created / updated / accessed:** 2026-10-05
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by / review:** Codex / author self-check only
- **Related note:** [NOTE-LIVED-EVAL-001](../notes/lived-experience-informed-ai-evaluation-2026.md)

Compact [source-template](_template.md) adaptation; one corporate evidence
line, separate from MindBench.

## Bibliographic and temporal record

- **Title:** “MentalHealthBench: An Expert-Informed Benchmark of AI Capabilities
  in Realistic Mental Health Conversations.”
- **Authors / affiliation:** Ali Malik, Declan Grabb, Rebecca Soskin Hicks,
  Rahul K. Arora, Preston Bowman, Michael Sharman, Sahra Ghalebikesabi,
  Mikhail Trofimov, Vinnie Monaco, Karan Singhal / OpenAI.
- **Source / version:** [32-page technical paper](https://cdn.openai.com/ctf-cdn/MentalHealthBench_A_Comprehensive_Benchmark_of_AI_Capabilities_in_Realistic_Mental_Health_Conversations.pdf)
  linked from the dated [2026-09-23 release](https://openai.com/index/introducing-mentalhealthbench/).
  No numbered PDF revision or peer-reviewed venue established; treat as a
  corporate technical report, not confirmed peer-reviewed research.
- **Status:** No correction/withdrawal notice identified in the checked
  release; later publication/revision status not conclusively established.
- **Systems / configuration:** Multiple provider APIs at default reasoning,
  temperature, and verbosity settings; GPT-5.6 Sol automated grader (§2.3).
  No model ranking is imported into the note. Exact user-study stimulus
  checkpoints and collection dates were not established in this intake;
  system release/training dates unknown here. Inclusion date: 2026-10-05.
- **Applicability:** Sampled users, matched non-acute tasks, and reported
  rubrics; not all human lived experience or present product behavior.

## Source report and contrary material

Sections 2.2–2.3 and 3.2 describe weighted expert criteria, adjudication, and
automated grading of final-turn responses in synthetic conversations. Section
3.3 selects English-proficient AI-support users through onboarding assessment;
the release supplies the exact cohort count used in the note. The paper's
§4.6 reports differences in user/expert ratings and criteria, including
penalties when user-rubric-optimized responses are graded against expert
criteria. Section 5.2 leaves safe integration of these perspectives open.
The release explicitly says the separate user analysis did not alter scoring
criteria. Neither publication establishes clinical benefit from participation.

## Claim-specific quality and lineage

| Dimension | Assessment for nonredundant user perspectives |
| --- | --- |
| Relevance / method | Direct matched-task comparison, limited by selected cohort, synthetic tasks, and rubric construction |
| Robustness / replication | Cohort comparison reported; not independently reproduced here, no independent replication established |
| Causal strength / alternatives | Descriptive; differing instructions, scale use, or preferences could contribute alongside construct differences |
| Discriminating value | Complementarity and conflict weigh against treating either cohort as interchangeable or infallible |
| Independence / conflicts | OpenAI authors, system access, benchmark construction, grader and release; developer interest in favorable evaluation, with proprietary pipeline limits |
| Uncertainty | Material for representation, causal usefulness, clinical outcomes, and transfer to acute settings |

The paper and announcement are dependent sources, not two confirmations.
Clinical expertise does not automatically represent user priorities, and user
preference does not automatically resolve safety. Additional funding or
external-control arrangements were not independently established.

## Verification and update

Paper byline, methods, cohort comparison, contrary material, discussion, and
dated release were checked; no quotations or fresh model tests. Exact
percentages from semantic rubric-overlap analysis are omitted because they
do not directly measure the fraction of clinically important needs captured.

**TODO: verify:** Independent replication, raw annotation/recruitment audit,
user-study dates and exact stimulus checkpoints, grader sensitivity, later
publication/corrections, and longitudinal outcome validity before stronger
claims. Source revision or outcome validation should trigger review.

**2026-10-05 — Codex:** Initial bounded extraction; no clinical or project
conclusion adopted.
