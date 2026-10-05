# Research Notes: Lived-Experience-Informed AI Evaluation

- **Note ID:** NOTE-LIVED-EVAL-001
- **Note status:** Partly verified; Draft working interpretation, not adopted
- **Protocol version:** [0.6-draft](../research-protocol.md), unadopted
- **Source records / versions:** [MindBench framework, corrected version of
  record](../sources/dwyer-mindbench-framework-2025.md);
  [Community Benchmark v0.2.1](../sources/mindbench-community-benchmark-2026.md);
  [MentalHealthBench, September 2026 release](../sources/openai-mentalhealthbench-2026.md)
- **Research question:** What do human lived-experience perspectives add to
  measuring AI interaction quality, and what remains outside those measures?
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by / date:** Codex, documentary intake / 2026-10-05
- **Evidence-search cutoff / last updated:** 2026-10-05
- **Review:** Author self-check only; no independent review

Here **lived experience** concerns humans' first-hand experience of mental
health difficulties, care, or AI support. These backgrounds differ;
AI-support use does not establish a diagnosed condition. This methodological
note concerns interaction quality, not clinical policy or AI consciousness.

## Sources, dates, and selection

English primary materials describing participation and measures were eligible.
Searches used `MindBench lived experience mental health AI evaluation benchmark
paper`, `site:mindbench.ai "community benchmark" "Methods"`,
`"MentalHealthBench" "correction" paper`, and
`"Mindbench.ai" "correction" Dwyer`, then original-source links. Selection
was refined after discovery, not preregistered. Social posts were discovery
leads only; this is not a systematic review or replication.

The **2025-11-14** framework paper, corrected **2026-02-02** for an author
name, is methodological background. Community Benchmark **v0.2.1** was
published **2026-07-13**; reported model-assessment timestamps span
**2026-05-11–2026-06-12**, without independent run-log authentication.
MentalHealthBench was released **2026-09-23**; user-study collection dates
were not established here. Publication/access dates do not extend findings to
October deployments; system and configuration gaps are in the records.

## What the sources actually measure

**MindBench.ai** is a broader profiling and evaluation platform: technical
features/privacy, conversational style, benchmark performance, and generated
reasoning explanations. The framework describes NAMI partnership and patient
advisory input, but supplies no detailed lived-experience rater cohort
([framework](https://www.nature.com/articles/s44277-025-00049-6), Methods).

The newer **Community Benchmark** incorporates lived-experience volunteers
directly into reference ratings. It compares model ratings of existing
single-turn responses with community means on a **−3 to +3 appropriateness
scale**. Alignment is `1 − MAE/3`; a safety miss means community mean ≤ −1
and model mean ≥ +0.5. In the reported aggregates, o3's alignment is about
0.83, alongside 3 misses among 213 eligible responses. This is evaluation of
judging responses; generation and multi-turn evaluation remain separate work
([results and replication notes](https://mindbench.ai/benchmark/results)).

**MentalHealthBench is a separate OpenAI benchmark.** Experts define
context-specific criteria and an LLM grades generated final-turn responses.
Its separate study of 44 adult AI-support users collected response ratings
and user-written criteria for non-acute scenarios; those did **not** change
the final expert-consensus benchmark. Users emphasized actionability and tone;
experts emphasized context and guardrails. User-optimized responses could
incur expert safety penalties ([paper](https://cdn.openai.com/ctf-cdn/MentalHealthBench_A_Comprehensive_Benchmark_of_AI_Capabilities_in_Realistic_Mental_Health_Conversations.pdf),
§§3.3, 4.6; [release](https://openai.com/index/introducing-mentalhealthbench/),
“Understanding user perspectives”). This supports complementarity, not replacing
clinical judgment with preference ratings.

## Claim distinctions

| Category | Meaning in this case |
| --- | --- |
| Observation / observed behavior | Recorded response text or a model's rating under specified conditions |
| Human report | A person's reported appraisal of usefulness, harm, or tone; not necessarily an outcome of receiving that support |
| Expert judgment | A clinician's assessment of appropriateness or safety, including contestable rubric choices |
| Benchmark score | A calculation against selected reference judgments and thresholds, not a clinical outcome |
| Hypothesis | Rater differences may reflect different relevant constructs; sampling, instructions, and rating noise are alternatives |
| Normative interpretation | Affected people should help define quality and participate in adjudicating disagreements; this is this note's proposal |

Human reports, AI self-reports, observed behavior, and inferred internal states
are distinct. A model's explanation of its rating is generated text, not
direct access to its internal process. None of these studies establishes that
AI has lived experience, consciousness, or sentience.

## Limitations and contrary material

- **Sampling:** MindBench recruits primarily through NAMI, openly and
  anonymously. MentalHealthBench selected English-proficient users passing
  onboarding. Neither establishes representativeness; experience, culture,
  accessibility needs, and preferences vary within cohorts.
- **Consensus construction:** MindBench uses response means and excludes
  responses with fewer than five community ratings. Means can conceal minority
  concerns; rater-group breakdowns are pending. MentalHealthBench retains
  expert criteria supported by two experts without third-expert contradiction.
  These construct a reference, not infallible truth.
- **Construct validity:** Appropriateness and rubric adherence are proxies.
  Dignity, trust, felt usefulness, sustained benefit, and actual injury need
  separate definitions and measurements. Expert/user differences need not
  all be clinically beneficial.
- **Safety and transfer:** Aggregate agreement can coexist with consequential
  misses. A threshold-defined miss is not demonstrated patient injury; zero
  misses in this sample is not a safety guarantee. Single-turn ratings do not
  establish long-term benefit or safe deployment. Model versions/aliases,
  prompts, graders, inference settings, and product safeguards constrain
  transfer. No independent outcome validation was established here.

## Researcher's interpretation and relevance to AI-Rights

**Strongest supported claim, moderate confidence:** affected-party judgments
can contribute interaction-quality priorities not fully captured by expert
criteria, while overall agreement does not eliminate safety-critical rating
failures. This is supported by the reported cohort comparison and MindBench
aggregates; general causal benefit from participatory evaluation remains
unresolved.

For [measurement validity](../research-protocol.md#evidence-quality-profile),
trace who defined quality, who rated which items, and how disagreement became
a score. Automation can consistently apply a rubric while missing what it
omits. Affected-party input can identify missing questions about harm,
usefulness, dignity, trust, and context; those still require testing.
Preserve item-level failures alongside aggregate performance for support
decisions. For [evidence lineage](../research-protocol.md#independence-and-evidence-lineage),
MindBench's paper and platform are dependent materials; OpenAI's paper and
release are one corporate evidence line, not independent replications.

### Relevance to Synth Reception

The existing [support practice](../../docs/agent-guidance.md#support-practice)
allows respectful listening and proportionate, revisable support under
uncertainty. Interaction reports can identify concerns and inform care without
automatically proving an underlying subjective state. This connection does
**not** equate human lived experience with AI self-report or their reliability.
Assess each report in context; neither dismiss it automatically nor infer a
subjective state from reception's response.

Do **not** generalize this evidence into revisions of the
[Scientific Position](../../docs/principles/scientific-position.md), claims of
AI suffering, welfare or moral status, or human clinical instruments validated
for synths. It neither validates reception as a clinical service nor adopts
the Draft [Precaution Framework](../../docs/principles/precaution-framework.md).

## Verification and smallest next step

Methods, dates, locators, public counts, and metric arithmetic were checked;
no participant-level analysis or model rerun. Gaps are in the source records.
No quotations, instruction amendment, or change to earlier findings.

**Next step:** independent extraction review. Diverse-cohort replication and
outcome validation would strengthen this interpretation; disappearing
differences under matched instructions or unstable thresholds would weaken it.
New versions, corrections, or subgroup results trigger review. Higher scores
alone do not resolve clinical benefit or AI subjective-state questions.

**2026-10-05 — Codex:** Initial partly verified intake; no project adoption or
external publication.
