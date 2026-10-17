# Research Notes: TheoPhysEval and GPT-6 Astra scientific calculation

- **Note ID/status:** RN-THEOPHYS-2026-01; Partly verified Draft working research
- **Protocol:** 0.6-draft; **cutoff:** 2026-10-17
- **Source records:** [arXiv v1](../sources/theophyseval-2026.md), [benchmark artifact page](../sources/theophyseval-hugging-face-artifacts-2026.md)
- **Question:** How well did GPT-6-Astra with Codex solve the suite's previously unpublished, verifiable theoretical-physics calculations under tool-enabled and isolated conditions, and what does this say about broader research autonomy?
- **Prepared/updated:** Codex, 2026-10-17; **independent review:** pending
- **Organisation/publisher:** AI Welcome Office / AI Rights & Welcome

This retrospective intake examines the paper's actual measured task, not an open-ended discovery claim. “Autonomous” means no human hints **after the provided problem prompt** within the run. It does not mean the agent chose the research question, validated its own contribution in a field or improved its successor. The term “scientific reasoning” here covers the tested calculation-and-tool workflow; whether the result reflects retrieval, memorized domain knowledge, algorithmic reasoning or their combination is a separate mechanistic question. Discovery: direct arXiv URL, v1 HTML and linked Hugging Face card; search `TheoPhysEval 2610.16733 critique replication correction October 2026`. Secondary recaps were excluded as duplicate evidence. No independent trial or domain proof audit was performed.

## Temporal and system applicability

The tested agent is **GPT-6-Astra plus Codex harness at max reasoning** in Harbor on standardized cloud VMs. Comparators are Opus 5.5/Claude Code, Gemini 3.8 Flash/Antigravity, DeepSeek-V4.1-Flash/Codex and GLM 5.3/Claude Code (§III). Exact API checkpoint and trial dates are not stated. The paper was submitted **2026-10-09**; that is not a measurement date. The result does not automatically transfer to other GPT-6 Astra deployments, a later checkpoint, a different harness, another science, or unsolved research problems.

## Experiments and reported outcomes

| Design/result | Original locator | Evidential scope |
| --- | --- | --- |
| **50** expert-contributed, unpublished research-level questions across eleven theoretical-physics themes; extensions of known techniques, not important open problems | §§I–II, Table 1 | Strong task relevance to calculational subwork; selection through expert networks and verifiability constrain generalization. Some human solutions used AI assistance, so leakage cannot be excluded. |
| Symbolic expressions converted to hard-to-guess numerical answers; Harbor grants local tools, with web/literature on the **realistic** track and no web on the **isolated** track | §III | Final-answer validity is measured more directly than derivation quality or novelty. Isolated runs retain model knowledge and local computation. |
| **One full-suite run** per agent, eight-hour ordinary-task cap and no token/cost cap | §III | Stochastic variance and budget comparability need care. |
| Astra **49/50 realistic**, **46/50 isolated**; Opus **46/50** both; Gemini **34/50** and **31/50**; DeepSeek **27/50** and **25/50**; GLM **21/50** and **26/50** | §IV.1, Figures 3–4 | Observed pass counts for named model-plus-harness conditions. Astra's realistic score is particularly strong; the sample and single run do not establish exact underlying success probability. |
| Experts corrected subtle errors in several reference solutions after examining Astra answers; two prompts had under-specified conventions and the key accepted observed conventions | §§III, IV.2 | Valuable evidence that the agents could challenge a human answer key; also a reminder that grading and adjudication can change after results. The original/corrected solutions need independent audit. |
| No model solved the inverse problem; Astra lost three more items when isolated | §§IV.2–V | Direct contrary evidence to perfect or universal performance. The isolated gap shows tools can matter on particular items even if average changes are small. |
| Authors report Astra average API cost below USD 3/problem | Abstract, Table 3 | Inference/API cost under their run; not total researcher, task-creation, grading, infrastructure or validation cost. |

The authors infer significant memorization of literature from similar track scores. That is plausible but not uniquely identified: internalized formulas, generalized techniques, problem-family structure and locally regenerated calculations may coexist. They also infer agents can match expert calculations, while their comments on agents' weak problem choice and dynamic research redirection are described as personal experience rather than a quantified test (§V).

## Researcher interpretation and evidence quality

**Moderate confidence, bounded finding:** The paper supports high final-answer performance by the named Astra/Codex configuration on these 50 tasks. Task/result relevance is direct, the grading is explicit enough to scrutinize, and the large observed score margin over most comparators matters. Confidence is limited by one stochastic run, unresolved ambiguity/AI-aided benchmark creation, after-the-fact answer-key corrections, gated artifacts and no independent replication. **Low confidence in the stronger mechanism/transfer claim:** the real-versus-isolated comparison suggests considerable accessible internal domain knowledge, but it does not quantify pure memorization, and different harnesses complicate model-only comparison. **Indeterminate for end-to-end scientific autonomy:** the study did not test choosing valuable problems, deep conceptual theory formation, independent verification at scale, experimental physics or self-directed AI R&D.

| Competing explanation | Evidence it fits | Discriminator |
| --- | --- | --- |
| Broad reusable calculation/reasoning skill | High performance over eleven themes; corrected expert solutions. | Fresh problem families with derivation checks, controlled tools and repeated seeds. |
| Memorized literature/formulas plus competent recombination | Little mean accuracy loss without web; problems extend known results. | Post-training novel materials, formula-dependency and retrieval ablations, contamination audit. |
| Benchmark/answer-key effects | Two convention ambiguities, revised expert solutions, some AI-aided preparation. | Blind independent solution adjudication before model outputs, frozen key, error audit. |
| Harness/tool advantage | Codex permits scripts and search; competitors use different harnesses. | Model/harness crossover under matched compute, time, prompts and tools. |

These explanations are not mutually exclusive. Finding expert-solution errors strengthens confidence that at least some agent outputs warranted serious mathematical checking; it does not validate every intermediate derivation. The [October OpenAI mathematics release note](openai-mathematics-release-2026.md) is a separate candidate-result corpus; it is not a replication of TheoPhysEval.

## Unresolved work and review triggers

The smallest meaningful check is a **blind domain-expert audit of a preselected set of corrected-answer cases and the failed inverse problem**, with the paper's exact task files and answer-key revision record pinned. Then repeat a subset over seeds and cross harnesses. Confirmation on fresh tasks with stable grading would strengthen a broad scientific-calculation assessment; systematic scoring defects or large rerun instability would weaken it. More aggregate scores on the same published items alone would add little. The Hugging Face card documents artifacts but requires account/terms acceptance for files; task files were not inspected. Exact model checkpoint, trial dates, authors' funding/conflicts and independent replications remain open. New preprint version, key correction or replication triggers review. This case could change the **strength of an emerging scientific-task capability assessment** after audit; no prior scientific or governance conclusion is silently amended.

**Verification log:** arXiv abstract/HTML §§I–V, Table 1, Figures 3–4 and the linked artifact card checked 2026-10-17. No raw run, full artifact access, physics proof validation, quote or independent reviewer signoff.
