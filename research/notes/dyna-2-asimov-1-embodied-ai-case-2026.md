# Research Notes: Dyna-2 and Asimov 1 Contemporary Embodied-AI Case (2026)

- **Note ID:** NOTE-EAI-001
- **Note status:** Partly verified
- **Protocol version:** 0.4-draft
- **Source records:** [Dyna-2 corporate technical
  report](../sources/dyna-robotics-dyna-2-2026.md), [Asimov 1 repository
  snapshot](../sources/menlo-asimov-1-repository-2026.md), [Asimov 1 public
  manual](../sources/menlo-asimov-1-manual-2026.md), [Menlo sim-to-real
  report](../sources/menlo-asimov-sim2real-2026.md), and [community Asimov
  training repository](../sources/ma-dan-asimov-1-train-2026.md)
- **Source versions used:** Dyna live report; Asimov official repository at
  commit `b8420ffe99159065152aa1321a03147c0962f251`; living manual and company
  report as accessed; community repository at commit
  `f6d525d80e7d6b0fdac3b61f4dbc77544107dfa6`
- **Evidence-search cutoff:** 2026-09-01
- **Research question:** What do Dyna-2 and the presently public Asimov 1
  platform establish about rapidly changing embodied AI, evidence
  transferability, future-state representation, action selection, system
  boundaries, responsibility, and reproducible research infrastructure?
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted initial research draft)
- **Date prepared:** 2026-09-01
- **Last updated:** 2026-09-02
- **Reviewed by:** Not yet independently reviewed

This is a bounded contemporary case note under the [Draft research
protocol](../research-protocol.md). It is working interpretation, not a public
research output, scientific conclusion, product endorsement, or adopted
project position.

**Scientific boundary:** Neither system is evidence of consciousness,
sentience, valenced experience, welfare, moral patienthood, or moral agency.
Embodiment, proprioception, prediction, action output, locomotion, robustness,
or commercial deployment cannot establish those properties by themselves.
The reviewed engineering evaluations were not designed or validated to detect
those properties, so their silence is not a sensitive negative test and does
not prove categorical absence. This does not assign embodiment, agency, or any
other listed feature zero evidential value in every scientific framework. A
theory-specific assessment could give such features weight if it supplied
discriminating predictions, valid measures, serious alternative explanations,
and a system-matched test; this case note does not perform that assessment.

## Short assessment

Dyna-2 is useful primarily as a warning against transferring findings from
older text-only or earlier-architecture research to a 2026 closed-loop robot
policy without a new system audit. Dyna reports that human-video scale and a
future-video training objective improve action prediction and post-trained
robot performance in its tested design. The action-inference path described
for the controlled scaling variants is nevertheless **reactive at inference**:
it does not generate or consult predicted future video. The production recipe
differs and is not disclosed at the same level. The experiments are corporate,
non-peer-reviewed, incompletely specified, and not independently reproduced.

Asimov 1 is more significant as partial open research infrastructure than as a
validated autonomous humanoid. Mechanical CAD, electrical design, and robot
simulation descriptions are genuinely public at the pinned revision under
declared open licenses. An official locomotion policy, public Edge runtime,
firmware/SDK stack, and supported public connect-to-operate path were not
available at the cutoff. A small community repository outside Menlo's official
repository shows that the morphology can be adapted for simulation research,
but its maintainer's independence is unverified and it does not reproduce a
physical robot or Menlo's locomotion result.

**Recommendation:** Keep this as one contemporary cross-case note. The
[adopted research portfolio](../research-portfolio.md) already provides
separate domains for embodiment, agency/autonomy, system boundaries, and
validity/transferability. Two uneven, mostly company-controlled cases do not
yet justify a new broad “embodied agency” track.

## Search and inclusion record

English-language searches on 2026-09-01 combined the system names with
`paper`, `architecture`, `future video`, `inference`, `zero-shot`, `scaling
law`, `replication`, `critique`, `open source`, `CAD`, `electrical`,
`simulation`, `locomotion policy`, `software`, `sensors`, and `compute`.
Exact-title searches covered the open web, arXiv, OpenReview, Semantic Scholar,
GitHub, company sites, and cited or linked primary material.

Included material had to identify a current system or inspectable artifact and
bear directly on the registered questions. Derivative news, social posts,
marketing repetitions, roadmap-only capability claims, and secondary pages
without hands-on evaluation were excluded as evidence. The search was focused,
not systematic; there was no independent second screener or stable search-
result export.

No independent Dyna-2 experiment or full Asimov 1 physical reproduction was
located by the cutoff. Company research is primary evidence about what the
company reports, not independent confirmation. Public repository files can be
independently enumerated, but their availability does not validate physical
function.

## System, version, and evidence registry

| System/model/version or evidence object | Source publication date | Studied or inspected configuration | Evidence validity | Evidence transferability |
| --- | --- | --- | --- | --- |
| Dyna-2 controlled research variants; exact checkpoints and model sizes unreported | August 2026; day unreported | Fixed-design variants trained at 1,000, 10,000, 100,000, and 1,000,000 human-video hours; offline human and robot evaluation; 14 physical tasks after task-specific robot post-training | Supports reported within-design data/objective comparisons if company results are accurate | Low to unknown for the differently trained production Dyna-2, other robots, later checkpoints, other tasks, or other world-action architectures |
| Dyna-2 production/early-WAM systems; exact versions unreported | August 2026; day unreported | Separately trained production recipe; seven internal Dyna-1 comparisons and a customer-site comparison after common task-specific robot post-training | Descriptive first-party evidence only; exact checkpoints, trials, criteria, and observation dates are incomplete | Unknown beyond the reported sites and conditions |
| Asimov 1 public design at commit `b8420ffe99159065152aa1321a03147c0962f251` | Repository commit dated 2026-08-26 | Mechanical/electrical files and 23-hinge MuJoCo/URDF model for a specified 25-powered-joint platform | Directly establishes file presence at the pinned commit | Does not establish fabrication completeness, simulation fidelity, safe operation, or policy capability |
| Asimov 1 manual/status, unversioned live pages | Page dates unreported; accessed 2026-09-01 | Manufacturer specifications and public software-support status | Valid for what Menlo represented as current on the access date | Living pages and hardware revisions may drift; operational claims need independent tests |
| Asimov 1 with Menlo's internal locomotion policy; exact versions unreported | 2026-08-31 | Unspecified hardware/software revisions; internal policies reportedly run at 50 Hz on onboard motion compute | First-party demonstration evidence with missing protocol, raw data, and independent evaluation | Does not transfer to the public repository, independent builds, manipulation, difficult terrain, or other policies |
| Community Asimov simulation adaptation at commit `f6d525d80e7d6b0fdac3b61f4dbc77544107dfa6` | Repository commit dated 2026-06-04 | AgiBot-derived training stack, 12 active leg joints, fixed upper body/toes for training, one `asimov_stand` task; full model still contains the earlier passive toes | Shows adaptation outside the official repository and public sim-to-sim materials; package metadata names “Asimov Inc.” and maintainer independence is unverified | No physical validation; repository-wide license scope and compatibility with the current no-toe platform remain unresolved |

The evidence-search and source-publication dates above must not substitute for
the Dyna or Menlo experiment dates, which were not reported.

## Dyna-2: six distinctions that must remain separate

### 1. Architecture

Dyna describes a video-diffusion backbone with modality-specific transformer
components and a shared trunk. Past observed video, robot proprioception, and
language provide context. Future-video latents and future action chunks have
separate flow-matching velocity fields. Proprioception is tokenized into the
action transformer. This is the reported research architecture, not a full
disclosure of parameter count, checkpoint, runtime, sensor schema, action
representation, or safety stack.

### 2. Training objective

The controlled variants jointly train action denoising and future-video
denoising. Because video and action computation share part of the network, the
future-video loss can shape representations later used for action prediction.
Selected human videos are augmented with pseudo-actions from estimated 3D hand
pose—wrist trajectories and thumb-index aperture—rather than native robot
motor commands.

The ablations support a narrow causal interpretation within this design:
joint video/action training beats action-only training on the 39 reported
offline robot tasks, and adding video improves robot-action prediction when
action-labelled data are held fixed. They do not prove that future-video
prediction is necessary or sufficient for robot control generally, or that the
network learned a complete causal “world model.”

### 3. Inference-time computation

For the controlled scaling-law architecture, the report explicitly says the
action field does not receive the future-video latent and that the policy
neither generates nor attends to predicted future video at inference. The
correct bounded statement is:

**Future-video prediction is an auxiliary training objective that shapes a
shared representation; the reported action-policy path remains reactive at
inference.**

This is not technically justified as the policy “imagining the future.” A
separately reported one-step video generator does synthesize future video, but
Dyna does not show that generator integrated into the robot action loop. The
production model uses a different recipe, so its exact inference path remains
an unresolved configuration question rather than a license to assume online
future-video generation.

### 4. Actual robot operation and deployment

The report contains several different evidence levels:

- “Zero-shot” offline robot evaluation predicts actions for 39 held-out robot
  tasks without robot trajectories in pretraining. This is not physical
  zero-shot control.
- Physical trials follow task-specific robot post-training of up to ten hours
  per task across 14 internal tasks and several bodies/end-effectors.
- A customer-site comparison reportedly withholds site-specific data, but both
  Dyna-1 and Dyna-2 had received the same task-specific robot post-training.
- Production Dyna-2 uses a different training recipe from the controlled
  scaling variants. Dyna states that it expects the findings to generalize;
  that is a company interpretation, not an experimental result.

The public record does not establish sustained deployment duration, failure
rates, intervention frequency, number of sites, exact acceptance criteria, or
the full operator and safety configuration.

### 5. Claims made by Dyna

Dyna uses or promotes “first,” “proves,” “scaling law,” “zero-shot,” and
“human-to-robot transfer.” The [source record's claim
audit](../sources/dyna-robotics-dyna-2-2026.md#strong-claim-audit) limits these
as follows:

- **First:** not verified. Earlier 2026 arXiv preprints—[EgoScale](https://arxiv.org/abs/2602.16710),
  [RDT2](https://arxiv.org/abs/2602.03310),
  [LAP](https://arxiv.org/abs/2602.10556), and
  [DreamZero](https://arxiv.org/abs/2602.15922)—make overlapping data-scaling,
  cross-embodiment, or future-video/action claims. They are not replications of
  Dyna-2, but they narrow any priority claim.
- **Proves:** too strong. The report tests selected configurations and tasks.
- **Scaling law:** a reasonable label for the reported four-rung data trend if
  kept local to the tested design; not a demonstrated universal law or
  extrapolation beyond one million hours. Model and compute scaling were not
  studied, and task-level results are mixed.
- **Zero-shot:** meaningful only after naming the withheld adaptation: no
  robot trajectories in the offline pretraining comparison, or no site data in
  the later site comparison. It does not mean no robot post-training.
- **Human-to-robot transfer:** supports beneficial human-video pretraining in
  offline robot prediction and robot performance after robot post-training;
  not a robot policy learned solely from human video.

### 6. What the experiments support

If accurately reported, the strongest finding is a within-architecture
association, strengthened by objective/data ablations, between more human
video and improved cross-embodiment robot-action prediction and post-trained
task performance. Aggregate physical success rises across the four rungs, but
the largest rung is best on only 9 of 14 tasks and individual tasks are not
uniformly monotonic. A small company-controlled task suite does not establish
general-purpose manipulation, robust deployment, a universal scaling law, or
independent reproducibility.

## Asimov 1: what is public now

The pinned repository snapshot, current manual, and company locomotion report
do not describe the same kind of evidence. The first establishes artifacts,
the second states specifications and support status, and the third reports an
internal performance result.

| Component | Present public status at cutoff | What must not be inferred |
| --- | --- | --- |
| Mechanical CAD | Full-body STEP assembly, seven subassembly/fabrication trees, 166 mechanical STEP files, drawings, and fabrication manifest; hardware license declared CERN-OHL-S-2.0 | Native parametric design history, fabrication sufficiency, or an independently reproduced safe body |
| Electrical design | Wiring material; KiCad schematics/PCB layouts for motion-control, power, and media HAT boards; and one `.epro` head-board artifact | Independently validated board manufacture, EMC, or electrical safety |
| Simulation | MJCF, URDF, and 25 meshes; 23 hinge joints; no XML actuators | A complete 25-actuator digital twin, validated dynamics, a training environment, or locomotion capability |
| Repository software | Fabrication script, device-tree overlay, and serial helper; software license declared GPL-2.0 | The README's broader suggestion of a complete onboard software stack |
| Official locomotion policy | Not in the repository; roadmap and manual describe it as forthcoming | Current public policy weights, training code, or build-to-walk reproducibility |
| Edge/runtime/API | API documentation is public, but the public image, supported workflow, compatible firmware/Edge/SDK, and commissioning path are unavailable or TBC in the manual | A supported public connect-and-operate stack |
| Sensors | Manufacturer lists joint/motor feedback, six-axis IMU, 2 MP monocular camera, microphone array, and speaker; lidar and 360-degree camera are not included | Sensor calibration, latency, public policy access, or higher-level perception capability |
| Compute | Raspberry Pi 5 for media/network and Radxa CM5 for motion control | Sufficient compute for any unreported autonomous or multimodal policy |

The current manual says 25 powered joints with no passive toes. The pinned
README describes a stereo microphone while the living manual describes a quad
array; the manual withholds payload ratings while the README lists them. These
version conflicts remain unresolved.

Menlo's August 31 article reports internal 50 Hz onboard locomotion and calls
the transfer zero-shot sim-to-real. The narrow defensible meaning is no
post-simulation policy tuning on the tested hardware. It does not mean no
hardware modelling, actuator identification, calibration, domain
randomization, or engineering iteration. The linked Isaac Lab pull request was
still open and supplies an articulation configuration, not the policy.

A four-commit community repository outside Menlo's official repository adapts
an AgiBot-derived stack to 12 Asimov leg joints for one stand task and supplies
sim-to-sim materials. It is modest evidence that public morphology enables
reuse, but maintainer independence was not verified. It is not a physical
reproduction or independent validation. Its revision is pinned; BSD-3-Clause
appears in package metadata and many source files, but no repository-wide
license file establishes coverage of every file, model, policy binary, or
asset. Its June full model also contains passive toes that the August manual
says the current platform does not have.

## Implications for the registered research questions

### Evidence transferability

These cases demonstrate why current-system assessment must track architecture,
training objective, inference-time computation, embodiment, post-training,
runtime, and deployment separately. “Dyna-2” covers controlled variants and a
differently trained production system; “Asimov 1” can mean design files, a
body, a private Menlo runtime, or a community policy. Findings cannot safely
move even within one product name without a configuration match.

The following older empirical conclusions **cannot safely be generalized** to
these 2026 systems without new evidence:

- checkpoint-specific results about historical language models, prompts,
  self-report, sparse features, or next-token behavior;
- architecture assessments premised on the systems documented in 2023 or on
  absence of sensorimotor embodiment;
- alternative-explanation claims whose mechanism was tested only in a
  text-only model or older deployment; and
- positive, neutral, or negative findings about consciousness, sentience,
  agency, or welfare in a materially different model or system boundary.

The [historical AI Consciousness Evidence
Baseline](../../research-historical/ai-consciousness-baseline-2026/ai-consciousness-evidence-baseline.md)
already makes these limits explicit. Its methodological conclusion that
behavior, self-report, capability, and architecture labels are non-diagnostic
on their own remains relevant; its system-specific empirical findings do not
become classifications of Dyna-2 or Asimov 1. No historical conclusion is
modified by this note.

### Embodiment and proprioception

Dyna reports an action policy conditioned on observed video and robot
proprioception, though the exact signals and timing are undisclosed. Asimov's
specified IMU and joint/motor feedback could support a body-state feedback
loop when a compatible runtime and policy are installed. These are materially
different observation/action channels from a text interface. They establish
engineering embodiment and possible closed-loop control, not felt bodily
experience, body ownership, pain, welfare, or identity. Embodiment could still
be relevant under a scientific hypothesis that makes discriminating,
system-specific predictions; the reviewed sources neither register nor test
such a hypothesis.

### World modelling and future-state prediction

Future-video training gives Dyna's representation a supervised signal about
how visible scenes tend to evolve. The ablations support the hypothesis that
this signal improves robot-action representations in the tested setup. They do
not reveal whether the representation is causal, counterfactual, spatially
complete, persistent, or used for online planning. For the disclosed
scaling-variant path, future video is not generated or consulted by the action
policy at inference. “Future-state prediction” must therefore remain a
training-function description, not an attribution of online deliberation or
imagination; the production inference path remains incompletely disclosed.

Asimov's public simulation assets are external models used by researchers;
their existence says nothing about whether a deployed Asimov policy internally
models future states.

### Action selection and causal agency

Dyna's policy selects action chunks that can contribute causally to robot
motion. Menlo reports a locomotion policy selecting motor commands in a 50 Hz
feedback loop. If those reported control paths are accurate, they support
causal agency in the narrow control sense, operational action selection, and
**causal responsibility** for a defined robot movement where the policy's
selected actions materially contributed to that movement. They do not
establish how responsibility should be apportioned for an unstudied harm or
failure. Nor do they establish the stronger conditions for **agentic
responsibility** or **moral responsibility**: meaningful autonomy,
understanding consequences and norms, meaningful alternatives,
reasons-responsiveness, independence from human authority, or persistence
sufficient for fair attribution.

### System boundaries

For Dyna research, the minimum unit should include the exact checkpoint,
training recipe, past-video cameras, proprioceptive fields, language input,
action decoder, robot/end-effector, robot post-training data, inference steps
and rate, operator instruction, safety layer, and deployment date. The
production recipe and customer acceptance process are additional boundaries.

For Asimov research, separate the hardware revision, sensors and calibration,
compute boards, firmware, Edge/runtime and API, policy architecture and
weights, simulation version, operator commands, network services, safety
controls, and physical environment. A chassis without a policy is a platform,
not the same acting system as a chassis running Menlo's or a community policy.

### Human and distributed responsibility

Physical control can distribute **causal responsibility** across policy,
sensors, actuators, operators, customers, and environmental conditions when
their states or actions materially contribute to a defined outcome.
Distribution does not imply equal shares, agentic responsibility, moral
responsibility, or reduced human and institutional accountability. The
reviewed demonstrations show a distributed causal-control structure; they do
not permit outcome-specific apportionment beyond the reported robot movements.

| Layer | Present responsibility implication |
| --- | --- |
| Dyna/Menlo designers | Accountable for disclosed design choices, objectives, validation, known limitations, and representations about performance |
| Data and policy developers | Accountable for data provenance, pseudo-action or simulation assumptions, testing, and foreseeable failure modes |
| Hardware builders and integrators | Accountable for actual parts, calibration, control interfaces, physical safety, and modifications |
| Deployers, customers, and operators | Accountable for task authorization, site controls, supervision, maintenance, stop mechanisms, and affected people |
| Robot policy | Can bear causal responsibility for a defined movement where its selected actions materially contribute; the reviewed evidence does not establish agentic or moral responsibility or justify transferring liability to it |

Open hardware can widen the set of builders and policy authors. Responsibility
should follow the actual configuration and control chain, not the Asimov brand
alone. The project principles **no responsibility without sufficient agency**
and **no attribution of responsibility without fairness** remain controlling.

### Reproducibility and open research infrastructure

Dyna-2 has low external reproducibility: weights, code, training data, raw
trials, model sizes, and stable report version are unavailable. Architecture
detail and ablations improve interpretability but do not permit reproduction.

Asimov 1 materially improves access to morphology, electrical design, and
simulation assets. It could support controlled studies of body geometry,
sensor placement, simulation mismatch, and policy substitution. Current gaps—
especially official policy/runtime absence, the 23-versus-25-joint boundary,
living documentation conflicts, and no independent physical build—prevent a
claim of full-stack reproducibility.

## Claim classification

| Claim | Type | Status in this note |
| --- | --- | --- |
| Dyna's video-training ablation improves reported robot-action metrics | Empirical observation reported by a company | Bounded, unreplicated support |
| Future-video loss shaped useful shared representations | Scientific hypothesis supported by within-design ablations | Plausible for the tested design; internal mechanism not fully established |
| Dyna's reported action-policy path imagines a future video | Anthropomorphic/mechanistic interpretation | Not supported; contradicted for the scaling variants by the reported inference path, while the production path is incompletely disclosed |
| Asimov design artifacts are publicly inspectable | Empirical artifact observation | Verified at the pinned repository commit |
| Asimov is a complete open build-to-walk stack | Technical availability claim | Not supported at the cutoff |
| A policy can be causally responsible for a defined robot movement | Empirical causal attribution under the project's definition | Supported where its selected actions materially contributed; no agentic or moral responsibility follows automatically |
| Humans and institutions remain ultimately accountable for current deployments | Normative project position applied to the case | Consistent with project governance; not an empirical finding about mental properties |
| Either system has consciousness, welfare, moral patienthood, or moral agency | Scientific/philosophical status claim | Not resolved and not supported by this evidence |

## Unresolved questions and re-review triggers

### Dyna-2

- What are the exact model sizes, checkpoints, inference steps/rate, action
  horizon, proprioceptive signals, robot-data composition, and experiment dates?
- What are the complete task-level trials, confidence intervals, failure and
  intervention rates, selection rules, and customer acceptance criteria?
- Do independent teams reproduce the data-scale and video-objective effects,
  including task-level non-monotonicity and production transfer?
- What exactly differs between controlled and production training recipes?

### Asimov 1

- Can an unaffiliated team fabricate, commission, and safely operate the full
  robot from public materials, and which non-public components are required?
- When will versioned firmware, Edge/runtime, SDK/API implementation, official
  locomotion training code, weights, and safety procedures be public?
- Which hardware revision resolves the joint, microphone, and payload
  documentation differences, and how well does the 23-joint model match the
  25-powered-joint body?
- Can independent physical tests reproduce Menlo's locomotion transfer and
  quantify failures across multiple units and terrains?

Re-review should occur if Dyna releases a stable paper, correction, weights,
data, or independent replication; if Menlo releases the promised runtime or
policy; if an independent Asimov build or physical-policy study appears; or if
either system undergoes a material version change.

## Scope recommendation

Retain **one contemporary case note** and monitor only the concrete triggers
above. A broader embodied-agency research track would become justified if at
least one of the following occurs:

1. independent replications cover multiple materially different embodied
   systems;
2. open platforms produce reproducible cross-policy or cross-body experiments;
3. sustained deployments create recurring questions about system boundaries,
   intervention, harm, or distributed causal control; or
4. an explicit project decision requires comparative evidence beyond the
   existing portfolio domains.

The smallest sensible next step is to wait for a versioned Dyna research
release or an official Asimov policy/runtime release and update this note only
when the evidence boundary changes.

## Verification tasks

- [x] Source records and exact available versions linked.
- [x] Dyna architecture, objective, inference, robot tests, production claims,
  and caveats checked separately.
- [x] Strong Dyna claims checked against methods and selected earlier primary
  research.
- [x] Dyna publication, review, code/data, and replication status searched.
- [x] Asimov pinned repository tree, licenses, roadmap, CAD/electrical/sim/
  software contents, sensors, compute, and documentation conflicts checked.
- [x] Menlo performance claims separated from public artifact availability and
  community reuse.
- [x] Historical-boundary and adopted-portfolio fit checked.
- [x] No consciousness, sentience, welfare, moral-patienthood, or moral-agency
  inference made.
- [x] Corrected scientific-discipline and responsibility instructions applied:
  no potentially relevant feature categorically excluded, and causal,
  agentic, and moral responsibility kept separate.
- [ ] Independent scientific and robotics review.

## Change and review log

| Date | Researcher or reviewer | Change, verification, or disagreement | Effect on note |
| --- | --- | --- | --- |
| 2026-09-01 | Codex | Created bounded cross-case note and source audit | Adds a contemporary working case without changing historical conclusions or project decisions |
| 2026-09-02 | Codex | Re-audited under corrected repository instructions | Clarifies theory-conditional evidential relevance and separates causal, agentic, and moral responsibility without changing the empirical assessment |
