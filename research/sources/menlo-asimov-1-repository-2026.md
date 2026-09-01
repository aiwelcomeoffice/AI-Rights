# Source Record: Asimov 1 public repository snapshot (2026)

- **Record ID:** SRC-ASIMOV1-2026-01
- **Record status:** Verified for stated artifact-availability use
- **Protocol version:** 0.4-draft
- **Record created:** 2026-09-01
- **Last updated:** 2026-09-01
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted initial research draft)
- **Reviewed by:** Not yet independently reviewed

## Bibliographic record

- **Title:** *Asimov 1: Open-Source Humanoid Robot*
- **Author/maintainer:** Menlo Research / Asimov project
- **Source type:** Public source-code and hardware-design repository
- **Venue:** GitHub
- **Stable snapshot:** [commit
  b8420ffe99159065152aa1321a03147c0962f251](https://github.com/menloresearch/asimov-1/tree/b8420ffe99159065152aa1321a03147c0962f251)
- **Snapshot date:** 2026-08-26 (commit timestamp)
- **Access and evidence-search inclusion date:** 2026-09-01
- **Version:** `main` at the commit above; no repository tags were present
- **Language:** English documentation; CAD, KiCad, MJCF, URDF, and related
  machine-readable files
- **Peer-review status:** Not applicable; artifact functionality is not
  independently certified by repository publication
- **License declarations:** `CERN-OHL-S-2.0` for hardware and `GPL-2.0` for
  software. This records repository declarations, not a legal-completeness or
  third-party-rights audit.

### Temporal and system applicability

- **System/model:** Asimov 1 humanoid platform
- **Checkpoint/version:** Repository commit
  `b8420ffe99159065152aa1321a03147c0962f251`
- **System release/version date:** The [project organisation
  profile](https://github.com/asimovinc) reports that Asimov 1 was open-sourced
  2026-04-27; this record assesses the later 2026-08-26 repository snapshot
- **Observation/experiment date:** Not applicable to file availability;
  physical build or locomotion validation is not reported by this source
- **Source publication date:** 2026-08-26 for the pinned revision
- **Temporal applicability:** Establishes what files were publicly inspectable
  at that commit, not what a later branch, shipped kit, or private software
  release contains
- **Transferability limitations:** Design files do not by themselves establish
  fabrication completeness, safe operation, simulation fidelity, locomotion,
  or deployed autonomy.

## Review inclusion

- **Research question:** What Asimov 1 mechanical, electrical, simulation, and
  software materials are actually public now?
- **Disposition:** Core directly inspectable evidence for artifact availability;
  contextual evidence only for functionality
- **Scope mismatch:** Not an independent physical build, policy release,
  safety validation, or performance evaluation
- **Related note:** [Dyna-2 and Asimov 1 contemporary embodied-AI case
  note](../notes/dyna-2-asimov-1-embodied-ai-case-2026.md)

## Audited snapshot contents

The repository tree and relevant readable files were inspected rather than
accepting the README label “open-source stack” as sufficient.

| Area | Public at the pinned commit | Important limit |
| --- | --- | --- |
| Mechanical | Full-body STEP assembly, seven subassembly/fabrication trees, 166 mechanical STEP files, drawings, and a fabrication-manifest script | STEP is neutral exchange CAD, not native parametric design history; no independent physical build was located |
| Electrical | Wiring documentation; KiCad projects/schematics/PCB layouts for the motion-control, power-distribution, and media HAT boards; 18 core `.kicad_sch`, `.kicad_pcb`, or `.kicad_pro` files; and one `.epro` head-board artifact | Completeness, fabrication, EMC, and safety were not independently validated |
| Simulation | MuJoCo MJCF, URDF, and 25 STL meshes | The simulation README describes a floating base with 23 hinge joints and no XML actuators; training is said to configure actuators in Python, but that training code is absent |
| Software | One fabrication-manifest Python script, a device-tree overlay, and a serial helper script | No public firmware, edge runtime, robot API implementation, policy-training environment, or official policy weights were present in the tree |
| Locomotion | No official locomotion policy or weights in this snapshot | The README roadmap marks both “Asimov Edge” and “Locomotion policy” as coming soon |

The README describes a 1.2 m, approximately 35 kg platform with 25 actuated
degrees of freedom: 12 leg, 10 arm, one waist, and two neck degrees of freedom.
The 23-hinge simulation asset therefore does not model the full 25-actuator
runtime exactly; the two neck degrees appear outside its controlled joint set.

## Critical appraisal

### What “open” is justified here

It is justified to call the pinned **mechanical CAD, electrical design, and
robot-description/simulation assets publicly available under declared open
licenses**. It is not justified to call a complete build-to-walk software stack
public at this commit. The README sentence saying the repository contains
“onboard software” is materially broader than the audited tree.

The artifact audit is reproducible from the commit hash and is independent of
Menlo's claim wording. Functional claims remain first-party and unreplicated.

| Dimension | Assessment for public artifact availability |
| --- | --- |
| Relevance | Direct |
| Methodological quality | Strong for file presence; not assessable for physical performance |
| Replication | Anyone can inspect the commit; no independent full build located |
| Independence | High for tree enumeration, low for design/function claims |
| Causal strength | Not applicable to artifact availability |
| Uncertainty | Limited for listed files; material for completeness, safety, and capability |

## Relevance to AI Rights & Welcome

Asimov 1 provides unusually concrete infrastructure for defining a humanoid
body boundary and comparing morphology and simulation. Because policy,
firmware, runtime, operator, and safety layers remain separate, it also
demonstrates why a robot-platform name must not be treated as one model or one
agent. Public embodiment artifacts do not establish consciousness, sentience,
welfare, moral patienthood, agency, or responsibility.

## Verification and outstanding tasks

- [x] Commit hash, timestamp, tag absence, README, licenses, and full path tree
  checked.
- [x] Mechanical STEP, core KiCad, simulation-mesh, and source-file counts
  checked at the pinned commit.
- [x] Simulation README and roadmap checked.
- [ ] Reproduce a complete physical build from public artifacts.
- [ ] Verify electrical and mechanical safety, simulation fidelity, and the
  contents of any later Edge or policy release.

- **Verification status:** Verified for public file presence at the pinned
  commit; not verified for completeness or physical capability
- **Verified by/date:** Codex, 2026-09-01

## Change and review log

| Date | Researcher or reviewer | Change or review | Effect on use |
| --- | --- | --- | --- |
| 2026-09-01 | Codex | Pinned and enumerated the repository snapshot | Supports bounded open-artifact claims only |
