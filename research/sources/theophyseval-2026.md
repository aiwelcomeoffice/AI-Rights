# Source Record: TheoPhysEval, arXiv:2610.16733v1

- **Record ID/status:** SRC-THEOPHYS-2026-01; Partly verified Draft
- **Protocol:** 0.6-draft
- **Created/updated:** 2026-10-17
- **Prepared by:** Codex, AI-assisted intake; **reviewed by:** not yet independently reviewed
- **Organisation/publisher:** AI Welcome Office / AI Rights & Welcome

## Bibliographic record and scope

A. Ramesh Chandra **et al.** (34 listed authors), [“TheoPhysEval: Assessing AI agents at autonomous theoretical physics problem solving”](https://arxiv.org/abs/2610.16733), arXiv **2610.16733v1**, submitted **2026-10-09**, 8+48 pages, English preprint; [HTML v1](https://arxiv.org/html/2610.16733v1) inspected 2026-10-17. The arXiv record identifies v1; no later version, journal peer review, correction or retraction was identified at the cutoff. Full author order is in the arXiv record. Affiliations and funding/conflict declarations need a dedicated audit.

**Disposition:** Core primary experiment. **System:** five model-plus-harness agents; GPT-6-Astra with Codex at max reasoning is the focal configuration. Exact API checkpoint, model training/development dates and experiment dates are not specified in the inspected text. A model release date or paper submission date must not substitute for trial dates. Transfer to plain GPT-6 Astra, another harness, novel open-problem discovery or later systems is untested.

## Source report and evidence profile

Experts supplied **50 unpublished, verifiable, research-level theoretical-physics problems**, mainly extensions of known techniques, across eleven themes (§§I–II). The authors added numerical values so symbolic answers could be graded numerically. Harbor ran a realistic track with literature/web access and local tools, and an isolated track with local tools but no web access (§III). Each agent completed **one full-suite API run**; ordinary tasks had an eight-hour cap, with no token or total-cost cap. Astra scored **49/50 realistic**, **46/50 isolated**; Opus 5.5 scored **46/50 in both**; others scored lower (§IV.1). The abstract reports Astra average API cost under USD 3 per problem. The team corrected several expert reference solutions after inspecting Astra answers; two prompts had under-specified conventions and the grading key was adjusted to accept observed convention choices (§§III–IV.2). No model solved one inverse problem. Some experts had used AI while preparing problems, so leakage cannot be ruled out (§I). The authors' qualitative claims about weaker problem choice and direction changes are explicitly anecdotal, not quantified (§V).

**Direction and quality:** Strongly relevant to bounded final-answer calculation performance; good task and setup disclosure, but a single stochastic run and adjudication after results limit precision. Numerical final-answer grading measures correct outputs more directly than derivational soundness or novelty. The problem set is neither exhaustive nor adversarial; expert network sampling and AI-aided preparation affect representativeness and contamination risk. Open benchmark materials improve potential reproducibility, but gated access and no rerun here leave replication unattempted. Authors designed/graded the tasks and used agents in evaluation code and manuscript preparation (§Acknowledgments); those dependencies require independent checking. The paper supports strong performance on this suite, not end-to-end autonomous scientific agenda setting or autonomous AI R&D improvement.

**Verification:** arXiv abstract, HTML §§I–V, tables and Appendix references inspected 2026-10-17. Search: direct user URL; `TheoPhysEval 2610.16733 critique replication correction October 2026`. Secondary summaries excluded as duplicate evidence. TODO: audit exact grading files, solution corrections and per-task traces with domain experts, repeat seeds, verify experimental dates/checkpoints and author conflicts, monitor version/correction status.
