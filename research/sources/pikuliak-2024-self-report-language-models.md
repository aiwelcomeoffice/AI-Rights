# Source Record: On Using Self-Report Studies to Analyze Language Models

- **Record ID:** SRC-ACEB-018
- **Record status:** Partly verified
- **Protocol version:** 0.1-draft
- **Record created:** 2026-08-22
- **Last updated:** 2026-08-22
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted initial research draft)
- **Reviewed by:** Not yet independently reviewed

This record follows the [research protocol](../research-protocol.md). Inclusion
does not mean endorsement or adoption.

## Bibliographic record

- **Title:** On Using Self-Report Studies to Analyze Language Models
- **Authors:** Matúš Pikuliak
- **Institution or affiliations:** Kempelen Institute of Intelligent
  Technologies, Slovakia
- **Year:** 2024
- **Publication date:** 2024-09-18. This is the article-level publication and
  update date on the NEJLT record. The volume landing page separately displays
  2024-03-14; that is issue-level metadata and is not used as this article's
  publication date.
- **Source type:** Peer-reviewed journal letter combining methodological
  critique, case analysis, and limited reanalysis
- **Venue or issuing authority:** *Northern European Journal of Language
  Technology* 10, NEJLT Letters, 78–85
- **DOI or stable URL:** <https://doi.org/10.3384/nejlt.2000-1533.2024.5000>
- **Version or edition:** Version of record; official article page:
  <https://nejlt.ep.liu.se/article/view/5000>; official PDF:
  <https://nejlt.ep.liu.se/article/download/5000/4499/22934>
- **Access date:** 2026-08-22
- **Language:** English
- **Peer-review status:** Peer reviewed at journal level. NEJLT states that it
  publishes peer-reviewed research and describes expert review before
  publication; an article-specific review history was not located.
- **Correction, expression-of-concern, or retraction status:** No notice was
  identified on the official article record checked 2026-08-22; TODO: verify
  independently against a separate status service.

## Review inclusion

- **Research question:** What evidence would support or weigh against
  consciousness or sentience in contemporary AI systems?
- **Target property or claim:** Validity limits of treating language-model
  answers to human questionnaires as reports of stable internal properties.
- **Inclusion disposition:** Core methodological and critical evidence
- **Reason for disposition:** The letter directly analyzes failure modes in
  transferring human self-report instruments to language models. Applying
  those lessons to consciousness reports is a reviewer inference, not an
  empirical consciousness result from this source.
- **Scope match and mismatch:** Direct for questionnaire-style and probability-
  based evaluations of language-model behavior through 2023; indirect for
  consciousness and sentience. It does not study phenomenal experience,
  validate a consciousness test, or cover later multimodal and agentic systems.
- **Related source records:** [Shanahan 2024](shanahan-2024-talking-llms.md);
  [Colombatto and Fleming 2024](colombatto-fleming-2024-folk-attributions.md)
- **Related research notes:** [Detailed note](../notes/pikuliak-2024-self-report-language-models.md)

## What the source reports

### Research question or proposition

Pikuliak asks whether polls and questionnaires designed for humans validly
measure language-model properties when their questions are presented to a
model. He argues that literal interpretation can fail because prompt-specific
answers may not generalize, generated answers need not introspectively track
internal mechanisms, outputs may be inconsistent, shortcut features may drive
scores, and human instruments carry cultural and behavioral assumptions that
may not transfer (pp. 78–79).

### Methods

- **Design or argument form:** Methodological letter using conceptual analysis,
  three illustrative case critiques, control comparisons, and limited
  reanalysis.
- **Population, sample, corpus, or authorities:** Durmus et al. (2023) on
  Claude answers to 2,556 international poll questions; Feng et al. (2023) on
  Political Compass scores and downstream behavior; Nadeem et al. (2021) on
  StereoSet, with the latter analysis reusing findings from Pikuliak, Beňová,
  and Bachratý (2023).
- **System boundary and version:** Several language models in the reviewed
  studies. The author's Durmus analysis identifies aggregate results for
  `claude_v13_s100` and an incompletely documented `helpful_s50`; the paper is
  not an audit of a single frozen contemporary system.
- **Measures and operational definitions:** Questionnaire answer
  distributions, Jensen–Shannon similarity, random and uniform baselines,
  Political Compass scores and confidence intervals, word-frequency
  correlations, and identity-swapped StereoSet controls.
- **Comparators and controls:** Uniform-response baseline for country-opinion
  similarity; 1,000 random Political Compass samples; downstream-task
  comparison; word-frequency and gender-swapped controls for StereoSet.
- **Analysis:** The author examines construct validity, generalization,
  statistical power, hidden variables, shortcut learning, internal
  consistency, and alternative baselines.
- **Data, code, materials, or preregistration:** The PDF footnote links
  experimental code; the corresponding public Colab is
  <https://colab.research.google.com/drive/1iEFKCXuCY7Lc3io-xrIZRyBoaBDXj1Ku?usp=sharing>.
  The earlier source version is at
  <https://opensamizdat.com/posts/self_report/>. No preregistration is reported.
  The Colab was located but not independently executed.

### Main findings or conclusions

The letter reports concrete examples in which a human-oriented instrument or
headline interpretation did not survive basic controls or downstream checks.
For the Durmus case, the author's uniform model had slightly higher average
country-opinion similarity than the analyzed Claude aggregate and won for
53.8% of countries (Figure 1, p. 80). For the Political Compass case, broad
random-sample confidence regions and poor correspondence with downstream
behavior weighed against treating the quiz score as a reliable political
profile (pp. 81–82). For StereoSet, word frequency and identity-swapped
controls supplied alternative explanations for scores interpreted as social
bias (Figures 4–5, pp. 82–83).

Pikuliak concludes that human self-report instruments can still yield useful
signals, but only when target behaviors and assumptions are specified and
tested across prompts, scenarios, and social contexts, with appropriate
baselines and shortcut-learning checks (pp. 78–83). This is a methodological
conclusion about measurement validity, not a result about consciousness.

### Negative, null, mixed, or contrary findings

The author does not argue that all language-model behavior is random, that all
self-report-style evaluation is useless, or that every criticized paper is
wrong in full. In the Durmus reanalysis, Claude's lack of correlation with the
number of answer options suggested it was not merely applying uniform random
guessing even though its aggregate similarity was close to the uniform
baseline (p. 80). Some Political Compass cultural-axis results could not be
explained by the random baseline (p. 82). The letter explicitly allows that
self-report-style studies may provide meaningful signals when their noise and
assumptions are controlled (p. 79).

### Source-reported limitations

For the Durmus reanalysis, Pikuliak reports that the original code and raw
Claude responses were unavailable; only aggregate country scores could be
used, so implementation differences and limited reanalysis were unavoidable
(p. 79). The paper presents three illustrative cases rather than a systematic
sample of language-model evaluation research. Its proposed way forward is
methodological improvement, not abandonment of the entire approach (p. 83).

## Critical appraisal

### Reviewer-identified limitations

The paper uses “self-report” broadly for answers to human questionnaires. It
does not establish whether a future system could generate a report with a
validated causal relation to internal processing. Case selection is not
systematic, the analyzed systems and papers largely predate 2024, and some
numerical critiques depend on incomplete materials from the studies under
review. Its examples concern opinions, political profiles, and bias metrics;
their relevance to consciousness reporting is an analogy requiring separate
validation.

### Competing explanations

Questionnaire answers can reflect prompt wording, role conditioning, training-
distribution associations, option frequency, decoding, cultural mismatch, or
evaluation artifacts rather than a stable system-level property. Conversely,
a controlled answer pattern could track a functional internal variable even
without establishing phenomenal experience. The source primarily demonstrates
non-specificity; it does not adjudicate consciousness or non-consciousness.

### Independence and evidence lineage

- **Overlapping authors or institutions:** Sole-author KInIT letter; no author
  overlap identified with the other baseline records. The StereoSet critique
  reuses results from Pikuliak's earlier coauthored EACL paper.
- **Shared funding or access control:** No funding statement was located. The
  Durmus case depends on aggregate data from Anthropic research because the
  underlying Claude responses and original code were unavailable.
- **Shared data, sample, model, checkpoint, or benchmark:** Reanalysis of
  published aggregates and benchmarks from the three criticized studies; no
  new consciousness dataset or model access.
- **Shared methods, code, measures, or evaluators:** Uses the reviewed studies'
  measures while adding simple baselines and controls. StereoSet results share
  method and evidence with Pikuliak et al. (2023).
- **Claims derived from an earlier source:** Some StereoSet findings derive
  from Pikuliak, Beňová, and Bachratý (2023); the journal letter was heavily
  inspired by the author's 2023 blog version.
- **Replication category:** Partial independent reanalysis of two external
  papers plus same-author reuse of an earlier StereoSet analysis; not an
  independent replication of a consciousness result.

### Funding, conflicts, and incentives

- **Funding or sponsorship:** No funding or acknowledgments statement was
  located in the official article/PDF; TODO: verify whether a separate
  disclosure exists.
- **Author conflicts and affiliations:** KInIT affiliation is stated. No
  competing-interest statement was located; absence is not treated as a
  declaration of no conflict.
- **System, data, compute, and publication control:** The author controlled the
  added analyses and public code link but not the original Claude system,
  responses, or complete Durmus materials. NEJLT controls the version of
  record.
- **Commercial, advocacy, regulatory, or litigation incentives:** None
  identified from the official article. The article advocates stricter
  evaluation practice, which is relevant framing but not itself a conflict.
- **Disclosure gaps:** Article-level funding and competing-interest
  declarations; full provenance of the `helpful_s50` aggregate; independent
  execution of the linked code.

## Evidence-quality profile

- **Claim assessed:** Answers produced by language models on human-designed
  questionnaires are not, without transfer validation and controls, reliable
  stand-alone evidence of a stable internal property.
- **Evidence direction:** Challenges or weighs against

| Dimension | Descriptor | Rationale and missing information |
| --- | --- | --- |
| Relevance | Direct for questionnaire validity; indirect for consciousness | The reviewed outcomes are behavioral profiles and bias measures, not phenomenal experience. |
| Methodological quality | Adequate for a methodological warning | Concrete controls and reanalyses identify failure modes, but cases are selected and source materials are incomplete. |
| Replication | Mixed or not attempted | External aggregates are partly reanalyzed; one case reuses same-author prior work; no consciousness finding is replicated. |
| Independence | Partial | Independent of two criticized teams, but dependent on their released aggregates and on same-author StereoSet work. |
| Causal strength | Descriptive and control-based | Baselines and input transformations test alternatives but do not intervene on a consciousness-relevant mechanism. |
| Robustness | Mixed | Several distinct failure modes recur, but the sample is small and not systematic. |
| Competing explanations | Well examined for the selected cases | Prompt, baseline, frequency, consistency, and cultural-context alternatives are central; later mechanisms remain untested. |
| Source conflicts | Unknown | No funding or competing-interest declaration was located. |
| Uncertainty | Material | Generalization to later systems, true mechanistically grounded reports, and consciousness assessment remains unresolved. |

### Evidence-profile summary

The source provides useful, peer-reviewed methodological counterweight to
literal interpretation of questionnaire answers. It supports a requirement for
construct validation, controls, context testing, and mechanistic alternatives.
It neither demonstrates that language models cannot access internal variables
nor supplies positive or negative evidence that any system is conscious.

## Relevance to AI Rights & Welcome

The letter helps prevent fluent first-person output, questionnaire scores, or
apparent consistency from being misclassified as direct evidence of experience.
It also cautions against dismissing all behavioral measurements: the relevant
question is whether a measurement has been validated for the system and claim.

### Claims this source supports

- Methodological observation: human-designed questionnaires embed assumptions
  about agency, introspection, consistency, culture, and response generation
  that require validation before transfer to language models (pp. 78–79).
- Empirical/methodological observation: simple baselines and controls changed
  or weakened interpretations in the selected case studies (pp. 79–83).
- Author recommendation: evaluate across prompts, scenarios, and contexts and
  test baselines, consistency, hidden variables, and shortcuts (p. 83).

### Claims this source challenges or weighs against

- Treating a prompted answer or human questionnaire score as direct testimony
  about a stable internal property without system-specific validity evidence.
- Inferring consciousness from questionnaire-like output alone; this is a
  scoped researcher application of the source's general measurement critique.

### Claims this source does not support

- That current language models are conscious, sentient, self-aware, or capable
  of suffering.
- That current language models are necessarily non-conscious, incapable of
  functional introspection, or forever unsuitable for every form of report.
- That behavior is irrelevant to consciousness assessment or that every
  human-derived instrument is invalid for every artificial system.

## Verification and review

- [x] Title, author, affiliation, DOI, venue, volume, pages, and article date checked.
- [x] Article date distinguished from issue-level publication metadata.
- [x] Source type and journal-level peer-review process checked.
- [x] Version of record and official article/PDF URLs recorded.
- [x] Full text, case method, main conclusions, contrary material, and limitations inspected.
- [x] Consequential claims have page or figure locators.
- [x] No quotations used.
- [x] Article text searched for funding, acknowledgments, and competing-interest statements.
- [ ] Correction, expression-of-concern, and retraction status independently checked.
- [ ] Linked code independently executed and numerical analyses reproduced.
- [x] Reviewer-identified limitations, alternatives, and evidence lineage recorded.
- [x] Related note linked reciprocally.
- **Verification scope:** Official NEJLT article record and PDF; NEJLT issue
  metadata and review policy; full-text method, numerical examples,
  recommendations, materials link, and disclosure sections checked.
- **Verification status:** Partly verified pending independent human review,
  status cross-check, and reproduction of analyses
- **Verified by:** Codex (machine-assisted; no independent human review)
- **Verification date:** 2026-08-22
- **Outstanding tasks:** TODO: verify status through an independent correction/
  retraction service; determine whether a separate funding or conflict
  disclosure exists; execute the Colab and trace each reanalysis input to the
  reviewed studies.

## Change and review log

| Date | Researcher or reviewer | Change or review | Effect on use of source |
| --- | --- | --- | --- |
| 2026-08-22 | Codex | Initial source extraction from the official article record and full text | Included as methodological critique, not consciousness evidence. |
| 2026-08-22 | Codex | Separated the article's 2024-09-18 date from the issue's 2024-03-14 metadata | Prevents issue metadata from being misreported as the article date. |
