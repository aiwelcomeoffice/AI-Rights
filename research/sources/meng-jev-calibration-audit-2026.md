# Source Record: Meng on Jev Probability Calibration (2026)

- **Record ID:** SRC-JEV-006
- **Record status:** Partly verified for the preprint's identity, methods,
  reported findings and limitations; not an independently repeated Jev test
- **Protocol version:** [0.6-draft](../research-protocol.md), unadopted
- **Created / last updated:** 2026-09-27
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by / review:** Codex, AI-assisted documentary appraisal / author
  self-check only; no independent project reviewer
- **Related records:** [Zenodo release audit, SRC-JEV-007](meng-jev-calibration-archive-2026.md);
  [Rafe and Das crash-narrative preprint, SRC-JEV-003](rafe-das-jev-crash-narratives-2026.md)
- **Related note:** [NOTE-JEV-001](../notes/jev-decision-native-ai-intake-2026.md)

This compact [source-template](_template.md) adaptation appraises one primary
preprint. A separate record checks its code and per-item release. Inclusion is
not peer review, replication of another task, or project adoption.

## Bibliographic and temporal record

- **Source:** Lingsen Meng, [*How far can a commercial decision model's
  probabilities be trusted? A calibration audit of Jev against open and
  general-purpose classifiers*](https://lsmeng.github.io/pdf/preprint-jev-calibration-audit.pdf),
  preprint draft dated 2026-09-24, 15 pages. The author's [public summary](https://lsmeng.github.io/blog-jev-confidence.html)
  covers the favorable and adverse findings. The PDF lists UCLA's Department
  of Earth, Planetary, and Space Sciences as the author's affiliation.
- **Type / version / review:** Original empirical preprint, draft dated
  2026-09-24; no numbered paper version or peer-review claim appears in the
  checked PDF. Accessed 2026-09-27. No correction, withdrawal or later
  version was identified on the author page or in a bounded title/version
  search that day; **TODO: verify** subsequent publication and notices.
- **System / version:** The paper reports Jev `1.13.0` called through its
  public API with the model version pinned (§2.2, Appendix A). The companion
  archive's request code and response-model check are assessed separately in
  [SRC-JEV-007](meng-jev-calibration-archive-2026.md).
- **Experiment dates:** The paper says its two Jev wording runs were four
  days apart (§4.3), but gives no authenticated per-call dates. Archived cache
  file times are possible run-window proxies, as SRC-JEV-007 specifies; the
  exact API execution dates remain **TODO: verify**. The model release date
  is not established by this preprint. Source publication and this project's
  2026-09-27 inclusion date do not extend empirical applicability.
- **Temporal applicability:** The reported Jev 1.13.0 answers to these English
  public classification examples and question wordings. Other domains,
  prompt forms, later versions, and live deployment traffic require new tests.

## Question, method and evidence lineage

**Inclusion question:** For the tested Jev version, do returned top-label
probabilities track observed correctness across specified text tasks and
question forms? This independently executed study was found through bounded
public search on 2026-09-27 and followed to the original PDF. The project
search was not preregistered. Discovery included `"Jev" "1.13.0"
calibration probability`; follow-up opened the author summary, original PDF
and linked Zenodo DOI. A bounded 2026-09-27 status search included
`"Lingsen Meng" "Jev" calibration v2 correction` and the exact title
with `correction retraction`. It is supplementary evidence for the Jev
calibration inquiry, not a task-matched replication of crash-narrative coding.

The PDF's §§2–3 and Appendix A use 872 SST-2 development-set movie-review
sentences, each asked as a Noul yes/no and a binary Choice, plus a seeded
1,500-item sample from the AG News test set asked as a four-way Choice. That
is 3,244 primary calibration evaluations of 2,372 distinct texts. A second
set of label descriptions adds 2,372 Jev calls, for 5,616 total (§2.1).
The Noul and Choice questions differ in their instructions and criteria as
well as question type, so the paired comparison tests **complete question
forms**, not the isolated effect of the primitive (§2.1). Accuracy uses the
delivered Choice even when rounded probabilities tie. Top-label ECE uses 15
equal-width bins of the probability of the chosen class and item-bootstrap
intervals. This measure differs from Rafe and Das's pooled positive-class
probability/prevalence gap and calibration slope. Temperature scaling is fit
on one half and evaluated on the other over 200 random splits (§3). The
comparators are two DeBERTa checkpoints with different reported task
exposure and two small general-purpose language models (§2.2).

The author and UCLA affiliation differ from TypeSafe and the Rafe–Das team;
the public datasets, labels and prompts differ as well. That makes this a
separate Jev execution and a useful adjacent calibration test. No direct
funding or access lineage was identified in the checked PDF, but full
funding, vendor access terms and publication control remain **TODO: verify**.
The PDF discloses Claude as a coding, analysis and manuscript assistant, with
Meng responsible for the claims (p. 12). No method here reproduces the
weighted 2,416-pair human-reference estimate on crash narratives.

## Findings and contrary material, with original locators

| Source-reported observation | Locator | Claim-specific interpretation |
| --- | --- | --- |
| SST-2 Noul: accuracy 0.948, top-label ECE 0.091; Choice on the same 872 sentences: accuracy 0.961, ECE 0.020 | PDF Table 2, §4.1; [author summary §1](https://lsmeng.github.io/blog-jev-confidence.html) | Favorable near-calibration for the Choice form and contrary underconfidence for Noul. The paired ECE difference is 0.071, bootstrap interval [0.047, 0.086]; wording and primitive vary together. |
| AG News Choice: accuracy 0.867, ECE 0.089. Below the top bin, 258 answers average stated top probability 0.750 against accuracy 0.612. 71.6% of answers report top probability 1.00 but only 94.3% are correct | PDF Table 2, §4.1, Figure 1; [author summary §1](https://lsmeng.github.io/blog-jev-confidence.html) | Evidence against unqualified raw calibration for that task/range; quantization limits probability-threshold resolution. |
| Held-out temperature scaling changes ECE from 0.091 to 0.023 for SST-2 Noul and 0.092 to 0.028 for AG News; it does not improve already near-calibrated SST-2 Choice (0.024 to 0.034) | PDF Table 4, §4.1; author summary §2 | A useful correction for two tested conditions, not a universal benefit or transferable map. The fitted AG News temperature depends on how exact zeros are clipped. |
| Jev is more accurate than the checkpoint reported as task-unexposed across 16 wording/rule cells, but less accurate than the task-exposed checkpoint on AG News; label descriptions move the AG News gap | PDF §§4.3–4.4, Tables 6–8; author summary §§3–4 | Mixed comparator evidence; checkpoint training and evaluator wording materially affect any ranking. The full-test-set estimate is exploratory (§6). |
| Under one three-way threshold procedure, Jev passes a 5% AG News auto-routing test in 0/2,000 random splits and the SST-2 test in 191/2,000 using the comparison author's wording | PDF §4.5; author summary §5 | Procedure- and data-budget-specific. Changing the threshold-selection rule changes pass rates sharply; this does not show no useful operating point exists. |

The paper also reports that randomized split conformal prediction meets its
**marginal** 95% AG News coverage target, while the selected single-label
answers are wrong 5.93% of the time (§4.2, Table 5). Neither a low top-label
ECE nor marginal coverage alone establishes safe performance of a specific
downstream action. The PDF's §6 limits conclusions to two English tasks, one
version, in-distribution splits and an exploratory comparison; it did not
test domain-specific data, longer contexts, other languages, latency or cost.
Source texts are omitted from the archive for licensing, while predictions
and cached responses are released (data and code availability, p. 12).

## Claim-specific quality and independence appraisal

**Claim A assessed:** Jev 1.13.0 is calibrated as returned across these
question forms and English tasks. **Direction:** Mixed: near-calibrated SST-2
Choice, underconfident SST-2 Noul, and overconfident AG News mid-range.

| Dimension | Assessment |
| --- | --- |
| Relevance | Direct for the three specified task/form conditions; indirect for crash-narrative positive-class calibration. |
| Methodological quality | Adequate exploratory outside-API audit with public labels, paired SST-2 items, stated metrics and released outputs; form changes are confounded and benchmark exposure is unknown. |
| Replication | No independently repeated API run of this study identified; companion archived-output recalculation is a dependent computational check. |
| Independence | Separate author, institution, corpus and prompts from Rafe–Das and TypeSafe; funding and access-control details not fully established. |
| Causal strength | Descriptive calibration evidence, not a controlled mechanism test. |
| Robustness | Paper checks several ECE bin schemes; cross-domain and cross-version robustness remain untested. |
| Discriminating value | Strong against a universal raw-calibration claim; the favorable Choice result prevents a universal miscalibration claim. |
| Competing explanations | Wording, task difficulty, labels, model-training exposure and quantization partly examined or acknowledged; no transfer test to crash narratives. |
| Source conflicts | No vendor employment shown; funding, access terms and publication control unresolved. |
| Uncertainty | Material for exact experiment dates, benchmark exposure and practical threshold behavior beyond these samples. |

**Claim B assessed:** A task-specific temperature fit improves calibration
on the two initially miscalibrated study conditions. **Direction:** Supports
for those held-out same-dataset splits, while the null/worse Choice result
limits generalization. Relevance and within-sample method are direct and
adequate; replication is same-team only, robustness outside the sampled
distributions is untested, and exact-zero handling affects the fitted map.
It supplies no correction factor for Rafe and Das's task. Neither claim
measures Jev's internal cognition, subjective state, welfare, agency or
responsibility, and neither is a project decision.

## Verification and update

- [x] PDF identity, method, Table 2, Table 4, §§4–6 and author summary checked
  against the original on 2026-09-27.
- [x] Linked Zenodo v1.0.0 release inspected separately; the three Table 2
  point estimates were recomputed from its per-item files (SRC-JEV-007).
- [ ] **TODO: verify** authenticated run dates, funding and access terms,
  independent fresh execution, later review/correction status, and any
  task-matched crash-narrative replication.

**2026-09-27 — Codex source intake:** New partly verified primary source.
The earlier crash-specific position is not superseded; this record adds
independent adjacent evidence with favorable and contrary outcomes. Revisit
after a revised preprint, material criticism/correction, fresh independent
replication, or a model, question, corpus or decision-rule change.
