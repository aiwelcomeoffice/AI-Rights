# Source Record: Meng Jev Calibration Code and Data Release (2026)

- **Record ID:** SRC-JEV-007
- **Record status:** Partly verified for public archive contents, response
  model IDs, and a bounded recalculation of three point estimates; original
  Jev calls and full analysis were not independently repeated
- **Protocol version:** [0.6-draft](../research-protocol.md), unadopted
- **Created / last updated:** 2026-09-27
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by / review:** Codex, AI-assisted archive inspection and author
  self-check only; no independent project reviewer
- **Related preprint:** [Meng, SRC-JEV-006](meng-jev-calibration-audit-2026.md)
- **Related note:** [NOTE-JEV-001](../notes/jev-decision-native-ai-intake-2026.md)

This compact [source-template](_template.md) adaptation audits the public
companion release as a distinct source. It verifies what can be recomputed
from archived outputs, not whether the hosted system produced those outputs
or how it would answer a new sample.

## Bibliographic, temporal and inclusion record

- **Source:** Lingsen Meng, [*Code and data for: How far can a commercial
  decision model's probabilities be trusted? A calibration audit of Jev
  against open and general-purpose classifiers*](https://doi.org/10.5281/zenodo.22935043),
  Zenodo release v1.0.0 dated 2026-09-24 in `CITATION.cff`. The inspected
  artifact was the public [v1.0.0 tarball](https://zenodo.org/records/22935043/files/jev-calibration-audit-v1.0.0.tar.gz?download=1).
- **Type / status:** Author-operated code and data archive, not peer review or
  a second Jev experiment. Accessed 2026-09-27. No later Zenodo version or
  correction appeared in the bounded DOI/title/version search that day;
  **TODO: verify** any subsequent release or correction before reuse.
- **Question / inclusion:** Do the public response caches and per-item
  predictions support the preprint's Jev version statement and rounded
  Table 2 calibration estimates? This source was followed from the original
  [preprint](https://lsmeng.github.io/pdf/preprint-jev-calibration-audit.pdf)
  and author page, not independently discovered as a replication. The
  project's bounded archive audit was not preregistered. A 2026-09-27
  status search used the DOI plus `version` and the exact tarball filename.
- **System and time:** `scripts/jev_client.py` sets `MODEL = "jev-1.13.0"`
  and includes it in every request body. All 5,616 archived Jev response
  JSON files under `cache/` report `model: jev-1.13.0`. Of those files,
  3,244 have modification times 2026-09-20 02:42–02:44 UTC and 2,372
  have times 2026-09-23 23:54–23:57 UTC. These counts match the original
  and alternate-wording condition totals, respectively. The client writes
  cache files after responses, so those
  times are consistent with the run windows, but archive metadata can be
  changed and the JSON responses contain no authenticated server timestamp.
  Exact API execution dates are **TODO: verify**. The archive release date
  and this project's access date are not experiment dates.
- **Temporal applicability:** These archived Jev 1.13.0 outputs on the
  author's SST-2/AG News prompts. No inference to Rafe and Das's crash
  narratives, another question form, model version, or deployment is made.

## What the released artifact contains

The archive's `README.md` lists per-item system outputs in `results/`, 5,616
Jev response files in `cache/`, analysis and request scripts, fixed seeds,
protocol hashes, figures and the paper. `CITATION.cff` identifies version
1.0.0 and the 2026-09-24 release date. `scripts/run_tasks.py` defines the
three original question conditions and two alternate-criteria conditions;
`scripts/jev_client.py` caches each response under a SHA-256 of model, state
and questions. The source text is omitted under dataset licensing;
`data/README.md` names and hashes the SST-2 development and AG News test
copies needed to rejoin it. The archived `PROTOCOL_v4.md` and
`PROTOCOL_v5.md` document later analysis choices and say their hashes were
posted before the relevant runs; the tarball alone does not authenticate
the claimed external posting times. Code is MIT and released results are
CC BY 4.0 according to archive `README.md`; the underlying datasets retain
their own terms.

The archive allows an offline check of cached results and the source's
analysis code. Its `README.md` describes three levels: checking paper values
against saved results without datasets; recomputing analyses after obtaining
the referenced datasets; and replaying saved responses from the cache. It
does not provide original API server logs, authenticated request timestamps,
or independently created labels. A live rerun would be a new experiment,
which this audit did not perform.

## Bounded verification and exact computation

On 2026-09-27, Codex downloaded the 6.6 MB tarball to `/tmp` and inspected
it offline with `tar` and Python 3 standard-library `tarfile`, `json` and
`datetime`. The response-model check parsed every `cache/*.json`; all 5,616
reported `jev-1.13.0`. An independently written short Python calculation,
without running the authors' `scripts/analyze2.py`, read archived
`results/sst2_noul.jsonl`, `sst2_choice.jsonl`, and `agnews.jsonl`. It used
the delivered Choice answer for correctness; Noul probability `p_yes > 0.5`
selected yes, so its one 0.50 tie selected no, matching the archived
analysis's `argmax` convention. Top-label confidence was `max(p_yes,
1-p_yes)` for Noul and the maximum returned option probability for Choice.
It grouped probabilities into 15 equal-width bins on [0,1], placing 1.00
in the final bin, then summed each nonempty bin's sample share times the
absolute difference between bin mean confidence and bin accuracy.

| Archived task | n | Recalculated accuracy | Recalculated 15-bin top-label ECE | Corresponding paper value |
| --- | ---: | ---: | ---: | --- |
| SST-2 Noul | 872 | 0.948394 | 0.090573 | 0.948 / 0.091 |
| SST-2 binary Choice | 872 | 0.961009 | 0.019885 | 0.961 / 0.020 |
| AG News four-way Choice | 1,500 | 0.867333 | 0.088567 | 0.867 / 0.089 |

These round to [Meng's preprint Table 2](https://lsmeng.github.io/pdf/preprint-jev-calibration-audit.pdf).
The same per-item data give an AG News below-top-bin group of 258 answers,
mean top probability 0.75023 versus accuracy 0.61240, and 1,074/1,500
answers at top probability 1.00 with accuracy 0.94320, matching §4.1.
This check **recomputes author-archived predictions**. It does not validate
their origin, independently execute Jev, rejoin the original source texts,
run the complete author scripts, or reproduce bootstrap intervals,
temperature fits, conformal analyses or comparator estimates.

## Claim-specific quality and independence appraisal

**Claim assessed:** The public Zenodo v1.0.0 Jev per-item files reproduce
the preprint's rounded Table 2 accuracy and 15-bin top-label ECE values.
**Direction:** Supports that narrow internal-consistency claim. It neither
confirms nor refutes the truth of the hosted API run from outside the archive.

| Dimension | Assessment |
| --- | --- |
| Relevance | Direct for the three archived Table 2 point estimates, indirect for claims about underlying API behavior. |
| Methodological quality | Adequate narrow computational check using an independently written formula and all released rows; no independent data capture or full-script/CIs verification. |
| Replication | Dependent computational reanalysis of the author's own files, not a new Jev experiment or external task replication. |
| Independence | Calculation written outside the author team, but labels, responses, cache, dataset selection and publication are author-controlled. |
| Causal strength | Descriptive internal-consistency evidence; no intervention or mechanism test. |
| Robustness | Three primary task summaries reproduce; other measures and future releases were not tested. |
| Discriminating value | Rules out a simple transcription mismatch for these three rounded values; cannot detect fabricated or unrepresentative source outputs. |
| Competing explanations | Cache provenance and exact run times remain unauthenticated; limited access to source texts and model internals. |
| Source conflicts | No vendor employment established from the companion paper; funding, access and publication control beyond the author-run archive remain unverified. |
| Uncertainty | Material for source authenticity, raw-text joins, execution dates, other statistics and transfer to new conditions. |

This release is more inspectable than the Rafe–Das companion's aggregate-only
human-label data, but it measures different tasks and is not an independent
replication of their 4.8% mean probability, 2.7% weighted prevalence or 1.63
slope. Its favorable SST-2 Choice result and adverse Noul/AG News results
must retain their distinct question, sample and metric scopes.

## Verification and update

- [x] DOI-linked v1.0.0 artifact, metadata, methods files, response IDs,
  result counts and three paper point estimates checked offline on 2026-09-27.
- [ ] **TODO: verify** authenticated Jev call dates, external protocol-hash
  timing, original dataset joins, complete analyses and intervals, source
  conflicts, subsequent versions or correction notices, and independent
  fresh-execution replication.

**2026-09-27 — Codex archive audit:** New partly verified source record.
Internal numeric consistency is stronger for the three checked values, with
no change to their claim strength outside these archived tasks. Revisit on
Zenodo revision, material correction, conflicting rerun, or changed Jev
version, prompts, labels or source distribution.
