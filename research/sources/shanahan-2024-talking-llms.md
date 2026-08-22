# Source Record: Talking about Large Language Models

- **Record ID:** SRC-ACEB-012
- **Record status:** Partly verified
- **Protocol version:** 0.1-draft
- **Record created:** 2026-08-22
- **Last updated:** 2026-08-22
- **Prepared by:** Codex (AI-assisted initial research draft)
- **Reviewed by:** Not yet independently reviewed

This record follows the [research protocol](../research-protocol.md). Inclusion
does not mean endorsement or adoption.

## Bibliographic record

- **Title:** Talking about Large Language Models
- **Authors:** Murray Shanahan
- **Institution or affiliations:** The article lists Imperial College London.
  Contemporaneous Google DeepMind employment is externally verified through
  the author's Imperial page and a 2023 *Nature* article, but is not listed as
  an affiliation on this article.
- **Year:** 2024
- **Publication date:** 2024-01-25
- **Source type:** Peer-reviewed conceptual/technical article
- **Venue or issuing authority:** *Communications of the ACM* 67(2), 68–79
- **DOI or stable URL:** <https://doi.org/10.1145/3624724>
- **Version or edition:** Version of record
- **Access date:** 2026-08-22
- **Language:** English
- **Peer-review status:** Peer reviewed, per the author's publication page;
  ACM classifies it as a research article
- **Correction, expression-of-concern, or retraction status:** None identified
  on ACM record checked 2026-08-22; TODO: verify independently.

## Review inclusion

- **Research question:** What evidence would support or weigh against
  consciousness or sentience in contemporary AI systems?
- **Target property or claim:** Evidential limits of literal psychological
  interpretation of LLM language and intentional-stance vocabulary.
- **Inclusion disposition:** Core conceptual/technical evidence
- **Reason for disposition:** Explains how LLM output can invite but not warrant
  psychological attribution.
- **Scope match and mismatch:** Direct for text-generating LLM behavior; does
  not audit every multimodal or agentic system.
- **Related source records:** [Colombatto and Fleming 2024](colombatto-fleming-2024-folk-attributions.md);
  [Chalmers 2023](chalmers-2023-llm-consciousness.md)
- **Related research notes:** [Detailed note](../notes/shanahan-2024-talking-llms.md)

## What the source reports

### Research question or proposition

Shanahan asks how to describe LLMs without sliding from a model's generation of
humanlike text to unsupported claims about beliefs, intentions, or inner states.

### Methods

- **Design or argument form:** Technical explanation plus conceptual analysis
- **Population, sample, corpus, or authorities:** Autoregressive language
  modeling, prompt prefixes, dialogue examples, and philosophy of
  interpretation.
- **System boundary and version:** LLMs and dialogue applications available by
  the article's cutoff; model/runtime details vary.
- **Measures and operational definitions:** Next-token generation, prompt-
  prefix conditioning, pattern completion, and ordinary psychological
  vocabulary.
- **Comparators and controls:** Literal psychological interpretation versus
  mechanism-aware descriptions.
- **Analysis:** Conceptual reconstruction grounded in model operation.
- **Data, code, materials, or preregistration:** No new empirical dataset.

### Main findings or conclusions

The paper explains fluent dialogue through autoregressive sequence
continuation and argues that psychological language about an LLM should be
qualified. This provides a mechanistic alternative that does not require
positing phenomenal experience; it does not claim that mental-state vocabulary
could never be warranted or that language models could never be conscious.

### Negative, null, mixed, or contrary findings

Useful intentional descriptions may sometimes summarize behavior, but their
pragmatic value does not make them literal evidence of subjective experience.

### Source-reported limitations

The account is conceptual and does not offer a consciousness test or a complete
theory of agency.

## Critical appraisal

### Reviewer-identified limitations

Mechanism-aware caution about output does not settle whether hidden or added
mechanisms could support experience. The article predates some later agentic,
memory, and multimodal deployments.

### Competing explanations

Observed language can be explained by training distributions, prompt-prefix
conditioning, autoregressive pattern completion, and decoding without positing
a corresponding phenomenal state.

### Independence and evidence lineage

- **Overlapping authors or institutions:** No author overlap identified with
  other core records.
- **Shared funding or access control:** No dataset or system access is used;
  no article-level funding statement was located. Contemporaneous Google
  DeepMind employment is relevant to the topic.
- **Shared data, sample, model, checkpoint, or benchmark:** None; illustrative
  model class.
- **Shared methods, code, measures, or evaluators:** No shared dataset with the
  anthropomorphism survey.
- **Claims derived from an earlier source:** Draws on LLM technical literature.
- **Replication category:** Not applicable

### Funding, conflicts, and incentives

- **Funding or sponsorship:** No article-level funding statement located;
  TODO: verify independently that none was published elsewhere.
- **Author conflicts and affiliations:** The article lists Imperial College;
  contemporaneous Google DeepMind employment is externally verified, but no
  article-level competing-interest statement was located.
- **System, data, compute, and publication control:** Analysis concerns models
  often controlled by developers; no privileged access stated in this record.
- **Commercial, advocacy, regulatory, or litigation incentives:** Potential
  industry relationship requires disclosure, not automatic discounting.
- **Disclosure gaps:** Article-level funding and competing-interest statements.

## Evidence-quality profile

- **Claim assessed:** Fluent language and psychological vocabulary from an LLM
  have a mechanistic alternative that does not require positing phenomenal
  experience and are not stand-alone evidence of it.
- **Evidence direction:** Challenges or weighs against

| Dimension | Descriptor | Rationale and missing information |
| --- | --- | --- |
| Relevance | Direct | Concerns LLM outputs used in attributions. |
| Methodological quality | Adequate | Mechanism-grounded analysis; no experiment. |
| Replication | Not applicable | General technical/conceptual account. |
| Independence | High | Distinct author/method lineage. |
| Causal strength | Conceptual | No controlled consciousness outcome. |
| Robustness | Untested | The alternatives are technically plausible across many configurations, but the article reports no empirical test. |
| Competing explanations | Well examined | Central focus is alternative interpretation. |
| Source conflicts | Unknown | Industry disclosure pending. |
| Uncertainty | Material | Does not address all internal mechanisms. |

### Evidence-profile summary

The paper strongly supports treating language and self-description as
non-diagnostic when isolated. It cannot prove that the producing system has no
experience.

## Relevance to AI Rights & Welcome

It supplies a technically grounded safeguard against manipulative
anthropomorphism while leaving the scientific question open.

### Claims this source supports

- Technical/conceptual claim: LLM-generated psychological language can arise
  from autoregressive sequence continuation and prompt conditioning.

### Claims this source challenges or weighs against

- Inference from fluent or psychologically framed language alone to experience.

### Claims this source does not support

- Universal non-consciousness of LLMs or future artificial systems.

## Verification and review

- [x] Title, author, DOI, venue, pages, and date checked.
- [x] Source type and version identified.
- [x] Main argument checked against ACM article.
- [x] No quotations used.
- [ ] Full disclosures and correction status independently checked.
- [x] Alternative explanations recorded.
- **Verification scope:** ACM metadata/full article and author affiliation
  available on the article page.
- **Verification status:** Partly verified
- **Verified by:** Codex (machine-assisted; no independent human review)
- **Verification date:** 2026-08-22
- **Outstanding tasks:** TODO: verify whether an article-level funding or
  competing-interest statement exists and check correction status independently.

## Change and review log

| Date | Researcher or reviewer | Change or review | Effect on use of source |
| --- | --- | --- | --- |
| 2026-08-22 | Codex | Initial baseline record | Used for output interpretation, not system verdict. |
| 2026-08-22 | Codex | Corrected robustness and clarified article versus external employment metadata | Prevents a conceptual argument from being described as empirically tested. |
