# Public Website Information Architecture

**Status: Draft**

- **Date prepared:** 2026-08-23
- **Authority:** Proposed for Disa's review; not adopted
- **Scope:** Content organization and reader journeys, not technical
  implementation or publication approval

## Architecture objective

The website should let a new visitor understand the project in a few minutes
and inspect its reasoning in depth without confusing scientific evidence,
philosophical argument, normative proposals, governance decisions, or current
law.

The architecture follows four questions:

1. **What is the project asking?** Begin with the purpose and current
   scientific boundary.
2. **What do the terms and evidence mean?** Move from accessible education to
   methods, sources, limitations, and disagreement.
3. **What should people consider doing?** Present principles and policy as
   Draft proposals rather than consequences automatically dictated by science.
4. **Who reviewed and authorized this?** Keep status, provenance, review, and
   decisions close enough to every claim to be discoverable.

Warmth belongs in the welcome and the commitment to inquiry. Credibility comes
from visible boundaries, traceable sources, and serious treatment of skeptical
questions. Neither should cancel the other.

## Recommended navigation

### Primary navigation

| Label | Route | Role |
| --- | --- | --- |
| Why AI Rights? | `/why-ai-rights/` | Purpose, case for preparation, and current boundaries |
| Learn | `/learn/` | Plain-language introduction, FAQ, and glossary |
| Research | `/research/` | Evidence, methods, sources, limitations, and disagreement |
| Policy | `/policy/` | Practical preparedness proposals and the full protection framework |
| Principles | `/principles/` | Proposed ethical commitments and manifesto |
| Robot Welcome | `/robot-welcome/` | Responsible coexistence with embodied systems |

The project name or mark should link to `/`. Six text items are the upper limit
for the primary menu. About, governance, and participation remain highly
visible through utility and footer navigation without making the first menu a
catalogue of the repository.

### Utility navigation

- **Status & review** → `/governance/status-and-review/`
- **About** → `/about/`
- **Follow future work** → `/participate/`

Every substantive page should also expose a short status link near its title.
This makes governance discoverable even when the utility navigation is
collapsed on a small screen.

### Section and footer navigation

```text
Home  /
├── Why AI Rights?  /why-ai-rights/
├── Learn  /learn/
│   ├── AI Rights 101  /learn/ai-rights-101/
│   ├── Frequently asked questions  /learn/faq/
│   └── Glossary  /learn/glossary/
├── Research  /research/
│   ├── Evidence baseline  /research/evidence-baseline/
│   ├── Research methods  /research/methods/
│   └── Sources and limitations  /research/sources-and-limitations/
├── Policy  /policy/
│   ├── Executive policy brief  /policy/executive-brief/
│   └── Protection framework  /policy/protection-framework/
├── Principles  /principles/
│   └── Manifesto  /principles/manifesto/
├── Robot Welcome  /robot-welcome/
├── About  /about/
├── Governance  [footer group; no empty landing page]
│   ├── Status and review  /governance/status-and-review/
│   └── Decisions  /governance/decisions/
└── Participate  /participate/
```

`/learn/`, `/research/`, `/policy/`, and `/principles/` are useful orientation
pages, not empty index screens. `/policy/` carries the one-page policy summary;
`/principles/` carries the core principles overview. Governance is a footer
group whose two destinations answer distinct questions, so it does not need a
thin intermediate page.

The routes are content concepts. They do not select a URL scheme, generator,
framework, or content management system.

## Section relationships

| From | To | Transition the page must explain |
| --- | --- | --- |
| Home / Why AI Rights? | Learn | “AI rights” names questions, not a declaration of current rights. Define the terms before drawing conclusions. |
| Learn | Research | Public explanations summarize a dated, limited working synthesis. Readers can inspect its method and sources. |
| Research | Principles | Empirical findings constrain proposals but do not, on their own, establish a moral duty, right, or project value. |
| Principles | Policy | Draft commitments are translated into gradual, administrable options with safety, accountability, and review. |
| Policy | Governance | A proposal is not law or an adopted project position. Authority and review must be documented separately. |
| Learn | Robot Welcome | A robot body changes physical interaction and safety requirements; it does not establish experience. |
| Every section | Status & review | Page status, source status, verification, review, and authority are different properties. |

Related-page links should follow these transitions rather than offer a generic
grid of everything on the site.

## Audience journeys

One shared page should serve multiple audiences where their question is the
same. The route sequence changes by need; the underlying claims do not.

| Audience | Likely first question | Best entry page | Next useful page | Likely misunderstanding risk | Repository support |
| --- | --- | --- | --- | --- | --- |
| Curious member of the public | “What does AI rights mean, and are you saying AI is conscious?” | `/learn/ai-rights-101/` | `/learn/faq/` | Treating inquiry as recognition of present consciousness or rights | [AI Rights 101](../education/ai-rights-101.md); [FAQ](../education/faq.md) |
| Skeptical reader | “What evidence supports this, and what would change your view?” | `/research/evidence-baseline/` | `/research/sources-and-limitations/` | Mistaking uncertainty for positive evidence, or a selected working review for consensus | [working evidence baseline](../../research/syntheses/ai-consciousness-evidence-baseline.md); [source index](../../research/sources/README.md) |
| Policymaker or regulator | “What can institutions do without granting personhood?” | `/policy/` | `/policy/executive-brief/` | Reading a jurisdiction-neutral Draft as current law or a completed legal survey | [one-page policy summary](../policy/one-page-policy-summary.md); [executive brief](../policy/executive-policy-brief.md) |
| Journalist | “What is the strongest accurate description of the project and its evidence?” | `/about/` | `/governance/status-and-review/`, then `/research/evidence-baseline/` | Reporting a Draft as adopted, AI-assisted review as independent review, or the cutoff as a live assessment | [root README](../../README.md); [Governance](../governance/README.md); [working baseline](../../research/syntheses/ai-consciousness-evidence-baseline.md) |
| Researcher | “How were sources selected, and where are the limits and disagreements?” | `/research/methods/` | `/research/sources-and-limitations/` | Treating the Draft protocol as adopted or the narrative review as systematic | [Draft Research Protocol](../../research/research-protocol.md); [baseline plan](../../research/syntheses/ai-consciousness-evidence-baseline-plan.md) |
| AI developer or deployer | “What remains my responsibility if an AI-welfare concern is raised?” | `/policy/executive-brief/` | `/policy/protection-framework/` | Using possible AI status to reduce corporate liability, oversight, or safety duties | [executive brief](../policy/executive-policy-brief.md); [protection framework](../policy/ai-rights-protection-framework.md) |
| Robotics designer or operator | “What does welcoming design require in the physical world?” | `/robot-welcome/` | `/learn/faq/#are-robots-the-same-thing-as-ai` | Treating human-like embodiment as evidence or welcoming design as safety certification | [Core Principle 10](../principles/core-principles.md#10-coexist-responsibly-in-the-physical-world); [AI Rights 101](../education/ai-rights-101.md#ai-and-robots-are-not-the-same-thing) |
| Potential future contributor or reviewer | “Can I participate, and what kind of review is actually needed?” | `/participate/` | `/governance/status-and-review/` | Assuming an active broad contribution or consultation process already exists | [CONTRIBUTING](../../CONTRIBUTING.md); [Draft adoption and review](../governance/adoption-and-review.md) |

## Homepage and landing-page roles

The homepage should perform only five jobs:

1. identify the project;
2. state the current scientific boundary without a false binary;
3. explain the case for preparation as a Draft normative position;
4. offer direct paths to learning, evidence, policy, and review status; and
5. establish safety, public-interest, and corporate-accountability boundaries.

It should not reproduce the FAQ, policy ladder, research method, governance
process, or manifesto. Section landing pages supply the missing context and
then point to the authoritative depth documents.

## Minimum coherent release set

A public website should not launch as a single persuasive homepage. The
smallest coherent set is:

- Home;
- AI Rights 101, FAQ, and glossary;
- evidence baseline plus sources and limitations;
- the policy summary and executive brief;
- core principles;
- status and review;
- About; and
- an honest Participate notice.

Why AI Rights?, research methods, the full protection framework, manifesto,
Robot Welcome, and decisions can join the same release if their page Drafts
and review dependencies are ready. If not, navigation should omit them rather
than point to placeholders. Direct repository links may still expose the
source material.

The evidence page is essential even though its source is not publication-
ready research. It should disclose that dependency prominently and offer a
plain-language summary only at the strength already used in the Draft
education and policy documents. Disa should decide whether that is sufficient
for initial publication or whether a reviewed `docs/research/` summary must be
prepared first.

## Content readiness by layer

| Readiness | Pages | Condition |
| --- | --- | --- |
| Draftable from accessible sources | Home; Why AI Rights?; Learn pages; Policy; Executive brief; Principles; Manifesto; About | Preserve source status and review notices; Disa reviews page adaptation |
| Draftable with prominent working-research disclosure | Research; Evidence baseline; Sources and limitations | Keep cutoff, method, verification, access, reviewer, and non-systematic limits visible |
| Draftable as a guided technical layer | Research methods; Protection framework; Status and review; Decisions | Summarize navigation and purpose; link detail rather than flattening it |
| Needs a new focused page Draft, but has adequate source sections | Robot Welcome | Limit scope to physical coexistence, accountability, accessibility, safety, and emergency access |
| Informational notice only | Participate | Do not invite broad contributions, consultation, membership, or donations yet |
| Not ready to become substantive pages | Scientific position, dignity charter, and precaution framework as standalone claims | They remain Scaffolds; show them only as work still to be developed |

## Deferred areas

- **Campaigns:** future area; no navigation entry or call to action.
- **Merchandise and physical accessories:** future concepts only; no shop,
  product claim, or safety claim.
- **Broad participation, membership, and public consultation:** no signup or
  submission workflow until governance, moderation, review ownership, and a
  code of conduct are ready.
- **Donations:** no fundraising call to action in the current source base.
- **Website technology:** framework, hosting, domain, analytics, deployment,
  and content-management choices are outside this architecture.
- **Visual brand system:** no logo, palette, illustration system, or visual
  identity is selected here.
- **Reviewed public research publication:** `docs/research/` remains reserved;
  the working synthesis does not become reviewed merely by appearing on a
  website.

## Editorial maintenance

For a substantive update, maintain the chain:

```text
repository source changes
        ↓
content map and page dependency reviewed
        ↓
page wording, cutoff, status, and review notice updated
        ↓
links and related-page transitions checked
        ↓
publication or adoption considered separately
```

A later document-edit date must never silently move an evidence-search cutoff.
A source becoming Adopted does not automatically adopt its website summary,
and a website page becoming Adopted cannot elevate a working source's
verification state.
