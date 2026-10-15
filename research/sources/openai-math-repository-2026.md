# Source Record: OpenAI mathematics collection and change log

- **Record ID:** SRC-MATH-002
- **Record status:** Partly verified
- **Protocol version:** 0.6-draft
- **Record created / last updated:** 2026-10-15
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted research intake)
- **Reviewed by:** Not yet independently reviewed

## Bibliographic record

- **Title / author:** `openai/math`, README and `history.md`; OpenAI
- **Publication date / type:** Public repository announced 2026-10-06; versioned first-party manuscript collection and revision log
- **Originals:** [README](https://github.com/openai/math/blob/main/README.md), [history.md](https://github.com/openai/math/blob/main/history.md), [formalization catalogue](https://github.com/openai/math/blob/main/lean/formalization.yaml)
- **Version / access date:** `main` as viewed 2026-10-15; moving branch, no immutable commit pinned in this intake. History entry dated 2026-10-07.
- **Peer review:** Repository publication is not journal peer review; status of individual manuscripts not checked.
- **Corrections / withdrawals:** `history.md`, 2026-10-07: three withdrawn manuscripts after a sign error invalidated a shared argument; fourteen other manuscripts revised with proof repairs, clarified statements/dependencies or a citation correction; thirteen companion papers received citation updates.

## Review inclusion and applicability

- **Question / disposition:** Core primary artifacts for collection size, disclosed procedure and revision status; sampled metadata only, not a proof audit.
- **System / version:** Mostly one unreleased internal OpenAI model; exact checkpoint and detailed configuration unreported. README names exceptions to the common procedure but does not establish an independent model for them.
- **Observation dates:** Problem-solving runs not dated in README; collection release 2026-10-06 and revisions 2026-10-07 are document events.
- **Temporal scope:** Public catalog and OpenAI process account as viewed 2026-10-15; no inference to default public models or later systems.
- **Related sources:** [Announcement](openai-sharing-math-progress-2026.md); [advisory recommendations](agmai-responsible-release-math-2026.md).
- **Related note:** [October mathematics release intake](../notes/openai-mathematics-release-2026.md).

## Source report and appraisal

The README, “Navigating the collection,” currently states **719 manuscripts in 372 families**, with a family grouping related papers rather than independent confirmations. It reports that **300 of 719 top-line results (~42%)** have Lean formalizations (README and 2026-10-07 history). This is the repository's coverage claim; this intake did not compile the Lean artifacts or check whether each formal theorem matches the natural-language claim.

In “How the results were produced,” OpenAI says the model was posed approximately **4,000 problems**, that most results followed a common procedure with average compute equivalent to three hours of ChatGPT Pro thinking, and that significance screening and grouping led to the catalog. It identifies exceptions for a Riemann zeta zero-free-region result and a Hodge-conjecture result for CM abelian varieties, and human editing for readability of one zeta manuscript. Ten abridged reasoning summaries are listed. The denominator is problems *posed*, not a documented matched control sample or an independently audited success rate.

The README warns that some unformalized results may have issues. The 2026-10-07 history provides concrete contrary evidence to blanket correctness: a sign error led to three withdrawals, and fourteen other manuscripts required revisions. The current count and documented withdrawals must be read together; this record uses the repository's 2026-10-15 count and preserves the change history.

**Evidence-quality profile for the public-catalog and correction facts:** direct relevance, adequate documentary quality, descriptive causal strength, same-source confirmation, low independence and limited uncertainty for the repository's *current self-description*. **For the stronger claim that the collection contains 372 valid breakthroughs:** direct candidate artifacts but correctness, novelty, robustness and mathematical importance vary by family and remain unassessed here; no independent replication established; low independence and material uncertainty. Lean coverage improves checkability for its exact formal statements but does not by itself settle informal-statement equivalence, novelty, significance or all other manuscripts.

OpenAI controls the proprietary model, attempt selection, compute, repository and updates. The artifacts permit outside review, but the number of manuscripts is one related output lineage, not hundreds of independent replications. Revisions must be checked at the manuscript level before reliance.

**Supports:** A large, publicly inspectable candidate-result corpus and a documented correction process. **Challenges:** Any unqualified claim that every released manuscript is correct. **Does not support:** A verified count of mathematical discoveries, an independently established model success rate, or transfer to other AI properties.

**Verification:** README and dated `history.md` paragraphs checked 2026-10-15; formalization catalogue linked, not run; individual PDFs, Lean builds and field-specific literature not reviewed. TODO: pin an immutable repository commit and audit selected manuscript/Lean pairs with domain experts.
