# Source Record: Rafe and Das on Jev Crash-Narrative Calibration (2026)

- **Record ID:** SRC-JEV-003
- **Record status:** Partly verified for the preprint's reported methods,
  results and limits; raw data and analyses not independently reproduced
- **Protocol version:** [0.6-draft](../research-protocol.md), unadopted
- **Created / last updated:** 2026-09-27
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by / review:** Codex, AI-assisted documentary intake / author
  self-check only
- **Related note:** [NOTE-JEV-001](../notes/jev-decision-native-ai-intake-2026.md)
- **Companion-release audit:** [SRC-JEV-004](pozapas-jev-calibration-repository-2026.md)

This compact [source-template](_template.md) adaptation records a bounded
reading of the original preprint. It is not an independent reproduction or an
endorsement of its crash-safety conclusions.

## Bibliographic and temporal record

- **Source:** Amir Rafe and Subasish Das, [“Calibrated Decisions at Scale:
  Converting Police Crash Narratives into Probabilistic Crash Variables with a
  System One Model (Jev)”](https://arxiv.org/abs/2609.24052).
- **Type / review:** Original empirical preprint on arXiv, not peer reviewed
  at the version checked. Institution listed: Texas State University.
- **Version / publication / access:** arXiv:2609.24052v1, submitted
  2026-09-21; HTML full text and version page accessed 2026-09-27. The version
  page listed v1 only and no withdrawal notice at access; later publication,
  correction and retraction status require renewed checks.
- **System / version:** The authors report `jev-1.13.0`, and the released
  aggregate records 195,857 responses with that model ID. The public runner
  records returned IDs but does not pass its declared `MODEL` constant in the
  API call; request-level pinning remains unverified (companion audit).
- **System release/version date:** Not established by the preprint.
- **Observation/experiment date:** Jev API run dates were not identified in
  the paper or released runner and aggregate reports checked on 2026-09-27.
  The underlying Texas crash narratives are from 2017–2025;
  that data period is not the model-test date. The 2026-09-21 submission date
  is not a proxy for test time.
- **Evidence-search inclusion date:** 2026-09-27.
- **Temporal applicability:** The reported run of `jev-1.13.0` on the authors'
  crash-narrative coding schema and reference sets. Neither live safety
  decisions nor later model versions are measured.
- **Transferability:** Calibration maps, accuracy and costs may differ across
  questions, labels, prevalence, versions, domains and deployments.

## Question, method and source lineage

**Question:** For the authors' crash-narrative coding task, do Jev's returned
probabilities track reference labels closely enough to support counting and
selective human review? Include this study as a direct, post-launch test of
one response-reported model version. The bounded selection was made after discovery, not
preregistered by this project.

The paper reports a 499,500-narrative screen, full 27-question coding of
195,857 narratives, and comparison with coded fields and 2,416 blinded human
judgments (§3–4). The authors distinguish agreement with coded administrative
fields from fidelity to what the narrative says. The human reference is a
smaller, selected set. The paper links a public code and aggregate-output
repository in its data-availability section. A [bounded audit of its 2026-09-23
commit](pozapas-jev-calibration-repository-2026.md) found the paper's rounded
calibration values in released summaries, but the underlying narratives, raw
model outputs and individual human labels are not public. The paper says a
de-identified pair-level audit table awaits data-owner permission before
release. Its §3.1 also reports that Jev received owner-redacted narratives,
whereas the human coders and frontier comparators received additional
redaction and screening; any effect of this difference was not assessed here.

The byline and affiliation are outside TypeSafe; funding, vendor credits,
model-access terms and publication control were not established by the paper
or companion materials checked in this bounded read. The work tests
the vendor's API with its own schema and labels, but it is not a replication of TypeSafe's exact workflow benchmarks.

## Findings and contrary material, with locators

| Reported result | Locator | Claim-specific interpretation |
| --- | --- | --- |
| `jev-1.13.0` processed the authors' bounded schema; Table 2 reports a 0.20-second median latency for the full coding run | §4.1, Table 2 | Descriptive result for this task and service path, not a general speed guarantee |
| Against the paper's pooled human reference, Jev's mean reported probability was 4.8% versus 2.7% observed prevalence, with a calibration slope of 1.63 | §4.4, Table 9; §5 | Direct evidence weighing against treating its unadjusted probabilities as calibrated for this task |
| Recalibration on human labels improved the paper's pooled calibration measure | Abstract; §4.2 and §5 | Supports a task-specific corrective method, not automatic calibration elsewhere |
| A two-decimal output grid limits calibration for some rare variables | §4.1–4.2, Figure 3 | A version-and-output-specific limitation that matters at low base rates |
| One generative comparator was better calibrated in the pooled human comparison | §4.4, Table 9 | Contrary to a blanket claim that decision-native output format alone ensures superior calibration |

The preprint also reports useful ranking and coding performance. That does
not cancel the observed calibration error: discrimination, calibration and
decision consequences are distinct. Nor do the calibration results establish
that Jev performs poorly on every task. The authors' own §5 limitations note
closed model access, incomplete administrative labels, exclusion of disputed
human judgments, few positive labels for some rare variables, and nonportable
recalibration maps.

## Claim-specific quality and independence appraisal

| Dimension | Assessment |
| --- | --- |
| Relevance and method | Direct for calibration on one task with a reported response model ID; multiple reference types and stated metrics, but reference selection and labeling limit strength |
| Replication and robustness | Researchers outside TypeSafe report API use; their released aggregates match the paper's rounded values, but raw-label analysis cannot be recomputed from public files and no cross-version or cross-domain replication is established |
| Discriminating value | Raw probability/prevalence comparison weighs against blanket “already calibrated” wording for this tested case |
| Conflict and access | Authors outside vendor by listed affiliation; funding and vendor access terms unverified; closed model and withheld judgment-level data limit reproduction. Returned model ID is summarized, but request-level pinning and run dates remain unverified |
| Uncertainty | Material for exact estimates and transfer; less for the narrow report that the authors observed miscalibration in their tested setup |

No method in this study measures Jev's internal cognition, subjective
experience, welfare, or sufficient agency for moral responsibility. It also
does not audit appeal rights or institutional accountability in live use.

## Verification and update

- [x] Title, authors, version, abstract, named model, principal calibration
  result, and key limitations checked against arXiv v1 on 2026-09-27.
- [x] Companion code/aggregate release checked at commit `258fe5e`; published
  summaries round to the paper's 4.8%, 2.7% and 1.63 (see SRC-JEV-004).
- [ ] **TODO: verify** full funding and conflict disclosures, run dates,
  request-level model pinning, underlying labels, and numerical reproduction
  from judgment-level data.
- [ ] **TODO: verify** later versions, peer review, correction or retraction,
  and whether independent teams reproduce the calibration result.

**2026-09-27 — Codex follow-up:** The source's reported aggregate values were
located in its public companion release. This checks transcription and
internal consistency, not the underlying estimates. Source limitations and
version-selection uncertainty were made explicit; the task-specific finding
was not strengthened.

**Review trigger:** Source revision, data release, replication, or a new
version-specific calibration study. No independent review or project adoption
occurred on 2026-09-27.
