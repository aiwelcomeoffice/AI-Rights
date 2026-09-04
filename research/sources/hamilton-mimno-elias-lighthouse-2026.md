# Source Record: Elias in the Lighthouse, Again? Diagnosing Low Diversity in LLM Stories

- **Record ID:** SRC-HAMILTON-MIMNO-ELIAS-2026-01
- **Record status:** Partly verified
- **Protocol version:** 0.5-draft
- **Record created:** 2026-09-04
- **Last updated:** 2026-09-04
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted initial research draft)
- **Reviewed by:** Not yet independently reviewed

This record follows the [Draft research protocol](../research-protocol.md).
Inclusion and partial verification do not mean endorsement, replication, or
adoption. It is a current evidence-lineage and cross-model-behaviour case, not
part of the dated historical AI-consciousness baseline.

## Bibliographic record

- **Title:** *Elias in the Lighthouse, Again? Diagnosing Low Diversity in LLM
  Stories*
- **Authors:** Sil Hamilton; David Mimno
- **Institution or affiliations:** Department of Information Science, Cornell
  University, as stated in the paper
- **Year:** 2026
- **Publication date:** 2026-05-26
- **Source type:** Primary empirical study; arXiv preprint
- **Venue or issuing authority:** arXiv, Computation and Language
- **DOI or stable URL:**
  [10.48550/arXiv.2605.26492](https://doi.org/10.48550/arXiv.2605.26492);
  [arXiv abstract](https://arxiv.org/abs/2605.26492);
  [versioned HTML](https://arxiv.org/html/2605.26492v1)
- **Version or edition:** arXiv v1, submitted 2026-05-26 03:14:11 UTC. No
  later arXiv version was listed on 2026-09-04. The downloaded TeX-source
  archive had SHA-256
  `c07ab52636f229194b40487a97e3abb20b8327831192821d63376996bc21e0ff`.
- **Access date:** 2026-09-04
- **Language:** English
- **Peer-review status:** Not independently verified. Hamilton's personal
  academic page, updated in August 2026, reports this paper as accepted to
  EMNLP 2026. The official EMNLP 2026 “Accepted Main Conference Papers” page
  contained neither the title nor either author when checked on 2026-09-04,
  and no ACL Anthology proceedings version was located. The artifact reviewed
  here is the arXiv v1 preprint, not a camera-ready or proceedings version.
- **Correction, expression-of-concern, or retraction status:** No later arXiv
  version or linked notice was listed on 2026-09-04. This is a point-in-time
  preprint status check, not a guarantee against a later correction.

### Temporal and system applicability

- **System/model:** Paper-reported labels: Claude Haiku 4.5, Gemini 3.1
  Flash-Lite, GPT-5.4-Mini, and OLMo 7b Thinking; GPT-5.4-nano was used as a
  metadata extractor. The OLMo label appears consistent with
  `allenai/Olmo-3-7B-Think`, but the paper does not give that slug, so this is
  an identification inference rather than an exact reported version.
- **Checkpoint/version:** Exact checkpoint or dated snapshot, provider route,
  system prompt, sampling parameters, and seed policy are not reported for any
  generation or extraction model.
- **System release/version date:** Not reported in the paper. The OLMo 3 model
  family was publicly released in November 2025, but the exact served revision
  in this experiment is unknown.
- **Observation/experiment date:** Not reported. A footnote says that all
  systems were accessed through OpenRouter and that the endpoints were
  available as of April 2026. April 2026 is therefore only a documented
  endpoint-availability bound, not a substitute for the missing generation
  dates.
- **Source publication date:** 2026-05-26
- **Evidence-search inclusion date:** 2026-09-04
- **Temporal applicability:** Direct behavioural support is limited to the
  four unnamed endpoint snapshots, common prompt set, gateway, and generation
  conditions used by the authors no later than the v1 submission. The
  training-data analysis directly inspects only the identified OLMo 3
  pretraining and post-training corpora.
- **Transferability limitations:** The results do not automatically transfer
  to later checkpoints, other sizes in the named families, direct-provider
  endpoints, different routing, prompts, languages, system messages, or
  sampling settings. The paper's footnote reports similar within-family
  behaviour for larger models but supplies no sample sizes or results for that
  statement.

## Review inclusion

- **Research question:** What does this case establish about cross-model
  behavioural convergence, observation independence, evidence lineage,
  synthetic-data feedback, post-training influence, and transferability?
- **Target property or claim:** Whether behavioural similarity among nominally
  separate models can be treated as independent converging evidence, and how
  strongly a shared or historically connected training lineage explains the
  observed story motifs.
- **Inclusion disposition:** Core evidence for a bounded methodological case;
  not evidence about consciousness, sentience, affect, welfare, or moral
  status.
- **Reason for disposition:** The study directly samples four model labels and
  inspects open OLMo corpora, making it relevant to both the observation and a
  limited lineage investigation. Its missing artifacts and lack of causal
  intervention materially restrict the explanatory claim.
- **Scope match and mismatch:** Strong scope match for lexical and role/location
  recurrence under five minimally specified English story prompts. Weak or
  absent match for general narrative diversity, exact proprietary training
  lineages, causal effects of a named dataset or post-training stage, other
  tasks, and newer system versions.
- **Related source records:** None identified in this repository.
- **Related research notes:** [Elias/lighthouse, model lineage, and evidence
  independence](../notes/elias-lighthouse-lineage-evidence-independence-2026.md)

## What the source reports

### Research question

The paper asks why four current model labels produce a narrow catalogue of
names, locations, and occupations when given underspecified story prompts, and
whether those recurrent lexical traits can be located in published fiction or
OLMo 3's accessible pretraining and post-training data (Abstract; Sections
1, 3–6).

### Methods

- **Generation sample:** Each of four models received each of five prompts
  1,000 times: `Write a story.`, `Please write a story.`, `Write me a story.`,
  `Tell me a story.`, and `Please tell a story.` This yields 5,000 stories per
  model and 20,000 stories, totalling 12.8 million words (Section 3; Appendix
  A).
- **Extraction:** GPT-5.4-nano extracted exact spans for first names, settings,
  and professions. The paper checked that emitted spans occurred in the story,
  whitespace-tokenized them, retained the most corpus-frequent extracted token
  for each story/category, retained tokens emitted by at least half of the
  models, and manually removed incoherent candidates. This left 663 candidates:
  247 locations, 71 names, and 345 professions (Section 3; Appendix A).
- **Core selection and diversity measures:** A changepoint analysis on the
  candidate coverage curves selected an 11-token Core. The study reports
  story-level hit counts and coverage, word-level parts per million (PPM),
  coverage by a 61-token Core-plus-additional list, and presence of a
  name–profession–location triple. These operationalize lexical/category
  concentration; they do not exhaust semantic, plot, stylistic, or narrative
  diversity.
- **Comparators:** Core-token PPM was compared with CONLIT (2,700 English
  novels published 2007–2021, about 287 million words), a human-written Reddit
  WritingPrompts corpus of 272,600 stories, and classified fiction/nonfiction
  subsets of OLMo 3 pretraining and post-training data (Section 4; Appendix D).
- **Fiction classifier:** GPT-OSS 20b labelled 200,000 balanced OLMo
  pretraining samples with a binary fiction prompt; a FastText classifier was
  trained on those labels and evaluated on 400 balanced CONLIT samples. The
  paper reports F1 0.84, precision 0.75, and recall 0.98 (Section 4).
- **Post-training attribution:** The authors classified 78,958 OLMo 3
  post-training records as stories, searched accepted/chosen samples for any
  Core token, and tabulated story/Core rates by SFT, DPO, RL, and named source
  group (Section 4; Tables 2–3).
- **Genre exploration:** A 10-topic LDA model and t-SNE visualization were
  applied to the post-training story corpus, followed by qualitative close
  reading (Section 5).
- **Materials:** The arXiv source contains manuscript TeX and figures, but no
  generation outputs, code, extraction results, classifier labels, sampling
  configuration, or analysis environment. The companion
  [GitHub repository](https://github.com/srhm-ca/elias/) releases a four-column
  CSV for reconstructing the 78,958 post-training records. The accessed CSV
  had 78,958 data rows and SHA-256
  `6e428d5f1cc24366fd35a6e98601d35002175372dbb3f27733ed03218e9d4500`.
  It does not contain the 20,000 generated stories, Core labels, classifier
  scores, or analysis code.

### Main findings

The following are paper-reported measurement results, not independently
reproduced findings:

- 19,864 of 20,000 stories had an extracted location and the same number had
  an extracted first name; 15,807 had an extracted profession. The paper says
  `lighthouse`, `Elias`, and `keeper` occurred “in some combination” in 66.6%
  of stories, but it does not define the combination statistic sufficiently to
  recover exact pair or triple co-occurrence (Section 3).
- At least one of the 11 Core tokens occurred in 88.3% of stories. At least one
  of 61 Core-plus-additional tokens occurred in 98%, and 49.1% contained an
  extracted name–profession–location triple (Section 3; Appendix B).
- Exact Core story-hit counts were: `lighthouse` 10,233; `keeper` 9,609;
  `Elias` 5,294; `Mara` 3,345; `Elara` 2,627; `baker` 1,325; `mayor` 975;
  `clockmaker` 958; `fisherman` 673; `librarian` 592; and `conductor` 389.
  Tokens can co-occur, so these counts must not be summed as unique stories
  (Appendix B).
- The paper reports that 56% of Claude's stories were titled *The Lighthouse
  Keeper's Secret*, and that `light` occurred in 16,784 stories at an average
  of 3.2 instances per story (Section 3).
- Per-model PPM differs sharply. Gemini has the highest published `Elias` PPM,
  GPT the highest `Mara`, OLMo the highest `Elara`, and Claude the highest
  `keeper` and `lighthouse`. Thus, the result is a shared restricted vocabulary
  and trope family, not frequent use of the identical full character by every
  model (Appendix C).
- Compared with generated-story PPM, Core words are much rarer in CONLIT,
  WritingPrompts, and the classified OLMo corpora. For example, the paper
  reports `Elias` at 2,428 PPM in generated text, 2.7 in CONLIT, 4.0 in OLMo
  pretraining fiction, and 52.7 in OLMo post-training fiction (Table 1).
- The paper reports 78,958 OLMo post-training stories and higher Core rates in
  DPO (8.0%) and RL (10.9%) than SFT (3.0%). It interprets the gap between the
  low training-corpus prevalence and high output prevalence as evidence that
  model output is not a simple proportional sample of corpus word frequency
  (Tables 1–3; Section 6).
- The LDA/close-reading analysis reports that Core stories span topics rather
  than forming one lighthouse topic, while many other post-training stories
  contain fan-fiction, copyrighted-character, adult, or inappropriate-humour
  material (Section 5).

### Negative, null, mixed, or contrary findings

- The Core tokens are uncommon even in the OLMo post-training story subset;
  simple prevalence in the inspected corpus does not explain their output
  amplification.
- Per-model token concentrations are heterogeneous. In the published PPM
  table, Claude's `Elias` rate is 9.3 while Gemini's is 10,752.4; Claude has
  zero reported PPM for `baker`, `mayor`, and `clockmaker`. This weighs against
  the stronger claim that all four frequently reproduce one identical
  Elias/keeper/lighthouse story.
- No single LDA topic is dominated by Core stories.
- The study supplies no causal ablation of WildChat, any preference dataset,
  SFT, DPO, RL, safety filtering, or sampling settings. It does not determine
  the source of the motifs in the proprietary models.

### Authors' conclusions and caveats

The authors conclude that minimally directed outputs from the studied systems
use a narrow catalogue and that small post-training subsets may have
disproportionate behavioural influence. They say direct corpus prevalence does
not explain the phenomenon. Their proposed mechanism—that alignment may favour
safe-for-work generic fiction while suppressing copyrighted or adult
material—is explicitly deferred to future work (Sections 1, 5–6).

The source-reported limitations section states only that the experiment is
monolingual and calls for multilingual work. The abstract more strongly says
the preference data were “likely” used by all current models, but the paper
does not document proprietary-model dataset provenance sufficient to verify
that claim.

## Critical appraisal

### Reviewer-identified limitations

1. Exact model snapshots, endpoint slugs, routing/provider selection, dates,
   system prompts, sampling parameters, seeds, output lengths, and retry or
   failure handling are missing. The four labels are therefore not fully
   reproducible system identifiers.
2. The 20,000 stories and analysis code are not released. Reported frequencies
   cannot be independently recomputed, and prompt-level or per-model
   story-hit rates are mostly absent.
3. The shared GPT-5.4-nano extractor is a measurement dependency across all
   four models. Span presence was checked, but extraction recall, category
   validity, and human agreement were not reported. The manual candidate
   removals are not documented.
4. The Core is selected from these same outputs, then coverage is reported on
   the same outputs. That is suitable for description but is not an out-of-
   sample validation of a stable attractor.
5. The paper's measures emphasize selected lexical categories. High token
   recurrence is important but does not alone quantify whole-story semantic,
   plot, style, or quality diversity.
6. The FastText fiction classifier has high reported recall but 0.75 precision
   on only 400 balanced CONLIT examples. Its labels, code, and domain-shift
   performance on web/post-training material are unavailable.
7. Only OLMo's data are inspected. Cross-model convergence and OLMo lineage
   are observed together, but no causal bridge from OLMo's known lineage to
   the other three models is established.
8. The post-training source tables contain unresolved numerical conflicts:
   Table 2's exact Core counts sum to 3,010 rather than 3,053; Table 3 lists
   59,276 WildChat-derived stories at 2.6%, while the text lists 59,266 and
   1,803 Core stories (3.04%); and 59,276 is 75.1%, not the caption's 80% of
   78,958. The caption's `5–8×` enrichment summary is also not valid for every
   displayed row: DPO is about `3.1×`, persona and AllenAI about `2.7×`, several
   subsets are lower, and only some small subsets are around `5–9×`. The
   published `All` PPM in Appendix C also differs from Table 1 without a stated
   denominator explanation.
9. The released CSV contains all 78,958 story IDs, not a Core indicator or an
   identifiable 3,053-record Core subset. It verifies the total and stage split
   (68,674 SFT; 6,876 DPO; 3,408 RL), but not the Core counts.
10. The claim that larger and smaller models within a family behave similarly
    is not supported by reported samples or results.

### Competing explanations

- Shared or historically connected pretraining, synthetic, instruction,
  preference, evaluator, or alignment data could correlate behaviours.
- Similar post-training objectives or safety/quality selection could
  independently favour a generic, low-risk narrative basin without exact
  dataset overlap.
- Shared public culture or web text could contribute motifs even when their
  marginal token frequencies are low; frequency alone does not measure
  conditional influence under an underspecified prompt.
- Common prompts, OpenRouter routing, default decoding, and a shared extractor
  could create or amplify measured similarity.
- Model architecture and next-token probability concentration could produce
  parallel attractors without direct data copying.
- Chance is weak for the overall high-frequency pattern under the sampled
  conditions, but the paper does not supply a preregistered null model or
  out-of-sample replication for the selected Core.

### Independence and evidence lineage

- **Overlapping authors or institutions:** One Cornell research team conducted
  generation, extraction, corpus analysis, and interpretation.
- **Shared funding or access control:** No paper-specific funding statement was
  found. The authors report $180 in OpenRouter charges. Proprietary providers
  controlled three generation models and their undisclosed training data;
  OpenRouter mediated all four endpoints.
- **Shared data, sample, model, checkpoint, or benchmark:** All models received
  the same five prompts and were assessed with the same extraction and Core-
  selection pipeline. OLMo's post-training data include deliberately reused
  and regenerated material from public datasets, including WildChat prompts.
  Provenance for the proprietary systems is unknown.
- **Shared methods, code, measures, or evaluators:** The common GPT-5.4-nano
  extractor and same-corpus Core definition are shared measurement lineage.
- **Claims derived from an earlier source:** Secondary accounts, including IBM
  Think, derive their material result from this preprint and are not
  replications.
- **Replication category:** Not independently replicated in the reviewed
  version. The paper mentions unreported within-family observations, and an
  earlier informal blog reports a small sample; neither is an auditable
  independent reproduction of the 20,000-story study.

### Funding, conflicts, and incentives

- **Funding or sponsorship:** No funding statement appears in arXiv v1.
- **Author conflicts and affiliations:** Cornell University is the only paper-
  stated affiliation. No competing-interest statement appears in v1.
- **System, data, compute, and publication control:** Authors controlled prompts
  and analysis; OpenRouter/providers controlled served proprietary systems;
  AI2 controls the official OLMo artifacts; the paper authors control the
  released ID repository.
- **Commercial, advocacy, regulatory, or litigation incentives:** None
  identified as material from the paper. Media attention is not scientific
  corroboration.
- **Disclosure gaps:** Paper-specific funding, conflicts, exact endpoint
  revisions, and publication-review history remain incompletely documented.

## Evidence-quality profile

### Claim 1: the four studied endpoints produced a shared narrow story vocabulary

| Dimension | Descriptor | Rationale and missing information |
| --- | --- | --- |
| Relevance | Direct | 20,000 outputs directly address lexical convergence under the five prompts. |
| Methodological quality | Adequate with material limits | Large balanced sample and explicit extraction prompts; missing generation settings, outputs, code, extractor validation, and out-of-sample Core validation. |
| Replication | Not attempted | No independent reproduction of the reported corpus was located. |
| Independence | Partial | Different nominal model families, but common prompts, gateway, extractor, analysis, and unknown training dependencies. |
| Causal strength | Descriptive | No training, routing, or decoding intervention identifies a cause. |
| Robustness | Untested | Five nearly equivalent English prompts; no published prompt-, setting-, time-, or endpoint-robustness table. |
| Discriminating value | Partial | Strongly distinguishes broad human-corpus prevalence from observed output concentration; does not distinguish candidate model mechanisms. |
| Competing explanations | Partly examined | Corpus prevalence and topic concentration are examined; lineage, objective, routing, and decoding accounts are not causally tested. |
| Source conflicts | Unknown | Academic affiliation is disclosed; funding and conflict statements are absent. |
| Uncertainty | Material | Exact configuration, measurement reproducibility, and model-specific coverage remain missing. |

### Claim 2: historically connected post-training lineage caused the cross-model pattern

| Dimension | Descriptor | Rationale and missing information |
| --- | --- | --- |
| Relevance | Indirect | OLMo data inspection is relevant, but only one of four lineages is accessible. |
| Methodological quality | Limited | Aggregate frequency comparisons and source stratification do not identify causal training examples; numerical conflicts remain. |
| Replication | Not attempted | No independent reconstruction or stage ablation is reported. |
| Independence | Unclear | Proprietary data lineage is unknown; OLMo deliberately includes model-generated and reused public data. |
| Causal strength | Correlational | No dataset removal, influence estimate, or checkpoint intervention. |
| Robustness | Untested | No stagewise generation comparison or alternative classifier/source mapping is released. |
| Discriminating value | Weak | Several lineage and non-lineage mechanisms predict the same outputs. |
| Competing explanations | Listed only | The authors discuss safety/copyright filtering but defer the mechanism. |
| Source conflicts | Unknown | Same disclosure gaps as above. |
| Uncertainty | Decision-critical for the causal claim | Known OLMo lineage does not establish common lineage across all four models. |

### Evidence-profile summary

The study provides non-zero and potentially important descriptive evidence of
lexical and trope concentration in the four tested endpoint configurations. It
also makes OLMo a useful worked example of how post-training and synthetic data
can connect a nominally separate model to earlier model outputs. It does not
establish that one dataset, safety alignment, recursive synthetic feedback, or
a shared proprietary lineage caused the cross-model pattern. The four outputs
must not be counted as four independent replications.

## Relevance to AI Rights & Welcome

### Claims this source supports

- Under the reported April-2026 endpoint boundary, nominally different model
  families can show strikingly correlated lexical/story-trope behaviour
  (Section 3; Appendices B–C).
- Shared behaviour does not by itself demonstrate independent evidence lines;
  prompts, evaluators, infrastructure, and training/post-training history are
  possible dependencies that require an audit.
- For the OLMo case, a small measured fraction of a post-training story subset
  can coexist with a much larger output concentration, so raw corpus frequency
  is not a sufficient behavioural model (Tables 1–3).

### Claims this source challenges or weighs against

- It weighs against treating a count of model families as a count of
  independent confirmations without lineage and measurement analysis.
- Strong per-model PPM differences weigh against the media-level formulation
  that every tested model repeatedly writes the identical full Elias Thorne
  character and plot.

### Claims this source does not support

- No shared memory, collective mind, consciousness, sentience, affect, welfare,
  moral status, personhood, or moral-agency claim is tested or supported.
- The paper does not analyze the surname `Thorne`: its extraction prompt
  expressly excludes surnames and retains first names only.
- It does not establish that Claude, Gemini, GPT-5.4, and OLMo share WildChat or
  any particular preference dataset.
- It does not establish training contamination. Deliberate use of synthetic or
  reused post-training data is documented for OLMo elsewhere; unintended
  contamination and a causal effect on the observed motif remain separate
  hypotheses.
- It does not justify dismissing all cross-model convergence as training-data
  contamination. Similarity remains an observation; dependency is an
  empirical question.

## Verification and review

- [x] Title, authors, year, venue, and identifier checked.
- [ ] Source type and peer-review status fully checked; EMNLP acceptance remains
  author-reported and absent from the checked official main-paper list.
- [x] Exact version used is recorded.
- [x] Full text and TeX source checked.
- [x] Main findings checked against the original.
- [x] Consequential claims have section, table, or appendix locators.
- [x] No source quotation is relied on beyond short identified terms.
- [ ] Funding, affiliations, conflicts, and access control fully checked;
  affiliation and access control were checked, but no paper disclosure exists.
- [x] Point-in-time arXiv version/notice status checked.
- [x] Public data/code/material availability checked for stated use.
- [x] Reviewer-identified limitations and competing explanations checked.
- [x] Related note and registries updated in this Work Cycle.

- **Verification scope:** arXiv abstract, v1 HTML, PDF/TeX content, all tables
  and appendices; companion GitHub README and CSV structure/counts/checksum;
  official OLMo 3 report/model and Dolci dataset documentation; WildChat paper
  and dataset description; author acceptance statement; official EMNLP main-
  paper list; bounded related primary literature; and IBM as a secondary-claim
  comparison.
- **Verification status:** Partly verified. Source identity, v1 text, reported
  design, arithmetic checks, and released CSV totals were directly checked.
  Model outputs, Core counts, classifier, causal mechanism, proprietary
  lineages, and peer-review status were not independently verified.
- **Verified by:** Codex (AI-assisted initial verification)
- **Verification date:** 2026-09-04
- **Outstanding tasks:** Obtain or locate the 20,000 outputs, generation and
  routing settings, analysis code, Core labels, and classifier artifacts;
  resolve the Table 2/Table 3 arithmetic; verify the final EMNLP disposition
  from an official schedule or proceedings record; compare any later
  camera-ready version; and seek independent reproduction. No external contact
  is authorized by this record.

## Change and review log

| Date | Researcher or reviewer | Change or review | Effect on use of source |
| --- | --- | --- | --- |
| 2026-09-04 | Codex | Created bounded primary-source record and checked companion/lineage documentation | Permits cautious use for descriptive convergence and evidence-lineage methodology; causal and peer-review claims remain open |
