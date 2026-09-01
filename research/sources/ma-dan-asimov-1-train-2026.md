# Source Record: Community Asimov 1 training repository (2026)

- **Record ID:** SRC-ASIMOV1-2026-04
- **Record status:** Partly verified
- **Protocol version:** 0.4-draft
- **Record created:** 2026-09-01
- **Last updated:** 2026-09-01
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted initial research draft)
- **Reviewed by:** Not yet independently reviewed

## Bibliographic record

- **Title:** *Asimov v1 — Locomotion RL*
- **Author/maintainer:** GitHub user Ma-Dan; `setup.py` names “Asimov Inc.” as
  package author, so the institutional relationship is unresolved
- **Source type:** Public community software repository outside Menlo's
  official repository; maintainer independence was not verified
- **Venue and URL:** GitHub,
  [https://github.com/Ma-Dan/asimov_1_train](https://github.com/Ma-Dan/asimov_1_train)
- **Publication date:** 2026-06-04 for the pinned latest commit
- **Version/access date:** [commit
  `f6d525d80e7d6b0fdac3b61f4dbc77544107dfa6`](https://github.com/Ma-Dan/asimov_1_train/tree/f6d525d80e7d6b0fdac3b61f4dbc77544107dfa6),
  accessed 2026-09-01; no tags were present and the history contained four
  commits
- **Language:** English and Chinese documentation; Python and model assets
- **Peer-review status:** Not peer reviewed
- **License status:** No repository-wide license file is present. `setup.py`
  declares `BSD-3-Clause`, and many Python files contain BSD-3-Clause SPDX
  identifiers and license text. Coverage of every adapted file, model, binary
  policy, and asset was not audited.

### Temporal and system applicability

- **System/model:** Community adaptation of an AgiBot X1 training stack to an
  Asimov 1-derived model
- **Checkpoint/version:** Repository commit
  `f6d525d80e7d6b0fdac3b61f4dbc77544107dfa6`; included an exported policy at
  `logs/asimov_stand/exported_policies/20000/policy_dh.jit`
- **System release/version date:** 2026-06-04 for the pinned repository
  revision; physical-robot version not reported
- **Observation/experiment date:** Not reported
- **Source publication date:** 2026-06-04 for the pinned revision
- **Evidence-search inclusion date:** 2026-09-01
- **Temporal applicability:** Establishes that a small project outside Menlo's
  official repository had publicly exposed training and sim-to-sim materials
  by the access date.
- **Transferability limitations:** It does not establish physical-robot
  performance, compatibility with a shipped unit, Menlo endorsement, or
  reproduction of Menlo's internal locomotion report. Its June full-body model
  contains passive toe joints, while the current August manual says the
  platform has none.

## Review inclusion and source report

- **Research question:** Has the public Asimov morphology enabled a community
  adaptation outside the official repository?
- **Disposition:** Supplementary evidence about infrastructure reuse, not
  evidence about physical capability or verified maintainer independence
- **Related sources:** [Official repository
  audit](menlo-asimov-1-repository-2026.md) and [Menlo sim-to-real
  report](menlo-asimov-sim2real-2026.md)
- **Related note:** [Dyna-2 and Asimov 1 contemporary embodied-AI case
  note](../notes/dyna-2-asimov-1-embodied-ai-case-2026.md)

The README says the project ports training code from AgiBot X1 and adapts it to
an Asimov 1 model. It uses Isaac Gym for training and MuJoCo for sim-to-sim
checking. The only registered task is `asimov_stand`; it activates the 12 leg
degrees of freedom and freezes the upper body. The tree exposes training,
export, and sim-to-sim scripts plus exported policy artifacts.

This repository is outside Menlo's official repository and depends on Asimov
geometry and upstream locomotion code. Its package metadata names “Asimov
Inc.” as author, so its maintainer's institutional independence was not
verified. The repository does not provide an independent
physical build, real-robot test, quantitative evaluation, safety analysis, or
proof that the exported policy works on Asimov hardware.

## Critical appraisal and relevance

The source supports a narrow, useful claim: public body descriptions can lower
the barrier for community simulation adaptation. It does not validate the
official design, the company's “zero-shot sim-to-real” result, or the
community policy itself. The four-commit history, single task, repository-wide
license-scope uncertainty, older toe-joint model, and unreported experiment
details materially limit reproducibility and reuse.

For AI Rights & Welcome, this is evidence that public embodiment
infrastructure can enable reuse outside the official repository. It also means
system boundaries and responsibility can diverge: a community policy on an
Asimov-derived model is not the same system as Menlo's policy or a stock
Asimov 1. It supplies no evidence of consciousness, sentience, welfare, moral
patienthood, or moral agency.

## Verification and outstanding tasks

- [x] Repository page, README, tree summary, commit count, task scope, and
  upstream dependency checked.
- [x] Exact commit, timestamp, tag absence, exported-policy path, and absence
  of a repository-wide license file checked in a local clone.
- [x] Package and file-level BSD-3-Clause declarations and the older passive-
  toe model boundary checked.
- [x] Physical-validation and license gaps recorded.
- [ ] Perform a dependency/security review and full code audit.
- [ ] Reproduce training and sim-to-sim results.
- [ ] Test on a documented Asimov 1 hardware revision under an independent
  protocol.

- **Verification status:** Partly verified; useful only as supplementary
  evidence of public community adaptation
- **Verified by/date:** Codex, 2026-09-01

## Change and review log

| Date | Researcher or reviewer | Change or review | Effect on use |
| --- | --- | --- | --- |
| 2026-09-01 | Codex | Added bounded community-reuse record | Provides community infrastructure context, not capability validation |
