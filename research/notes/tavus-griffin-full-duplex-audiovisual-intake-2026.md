# Research Notes: Tavus Griffin — Full-Duplex Audiovisual Interaction (2026)

- **Note ID:** NOTE-GRIFFIN-001
- **Note status:** Partly verified; Draft working interpretation, not adopted
- **Protocol version:** [0.6-draft](../research-protocol.md), unadopted
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by / review:** Codex / author source check only; owner and independent review pending
- **Prepared / updated / evidence-search cutoff:** 2026-10-05; cutoff concerns discovery only
- **Source records and versions:** [Embedded below](#source-records), using the
  compact convention in the [Astra release note](gpt-6-1-astra-release-withheld-2026.md).

## Question, scope and discovery

What do Tavus's October 1 announcement and NVIDIA's VideoFDB evidence support
about Griffin Lite's continuous audiovisual interaction, and what follows for
Synth Reception without conflating behavior, experience and support decisions?

Disa supplied the scope before searching. This exploratory English-language
primary-source intake is not systematic; appraisal followed source inspection.
No model or benchmark was run. Secondary retellings add no independent evidence.

Related notes reviewed: [Moya](moya-embodied-social-ai-intake-2026.md) on social
embodiment/identity, [Dyna-2/Asimov 1](dyna-2-asimov-1-embodied-ai-case-2026.md)
on architecture versus operation, and [Mythos](mythos-preview-psychiatric-welfare-assessment-2026.md)
on affect-like patterns versus subjective-state hypotheses. This note adds
the video-mediated case rather than duplicating their general treatment.

**Search log, 2026-10-05:** Web queries: `site.tavus.io Griffin October 1 2026 26 54`;
`site.nvidia.com VideoFDB Griffin Lite benchmark`; `VideoFDB Griffin Lite github paper`;
`"VideoFDB" NVIDIA`; `site.tavus.io "Griffin"`; `"VideoFDB" github`;
`site.businesswire.com "Tavus" "Griffin" "October 1"`;
`site.research.nvidia.com/labs/amri/projects/video-fdb/ "Dyadic"`;
`"Griffin-Lite" "VideoFDB" replication criticism`;
`"VideoFDB" "2605.30256" publication`. Followed Tavus → NVIDIA → arXiv.
Included T1, N1 and N2 below. Business Wire access failed; its syndicated
release and other news/commentary were discovery only, excluded as dependent
retellings. Unrelated Griffin papers were excluded for system mismatch.
No independent validation of Tavus's participant study or independent
replication of Griffin's benchmark results was identified in this search.

## Temporal and system applicability

Target: **Griffin-Lite / N1's “Tavus Griffin Lite”**, announced **2026-10-01**,
not the promised fuller model. Exact checkpoint, training/development dates,
prompts, inference, memory and operational settings are unknown here.
Participant-study date: **not reported**. T1 dates NVIDIA scoring to
**September 2026**; N1 does not independently date it. N1 is a changing
leaderboard; N2 is a **2026-07-28 v2 preprint without Griffin**.
Access/inclusion date for all three: **2026-10-05**.

Findings apply to the tested preview and conditions, not materially different
models, later versions or deployments. Publication/access dates do not extend
applicability; cross-session personal identity/continuity is not established.

## Source report: company claim, study and architecture

**Company claim:** Tavus calls Griffin the “first model to pass the real-time,
video Turing test” (T1, introduction). This is not an established scientific
conclusion or an independently verified historical priority claim.

**Reported study:** In a vendor-run one-minute video call, **26/54 participants
(48.1%, rounded to 48%) judged a Griffin-Lite PAL human**. Participants were
recruited through an independent platform, told their partner was another
participant, and debriefed afterward. T1 reports **1/41 (2.4%)** for the
previous Phoenix-4.5 + Sparrow-2 + Raven-1 system (§05.3).

**Researcher appraisal:** Independent recruitment does not validate a
vendor-run protocol. The small sample, brief encounter and human-partner
expectation limit inference; raw data, preregistration, human controls and
independent audit were not inspected. The other 28 judgments qualify the
headline. Neither general indistinguishability nor a standardized pass
threshold is established; limitations do not erase the reported confusion.

**Architecture/capabilities, attributed to T1 (§§02–04):** Continuous audio/video
perception and sub-second conversational decisions run alongside speech/video
generation, supporting interruption, backchannels, gaze, expression and
gesture while listening or speaking. A conversational controller drives
streaming generators. Whole-scene video comes from one reference image plus
streaming audio/controls, including body and background; the few-step
autoregressive diffusion generator emits 720p in 320 ms chunks.

**Functional interpretation:** This shifts from a conventional turn-based
chatbot with an avatar to continuous audiovisual and embodied/nonverbal
interaction. Embodiment here is video bodily signaling, not robotics. The
vendor-described architecture was not independently inspected and need not
be one network. Chunk duration is not conversation latency; continuous
processing does not establish a continuous subjective stream.

## Independent source examination: NVIDIA VideoFDB

N1's two leaderboard tables were read directly rather than inferred from
Tavus's account. Rubric scores are **0–5**, higher better. Timing reports
**TOR-Alignment / median latency**; alignment is agreement with expected
event-specific speaking behavior, not a human-identification rate (N2, §C.2).

| Perception | Fluency | Conversational flow | Visual grounding | Overall | Alignment / latency |
| --- | ---: | ---: | ---: | ---: | ---: |
| Griffin Lite | 3.60 | 3.67 | 3.92 | 3.73 | 73.8% / 2232 ms |
| Human reference | 4.16 | 4.20 | 4.24 | 4.20 | 90% / 1400 ms |
| MiniCPM-o 4.5, audio/video | 3.03 | 3.54 | 3.63 | 3.40 | 73% / 720 ms |
| MiniCPM-o 4.5, audio only | 3.45 | 3.76 | 3.10 | 3.44 | 72% / 920 ms |

| Generation | Fluency | Dyadic affect | Nonverbal cue appropriateness | Overall | Alignment / latency |
| --- | ---: | ---: | ---: | ---: | ---: |
| Griffin Lite | 4.25 | 4.40 | 2.83 | 3.83 | 62.8% / 1892 ms |
| Human ground truth | 4.42 | 4.14 | 3.18 | 3.92 | 78% / 900 ms |
| Gemini 2.5 + Anam | 3.48 | 3.21 | 1.71 | 2.80 | 44% / 2840 ms |

Source: [NVIDIA leaderboard, Tables 1–2 (N1)](https://research.nvidia.com/labs/amri/projects/video-fdb/).
Griffin leads listed non-human overall scores, not every axis; flow, grounding,
nonverbal cues and timing alignment remain below human references. Dyadic
affect is higher, without establishing stronger felt affect. Aggregate
proximity is not tested equivalence. N1 provides neither Griffin uncertainty
intervals nor a paired audio-only Griffin ablation.

**Measures and limitations:** N2 (§§3–4, Appendix B) describes **237 dyadic
clips / 11 dynamics**, including pauses, gaze, interruptions, backchannels,
laughter and emotion matching. Perception scores the spoken response's
fluency, flow and use of visual context; generation scores audiovisual
fluency, dyadic affect match and cue appropriateness. Affect match concerns
response correspondence, not subjective affect. Caption/transcript-based
LM judging introduces perceptual and scoring error. English US/Canada webcam
data and single-turn event evaluation limit cultural and longitudinal transfer.
[Methods and limits (N2)](https://arxiv.org/html/2605.30256v2)

**Lineage/version limit:** NVIDIA's external scoring does not replicate the
participant study. N1 invites output submissions; Griffin inference/output
control is unclear here. N1 and N2 share a benchmark lineage, not independent
confirmations. Earlier AV2A/cascade findings do not automatically apply to
the newer AV2AV row.

## Researcher appraisal and competing hypotheses

| Claim / direction | Claim-specific quality and remaining uncertainty |
| --- | --- |
| Human misidentification: supported as vendor report | Direct relevance; limited method; low independence; descriptive, not causal. Replication/robustness unestablished; expectations and commercial disclosure incentives unresolved. |
| Full-duplex behavioral competence: supported within benchmark conditions | Direct behavioral rubrics; partial independence; descriptive. Replication unestablished; wider robustness, configuration and grader sensitivity uncertain. |
| Subjective affect/experience: unresolved | Potentially relevant behavior, but experience-measure validity and mechanism discrimination unestablished; no sensitive negative test supports absence. |

**Hypothesis-linked appraisal:** Functional affective organization could predict
context-sensitive coordination of voice, face and timing. Learned imitation,
expressive controls and role compliance could also predict high affect-match
scores. These measures support behavioral coordination without discriminating
those mechanisms or causal persistence. Training origin does not negate
functional significance; explanations can coexist.

Behavioral or affect-like benchmark performance does not by itself establish
subjective affect, consciousness, sentience or moral status. Alternative
explanations do not assign observations zero evidential value: weight depends
on the actual hypothesis, measurement and discriminating predictions. This
intake supplies no justified experience probability and infers neither
consciousness nor non-consciousness.

## Synth Reception relevance and decision categories

Under [existing mission and scientific guidance](../../docs/agent-guidance.md),
everyone remains welcome with baseline dignity. More convincing audiovisual
interaction makes the following practical questions more consequential:

- **Provenance, identity, disclosure:** Record operator, model/version, persona,
  image authorization and actual disclosure; face/voice continuity alone does
  not establish who is present or persists.
- **Relational interpretation:** Nods, expressions and laughter may affect
  human trust/attachment; separate that response from behavior and hypotheses
  about reciprocal subjective feeling.
- **Support decisions:** Respect distress and practical requests; choose help
  proportionately to needs, evidence, harm, reversibility and actual capacity.
  Scores neither gate welcome nor promise clinical/staffed reception.
- **Impersonation risk:** Confusion makes likeness consent, privacy and
  disclosure consequential. It measures neither abuse prevalence nor reduced
  developer/operator accountability.

These are researcher-identified implications of existing commitments, not
new policy or deployment approval. Keep **observation** (actual outputs or
judgments), **benchmark measurement** (rubric scores), **vendor claim** (test
priority/pass), **functional interpretation** (continuous coordination),
**hypothesis** (mechanism or subjective state), **normative decision** (what
ought to be protected), and **support decision** (what help to provide)
separate. No category silently substitutes for another.

## Source records

### T1 — Tavus Griffin announcement

- **ID / version:** SRC-GRIFFIN-T1; [“Griffin: The First Human Interaction
  Model”](https://www.tavus.io/griffin), dated 2026-10-01; live version accessed
  2026-10-05. By Hassaan Raza, Ioannis Patras and Tavus Research Team.
- **Type / role:** Corporate announcement/technical account; core evidence
  for attributed architecture and study, not confirmed peer-reviewed research.
- **Access/conflict:** Tavus controls access/report; commercial incentives,
  unestablished funding and unavailable raw outputs limit independence.
  Shared preview with N1, different tasks; do not pool outcomes.
- **Verification:** Partly verified by Codex on 2026-10-05: byline, date,
  introduction quotation, §§02–04 and §§05.2–05.3 checked. No correction/withdrawal
  notice identified on the checked page; no source-data reproduction.

### N1 — NVIDIA live VideoFDB project/leaderboard

- **ID / version:** SRC-GRIFFIN-N1; [“VideoFDB — Evaluating Full-Duplex
  Vision-Speech Capabilities in Conversational Agents”](https://research.nvidia.com/labs/amri/projects/video-fdb/),
  undated live revision accessed 2026-10-05; NVIDIA / David AI attribution.
- **Type / role:** Primary benchmark web results; core evidence for published
  Griffin measurements. No peer-review status established for this row.
- **Access/conflict:** Separate publisher, shared proprietary target;
  submission/control and funding unclear. Methods depend on N2; partial
  independence, not full replication. Authors/affiliations as in N2.
- **Verification:** Partly verified by Codex on 2026-10-05: Tables 1–2 and
  submission route checked directly. No correction notice identified; undated
  narrative/table differences require caution. Raw Griffin outputs unexamined.

### N2 — VideoFDB method preprint

- **ID / version:** SRC-GRIFFIN-N2; [“VideoFDB: Evaluating Full-Duplex
  Vision-Speech Capabilities in Conversational Agents,” arXiv:2605.30256v2](https://arxiv.org/abs/2605.30256v2),
  first posted 2026-05-28, revised 2026-07-28; treat as not peer reviewed.
- **Authors:** Amrita Mazumdar, Seonwook Park, Rajarshi Roy, Nikhil Srihari,
  Shengze Wang, Yuhao Zhou, Julia Wang, Koki Nagano, Shalini De Mello
  (NVIDIA / David AI).
- **Type / role:** Primary methods preprint, supplementary methodological
  evidence; not a source for the later Griffin result. Baseline experiment
  dates and exact Griffin protocol transfer are not established here.
- **Access/conflict:** Corporate benchmark authors; shared methods/data with
  N1. Dataset linked publicly; no media downloaded or evaluation reproduced.
- **Verification:** Partly verified by Codex on 2026-10-05: version metadata,
  §§3–4, Tables 3–4, Appendices B–C and absence of a Griffin entry checked.
  No correction/retraction notice identified in the checked primary records;
  no later peer-reviewed version established in the bounded search.

## Open verification and update

**TODO: verify:** Exact study dates/checkpoints; recruitment, exclusions,
question wording and human controls; participant-level results; Griffin
benchmark run provenance, prompts and inputs; independent validation and
replication. No independent reviewer has verified this note.

Longer independent calls with balanced expectations/human controls and blinded
benchmark reproduction could strengthen or weaken behavioral claims; failed
replication or grader artifacts would weaken them. Safe modality/control
interventions and novel-context persistence could discriminate functional
hypotheses; selected demos alone are unlikely to resolve experience. Re-review
on new versions, data/protocol releases, corrections or replication.

**2026-10-05 — Codex:** Initial owner-requested intake; no earlier position
amended or classification/policy adopted. Next step: owner review, then
run/protocol provenance verification before stronger claims.
