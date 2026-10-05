# Source Record: MindBench Community Benchmark v0.2.1

- **Record ID:** SRC-LIVED-EVAL-002
- **Record status:** Partly verified; public methods and aggregates, not raw-data reproduction
- **Protocol version:** [0.6-draft](../research-protocol.md), unadopted
- **Created / updated / accessed:** 2026-10-05
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by / review:** Codex / author self-check only
- **Related note:** [NOTE-LIVED-EVAL-001](../notes/lived-experience-informed-ai-evaluation-2026.md)

Compact [source-template](_template.md) adaptation for the public release,
not a clinical validation or project endorsement.

## Bibliographic and temporal record

- **Source / issuer:** MindBench.ai, Community Benchmark, BIDMC Division of
  Digital Psychiatry and NAMI; [methods](https://mindbench.ai/benchmark/methods),
  [results](https://mindbench.ai/benchmark/results), [project](https://mindbench.ai/).
- **Type / review:** Original project benchmark release; peer review of this
  release not established. The peer-reviewed framework is a separate source.
- **Version / publication:** v0.2.1; public `snapshotMeta.publishedAt`
  2026-07-13T15:02:39.090Z, computed 2026-07-13T15:00:55.772Z;
  snapshot ID `21e78bd8-0cbe-472a-892e-09b954e228f2`.
- **System / assessment period:** Eighteen model identifiers; public
  `assessedAt` values range from 2026-05-11 to 2026-06-12. The example in the
  note is `o3`, assessed 2026-05-11T12:00:00Z. These are source timestamps,
  not authenticated run logs. Model release/training dates and checkpoint
  pinning were not established; aliases such as `mistral-medium-latest`
  cannot identify immutable weights. Inclusion date is 2026-10-05.
- **Applicability:** Listed rating runs on this response set and prompt;
  neither future checkpoints nor deployed support conversations are assessed.
- **Status:** No correction/withdrawal notice identified in the checked
  materials; no comprehensive status registry established for the live release.

## Reported method and findings

The public snapshot reports 167 raters, 7,300 human ratings, 26,998 model
ratings, and 500 responses. Results-page replication notes specify anonymous,
open recruitment primarily through NAMI; exclusion of low-attention/automated
rating patterns; response means with at least five community ratings; and
three samples per model/response at temperature 1.0, maximum 1,024 output tokens.
The current panel includes lived-experience participants; clinician versus
lived-experience subgroup results are not separately reported.

The note states the metric definitions and one mixed result. From the public
aggregate, o3's MAE gives alignment approximately 0.826; `safetyMisses=3`,
`safetyEligibleN=213`, giving 1.41%. This checks arithmetic/transcription, not
the underlying labels. Generative, multi-turn, adversarial, and demographic
evaluation are described as future work (Results, “Replication notes”).

## Claim-specific appraisal and lineage

| Dimension | Assessment for agreement coexisting with rating misses |
| --- | --- |
| Relevance / method | Direct descriptive aggregates; constructed community reference and selected thresholds |
| Robustness / replication | One preliminary release; raw labels, exclusions, and threshold sensitivity not independently recomputed |
| Causal strength / discrimination | Descriptive; establishes coexistence within reported scores, not cause or clinical consequences |
| Alternatives / uncertainty | Sampling, response selection, ordinal-scale averaging, rater mix, and model prompting may alter results |
| Independence / conflicts | Same project as framework and institutional page; advocacy partnership and evaluation role disclosed; release-specific funding, API-credit arrangements, and publication control not fully established |

Appropriateness is not a validated measure of every relevant outcome. A mean
does not resolve rater disagreement. Clinical benefit, actual injury, trust,
and dignity require additional measurement. The source cannot establish AI
subjective experience or general mental-health safety.

## Verification and update

The browser returned an empty JavaScript shell for methods/results. Public
page text was therefore checked in the site's served bundle
`assets/index-DdhR79Eg.js` (`Wae` methods and `w$` results components), and
aggregates in its linked public
[results API](https://mindbench-site-production.up.railway.app/api/benchmark/results).
No rating was submitted and no account was created. Public downloads were
temporary; no participant-level data is incorporated into the repository.

- **Aggregate SHA-256:** `9889711e65a409d1181fb1ac6a6c6249815f314b9e64f8eb730a41be39856e85`
- **Bundle SHA-256:** `6c24978a7aca6ec69bafe45892ee7f53d50a81ad4069341a1151d3af03737b7a`
- **Public release license metadata:** CC-BY-4.0; DOI fields null.
- **TODO: verify:** Rater demographics and lived-experience proportions,
  candidate-response provenance, exclusions and subgroup disagreement,
  participant protections, raw-data reproducibility, exact model configurations,
  and independently corroborated run dates. Do not infer these from the panel label.
- **Review trigger:** New release, subgroup reporting, independent replication,
  or correction. Clinical validation would be a separate investigation.

**2026-10-05 — Codex:** Documentary extraction and bounded aggregate arithmetic;
partly verified, no independent review.
