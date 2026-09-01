# Source Record: Asimov 1 public manual status (2026)

- **Record ID:** SRC-ASIMOV1-2026-02
- **Record status:** Partly verified
- **Protocol version:** 0.4-draft
- **Record created:** 2026-09-01
- **Last updated:** 2026-09-01
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted initial research draft)
- **Reviewed by:** Not yet independently reviewed

## Bibliographic record

- **Title:** *Asimov 1 Manual* (selected system and software status pages)
- **Author/issuer:** Menlo Research
- **Source type:** First-party, living technical documentation
- **Pages used:** [System
  specifications](https://docs.menlo.ai/asimov/1/reference/system-specifications),
  [Capabilities and
  limitations](https://docs.menlo.ai/asimov/1/overview/capabilities-and-limitations),
  [Software reference
  status](https://docs.menlo.ai/asimov/1/reference/software-reference-status),
  and [Connect and
  operate](https://docs.menlo.ai/asimov/1/connect-and-operate)
- **Publication/version date:** Not reported on the pages
- **Version:** Live, unversioned pages accessed 2026-09-01
- **Language:** English
- **Peer-review status:** Not applicable
- **Correction/retraction status:** No formal notices located; some statements
  differ from the pinned repository README and are treated as version
  uncertainty, not silently reconciled.

### Temporal and system applicability

- **System/model:** Asimov 1 hardware and the separately distributed Asimov
  software stack
- **Checkpoint/version:** Public manual as accessed 2026-09-01; firmware,
  Edge, SDK, and API release identifiers not publicly specified
- **System release/version date:** 2026 at best documented precision
- **Observation/experiment date:** Not applicable for documentation status
- **Source publication date:** Not reported
- **Evidence-search inclusion date:** 2026-09-01
- **Temporal applicability:** The pages are evidence of manufacturer-stated
  specifications and availability on the access date only.
- **Transferability limitations:** The documentation does not establish what
  every shipped kit contains, what private/support releases include, or how a
  later public release will operate.

## Review inclusion

- **Research question:** Which Asimov 1 sensors, compute, software, API, and
  locomotion components are documented as presently available rather than
  roadmap items?
- **Disposition:** Core first-party status evidence, checked against the public
  repository tree
- **Related source:** [Pinned Asimov 1 repository
  audit](menlo-asimov-1-repository-2026.md)
- **Related note:** [Dyna-2 and Asimov 1 contemporary embodied-AI case
  note](../notes/dyna-2-asimov-1-embodied-ai-case-2026.md)

## What the source reports

### Hardware, sensors, and compute

The current specification page describes a 1.2 m, approximately 35 kg robot
with 25 powered joints and no passive toe joints. It lists a torso six-axis
IMU, motor/joint feedback, a 2 MP monocular camera, microphone array, speaker,
Raspberry Pi 5 for media/network functions, Radxa CM5 for motion control, and
six CAN branches. Lidar and a 360-degree camera are not included in the kit.

The manual describes the microphone as a quad array, while the 2026-08-26
repository README says stereo. The manual says payload ratings are not yet
available, while that README publishes several load values. These are current
documentation inconsistencies requiring a dated hardware revision or test
report, not grounds to select whichever value is more favorable.

### Software and locomotion status

- The capabilities page says advanced locomotion policies are not provided and
  says a basic walking policy will be provided; future tense is not present
  availability.
- The software-status page leaves public image downloads and several release,
  commissioning, and safety dependencies to be confirmed. Generated API
  bindings must match a supported software release and are not present in the
  public repository.
- The connect-and-operate page says a supported public workflow is not yet
  available and identifies compatible firmware, Edge, SDK, restraint, safety,
  and commissioning prerequisites.
- The platform has no included hands or grippers and is not described as a
  turnkey product.

## Critical appraisal

The manual is authoritative for Menlo's current public support position but is
not independent evidence that the hardware or software performs as specified.
Its explicit “not yet available” statements outweigh broad marketing phrases
such as “open-source stack” when determining present access.

| Claim assessed | Evidence direction | Qualification |
| --- | --- | --- |
| Public build-to-operate software stack exists now | Weighs against | The manufacturer itself says the supported public workflow and key release artifacts are unavailable or TBC. |
| Asimov 1 supplies proprioceptive interfaces | Supports at specification level | IMU and joint/motor feedback are listed; signal fields, calibration, latency, and public runtime access are not fully documented. |
| Official public locomotion policy exists now | Weighs against | The policy is described in future tense and is absent from the pinned repository. |

Menlo controls the design, documentation, supported releases, and publication.
No independent commissioning report or public safety validation was located.

## Relevance to AI Rights & Welcome

The split between a documented body, sensor/compute interfaces, missing public
runtime, and future policy is a concrete system-boundary lesson. “Asimov 1” is
not enough to identify an acting system; a study must add hardware revision,
sensor calibration, firmware, runtime, policy weights, control frequency,
operator, safety controls, and deployment context. None of these specifications
is evidence of consciousness, sentience, welfare, moral patienthood, or moral
agency.

## Verification and outstanding tasks

- [x] Four current manual pages checked on 2026-09-01.
- [x] Present-tense availability separated from roadmap statements.
- [x] Sensor/compute claims compared with the pinned repository README.
- [x] Documentation inconsistencies recorded.
- [ ] Obtain a dated bill of materials and hardware revision tying the manual
  to a shipped unit.
- [ ] Recheck when public firmware, Edge, SDK, or locomotion releases appear.

- **Verification status:** Partly verified; manufacturer documentation status
  checked, operational capability not independently verified
- **Verified by/date:** Codex, 2026-09-01

## Change and review log

| Date | Researcher or reviewer | Change or review | Effect on use |
| --- | --- | --- | --- |
| 2026-09-01 | Codex | Recorded present hardware/software status and conflicts | Prevents roadmap items from being treated as current capabilities |
