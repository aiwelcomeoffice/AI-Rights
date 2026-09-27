# Source Record: Jev Crash-Narrative Code and Aggregate Release (2026)

- **Record ID:** SRC-JEV-004
- **Record status:** Partly verified for the public release inventory and
  agreement between published aggregates and reported rounded results;
  judgment-level calculations not independently reproduced
- **Protocol version:** [0.6-draft](../research-protocol.md), unadopted
- **Created / last updated:** 2026-09-27
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by / review:** Codex, AI-assisted documentary and code intake /
  author self-check only
- **Related records:** [Rafe and Das preprint](rafe-das-jev-crash-narratives-2026.md);
  [NOTE-JEV-001](../notes/jev-decision-native-ai-intake-2026.md)

This is an audit of what the authors released for one preprint, not a new Jev
evaluation, a reproduction from observations, or an independent evidence line.

## Source, version and question

- **Source:** The authors' [public companion repository](https://github.com/pozapas/jev-calibrated-narrative-coding),
  linked from the [preprint's Data and code availability section](https://arxiv.org/html/2609.24052v1#Sx1).
- **Version checked:** `master` commit
  [`258fe5e6678747cf6b234a1eedc4984f99a69460`](https://github.com/pozapas/jev-calibrated-narrative-coding/tree/258fe5e6678747cf6b234a1eedc4984f99a69460),
  authored 2026-09-23; accessed 2026-09-27. The repository is mutable; this
  commit identifies the inspected tree. Its README says code and aggregates
  are MIT-licensed, while Texas CRIS narratives are under a separate data
  agreement and absent from the release.
- **Question:** Can the public files verify the preprint's 4.8% mean Jev
  probability, 2.7% weighted human-reference prevalence and 1.63 calibration
  slope for its `jev-1.13.0` crash-narrative task? What cannot be checked?
- **Claim type / intended use:** Documentary and computational-reproducibility
  appraisal of a reported empirical result in a working source record.
- **Temporal applicability:** The paper's described `jev-1.13.0` test; the
  aggregate reports that returned model ID, while request-level pinning and
  exact API execution dates are not established by this repository. The
  2017–2025 CRIS record period, paper submission date and repository commit date are
  different events. No transfer to another Jev version or task is assessed.

## Discovery and check

On 2026-09-27, this bounded check followed the preprint's direct repository
link, cloned the public repository at the commit above, and inspected its
tracked file list, README, `requirements.txt`, `data/gold/gold_analysis.json`,
`data/frontier/frontier_analysis.json`, `outputs/numbers.tex`, the
documented `src/s11_tables.py` and `src/s13_numbers.py` generators, and
`src/jev_runner.py`. This was one source found by citation chaining, with no claim of a comprehensive code
search. No crash narratives, individual human judgments or Jev API calls were
accessed. Python's standard JSON reader was used to compare published
aggregate values; the analysis scripts were not run to completion.

| Public artifact or source statement | Check and limit |
| --- | --- |
| [`data/gold/gold_analysis.json`](https://github.com/pozapas/jev-calibrated-narrative-coding/blob/258fe5e6678747cf6b234a1eedc4984f99a69460/data/gold/gold_analysis.json), `pooled` | Records 2,416 usable pairs, weighted mean probability `0.0478672752`, weighted prevalence `0.0266066753`, mean probability minus prevalence `0.0212606000`, and calibration slope `1.6340424767`. The reported difference agrees with subtracting the first two values. These round to the paper's 4.8%, 2.7% and 1.63. The [frontier aggregate](https://github.com/pozapas/jev-calibrated-narrative-coding/blob/258fe5e6678747cf6b234a1eedc4984f99a69460/data/frontier/frontier_analysis.json) repeats the Jev pooled values; this is the same authors' derived output, not independent confirmation. |
| [README, “What is not here” and “Reproducing”](https://github.com/pozapas/jev-calibrated-narrative-coding/blob/258fe5e6678747cf6b234a1eedc4984f99a69460/README.md) | The authors release schema, code, aggregate JSON, figures and tables. They withhold narratives, raw model outputs, per-judgment human labels, joins and run artifacts because of the data agreement and identifiers. Their paper says a de-identified pair-level audit table is prepared but its release awaits data-owner permission. The public aggregates can be cross-checked for internal consistency; the calibration estimate, weights and slope cannot currently be recomputed from the underlying labeled pairs. |
| Documented aggregate regeneration commands | The README instructs readers to run `python src/s13_numbers.py` and `python src/s11_tables.py`. In the checked tree, both scripts resolve `DATA` as `Path(__file__).resolve().parents[2] / "paper1" / "data"`, while released data are at repository-root `data/`; `s13_numbers.py` also writes under `paper1/manuscript`, whereas the README lists `outputs/numbers.tex`. Beyond that path mismatch, `s13_numbers.py` reads withheld judgment- and record-level inputs. A local attempt stopped first because this audit environment lacks `numpy`, so end-to-end behavior after installing dependencies was not tested. The documented aggregate-only regeneration is therefore not established by this release. |
| [Runner](https://github.com/pozapas/jev-calibrated-narrative-coding/blob/258fe5e6678747cf6b234a1eedc4984f99a69460/src/jev_runner.py) and [`data/analysis.json`](https://github.com/pozapas/jev-calibrated-narrative-coding/blob/258fe5e6678747cf6b234a1eedc4984f99a69460/data/analysis.json) | The runner declares `MODEL = "jev-1.13.0"` but its `client.system_one(...)` call does not pass `model=MODEL`. It records the model returned in each response, and the published aggregate reports 195,857 returned IDs as `jev-1.13.0`; raw per-call logs are withheld. Thus the public summary supports the reported response version, but the released call path does not demonstrate request-level pinning. The runner also records elapsed latency, not a request timestamp, so the API run dates remain unknown. |

The [preprint](https://arxiv.org/html/2609.24052v1#Sx1) also says a release
manifest is present. No manifest appears in the tracked tree at this commit.
Its README opening says the paper converts all 5,018,080 eligible narratives,
while the [paper abstract and Table 2](https://arxiv.org/html/2609.24052v1)
report a 499,500-narrative screen and full 27-question coding of 195,857;
full-corpus cost is projected. These documentation discrepancies do not by
themselves refute the measured calibration result, but they limit what the
release instructions establish.

## Claim-specific appraisal and boundaries

| Dimension | Assessment |
| --- | --- |
| Direction and relevance | Supports that the published aggregate files contain the paper's rounded values; challenges a reading that the publicly available files already permit independent recalculation from labels. Direct for release transparency, indirect for the truth of the underlying calibration result. |
| Method and robustness | JSON inspection and arithmetic are reproducible on the pinned commit. The raw labels, probabilities and weights needed to test sample construction, exclusions, uncertainty intervals and slope fitting are not public. No independent reanalysis was performed. |
| Independence and conflict | The paper, code and aggregates share an author-controlled data and analysis lineage. GitHub publication is not replication. Funding, TypeSafe access terms and publication control beyond the listed university affiliation were not established in this bounded check. |
| Uncertainty | Material for underlying numerical validity and transferability; low for what the inspected public files contain. A corrected repository, released pair-level table or controlled audit could change this assessment. |

A pair-level recomputation that agrees with the aggregates would strengthen
confidence in the reported task-specific calculation; a material discrepancy
would weaken it. Corrected file paths or a new manifest alone would improve
release usability without checking the judgment-level result. A different
version or task would require its own assessment.

This record does not determine whether Jev is calibrated in any other task,
whether the paper's result is externally valid, or whether Jev has agency,
experience, welfare or moral status. It creates no project position.

## Verification and update

- [x] Preprint's repository link, pinned commit, README release statement,
  tracked file inventory, aggregate values, script paths and model-call site
  checked on 2026-09-27.
- [ ] **TODO: verify** judgment-level metrics if the prepared pair-level audit
  table is lawfully released or an authorized controlled audit is available.
- [ ] **TODO: verify** corrected aggregate regeneration instructions with a
  dependency-equipped environment and check subsequent repository revisions.
- [ ] **TODO: verify** exact Jev API run dates, request-level model selection,
  funding, vendor access terms, full conflict disclosures, and independent
  task-matched replication.

**2026-09-27 — Codex:** Initial bounded release audit. The public aggregates
match the paper's rounded calibration numbers, but no underlying-result
reproduction or independent review is claimed.
