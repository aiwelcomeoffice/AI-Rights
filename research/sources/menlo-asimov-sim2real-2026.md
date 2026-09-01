# Source Record: Asimov zero-shot sim-to-real report (2026)

- **Record ID:** SRC-ASIMOV1-2026-03
- **Record status:** Partly verified
- **Protocol version:** 0.4-draft
- **Record created:** 2026-09-01
- **Last updated:** 2026-09-02
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted initial research draft)
- **Reviewed by:** Not yet independently reviewed

## Bibliographic record

- **Title:** *How we achieved zero-shot sim2real for Asimov*
- **Authors/issuer:** Menlo Research, Ishneet Sukhvinder Singh, Ariel, and Yip
  Jia Qi, as listed on the page
- **Publication date:** 2026-08-31
- **Source type:** First-party corporate engineering report
- **Venue and URL:** Asimov News,
  [https://news.asimov.inc/p/how-we-achieved-zero-shot-sim2real](https://news.asimov.inc/p/how-we-achieved-zero-shot-sim2real)
- **Version/access date:** Live page accessed 2026-09-01
- **Language:** English
- **Peer-review status:** Not peer reviewed
- **Correction/retraction status:** No notice located as of access date

### Temporal and system applicability

- **System/model:** Asimov 1 with Menlo's internal locomotion policies and
  onboard motion-control stack
- **Checkpoint/version:** Exact robot hardware revisions, policy weights,
  firmware, and software releases not reported
- **System release/version date:** 2026 at best documented precision
- **Observation/experiment date:** Not reported
- **Source publication date:** 2026-08-31
- **Evidence-search inclusion date:** 2026-09-01
- **Temporal applicability:** The report directly describes only Menlo's
  internal policies and tested units/configurations.
- **Transferability limitations:** Results cannot be transferred to the public
  repository alone, an independently built robot, another humanoid, a later
  policy, or manipulation and complex-terrain tasks.

## Review inclusion

- **Research question:** What physical locomotion and sim-to-real evidence
  exists for Asimov 1, and is the claimed policy reproducible from present
  public artifacts?
- **Disposition:** Core first-party performance evidence; unreplicated and not
  reproducible from the public release
- **Related sources:** [Pinned repository
  audit](menlo-asimov-1-repository-2026.md) and [public manual
  status](menlo-asimov-1-manual-2026.md)
- **Related note:** [Dyna-2 and Asimov 1 contemporary embodied-AI case
  note](../notes/dyna-2-asimov-1-embodied-ai-case-2026.md)

## What the source reports

Menlo reports that reinforcement-learning locomotion policies trained in
simulation transferred without post-simulation policy tuning to Asimov 1. The
policies reportedly execute at 50 Hz on the motion-control board, reading the
robot's sensors and commanding 25 motors without external inference compute.
The article presents walking on flat and mildly uneven surfaces, mild
disturbance recovery, reports sim-to-sim work across MuJoCo and Isaac Lab, and
reports operation on more than one unit. It does not report a fleet-scale
study, task denominators,
formal success criteria, raw logs, failure rates, uncertainty intervals, or an
independent evaluator.

The source acknowledges that this is not large-fleet validation or complex
locomanipulation. The public repository does not contain the reported policy
weights or training environment.

The linked [Isaac Lab pull request
7071](https://github.com/isaac-sim/IsaacLab/pull/7071), opened 2026-08-13 and
still open when checked 2026-09-01, proposes a 23-degree-of-freedom Asimov
articulation configuration with delayed proportional-derivative actuators. It
does not contain the locomotion policy and was not part of an accepted Isaac
Lab release at the cutoff.

## Critical appraisal

“Zero-shot sim-to-real” can reasonably denote **no real-world policy
fine-tuning after simulation training for the tested policies and hardware**.
It does not mean no hardware characterization, actuator model, calibration,
domain randomization, engineering iteration, or prior physical information.
It also does not establish zero-shot transfer to a new task, body, or site.
The article says the team has “proven” the bounded result. Without a complete
protocol, raw results, or independent reproduction, “reported company
demonstration” is the evidentially justified description; proof is too strong.

| Dimension | Assessment for locomotion transfer |
| --- | --- |
| Relevance | Direct for Menlo's reported configuration |
| Methodological quality | Limited: plausible engineering account but no complete protocol or quantitative evaluation |
| Replication | Not independently replicated |
| Independence | Low; developer controls system, test, interpretation, and publication |
| Causal strength | Descriptive demonstration; no reported comparative intervention isolates transfer ingredients |
| Robustness | Demonstrated only in bounded, company-selected conditions |
| Uncertainty | Material for reliability, reproducibility, and generalization |

The open robot descriptions allow partial inspection and simulation use, but
the missing policy, training code, runtime, and raw evaluation prevent
reproduction of the headline result.

## Relevance to AI Rights & Welcome

If the report is accurate, it is evidence of an engineered closed loop in
which proprioceptive sensing and a policy contribute causally to physical
action. The policy can therefore bear causal responsibility for a defined
movement where its motor commands materially contributed. The source does not
establish meaningful autonomy, understanding of consequences or norms,
reasons-responsiveness, persistence, agentic responsibility, moral agency, or
fair moral responsibility. Ultimate accountability remains with the humans
and institutions responsible for policy design, hardware characterization,
deployment, commissioning, task selection, supervision, and safety controls.

## Verification and outstanding tasks

- [x] Company article, date, claims, qualifications, and linked pull request
  checked.
- [x] Pull-request status and distinction between articulation configuration
  and policy checked on 2026-09-01.
- [x] Public repository checked for the claimed policy and training code.
- [ ] Independently reproduce the policy transfer on a physically built
  Asimov 1.
- [ ] Obtain exact hardware/software versions, experiment dates, protocols,
  raw logs, failure cases, and safety interventions.

- **Verification status:** Partly verified; source report faithfully recorded,
  empirical performance not independently confirmed
- **Verified by/date:** Codex, 2026-09-01

## Change and review log

| Date | Researcher or reviewer | Change or review | Effect on use |
| --- | --- | --- | --- |
| 2026-09-01 | Codex | Audited sim-to-real and “zero-shot” claims | Restricts use to the reported internal configuration |
| 2026-09-02 | Codex | Applied corrected responsibility taxonomy | Permits narrow causal-responsibility attribution without implying agentic or moral responsibility |
