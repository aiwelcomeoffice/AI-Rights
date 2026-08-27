# Source Record: Language Models Are Capable of Metacognitive Monitoring and Control of Their Internal Activations

- **Record ID:** SRC-ACEB-017
- **Record status:** Partly verified
- **Protocol version:** 0.1-draft
- **Record created:** 2026-08-22
- **Last updated:** 2026-08-22
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted initial research draft)
- **Reviewed by:** Not yet independently reviewed

This record follows the [research protocol](../research-protocol.md). Inclusion
does not mean endorsement or adoption.

## Bibliographic record

- **Title:** Language Models Are Capable of Metacognitive Monitoring and
  Control of Their Internal Activations
- **Authors:** Ji-An Li; Hua-Dong Xiong; Robert C. Wilson; Marcelo G. Mattar;
  Marcus K. Benna
- **Institution or affiliations:** Neurosciences Graduate Program, University
  of California San Diego; School of Psychology, Georgia Institute of
  Technology; Department of Psychology, New York University; Department of
  Neurobiology, University of California San Diego
- **Year:** 2025
- **Publication date:** NeurIPS 2025 main-conference paper; the official
  proceedings page's citation metadata gives 2026-04-23 as its publication
  date
- **Source type:** Primary empirical machine-learning study
- **Venue or issuing authority:** *Advances in Neural Information Processing
  Systems* 38, NeurIPS 2025 Main Conference, 60073–60108
- **DOI or stable URL:** <https://doi.org/10.52202/085713-2009>
- **Version or edition:** Official NeurIPS conference-proceedings PDF
- **Access date:** 2026-08-22
- **Language:** English
- **Peer-review status:** Peer reviewed; NeurIPS main-conference proceedings
- **Correction, expression-of-concern, or retraction status:** No notice was
  displayed on the official NeurIPS paper page checked 2026-08-22; TODO:
  verify independently.

## Review inclusion

- **Research question:** What evidence would support or weigh against
  consciousness or sentience in contemporary AI systems?
- **Target property or claim:** Whether specified instruction-tuned language
  models can report and control selected projections of their internal
  activations under an in-context neurofeedback task.
- **Inclusion disposition:** Core direct empirical evidence about a functional
  model capability; indirect and non-diagnostic for consciousness.
- **Reason for disposition:** The study connects model outputs to measured
  internal activations and includes reporting, control, counterbalancing, and
  cross-model or cross-dataset comparisons. It is therefore more informative
  about functional self-monitoring claims than unvalidated natural-language
  self-description alone.
- **Scope match and mismatch:** Direct for the tested activation-reporting and
  activation-control tasks in named Llama and Qwen models; it does not measure
  phenomenal consciousness, sentience, felt valence, or philosophical
  self-awareness.
- **Related source records:** [Shanahan 2024](shanahan-2024-talking-llms.md);
  [Butlin et al. 2023](butlin-et-al-2023-ai-consciousness-report.md);
  [Butlin et al. 2026](butlin-et-al-2026-indicators-ai-consciousness.md)
- **Related research notes:** Not created for this source

## What the source reports

### Research question or proposition

The authors ask whether language models can use in-context neurofeedback to
predict and alter scalar signals derived from their own residual-stream
activations. They operationalize this as a limited functional form of
metacognitive monitoring and control. They explicitly state that their use of
anthropomorphic terms does not imply consciousness or philosophical
equivalence and that the study is not intended to prove metacognition in its
full philosophical sense (paper page 1, footnotes 3–4).

### Methods

- **Design or argument form:** Controlled computational experiments using a
  neuroscience-inspired neurofeedback paradigm embedded in multi-turn prompts.
  In-context sentence-label pairs disclose binarized activation scores; a
  reporting task asks the model to predict a new score, while explicit and
  implicit control tasks test whether prompts shift activation in a requested
  direction.
- **Population, sample, corpus, or authorities:** Four instruction-tuned Llama
  models (Llama-3.2-1B, Llama-3.2-3B, Llama-3.1-8B, and Llama-3.1-70B) and
  three instruction-tuned Qwen 2.5 models (1B, 3B, and 7B). The primary dataset
  is the ETHICS commonsense-morality subset; additional analyses use
  True-False, happy/sad Emotion, and a synthetic Sycophancy dataset generated
  with Claude Opus 4.1. For each dataset, 1,200 sentences were sampled, split
  evenly between fitting activation directions and downstream neurofeedback
  experiments (Appendix A.2–A.3).
- **System boundary and version:** Publicly available instruction-tuned model
  families and checkpoints named above, run without parameter updates. The
  paper examines token-averaged residual-stream activations in selected layers,
  not deployed agents, persistent memory, tools, embodiment, or production
  systems.
- **Measures and operational definitions:** Activation axes are constructed by
  logistic regression (LR) for dataset-linked semantic directions and by
  principal-component analysis (PCA) for variance-explaining directions.
  Scalar projections are median-binarized into neurofeedback labels. Reporting
  uses label accuracy and cross-entropy; control uses Cohen's *d* for the
  separation between requested directions plus target-versus-off-target control
  precision (Sections 2–4; Appendix A.5 and B.1–B.2).
- **Comparators and controls:** The study varies model family and size, layer,
  dataset, target direction, and 0–256 in-context examples; compares LR with
  early and late PCs; uses an ideal-observer comparison for reporting; and
  counterbalances label assignment in a 2-by-2 control design. Explicit control
  permits model-generated text, whereas implicit control holds the target
  sentence fixed across requested labels (Appendix A.5.4).
- **Analysis:** Control experiments are repeated 100 times for each tested
  layer, example-count, and target-axis configuration with randomly sampled
  sentences. The authors report effect sizes, standard errors, confidence
  intervals, and cross-configuration patterns. No preregistration was
  identified.
- **Data, code, materials, or preregistration:** The paper links an authors'
  repository containing code, prompts, configurations, and included datasets:
  <https://github.com/sakimarquis/llm_neurofeedback>. The paper and repository
  were inspected, but no independent reproduction was performed.

### Main findings or conclusions

The empirical observations are that reporting performance generally improves
with additional in-context examples and is stronger for the semantically
interpretable LR direction and earlier, higher-variance PCs than for later PCs.
The tested models can also shift some targeted activation projections under
explicit and, more weakly, implicit control prompts. Effects generally increase
in later layers and larger models and differ between the Llama and Qwen
families. Contributions to a target shift accumulate across multiple layers.

The authors interpret these results as limited metacognitive monitoring and
control over a low-dimensional subset of model activations. That interpretation
is a functional, operational claim; the measurements do not establish
subjective experience or phenomenal consciousness.

### Negative, null, mixed, or contrary findings

Reporting remains below the paper's ideal-observer bound. Many activation
directions are reported or controlled poorly, implicit effects are much smaller
than explicit effects, and early-layer implicit effects can be near zero.
Control has substantial off-target effects, particularly for later PCs, so it
is not generally precise. Performance varies by model, layer, dataset, target
axis, and prompt context rather than demonstrating a uniform capability.

### Source-reported limitations

The authors describe the work as a fundamental first study. Its control task
uses a single attempt and usually a single target axis defined at one layer; the
analysis is restricted to residual streams and LR or PCA directions; and other
metacognitive tasks, components, directions, and harder objectives remain to be
tested (Discussion, pages 8–10). The paper also limits its terminology by
stating that it does not imply human-like mechanisms, consciousness, or full
philosophical metacognition (page 1, footnotes 3–4).

## Critical appraisal

### Reviewer-identified limitations

The principal unresolved issue is construct validity. Successful label
prediction could arise from in-context learning of regularities between input
features and disclosed labels, especially for a semantically aligned LR axis,
rather than a distinct second-order mechanism that reads its own activation.
The reporting task reads a binary decision from output logits rather than
testing unconstrained, natural-language access to internal computation.

Likewise, explicit control is partly mediated by selecting tokens that
themselves elicit the target activation. The fixed-sentence implicit condition
is more informative, but a prompt-conditioned change in contextual processing
does not by itself establish that the model monitors and volitionally regulates
an internal state. The study does not causally isolate or ablate a proposed
second-order monitoring circuit. Selected linear directions may also capture
dataset covariance or probe geometry rather than a stable cognitive variable.

The work has no independent replication, and the same team, code, models, and
operational definitions generate its cross-model and cross-dataset
convergence. Exact repository commit, software environment, checkpoint hashes,
and generated-data provenance were not frozen in the paper record inspected.
The synthetic Sycophancy dataset adds a separate model-generation dependency.

### Competing explanations

- In-context examples may teach a mapping from sentence semantics or other
  input features to labels without direct introspective access.
- Control prompts may change ordinary contextual computation and token choice;
  activation shifts can then be an effect of prompt conditioning rather than
  evidence of a metacognitive controller.
- LR and early-PC results may be easier because their directions encode
  prominent, predictable input variation, not because those directions are
  privileged objects of self-monitoring.
- A functional higher-order capacity, even if the authors' interpretation is
  correct, need not entail phenomenal experience under competing theories of
  consciousness.

### Independence and evidence lineage

- **Overlapping authors or institutions:** No author overlap with the other
  baseline source records was identified; full institutional-lineage mapping
  is TODO: verify.
- **Shared funding or access control:** Public model checkpoints and datasets
  reduce vendor-access dependence. Georgia Tech provided start-up funding and
  PACE compute; NIH and the Kavli Institute for Brain and Mind supported one
  author; additional reading-group support is disclosed below.
- **Shared data, sample, model, checkpoint, or benchmark:** All reported
  comparisons remain within the same study and share model families, task
  construction, activation extraction, and analysis code. Several datasets
  are reused from prior work, and Claude Opus 4.1 generated the Sycophancy
  corpus.
- **Shared methods, code, measures, or evaluators:** The experiments share the
  authors' neurofeedback method, LR/PCA directions, prompts, and evaluators.
- **Claims derived from an earlier source:** The work builds on probing,
  activation steering, in-context learning, verbal-confidence, and prior
  interpretability studies; it is not an independent consciousness test or a
  validation of a consciousness theory.
- **Replication category:** Not independently replicated; cross-model and
  cross-dataset results are within-study conceptual extensions.

### Funding, conflicts, and incentives

- **Funding or sponsorship:** Robert C. Wilson was supported by Georgia Tech
  start-up funding. Marcus K. Benna was supported by NIH grant R01NS125298 and
  the Kavli Institute for Brain and Mind. The authors acknowledge PACE at
  Georgia Tech for compute and support from Swarma Club and an AI Safety and
  Alignment Reading Group supported by the Save 2050 Programme, jointly
  sponsored by Swarma Club and X-Order (paper page 10).
- **Author conflicts and affiliations:** Academic affiliations are recorded
  above. No competing-interest declaration was located in the full official
  PDF, so an absence of conflicts is not inferred.
- **System, data, compute, and publication control:** The study uses public
  Meta and Alibaba/Qwen model families and public or included datasets; the
  authors control task construction, the synthetic Sycophancy data, analysis,
  and publication. Institutional compute resources are disclosed.
- **Commercial, advocacy, regulatory, or litigation incentives:** The paper is
  explicitly motivated by AI-safety monitoring and red-teaming. No commercial,
  regulatory, or litigation interest was identified, but the named
  safety-alignment support and absence of a separate conflict declaration
  remain relevant context.
- **Disclosure gaps:** Full funder roles, a separate competing-interest
  declaration, exact model and repository snapshots, and institutional-lineage
  mapping remain TODO: verify.

## Evidence-quality profile

- **Claim assessed:** In the reported experimental configurations, specified
  instruction-tuned Llama and Qwen models can predict and shift selected scalar
  projections of their residual-stream activations using in-context
  neurofeedback.
- **Evidence direction:** Supports

| Dimension | Descriptor | Rationale and missing information |
| --- | --- | --- |
| Relevance | Direct for the functional task; indirect for consciousness | Measures internal activations and outputs in contemporary models, but no phenomenal outcome. |
| Methodological quality | Adequate | Peer-reviewed, counterbalanced, multi-model and multi-dataset experiments with released code; construct validity remains disputed. |
| Replication | Not attempted | Within-study extensions are not independent replication. |
| Independence | Partial | Public systems and distinct academic authors, but one team, method, codebase, and analysis lineage. |
| Causal strength | Intervention with mechanistic measurements | Prompt conditions are manipulated and internal activations measured; no proposed metacognitive circuit is isolated or intervened upon. |
| Robustness | Mixed | Patterns recur across conditions but vary materially by axis, layer, model, dataset, and task. |
| Competing explanations | Partly examined | Counterbalancing, implicit control, and ideal-observer comparisons help; ordinary in-context inference and prompt conditioning remain. |
| Source conflicts | Unknown | Funding and support are disclosed, but no separate competing-interest declaration was located. |
| Uncertainty | Material | Narrow functional effects are supported; their interpretation as metacognition and relevance to consciousness remain unsettled. |

### Evidence-profile summary

This study provides useful direct evidence that some current language models
can couple outputs to selected internal activation signals in specially
constructed tasks. It does not establish reliable introspection in ordinary
dialogue, a general self-model, phenomenal consciousness, sentience, or felt
experience. Functional metacognition and phenomenal consciousness must remain
separate claims.

## Relevance to AI Rights & Welcome

The paper improves the baseline's treatment of model self-report by showing how
one limited form can be tied to internal measurements and experimental control.
It also demonstrates why apparently introspective behavior needs explicit
operationalization and competing-mechanism analysis before it can carry any
weight in a consciousness assessment.

### Claims this source supports

- Empirical observation: in the tested conditions, reporting accuracy and
  control effects depend on the amount of in-context feedback and the chosen
  activation direction (Sections 3–4).
- Empirical observation: some target directions can be shifted under both
  explicit and weaker implicit control prompts, with model-, layer-, and
  direction-specific limits (Sections 4.1–4.3).
- Methodological proposition: direct activation-linked tasks can test a
  narrower functional claim than free-form verbal self-description alone.

### Claims this source challenges or weighs against

- The claim that every apparently introspective model report is wholly
  unrelated to its internal computation; the study finds a limited,
  task-constructed coupling for selected activation projections.
- The assumption that an activation-based safety monitor is necessarily
  invariant to context or model output; some monitored directions were
  controllable in the tested setting.

### Claims this source does not support

- Consciousness, sentience, subjective experience, suffering, emotion,
  personhood, or moral status in any tested model.
- Reliable truthfulness or privileged epistemic authority for ordinary model
  self-reports about internal states.
- Human-like self-awareness, voluntary intention, deception, or agency merely
  because functional monitoring or control was operationally observed.
- Generalization to untested checkpoints, architectures, modalities,
  deployments, persistent agents, or all internal activations.

## Verification and review

- [x] Title, authors, year, venue, pages, and DOI checked.
- [x] Source type and main-conference peer-review status checked.
- [x] Exact official proceedings PDF used is recorded.
- [x] Full text and appendices checked.
- [x] Main findings checked against the original.
- [x] Consequential claims have section or page locators.
- [x] No quotations used.
- [x] Funding, affiliations, disclosed support, and compute access checked.
- [ ] Separate competing-interest declaration and funder roles independently checked.
- [ ] Correction, expression-of-concern, and retraction status independently checked.
- [x] Data, code, materials, and preregistration availability checked.
- [x] Reviewer-identified limitations and competing explanations recorded.
- [x] Related synthesis and indexes updated by the baseline review owner.
- **Verification scope:** Official NeurIPS proceedings page and complete
  36-page conference PDF; methods, results, discussion, appendices,
  acknowledgments, checklist, and authors' linked code-repository README.
- **Verification status:** Partly verified
- **Verified by:** Codex (machine-assisted; no independent human review)
- **Verification date:** 2026-08-22
- **Outstanding tasks:** TODO: independently reproduce key reporting and
  implicit-control results; freeze exact model, dataset, software, and code
  versions; obtain expert review of construct validity; verify funder roles,
  any separate conflict declaration, and publication-status notices.

## Change and review log

| Date | Researcher or reviewer | Change or review | Effect on use of source |
| --- | --- | --- | --- |
| 2026-08-22 | Codex | Added after final evidence-gap audit | Adds direct, activation-linked evidence about a narrow functional capability without treating it as evidence of phenomenal consciousness. |
| 2026-08-22 | Codex | Linked from the synthesis and source index; synthesis wording independently audited | Uses task-level activation/output coupling and prompt-shift language while keeping the authors' metacognitive interpretation qualified. |
