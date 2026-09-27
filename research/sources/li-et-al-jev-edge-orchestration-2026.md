# Source Record: Li et al. on Jev Edge-Service Orchestration (2026)

- **Record ID:** SRC-JEV-005
- **Record status:** Partly verified for the preprint's reported design,
  configuration, results, and limits; no raw-result reproduction or independent
  review
- **Protocol version:** [0.6-draft](../research-protocol.md), unadopted
- **Created / last updated:** 2026-09-27
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by / review:** Codex, AI-assisted source appraisal / author
  self-check only
- **Related note:** [NOTE-JEV-001](../notes/jev-decision-native-ai-intake-2026.md)

This record asks what one externally authored service experiment reports about
Jev's decision latency, semantic accuracy, delivered completion, and API fees.
It is not a calibration test, a reproduction of TypeSafe's benchmarks, or an
assessment of Jev's agency or experience.

## Source, scope, and search

- **Source:** Delong Li, Xu Wang, Haochen Gong, Rui Lang, and Guangsheng Yu,
  [“Replacing Large Language Models with Jev Decision Models for Low-Latency
  Edge Service Orchestration”](https://arxiv.org/html/2609.22753v1),
  arXiv:2609.22753v1, submitted 2026-09-19. The [version page](https://arxiv.org/abs/2609.22753)
  listed v1 only and no withdrawal notice when checked 2026-09-27. This is a
  preprint; peer review or later publication was not established.
- **Affiliation:** The paper lists the School of Electrical, Mechanical and
  Biomedical Engineering, University of Technology Sydney (§ heading). It
  does not state a TypeSafe affiliation. Funding, API access terms, and full
  conflict disclosures were not located in the checked full text; **TODO:
  verify** them before treating institutional independence as established.
- **Selection:** Included as core evidence for the bounded service-path
  question already identified, but unappraised, in NOTE-JEV-001. That earlier
  discovery and this source-specific selection were not preregistered. On
  2026-09-27 the arXiv v1 HTML and version page were read directly; bounded
  searches for the exact title with `GitHub`, `code`, `data`, and `funding` did
  not locate an author-linked release. No exhaustive repository search is
  claimed. The same authors' [related 6G preprint](https://arxiv.org/abs/2609.23136)
  was checked for lineage, not included as an independent replication here.
- **Target and claim type:** The reported service-path outcomes are empirical
  observations by the authors; their deployment recommendation is an author
  interpretation. The Jev note's accountability questions remain separate
  system-level and governance questions.

## Temporal and system applicability

- **Jev access path and reported version:** OpenRouter Decisions endpoint
  `typesafe/jev-1.13`; responses identified `jev-1.13-20260917` and provider
  TypeSafe (Appendix A-A). Four native Choice questions supply the intent
  fields in one request. The paper does not expose Jev weights or internal
  serving. Its returned ID differs in form from the `jev-1.13.0` ID reported
  in the separate crash-narrative study; checkpoint equivalence is unverified.
- **Comparison configurations:** `deepseek-v4.1-flash` via OpenRouter, pinned
  to Together with provider fallback disabled and a concise strict JSON
  response; self-hosted Qwen2.5-7B-Instruct revision `a09a35458c70` and a
  fixed rule parser appear in the real-service comparison (Appendix A-A).
- **Observation/experiment date:** 2026-09-18 (Appendix A-A). The study uses
  one measurement session. The 2026-09-19 submission and 2026-09-27 project
  inclusion dates do not extend its applicability.
- **Direct applicability:** The named hosted endpoints, prompts, four-field
  intent contract, 2-second deadline, workload, validation, admission,
  scheduler, cache policy, network path, and two-node OCR service described in
  §§III–IV and Appendix A. The fixed date and configuration limit transfer to
  later endpoints, other tasks, organizations, prices, or field deployments.

## Methods and reported findings

The four fields are service, locality, quality floor, and urgency, with 108
possible tuples (Table I). A common validator and scheduler handle each
backend's output. Study A uses 216 synthetic English requests, reused across
three consecutive API measurement blocks; it combines measured interpretation
timing with **modeled**, rather than executed, service work (§IV-B, Appendix
A-C). Study B runs a real two-node Tesseract OCR service using fixed request
descriptions, images, arrival schedules, and eight service conditions per
backend; each condition has 36 supported and 12 unsupported requests (§IV-B,
Appendix A-D). Complete backend runs are sequential in randomized order, so
matched inputs do not eliminate time-varying provider or network effects.

| Reported observation | Locator | Interpretation and limit |
| --- | --- | --- |
| Study A median client decision latency is 314.7–320.7 ms for Jev versus 381.4–434.7 ms for DeepSeek across three blocks, a reported 15.9–26.5% reduction. | §V-A, Table II | Supports a faster observed hosted path in this session; it does not isolate model inference from routing and network transport. |
| Exact four-field semantic correctness is 214/216, 213/216, and 212/216 for Jev versus 216/216, 215/216, and 216/216 for DeepSeek. Jev makes nine error occurrences across five texts; one maps an unsupported translation request to OCR. | §V-A, Table II, Figure 2 | Contrary to an unqualified “faster with equal interpretation quality” claim. Eight Jev errors replace unspecified with normal urgency, which this scheduler treats alike; the unsupported-to-OCR text was not selected into Study A's modeled execution traces. |
| In Study B, correct, on-time OCR completion is 168/288 supported arrivals for Jev and 166/288 for DeepSeek; Jev ties in seven of eight conditions and leads by two in one. Jev correctly rejects 92/96 unsupported arrivals versus 80/96 for DeepSeek, but falsely dispatches four unsupported requests to OCR. | §V-C, Tables III–IV | Descriptive outcomes for one service family; substantial OCR/execution failures remain, and the small completion difference is not a statistical noninferiority finding. |
| Among requests both systems complete correctly, Jev's median full request time is 11.1–25.3% lower in four uncached conditions. With repeated-text caching, paired median savings are -0.37 and -0.49 ms in two conditions. | §§IV-D, V-D, Table IV | The latency benefit is conditional on shared success and fresh interpretation; caching largely removes it for repeated descriptions. |
| Jev's billed API fees per correct OCR completion are reported 68.97–70.61% lower across Study B's eight conditions. | §V-E, Figure 8 | This is a provider-fee comparison for the tested calls, excluding local computation, communication, energy, and maintenance. |

The paper reports no forbidden off-site image bytes in these runs (§V-C),
while the textual request description still reaches the chosen interpretation
API (§III-C). That observation does not establish general privacy compliance
or a tested access-control guarantee for other deployments.

## Critical appraisal and evidence lineage

The claim-specific directions differ: the reported Study A result **supports**
lower client decision latency for the configured Jev path; its strict field
result **weighs against** equal semantic accuracy on the same texts. Study B's
completion counts are **descriptively close**, but do not establish
noninferiority or general completion equivalence. The claims share the
following design and provenance profile; the stated limits apply to both the
favorable and adverse observations.

| Dimension | Descriptor and rationale |
| --- | --- |
| Relevance | **Direct** to the dated four-field service-path comparison; **not applicable** to probability calibration. |
| Methodological quality | **Adequate for descriptive comparison, limited for generalization.** Matched inputs, common validator and scheduler, distinct semantic/completion endpoints, and explicit backend settings help; author-generated synthetic texts, selected deadlines, one OCR service, and sequential provider runs limit broader use (§§IV–VI). |
| Replication | **Not independently replicated here.** Three Study A blocks reuse the same 216 texts in one session; Study B has one run per condition/backend. No raw-result recomputation was performed. |
| Independence | **Partial.** Listed university authors separately executed a study outside TypeSafe's launch evaluations, but Jev calls use TypeSafe's hosted service through OpenRouter. The [related 6G paper](https://arxiv.org/html/2609.23136v1) has the same five authors and cannot count as independent-team confirmation; overlap of runs or data is **TODO: verify**. |
| Causal strength | **Configured substitution.** Holding the contract and scheduler common isolates the interpreter-path change within this pipeline, but the hosted timings combine model service, routing, and transport; Jev's internal architecture alone is not isolated. |
| Robustness | **Mixed/untested beyond these conditions.** The latency direction holds across three within-session blocks and uncached Study B conditions; repeated-text caching removes a material full-path advantage, and strict semantic accuracy favors DeepSeek. Other days, tasks, and endpoint versions are untested. |
| Discriminating value | **Partial.** Caching and a strict semantic endpoint discriminate against a blanket claim of uniformly faster, equally accurate decisions. The experiment does not discriminate internal model-speed causes from provider/network causes. |
| Competing explanations | **Partly examined.** The common scheduler and paired workloads limit downstream-policy differences; sequential runs leave provider/network variation possible, and author-written texts and the chosen comparison model may affect the result (§§IV-B, VI-C). |
| Source conflicts | **Unknown.** Full funding, vendor access terms, and publication-control disclosures were not located; the visible byline is university-affiliated. Unknown terms are not evidence of a conflict. |
| Uncertainty | **Material** for transfer, exact numerical reproduction, and completion equivalence. No author-linked raw traces/code were located in this bounded check; §IV-E reports descriptive comparisons without an application-justified noninferiority margin. |

The preprint is therefore a useful external observation of one **configured
service path**, with limits that do not erase its measured results. It is not
an independent reproduction of the Rafe–Das calibration estimate: its
endpoints, outcome measures, and returned model ID differ, and it does not
compare predicted probabilities with reference frequencies.

## Relevance, verification, and update

- **May inform:** A narrowly dated description of latency, field-level
  accuracy, completion, cache effects, and billed fees for decision-native AI
  in a downstream service workflow.
- **Cannot establish:** General Jev calibration or safety, overall operating
  cost, a field-deployment outcome, internal architecture, autonomous agency,
  moral responsibility, subjective experience, welfare, or a project policy.
- **Would strengthen this appraisal:** Public per-request traces and code,
  reproduction of the numerical tables, independently authored requests
  across days and services, and comparable versioned endpoints.
- **Would weaken or narrow it:** A corrected result, failed reproduction,
  changed endpoint or pricing, or evidence that the matched comparison did
  not hold as reported. A source revision or documented code/data release
  should trigger re-review.

- [x] Original full text, title, authors, v1 status, configurations, study
  date, key results and contrary material checked 2026-09-27.
- [x] Same-author related preprint identified for evidence-lineage caution.
- [ ] **TODO: verify** full funding/conflict and vendor access disclosures,
  author-linked code/data availability, request-level logs and arithmetic
  reproduction, later correction/publication status, and independence of the
  related paper's runs.

**2026-09-27 — Codex:** Initial bounded documentary appraisal; author
self-check only. No source result was independently reproduced, no public
claim was reviewed by another person, and no project position changed.
