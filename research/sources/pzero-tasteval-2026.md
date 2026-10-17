# Source Record: TasteVal, arXiv:2610.06824v1

- **Record ID/status:** SRC-RSI-2026-03; Partly verified Draft
- **Protocol:** 0.6-draft
- **Created/updated:** 2026-10-17
- **Prepared by:** Codex, AI-assisted intake; **reviewed by:** not yet independently reviewed
- **Organisation/publisher:** AI Welcome Office / AI Rights & Welcome

## Bibliographic record and scope

Oliver Jaffe and Dane Sherburn, [“TasteVal: Measuring the Experimental Research Taste of AI Systems Against Human Experts”](https://arxiv.org/abs/2610.06824), **arXiv:2610.06824v1**, submitted **2026-10-05**; [HTML v1](https://arxiv.org/html/2610.06824v1) and [P-Zero author's overview](https://pzeroresearch.com/work/tasteval/) inspected 2026-10-17. English, non-peer-reviewed preprint; authors publish through P-Zero Research. No later version/correction/retraction identified at cutoff. The author overview shares the same study and is not a separate replication.

**Disposition:** Core primary study behind Clark's October forecast. **Systems:** twenty 2023–2026 model releases as Researcher, with a fixed Opus 4.8 Coder/harness; the best reported result is Opus 5.5 max reasoning. Exact provider checkpoints and run dates require artifact audit. Paper submission and model release dates are not trial dates. Results transfer only to this Researcher/Coder setup and these eight tasks.

## Source report and evidence profile

Eight newly built, fixed AI R&D tasks cover data curation, pretraining, fine-tuning, preference modeling and adversarial robustness. The Researcher proposes and interprets experiments; an Opus 4.8 Coder implements them on one H100. Each run has **40 GPU-hours or 120 wall-clock hours**; 24 human experts, at least two per task, use the same Coder, and the best expert attempt per task forms the baseline (§§1–2). The paper defines “experimental research taste” as experimental-compute efficiency on these tasks. It reports Opus 5.5 **2.30×** the expert baseline (95% CI **1.15–4.37**) and a fitted **3.0-month** post-December-2025 doubling time (95% CI **1.7–5.0**). Crucially, **normalized final-performance trend shows no detected break** (§§abstract, 3 and Appendix H). Model forecasts of an RSI “taste-only singularity” depend on assumed trend continuation, transfer of unmeasured taste components and full automation (§5); they are simulations, not observations.

**Direction and quality:** Direct for benchmark-relative experiment selection under the paper's metric, indirect for frontier R&D and RSI. The fixed Coder and hidden test scores improve isolation of the measured component; task selection, Coder behavior, low-noise single-H100 scoring, human recruitment, best-of-experts baseline and analytical break choice still matter. The tasks are withheld to limit contamination, restricting independent audit and reproduction. Authors state top researchers were not in the baseline and that problem selection, large-scale coordination and deep novel ideas were not measured (§4). Limited agent elicitation and much lower per-run agent cost may bias the comparison in the other direction. Bootstrapped intervals address sampled variation, not construct mismatch or forecast assumptions. Author affiliation/financial interests beyond the stated P-Zero role remain to be checked. No independent replication found in the bounded search.

**Supports:** a substantial measured improvement on the operationalized experimental-design tasks. **Challenges:** a blanket statement that the work measures all scientific taste or demonstrates full RSI. **Does not establish:** autonomous design/training/deployment of successive frontier models, a 2027 RSI date, or general superiority to the best human AI researchers.

**Verification:** arXiv abstract, HTML §§1–5 and relevant methods/appendix passages inspected 2026-10-17. Search: Clark's original link; `P-Zero TasteVal paper 2026 experimental research taste human baseline 24 experts results`; `TasteVal 2610.06824 critique replication October 2026`. TODO: inspect runnable artifacts if released, exact run dates/checkpoints, task-level and Coder error audits, independent reruns and forecast sensitivity.
