# Source Record: Google DeepMind, Gemini 4 Argon model card

- **Record ID/status:** SRC-ARGON-2026-01; Partly verified Draft
- **Protocol:** 0.6-draft
- **Created/updated:** 2026-10-17
- **Prepared by:** Codex, AI-assisted intake; **reviewed by:** not yet independently reviewed
- **Organisation/publisher:** AI Welcome Office / AI Rights & Welcome

## Bibliographic record and scope

Google DeepMind, [“Gemini 4 Argon” model card](https://deepmind.google/models/model-cards/gemini-4-argon/), published **2026-10-13** (page also says “October 2026”), corporate technical disclosure, English live page accessed 2026-10-17. A [PDF edition](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-4-Argon-Model-Card.pdf) is linked; the web card was used for extraction. No numbered card revision, correction or retraction was identified; the card warns it may be updated. No peer review is reported.

**Disposition:** Core first-party statement about Argon's evaluation and Google's risk classification. **System:** Gemini 4 Argon, a sparse mixture-of-experts multimodal model; exact weights, checkpoint and evaluation harness not disclosed. Google announced limited access 2026-09-30 and broader rollout 2026-10-13; development/training and individual safety-challenge dates not reported. The card says benchmark results are as of October 2026; that is not a date for each challenge. Claims apply to Google's assessed configurations, not every API or product configuration, later weights or other Gemini models.

## Source report and evidence profile

In “Frontier Safety Assessment,” Google defines its **Stealth and Situational Awareness TCL** as a combined threshold involving discovery/use of deployment-setting details and circumvention of basic oversight. It reports **14/15 challenges passed**, says the TCL cannot be ruled out, and says safeguards and a residual-risk assessment reduce risk below the TCL. These are distinct claims: challenge performance, threshold judgment and post-mitigation risk judgment. The card also says its **ML R&D acceleration** and **automation** CCLs were not reached. In “Evaluation,” it reports benchmark results across tasks, including Argon losses to other models on some coding/science comparisons; the [methodology PDF](https://deepmind.google/models/evals-methodology/gemini-4-argon) says many non-Gemini comparison numbers come from providers' self-reports, so they do not form a uniform controlled comparison.

**Direction and quality:** Direct for Google's stated challenge count and decision; limited for independent causal or statistical appraisal. Challenge definitions, individual outcomes, prompts, sampling, criteria, monitor effects and confidence intervals are not in the card. Google controls the model, access, tests and publication; corporate incentives and proprietary access are material, while its explicit adverse threshold judgment remains informative. No independent replication of the 14/15 result was located in the bounded search. The card does not establish covert goal pursuit, spontaneous evasion, a stable internal self-model or subjective experience. Its “cannot rule out” wording is a risk-assessment conclusion, not observed threshold crossing.

**Verification:** Card §§Model Information, Evaluation and Frontier Safety Assessment inspected 2026-10-17. Search: direct user URL; `Gemini 4 Argon situational awareness 14 of 15 challenge independent evaluation October 2026`. The linked full safety report was identified but its PDF could not be retrieved through the available browser or sandbox; its uninspected contents are **not** treated as verified here. TODO: inspect the full report, challenge-level artifacts, exact tested checkpoint and independent replication; check revisions at re-review.
