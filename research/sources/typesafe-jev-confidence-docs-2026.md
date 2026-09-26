# Source Record: TypeSafe's Jev Confidence Documentation (2026)

- **Record ID:** SRC-JEV-002
- **Record status:** Partly verified for the documented interface and TypeSafe's
  interpretation of its confidence field; performance not independently verified
- **Protocol version:** [0.6-draft](../research-protocol.md), unadopted
- **Created / last updated:** 2026-09-27
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by / review:** Codex, AI-assisted documentary intake / author
  self-check only
- **Related note:** [NOTE-JEV-001](../notes/jev-decision-native-ai-intake-2026.md)

## Bibliographic and temporal record

- **Source:** TypeSafe AI, [“Confidence”](https://docs.typesafe.ai/confidence),
  official developer documentation.
- **Type / review / version:** First-party product documentation, not peer
  reviewed; live page without a visible publication date or immutable revision
  identifier, accessed 2026-09-27. Correction and revision history unknown.
- **System / version:** TypeSafe's documented Choice, Score and Noul answer
  types. The page does not pin a Jev checkpoint or report experiment dates.
- **Release, observation and applicability:** Documented behavior as viewed
  2026-09-27; no empirical observation date is supplied. Access date does not
  establish behavior of another API or later model version.

## Question and source report

**Question:** What does TypeSafe mean by a returned `confidence` value, and how
does it differ from an option probability? This page is included for interface
semantics, not as evidence that the values predict correctness in a particular
deployment. It belongs to the same developer-controlled lineage as the
[launch post](typesafe-jev-launch-2026.md).

The “Confidence is derived from the probabilities” section says Choice and
Score return distributions over options or levels and a `confidence` value
summarizing their concentration. Noul answers do not have that separate
`confidence` field. The “Three paths” and “Thresholds scale with risk” sections
show TypeSafe's proposed routing patterns and say thresholds should be tested
on the user's own data. A concentrated distribution is a statement about the
model's output; this page does not provide observed error rates at those
confidence values or validate any example threshold.

## Appraisal, contrary material and limits

The documentation is direct evidence for the developer's API description.
It is a weak source for the separate empirical claim that a probability or
confidence score is calibrated to outcomes. The page itself calls its
confidence definition a convenience and says another measure may serve a use
case better. It provides no calibration study, sample, reference labels, model
version, or deployment distribution. It cannot distinguish a correct strong
signal from a confident semantic error, missing option, distribution shift, or
downstream policy failure. TypeSafe has a commercial interest and controls the
documentation and model access; no independent review is reported here.

No negative calibration test is reported in this page. Its absence cannot be
read as evidence that calibration fails or succeeds.

## Verification and update

- [x] Page title, field distinction, Noul exception and threshold caveat
  checked against the original on 2026-09-27.
- [ ] **TODO: verify** precise computation of `confidence`, API behavior by
  pinned version, and calibration against observed outcomes for defined tasks.
- [ ] **TODO: verify** whether a later document revision or correction changes
  these definitions.

**Review trigger:** Versioned API documentation, an observed interface change,
or an outcome-based calibration study. No independent review or project
adoption occurred on 2026-09-27.
