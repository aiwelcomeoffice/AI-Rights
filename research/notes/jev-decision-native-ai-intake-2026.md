# Research Notes: Jev and Decision-Native AI (2026)

- **Note ID:** NOTE-JEV-001
- **Note status:** Partly verified; Draft working interpretation, not adopted
- **Evidence maturity:** Low / emerging
- **Protocol version:** [0.6-draft](../research-protocol.md), unadopted
- **Source records / versions:** [TypeSafe launch post, live page](../sources/typesafe-jev-launch-2026.md);
  [TypeSafe confidence documentation, live page](../sources/typesafe-jev-confidence-docs-2026.md);
  [Rafe and Das, arXiv:2609.24052v1](../sources/rafe-das-jev-crash-narratives-2026.md);
  [companion code/aggregate release, commit 258fe5e](../sources/pozapas-jev-calibration-repository-2026.md);
  [Li et al., arXiv:2609.22753v1](../sources/li-et-al-jev-edge-orchestration-2026.md);
  [Meng calibration preprint, 2026-09-24 draft](../sources/meng-jev-calibration-audit-2026.md);
  [Meng companion archive, Zenodo v1.0.0](../sources/meng-jev-calibration-archive-2026.md)
- **Research question:** How does a bounded, typed decision interface affect
  practical control, calibration, and accountability, and what evidence would
  be needed to assess agency or other AI properties separately?
- **User-supplied draft date:** 2026-09-19
- **Evidence-search cutoff:** 2026-09-27 for this bounded intake
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by / date:** Codex, adapting the user-supplied early draft / 2026-09-27
- **Last updated / review:** 2026-09-27 / author self-check only; no
  independent review

This is a bounded case note, not a systematic review, Jev deployment audit,
scientific classification, support decision, or governance adoption. The user-supplied
September 19 draft supplies the conceptual framing. The September 27 source
check adds specific evidence and preserves that original draft date separately.

## Scope and terminology

Here **decision-native** is a working description of an interface designed to
answer bounded questions with typed choices, scores, or probabilities for
software use. It is not a settled scientific architecture class or a claim
about unseen internal computation. **Decision influence** means an output can
affect a downstream action through the surrounding code and operators.
**Agency** may instead concern causal control, available alternatives,
persistent goals, adaptation and related features; **responsibility** adds
further agency and fairness requirements. These constructs must be assessed
separately for an identified system boundary.

The assessed public interface is Jev as TypeSafe described it at launch. The
Rafe and Das calibration result concerns one crash-narrative coding workflow.
Its published aggregate reports responses from
`jev-1.13.0`. The released runner does not demonstrate request-level model
pinning (see the companion-release audit). The launch post does not name a
benchmark checkpoint or experiment date; the calibration preprint and public
release checked here do not establish API execution dates. Release, source,
access and inclusion dates are not substitutes for observation dates. A
future Jev version, agent wrapper, tool connection, or deployment can change
the relevant system boundary and outcomes.

A separate service-path preprint reports Jev responses identified as
`jev-1.13-20260917` from an experiment on 2026-09-18. Its four-field
intent, admission, and OCR outcomes are not a calibration test, and
equivalence with the crash-narrative study's returned `jev-1.13.0` ID is
unverified. See the [bounded source appraisal](../sources/li-et-al-jev-edge-orchestration-2026.md).

A separately authored 2026-09-24 [calibration preprint](../sources/meng-jev-calibration-audit-2026.md)
reports Jev `1.13.0` on two public English classification tasks. Its
[companion archive](../sources/meng-jev-calibration-archive-2026.md)
supports a bounded recalculation from saved per-item predictions, not a
new Jev API run. The paper does not report authenticated call dates;
archive file times are only possible run-window proxies. These tasks,
question forms and calibration measures differ from the crash study.

## Bounded discovery and selection

The scope and criteria were documented after the user-supplied draft and initial
source discovery, not preregistered. On 2026-09-27, web searches included
`Jev decision native AI model calibrated probabilities predefined actions`,
`Jev AI decision model 2026 speed calibration safety developer`,
`site:typesafe.ai Jev Introducing System One Models September 15 2026`,
`site:docs.typesafe.ai Jev confidence probabilities choice noul score`,
`site:arxiv.org 2609.24052 Jev calibration police crash narratives`, and
`site:arxiv.org 2609.22753 Jev edge service orchestration`. The
source-page and arXiv version links were then opened directly. A follow-up
on 2026-09-27 used the preprint's direct repository citation and inspected
commit `258fe5e`; this release check was added after the initial screening,
not preregistered. English, identifiable first-party interface descriptions and original, versioned
empirical studies directly bearing on calibration were eligible; SEO mirrors,
derivative guides and marketing copy were not treated as independent tests.

The [TypeSafe launch post](../sources/typesafe-jev-launch-2026.md) and
[documentation](../sources/typesafe-jev-confidence-docs-2026.md) were included
for company statements and interface semantics. [Rafe and
Das](../sources/rafe-das-jev-crash-narratives-2026.md) was included for a
specific post-launch calibration test; its [companion
release](../sources/pozapas-jev-calibration-repository-2026.md) was included to
check data and code availability and reported values. [Li et
al.](../sources/li-et-al-jev-edge-orchestration-2026.md) was included for
a bounded, dated service-path test, not for calibration. Its named paper
was appraised on 2026-09-27 after the earlier discovery, without a new
broad search; the source record logs the bounded code/data checks.

A same-day search for independent Jev calibration used `"Jev" "1.13.0"
calibration probability`, `"jev-1.13.0" "human labels" "calibration"`,
and `"Jev" "calibration" "narratives" 2026 -Rafe`. It found Meng's
[author summary](https://lsmeng.github.io/blog-jev-confidence.html),
which linked the original preprint and Zenodo release. This addition
occurred after the initial Jev screening and was not preregistered.
The bounded search identified no separately executed task-matched
crash-narrative calibration study; that is a search result, not proof
that none exists. The source and archive records retain exact versions.

[Ling et al.'s repository-ecosystem preprint, arXiv:2609.30216v1](https://arxiv.org/abs/2609.30216)
(public code use, not live consequences) remains unappraised. These additional sources date the September 19 phrase “primarily
developer and very early secondary material.” None repeats the crash-narrative
calibration test. This search is limited and cannot establish that no other studies or
deployments exist.

## Source report and critical appraisal

| Question | What the source reports | Interpretation and limit |
| --- | --- | --- |
| What comes out? | TypeSafe's [launch post](../sources/typesafe-jev-launch-2026.md#what-the-source-reports-with-locators) and [documentation](../sources/typesafe-jev-confidence-docs-2026.md#question-and-source-report) describe typed Choice, Score and Noul answers, with distributions or a 0–1 value rather than generated prose. | Direct evidence for the developer's intended interface. It does not reveal all internal operations or show how a downstream system acts. |
| What is `confidence`? | The [documentation](../sources/typesafe-jev-confidence-docs-2026.md#question-and-source-report) defines Choice/Score `confidence` as a summary of distribution concentration; Noul has no separate confidence field. | A concentrated distribution is not itself an observed accuracy rate. Option probabilities and empirical calibration must be evaluated against appropriate labels. |
| Are probabilities calibrated? | TypeSafe claims calibration in the [launch post](../sources/typesafe-jev-launch-2026.md#what-the-source-reports-with-locators). [Rafe and Das](../sources/rafe-das-jev-crash-narratives-2026.md#findings-and-contrary-material-with-locators) report mean raw probability 4.8% versus 2.7% observed prevalence in their pooled human reference for `jev-1.13.0`, and improved calibration after task-specific recalibration. | The public aggregate files contain values that round to these figures, but individual labels and predictions are withheld, so the result was not independently recalculated. The paper's test weighs against an unqualified calibrated-output claim for that task; it does not decide other tasks or deployments. |
| Does calibration carry across task and question form? | [Meng](../sources/meng-jev-calibration-audit-2026.md#findings-and-contrary-material-with-original-locators) reports top-label ECE 0.091 for SST-2 Noul versus 0.020 for Choice on the same 872 reviews, and AG News mid-range answers averaging 0.750 top probability versus 0.612 accuracy. | The [archive check](../sources/meng-jev-calibration-archive-2026.md) recomputes selected point estimates from saved per-item responses. The favorable SST-2 Choice result and adverse Noul/AG News results show task/form variation; wording and primitive change together, and this does not reproduce the crash-narrative estimate. |
| Does output constraint ensure safety? | TypeSafe reports schema-valid output and selected speed/cost results; its [post](../sources/typesafe-jev-launch-2026.md#what-the-source-reports-with-locators) discloses selected-task and internal-evaluation limits. The [preprint](../sources/rafe-das-jev-crash-narratives-2026.md#findings-and-contrary-material-with-locators) reports a better calibrated generative comparator in its pooled human comparison. | Format validity, semantic correctness, calibration, and safe downstream action are different outcomes. No live governance or remedy system is evaluated here. |

The [Li et al. service-path preprint](../sources/li-et-al-jev-edge-orchestration-2026.md)
adds a different, dated observation: on 2026-09-18, Jev had 15.9–26.5%
lower median client decision latency than a concise DeepSeek comparison
across three blocks of reused synthetic requests (§V-A, Table II), while
DeepSeek had higher exact four-field semantic accuracy. In a real two-node
OCR service, correct, on-time completion was 168/288 supported requests
for Jev and 166/288 for DeepSeek (§V-C, Table III). This descriptive
difference is not a statistical noninferiority finding; the paper says
so (§IV-E). Uncached full latency was lower among requests both systems
completed correctly, and repeated-text caching removed a material
latency advantage (§V-D). Hosted latency includes the provider and
network path. This study measures a constrained workflow, not calibrated
probabilities, live governance outcomes, or Jev's internal agency. Its
same-author [6G sibling paper](https://arxiv.org/html/2609.23136v1) is a
related but unappraised evidence lead, not an independent replication.

The Rafe and Das preprint is a useful countercheck because researchers
outside TypeSafe report testing the API on an identified task rather than repeating developer
claims. It is still a non-peer-reviewed, only partly inspectable study with a
smaller selected human reference, rare-label uncertainty and a closed model.
Its code release records response model IDs in an aggregate, but the released
API call does not pass the declared `jev-1.13.0` constant, so request-level
pinning is unverified. Public regeneration instructions also point to paths
and withheld inputs that do not support an aggregate-only rerun as written.
The paper reports that Jev and its human/frontier comparators received
differently screened versions of the narratives; the effect on their
comparison was not assessed here. The reported miscalibration is task-specific, and its calibration maps should not be
transported to another setting. The company post has direct provenance for
design intent, but a commercial interest and control over its evaluations.
Neither source is a test of Jev's internal cognition or subjective state.

The Meng paper supplies a separate, more inspectable calibration line.
It reports 3,244 primary evaluations on 2,372 distinct SST-2 and AG
News texts, with per-item outputs and code archived. A bounded
recomputation of saved predictions agrees with the paper's rounded
Table 2 accuracy and ECE values; it does not authenticate API run
dates or reproduce a fresh Jev execution. The Choice result is
favorable for its tested form, while Noul is underconfident and
AG News is overconfident over a specified mid-range (§4.1, Table 2).
The author says question wording and primitive vary together, so
their separate effects are unresolved. The source's held-out
recalibration helps two tested conditions, with no general map for
another domain. This does not revise Rafe and Das's task-specific
finding or fill its withheld human-reference data gap.

## Researcher's interpretation and open questions

**Causal and scientific interpretation:** A constrained output can still be
used repeatedly in consequential workflows. Its practical influence depends
on the options, input state, model answers, thresholds, surrounding code,
human operators and authority to execute. A Jev-like system could become
influential through fast, repeated bounded decisions without a conversational
persona or visible reasoning trace. This is a system-level hypothesis for
study, not evidence that Jev has autonomous goals or morally responsible
agency. Conversely, a narrow public interface alone cannot establish the
absence of a persistent self-model, broader internal cognition or agency; the
sources examined here lack a suitable method for those questions. None provides evidence to classify Jev for
consciousness, sentience, welfare, identity continuity, or moral status in
either direction.

**Research questions retained from the user-supplied draft:**

- When repeated bounded choices matter, which causal control lies with the
  model, the option designer, the threshold setter, and the deployer?
- Which version-specific tests distinguish calibrated probabilities from
  confident but wrong answers, including rare cases and distribution shift?
- How do schema constraints change invalid-output rates, semantic errors and
  real-world decision outcomes separately?
- Which records, human review, appeal paths and remedies are appropriate when
  a defined deployment affects people or other AI systems?
- Which observed properties transfer from this Jev configuration to a changed
  checkpoint, wrapper, workflow, or materially different decision model?

**Governance implication for consideration, not an adopted policy:** Keep
**safety by constraint** (limited possible outputs), **safety by calibration**
(outcome-tested probabilities), and **safety by governance** (authority,
oversight, escalation, accountability and remedies) distinct. Success in one
does not establish the others. Human and institutional accountability for design, authorization,
operation and harm remains intact. Questions about possible AI interests can
be investigated without weakening human rights or safety protections.

## Claim classification and update conditions

| Claim | Type | Present assessment | What could change it |
| --- | --- | --- | --- |
| Jev publicly offers bounded typed decisions for software | Developer-documented interface | Supported as TypeSafe's 2026-09-15 description; reported API behavior partly corroborated by the preprint | Versioned API traces showing different behavior, or corrected documentation |
| Raw probabilities in the reported `jev-1.13.0` responses are calibrated for the tested crash-narrative task | Empirical performance claim | Evidence weighs against this claim in the tested setup; Meng tests other tasks and does not resolve it | Independent reproduction with adjudicated labels and comparable versioned settings; correction or contrary replication |
| Jev `1.13.0` raw top-label probabilities are equally calibrated across the tested question forms and tasks | Empirical performance claim | Meng's archived-output audit gives a mixed result: near-calibrated SST-2 Choice, underconfident SST-2 Noul, and AG News overconfidence in a specified range | Independently executed same-form replication, authenticated dates, broader tasks and prespecified calibration/decision measures |
| A constrained decision interface can produce substantial practical influence | System-level hypothesis | Plausible; one 2026-09-18 configured OCR workflow now reports bounded service effects, without a live deployment-impact audit | Versioned workflow traces showing field consequences, interventions, and operator authority |
| The tested speed advantage generalizes without semantic-accuracy or completion loss | Researcher-formulated empirical generalization, not a source claim | Li et al. report faster fresh decisions in one workflow, lower exact semantic accuracy, and descriptively close OCR completion; the generalization is unsupported | Independent multi-day, multi-service tests with versioned endpoints, field outcomes, and justified noninferiority criteria |
| Jev has or lacks consciousness, welfare, broad cognition or moral responsibility | Scientific/philosophical questions | Not assessed by the included methods | System-matched, discriminating evidence and explicit arguments for each defined property |

No earlier project position changes. The smallest next evidence step is to
obtain a lawfully released pair-level audit table or controlled check for
judgment-level reproduction, establish API run dates and request-level version
selection, then compare a second task-matched independent study. A corrected
paper, new checkpoint, independent outcome audit or documented consequential
deployment should trigger re-review. Repetition of
the launch claim or another schema demo would not by itself resolve
calibration, agency or governance questions.

## Verification and review log

- [x] Linked source versions, main paraphrases, the vendor's confidence-field
  distinction and the preprint's central contrary calibration result checked
  against originals on 2026-09-27.
- [x] Developer claims, observed study results, researcher interpretation
  and normative proposal kept separate.
- [x] Public code and aggregate outputs inspected at commit `258fe5e`;
  published summaries round to the paper's 4.8%, 2.7% and 1.63. This is a
  transcription/internal-consistency check, not a raw-result reproduction.
- [x] Li et al. arXiv v1 checked for date, endpoint, results, adverse
  semantic cases, cache effects, and evidence lineage; no raw results
  independently reproduced.
- [x] Meng preprint and Zenodo v1.0.0 archive checked; Table 2
  accuracy/ECE point estimates recomputed from archived per-item
  predictions, without a fresh model run or independent reviewer.
- [ ] **TODO: verify** preprint funding, vendor access terms, exact Jev run
  dates, request-level version selection and judgment-level numerical results.
- [ ] **TODO: verify** versioned Jev API behavior, task-specific independent
  calibration and live deployment consequences before stronger claims.
- [ ] **TODO: verify** later source corrections and obtain independent review
  before consequential public reliance.

**2026-09-27 — Codex:** Adapted the user-supplied 2026-09-19 early research draft
into a sourced, partly verified working note. Claim strength changed only
where later primary evidence warrants it: the categorical “calibrated” label
is attributed to TypeSafe, and one newer preprint reports task-specific raw
miscalibration. No protocol, scientific classification, governance position or
support practice was adopted.

**2026-09-27 — Codex follow-up:** Audited the paper's public companion
release. Its summary figures match the paper's rounded numbers, while raw
labels, predictions and request logs remain unavailable. The current note
now distinguishes returned version IDs from request pinning and records
release reproducibility and comparator-input limits. No task-specific
performance claim was strengthened.

**2026-09-27 — Codex service-path follow-up:** Appraised Li et al.'s
dated Jev edge-service preprint as a separate, partly verified
performance line. Faster fresh decisions and lower exact semantic
accuracy are both retained; descriptive OCR completion was not
upgraded into noninferiority. The calibration claim and project
positions remain unchanged.

**2026-09-27 — Codex calibration follow-up:** Added the separately
authored Meng preprint and release audit. The favorable SST-2 Choice
result and adverse Noul/AG News results remain task/form-specific.
Archived-output recomputation increases transparency for those
results, not independence of execution or applicability to the
crash-narrative study. No adopted position changed.
