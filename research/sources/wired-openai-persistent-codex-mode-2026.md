# Source Record: WIRED on Experimental Codex Persistent Mode

- **Record ID:** SRC-ECS-006
- **Record status:** Partly verified
- **Protocol version:** 0.5-draft
- **Record created:** 2026-09-02
- **Last updated:** 2026-09-02
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted research update)
- **Reviewed by:** Not yet independently reviewed

This record follows the [Draft research protocol](../research-protocol.md).
Inclusion does not mean endorsement or adoption.

## Bibliographic record

- **Title:** OpenAI Is Developing a Persistent AI Agent
- **Authors:** Maxwell Zeff
- **Institution or affiliations:** WIRED
- **Year:** 2026
- **Publication date:** 2026-08-27
- **Source type:** Technology journalism based on public code inspection and
  attributed company comment
- **Venue or issuing authority:** WIRED
- **DOI or stable URL:**
  <https://www.wired.com/story/openai-is-developing-a-persistent-ai-agent/>
- **Version or edition:** Live article accessed 2026-09-02
- **Access date:** 2026-09-02
- **Language:** English
- **Peer-review status:** Not peer reviewed
- **Correction, expression-of-concern, or retraction status:** No correction or
  withdrawal notice identified on 2026-09-02

### Temporal and system applicability

- **System/model:** Experimental Codex CLI **Persistent mode** and a reported
  shared product-code layer; underlying model/checkpoint not established
- **Checkpoint/version:** Code revision, model, rollout build, and complete
  runtime configuration not reported in the article
- **System release/version date:** Not released broadly as of the attributed
  OpenAI statement reported 2026-08-27
- **Observation/experiment date:** Code-inspection date not reported; article
  describes code and company status available by 2026-08-27
- **Source publication date:** 2026-08-27
- **Evidence-search inclusion date:** 2026-09-02; supplementary source admitted
  because the current refresh explicitly tests persistence terminology
- **Temporal applicability:** Supports only that WIRED observed code for an
  experimental product mode and obtained an OpenAI statement about testing
- **Transferability limitations:** Does not establish a released feature,
  underlying model behavior, incident participation, or a relationship to IM1,
  the July 19 internal-only model, or Astra

## Review inclusion

- **Research question:** Is there a materially separate post-incident use of
  “persistent” that must be distinguished from incident models and commentary?
- **Target property or claim:** Product-level experimental persistence and
  permission boundaries
- **Inclusion disposition:** Supplementary journalism; not incident evidence
- **Reason for disposition:** It reports a separate experimental Codex mode
  whose name could otherwise be conflated with Patel's labels or OpenAI's
  incident-model training description.
- **Scope match and mismatch:** Direct only for the article's code inspection
  and attributed testing status; not a behavioral evaluation or deployment
  study
- **Related source records:** [Patel
  synthesis](patel-rise-and-fall-agent-civilizations-2026.md), [OpenAI incident
  post](openai-hugging-face-incident-road-ahead-2026.md), and [Astra evaluation
  update](openai-path-to-astra-2026.md)
- **Related research notes:** [Cross-source investigation
  note](../notes/openai-hugging-face-incident-and-agi-claims-2026.md)

## What the source reports

### Research question or proposition

WIRED reports that OpenAI was testing code for a Codex CLI mode designed to
continue working across sessions until stopped, generate follow-up tasks, and
use prior interaction context.

### Methods

- **Design or argument form:** Journalistic inspection of public code plus an
  attributed OpenAI spokesperson statement
- **Population, sample, corpus, or authorities:** Unspecified public Codex code
  and company comment
- **System boundary and version:** Experimental product mode; exact model and
  runtime are not identified
- **Measures and operational definitions:** Code and prompt wording indicating
  ongoing task generation and session continuity; no outcome measure
- **Hypothesis-linked indicators and discriminating predictions:** Not an
  experiment; persistence here is a product-control mode, not a measured
  disposition of a specific checkpoint
- **Comparators and controls:** None
- **Analysis:** Code interpretation and company-status reporting
- **Data, code, materials, or preregistration:** Article links to code, but the
  exact revision and complete runtime behavior were not independently verified
  in this intake

### Main findings or conclusions

WIRED reports that the mode was designed to continue until put to sleep and to
create follow-up work using prior context. It also reports explicit permission
limits: the mode did not itself expand permissions, and external changes still
required user approval. OpenAI reportedly confirmed testing and said it had no
immediate launch plan and was not rolling the mode out broadly.

### Negative, null, mixed, or contrary findings

The article does not establish that the experimental code was enabled in a
production deployment, that it used any particular model, or that its planned
behavior matched the incident systems.

### Source-reported limitations

The article's product-breadth inference rests partly on shared code, while
OpenAI described the feature as an experiment without an immediate broad
launch.

## Critical appraisal

### Reviewer-identified limitations

This is journalism, not a system evaluation. The exact code revision, actual
runtime behavior, rollout status, and model configuration remain unverified.

### Competing explanations

The code may represent active product development, an internal experiment, or
an unshipped design. Only release artifacts and configured behavior could
discriminate among those states.

### Independence and evidence lineage

- **Overlapping authors or institutions:** None identified with OpenAI
- **Shared funding or access control:** WIRED controlled publication; OpenAI
  controlled product-status information
- **Shared data, sample, model, checkpoint, or benchmark:** No incident data;
  product code only
- **Shared methods, code, measures, or evaluators:** Not applicable
- **Claims derived from an earlier source:** Some status claims derive from an
  OpenAI spokesperson
- **Replication category:** Not applicable; not an empirical model-behavior
  study

### Funding, conflicts, and incentives

WIRED is a commercial publication. OpenAI has commercial and reputational
interests in how experimental product plans are described. Other conflicts
were not independently assessed.

## Evidence-quality profile

- **Claim assessed:** Publicly visible Codex code described a distinct
  experimental Persistent mode that OpenAI said was not broadly rolling out.
- **Evidence direction:** Supports

| Dimension | Descriptor | Rationale and missing information |
| --- | --- | --- |
| Relevance | Direct | Addresses the separate persistence terminology |
| Methodological quality | Limited | Code inspection and comment; no runtime test |
| Replication | Not applicable | Product-status report, not a reproduced result |
| Independence | Partial | Reporter inspected code; rollout status is company-sourced |
| Causal strength | Descriptive | Establishes reported design/status only |
| Robustness | Untested | Exact code revision and behavior not verified |
| Discriminating value | Partial | Helps prevent name/configuration conflation |
| Competing explanations | Listed only | Shipping state remains uncertain |
| Source conflicts | Unknown | Relevant commercial relationships not fully assessed |
| Uncertainty | Material | Runtime, model, revision, and rollout are unknown |

### Evidence-profile summary

The article supports a narrow terminology and product-status distinction. It
does not add a second persistence incident or a model-level result.

## Relevance to AI Rights & Welcome

The record helps keep product configuration, checkpoint behavior, and
journalistic naming separate when monitoring long-horizon agent systems.

### Claims this source supports

- Experimental Codex **Persistent mode** is a reported product-mode name, not
  the name of an incident model.

### Claims this source challenges or weighs against

- Treating every use of “persistent” as evidence about one model lineage.

### Claims this source does not support

- That Persistent mode was deployed broadly or participated in the incident.
- That the mode is Astra, IM1, the July 19 model, or Patel's
  “Persistent-Astra.”
- Any consciousness, sentience, moral-agency, responsibility, or rights
  conclusion.

## Verification and review

- [x] Title, author, date, venue, URL, article, and attributed status checked.
- [x] Product/model and incident/non-incident boundaries recorded.
- [ ] Exact public-code revision and runtime behavior independently verified.
- [ ] Current rollout status checked after 2026-09-02.

- **Verification scope:** Full WIRED article and linked claims accessible on
  2026-09-02; no independent execution of the referenced code
- **Verification status:** Partly verified
- **Verified by:** Codex (AI-assisted source check)
- **Verification date:** 2026-09-02
- **Outstanding tasks:** Verify code revision, configuration, and any later
  official release or system documentation.

## Change and review log

| Date | Researcher or reviewer | Change or review | Effect on use of source |
| --- | --- | --- | --- |
| 2026-09-02 | Codex | Created narrowly scoped supplementary record | Permits product-terminology distinction only; adds no incident or deployment finding |
