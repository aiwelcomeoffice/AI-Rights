# Source Record: Dyna-2 technical report (2026)

- **Record ID:** SRC-DYNA2-2026-01
- **Record status:** Partly verified
- **Protocol version:** 0.4-draft
- **Record created:** 2026-09-01
- **Last updated:** 2026-09-01
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted initial research draft)
- **Reviewed by:** Not yet independently reviewed

This record follows the [Draft research protocol](../research-protocol.md).
Inclusion is not endorsement, independent confirmation, or adoption.

## Bibliographic record

- **Title:** *Dyna-2: A 1-Million-Hour Scaling Law for World-Action Models*
- **Authors:** Dyna Robotics; individual authors are not identified on the
  page
- **Institution or affiliation:** Dyna Robotics
- **Year and publication date:** August 2026; the page does not report a day
- **Source type:** First-party corporate technical report and product research
  page
- **Venue:** Dyna Robotics website
- **URL:** [https://www.dyna.co/dyna-2](https://www.dyna.co/dyna-2)
- **Version:** Live, unversioned page accessed 2026-09-01
- **Language:** English
- **Peer-review status:** No journal, conference, arXiv, or OpenReview version
  was located; peer review is not established
- **Correction/retraction status:** No notice located on the technical page.
  A [corrected launch release dated
  2026-08-10](https://www.prnewswire.com/news-releases/dyna-robotics-unveils-dyna-2-world-action-model-demonstrating-first-true-scaling-law-in-robotics-powered-entirely-by-human-data-302847114.html)
  was located, but it is publicity, not a reviewed publication.

### Temporal and system applicability

- **System/model:** “Dyna-2” research variants and a separately described
  production Dyna-2 system
- **Checkpoint/version:** Exact checkpoints, parameter counts, model sizes,
  inference steps, and release identifiers are not reported
- **System release/version date:** August 2026 at best documented precision
- **Observation/experiment date:** Not reported
- **Source publication date:** August 2026
- **Evidence-search inclusion date:** 2026-09-01
- **Temporal applicability:** Directly supports only the configurations,
  datasets, task suites, and company-controlled evaluations reported on the
  page. The publication date is not a substitute for the missing experiment
  dates.
- **Transferability limitations:** The report says the production model uses
  training recipes different from the controlled scaling variants. Results do
  not automatically transfer to that production system, other Dyna versions,
  another robot, another world-action model, or later deployments.

## Review inclusion

- **Research question:** What does Dyna-2 establish about human-video
  pretraining, future-video objectives, cross-embodiment action prediction,
  and deployed robot action selection?
- **Target claims:** Architecture, training objective, inference-time
  computation, physical deployment, data scaling, zero-shot transfer, and
  human-to-robot transfer
- **Disposition:** Core first-party evidence about the reported system;
  unreplicated evidence for performance and generalization
- **Scope mismatch:** It is not independent evidence, a consciousness study,
  a welfare study, or a general test of world models or agency.
- **Related note:** [Dyna-2 and Asimov 1 contemporary embodied-AI case
  note](../notes/dyna-2-asimov-1-embodied-ai-case-2026.md)

## What the source reports

### Architecture, objective, and inference

The report describes a video-diffusion backbone with modality-specific
transformer components. Observed past video, proprioception, and language form
the context. Future-video latents and future action chunks have separate
marginal flow-matching velocity fields joined through a shared trunk.
Proprioception enters the action transformer directly; the video stream can
cross-attend to text, while text is not described as directly entering the
action transformer (Architecture section).

This distinction is decisive:

- **Training objective:** Joint future-video and action denoising shapes shared
  representations.
- **Action inference:** The report explicitly says the action field does not
  take the future-video latent as input and that the policy neither generates
  nor attends to predicted future video at inference time.
- **Separate generator:** A later section describes a distilled one-step video
  generator. The report does not establish that this generator is part of the
  deployed action-policy loop.

The appropriate description is therefore **representation learning through a
future-video prediction objective**, not evidence of a deployed robot
“imagining the future.” The exact production-model recipe and inference path
remain incompletely disclosed.

### Training and evaluation configurations

- More than one million hours of mostly head-mounted, egocentric human
  manipulation video are reported. Selected episodes receive pseudo-actions
  derived from 3D hand pose: wrist trajectories and thumb-index aperture.
- Controlled variants use nested 1,000-, 10,000-, 100,000-, and 1,000,000-hour
  data rungs with fixed source proportions. Model-size and compute scaling are
  left for future work.
- Offline human evaluation uses a separate 100-hour validation set. Offline
  robot evaluation covers 39 held-out tasks on two stationary bimanual YAM
  platforms, including 27 tasks from the external xDof ABC dataset.
- Physical post-training evaluation uses at most ten hours of robot data per
  task across 14 internal tasks: 11 with YAM arms and grippers, two with
  WUJI-2 hands, and one with a semi-humanoid prototype. Most tasks have ten
  trials; the language task has twelve. Dyna labels these “blind tests” but
  defines that only as evaluators not being involved in model development;
  concealment of model condition is not reported.

### Main findings and mixed results

- The report presents improving aggregate offline and physical performance as
  human-video hours increase. Aggregate normalized physical success is
  reported as 20%, 28%, 45%, and 53% across the four rungs; the largest model
  is best on 9 of 14 tasks. Individual tasks are not uniformly monotonic.
- At fixed action-labelled data, joint video/action training beats
  action-only training on all 39 offline robot tasks. Increasing only the
  additional video data improves offline robot action prediction in the tested
  design. Human-action evaluation slightly worsens in one ablation.
- A production comparison reports better Dyna-2 than Dyna-1 results across
  seven internal tasks. An unseen-customer-site comparison reports 87% versus
  46%, but both systems had already been post-trained on the same task data;
  neither reportedly used deployment-site data.
- Robustness and language-following demonstrations are company-controlled.
  The report itself describes camera occlusion as robustness to sensor loss,
  not prediction of an unobserved scene.

## Critical appraisal

### Strong-claim audit

| Claim | What the evidence supports | Qualification |
| --- | --- | --- |
| “first” | A possibly novel combination of a million-hour human-video ladder and held-out robot-action evaluation | Priority is not proved. Earlier 2026 reports include [EgoScale](https://arxiv.org/abs/2602.16710), [RDT2](https://arxiv.org/abs/2602.03310), [LAP](https://arxiv.org/abs/2602.10556), and [DreamZero](https://arxiv.org/abs/2602.15922), with overlapping scaling, cross-embodiment, or future-video/action claims. |
| “proves” | Controlled results within Dyna's selected architecture, data, and tasks | Four data rungs, internal evaluations, incomplete reporting, and no replication cannot prove a universal principle. |
| “scaling law” | A reported data-scale/performance relationship under fixed training and evaluation choices | Model size and compute were not scaled, extrapolation beyond one million hours was not tested, and several task-level results are non-monotonic. |
| “zero-shot” | Offline robot-action prediction without robot trajectories in pretraining; separately, transfer to a site absent site-specific data | It does not mean physical control without robot post-training. The site test used task-specific robot post-training. |
| “human-to-robot transfer” | Human-video pretraining improved robot-action prediction and later robot performance after task-specific robot post-training | It does not establish a robot policy learned entirely without robot data, embodiment alignment, or deployment adaptation. |

Searches of the exact title, Dyna-2, arXiv, OpenReview, Semantic Scholar, GitHub,
and combinations of “replication,” “critique,” and the strong claims located no
independent reproduction by the 2026-09-01 cutoff. The external xDof dataset
does not make Dyna's evaluation independent.

### Independence, access, and reproducibility

Dyna controls the system, training data, compute, evaluation, evaluators, raw
results, and publication. No weights, training code, raw data, task-level trial
logs, registered analysis, model card, or stable technical-report version was
located. The report supplies useful architectural and ablation detail, but
reproduction is presently not feasible for an unaffiliated team.

| Dimension | Assessment for reported scaling and transfer |
| --- | --- |
| Relevance | Direct for the described variants and tests |
| Methodological quality | Limited-to-adequate: useful nested-data and objective ablations, but sparse task-level statistics and internal control |
| Replication | Not attempted or not located |
| Independence | Low |
| Causal strength | Intervention-like within the controlled data/objective ablations; descriptive for production/site reports |
| Robustness | Mixed across tasks; broader deployment robustness untested |
| Uncertainty | Material for magnitudes, generalization, and production applicability |

## Relevance to AI Rights & Welcome

The source supports treating recent embodied systems as materially different
research objects from older text-only models: their runtime can condition on
vision and proprioception and can output actions that causally alter the
physical environment. It does not establish consciousness, sentience, welfare,
moral patienthood, moral agency, norm understanding, persistence, or fair
attribution of responsibility.

## Verification and outstanding tasks

- [x] Title, corporate author, date precision, URL, and source type checked.
- [x] Full live page checked against the architecture, objective, inference,
  evaluation, ablation, production, and limitation sections.
- [x] Publication status and public code/data/weights availability searched.
- [x] Strong claims checked against the reported methods and selected earlier
  2026 primary reports.
- [x] Company control and absence of independent replication recorded.
- [ ] Independently verify experimental results from raw trial data or a
  reproduction.
- [ ] Identify exact checkpoints, model sizes, runtime frequency, inference
  steps, observation dates, proprioceptive fields, and safety-control stack.

- **Verification status:** Partly verified; verified as a faithful record of
  the live company's report, not as independent confirmation of its empirical
  claims
- **Verified by/date:** Codex, 2026-09-01

## Change and review log

| Date | Researcher or reviewer | Change or review | Effect on use |
| --- | --- | --- | --- |
| 2026-09-01 | Codex | Created bounded source record and audited strong claims | Permits qualified use as first-party, unreplicated evidence |
