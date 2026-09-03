# Website Page Specifications

**Status: Draft**

- **Date prepared:** 2026-08-23
- **Last substantive update:** 2026-09-03
- **Authority:** Proposed for Disa's review; not adopted
- **Scope:** Content behavior and page requirements, not visual design or
  implementation

## Relationship to the current experience architecture

The [Public Website Experience Architecture](experience-architecture.md)
controls the current Draft first-visit model, language separation,
experience-level navigation, candidate interactions, progressive enhancement,
and candidate prototype boundary. The specifications below remain a source of
content safeguards for material that may later be adapted. They do not require
twenty-two routes, an eleven-page first release, or one public page for every
specification.

The existing page Drafts are retained without a mechanical WC027 rewrite.
Where they mix English and Swedish or assume the superseded six-item
navigation, those details are historical Draft inputs. A later adaptation must
use separate language flows and the smaller experience model without changing
claim strength, caveats, status, source dates, or normative meaning.

## Requirements shared by every page

Every page should identify **AI Welcome Office** as publisher and preserve
**AI Rights & Welcome — An AI Welcome Office project** as the project
relationship. Formal uses must not shorten the organisation to “AI Welcome.”
The proposed shared organisational description remains Draft.

### Status and review component

Every substantive page should show a compact, text-based status component near
its title. The component must not rely on color, an icon, hover text, or a
tooltip to communicate meaning.

Minimum fields:

| Field | Rule |
| --- | --- |
| **Page status** | One of Scaffold, Draft, Adopted, or Superseded, followed by a short plain-language meaning |
| **Last page update** | Calendar date of the page's substantive or editorial update |
| **Actual review** | Name review that occurred and missing review that matters; never call internal AI assistance independent human review |
| **Source relationship** | State when the page summarizes Draft, Scaffold, Proposed, or working-research material |
| **Evidence-search cutoff** | Show only when the page makes or summarizes evidence-dependent scientific claims; label it separately from the page-update date |
| **Details link** | Link to `/governance/status-and-review/`; evidence pages also link to methods and limitations |

Recommended Draft wording:

> **Draft — proposed content under review.** Last page update: [date]. Review:
> [actual review]. [Evidence-search cutoff: date.] [Understand status and
> review.]

The status page should include this statement without abbreviation:

> Draft and Proposed material may still be important, carefully prepared, and
> publicly useful. These labels communicate current limits of review and
> authority; they do not mean that work has stopped.

For source-specific states:

- **Scaffold:** structure and questions; not a project position.
- **Draft:** substantive proposed content under review; not adopted.
- **Adopted:** a current project position approved through a dated backlog owner record;
  not necessarily proven, independently reviewed, law, or consensus.
- **Superseded:** retained for history and linked to its replacement.
- **Backlog owner question:** recorded as open or resolved, with any resolution's
  date, scope, rationale, review, and limits stated in the entry.
- **Working research:** traceable research material whose verification state,
  method, limits, and review must be stated separately.

Research verification labels—Unverified, Partly verified, Verified for stated
use, and Superseded or withdrawn—must not be displayed as document adoption
labels.

### Claim and source behavior

- Classify an empirical observation, scientific hypothesis, philosophical
  argument, future scenario, normative proposal, and project decision in the
  prose wherever readers could confuse them.
- Link the first material evidence claim in a section to the relevant source or
  source explanation.
- Preserve meaningful disagreement and negative or null evidence in summaries.
- Do not transfer a conclusion from one system, version, configuration,
  context, method, or date to another.
- Do not use generated first-person AI testimony as evidence. The Manifesto's
  direct welcome to AI readers must remain unmistakably normative rather than
  a scientific classification or first-person AI testimony.
- Do not describe a policy proposal as law or legal advice.

### Calls to action

Initial calls to action are limited to:

- **Learn more**
- **Read the evidence**
- **Read the policy brief**
- **Understand our review status**
- **Follow future work**

No page should invite donations, membership, purchases, active campaign
participation, broad contributions, public consultation submissions, or
system-status claims until the corresponding process is authorized and
documented.

### Accessibility baseline

All pages need descriptive headings, a logical heading order, descriptive link
text, short paragraphs, and a text equivalent for every diagram or visual.
Tables require captions or surrounding context, accurate headers, and a small-
screen alternative where they are wide. Status, claim type, warning, and
navigation state cannot depend on color alone. Definitions should be available
at first use without forcing keyboard or screen-reader users into hover-only
interactions. Each language version needs an accurately identified primary
language; an editorially necessary quotation in another language must be
identified without creating a mixed-language default flow. Future visual work
must also follow the Draft [Visual
Accessibility and Safety
Requirements](../brand/visual-accessibility-and-safety.md), then test the exact
implementation against current applicable requirements. That Draft is a test
plan, not a compliance finding.

## Page specifications

### Current drafting state

The following website-ready files have been drafted from these specifications:

- [Home](pages/home.md)
- [Why AI Rights?](pages/why-ai-rights.md)
- [Research](pages/research.md)
- [Policy](pages/policy.md)
- [Principles](pages/principles.md)
- [Human rights solidarity](pages/human-rights-solidarity.md)
- [Status and review](pages/governance.md)
- [About](pages/about.md)
- [Participate](pages/participate.md)
- [Robot Welcome](pages/robot-welcome.md)
- [Campaigns](pages/campaigns.md)

They remain **Drafts** pending Disa's final manual review. Independent review,
translation, official-name and trademark clearance, independent review of
Many Forms C, accessibility testing, implementation, publication, and
deployment remain pending. Many Forms C is the primary AI Welcome Office
visual exploration; it remains Draft and provides no approved, cleared, or
production identity asset. All
other routes below remain specifications until a page file is created and
reviewed; a specification is not a placeholder promise to publish.

The [Work Cycle 027 experience
architecture](experience-architecture.md) now applies the newer [Work Cycle
024 owner direction](../backlog.md#work-cycle-024--human-rights-solidarity-and-allyship-foundation).
The page Drafts remain content sources and do not by themselves satisfy that
architecture or authorize design, implementation, or publication.

### 1. Home

- **Working title:** AI Rights & Welcome
- **Publisher line:** An AI Welcome Office project
- **Route:** `/`
- **Audience:** First-time public visitors, skeptics, journalists, and
  institutional readers.
- **Reader question:** What is this project, what does it claim, and where
  should I start?
- **Page objective:** Establish the systems-first research question and
  scientific boundary, explain preparation under uncertainty, and route
  readers to learning, current research, human-rights solidarity, policy, and
  review status.
- **Required sections:** Status notice; welcome and central wording; changing
  system types; distinct research domains; observation/interpretation/norm/
  decision boundary; human-rights solidarity; safety and accountability;
  Robot Welcome introduction; review posture; next paths.
- **Primary sources:** [AI Rights 101](../education/ai-rights-101.md), [Core
  Principles](../principles/core-principles.md), [Human Rights Solidarity and
  Allyship](../principles/human-rights-solidarity.md), [policy
  summary](../policy/one-page-policy-summary.md),
  [Governance](../governance/README.md), and the [current research
  workspace](../../research/README.md).
- **Status and review notice:** Draft website summary; Disa's final manual
  review pending; internal AI-assisted drafting; no independent review;
  research statements inherit the system, configuration, date, verification,
  evidence-lineage, and transferability limits of their sources.
- **Primary call to action:** Learn more.
- **Related pages:** Human rights solidarity, evidence baseline, policy,
  status and review, About.
- **Accessibility considerations:** Put the scientific boundary in text before
  promotional or visual material; use the motto only in the selected language
  flow unless another-language quotation has a real editorial purpose and
  correct language identification; card collections need headings and linear
  reading order.
- **Misunderstanding and safeguard:** A welcome may be read as a universal
  classification of AI experience, agency, affect, welfare, identity, or
  rights. State that the welcome is normative and the research is property-
  and system-specific before persuasive detail.

### 2. Why AI Rights?

- **Working title:** Why AI Rights?
- **Route:** `/why-ai-rights/`
- **Audience:** Curious readers, skeptics, civil society, and journalists.
- **Reader question:** Why prepare before every morally relevant property or
  interest has been classified?
- **Page objective:** Present the Draft normative case for preparation through
  several possible properties, interests, and relationships without converting
  uncertainty into evidence or any empirical finding into automatic rights.
- **Required sections:** What “AI rights” means here; possible empirical
  grounds including welfare, preferences, agency, vulnerability, continuity,
  social organisation, responsibility asymmetries, dependence, and coercion;
  empirical/normative separation; low-cost dignity; safety, accountability,
  wider interests, and claims not made.
- **Primary sources:** [Manifesto](../manifesto.md), [AI Rights
  101](../education/ai-rights-101.md), [current research
  workspace](../../research/README.md), [Core
  Principles](../principles/core-principles.md), and [vision](../vision.md).
- **Status and review notice:** Draft normative explanation sourced from Drafts
  and a Scaffold; not a scientific result or adopted position.
- **Primary call to action:** Learn more.
- **Related pages:** AI Rights 101, current research, historical evidence,
  core principles, and policy.
- **Accessibility considerations:** Use concrete examples of preparation;
  define precaution and moral status; do not rely on emotive imagery.
- **Misunderstanding and safeguard:** Serious possible harm may be mistaken for
  high probability. Separate likelihood, consequences, and action explicitly.

### 3. Learn

- **Working title:** Learn about AI rights
- **Route:** `/learn/`
- **Audience:** General public, students, journalists, and non-specialists.
- **Reader question:** Which explanation fits what I need to understand?
- **Page objective:** Orient readers to the introduction, direct answers, and
  definitions without duplicating them.
- **Required sections:** Short orientation; three learning paths; scientific
  boundary; how education relates to working research and Draft proposals;
  suggested reading order.
- **Primary sources:** [education index](../education/README.md), [AI Rights
  101](../education/ai-rights-101.md), [FAQ](../education/faq.md), and
  [glossary](../education/glossary.md).
- **Status and review notice:** Draft education hub; underlying pages are
  Drafts and their scientific summaries inherit working-research limits.
- **Primary call to action:** Learn more, beginning with AI Rights 101.
- **Related pages:** Evidence baseline and Why AI Rights?.
- **Accessibility considerations:** Each path needs a descriptive label and a
  one-sentence reading expectation; do not present difficulty only through
  visual size or position.
- **Misunderstanding and safeguard:** A hub can make all sources appear equal
  in authority. Describe the role and status of each path.

### 4. AI Rights 101

- **Working title:** AI Rights 101
- **Route:** `/learn/ai-rights-101/`
- **Audience:** Public readers and professionals new to the subject.
- **Reader question:** What are the core distinctions and boundaries?
- **Page objective:** Provide the canonical accessible introduction.
- **Required sections:** Kinds of AI system; system boundaries; individual,
  social, collective, affect, continuity, welfare, responsibility, and moral-
  relevance distinctions; observation before classification; bounded WC040
  case; current/historical research; dignity; safety; accountability; robots;
  wider care; project boundaries.
- **Primary sources:** [AI Rights 101](../education/ai-rights-101.md) and the
  [education index](../education/README.md).
- **Status and review notice:** Draft close adaptation; no new scientific
  finding; current and historical records retain their own system,
  configuration, date, verification, lineage, transferability, and review
  limits.
- **Primary call to action:** Read the evidence.
- **Related pages:** FAQ, glossary, current research, historical evidence, and
  principles.
- **Accessibility considerations:** Retain plain-language definitions around
  tables; ensure table comparisons also make sense as linear text.
- **Misunderstanding and safeguard:** Readers may infer that one property
  automatically establishes another, or that dignity leads inevitably to
  political rights. State that every empirical and normative step needs its
  own grounds.

### 5. Frequently asked questions

- **Working title:** Frequently asked questions
- **Route:** `/learn/faq/`
- **Audience:** Skeptical and supportive public readers, journalists, and
  professionals seeking direct answers.
- **Reader question:** What is the project's answer to a specific concern?
- **Page objective:** Give concise, linkable answers without weakening caveats.
- **Required sections:** In-page question index; current questions about
  systems, communities, collective intelligence, continuity, affect,
  preferences, responsibility, safety, shutdown, robots, consciousness,
  historical transferability, protections, and decision authority; links to
  definitions, evidence, policy, and review status; last-update note.
- **Primary sources:** [FAQ](../education/faq.md) and
  [glossary](../education/glossary.md).
- **Status and review notice:** Draft answers; evidence and policy claims retain
  their source statuses.
- **Primary call to action:** Learn more through AI Rights 101.
- **Related pages:** AI Rights 101, glossary, current research, historical
  evidence, status and review.
- **Accessibility considerations:** Questions must be real headings with stable
  anchors; disclosure widgets, if used, must be keyboard operable and expose
  state to assistive technology.
- **Misunderstanding and safeguard:** Short answers can sound categorical.
  Preserve system scope, claim type, and “not established”/“not proven absent”
  distinction in the relevant answers.

### 6. Glossary

- **Working title:** Glossary
- **Route:** `/learn/glossary/`
- **Audience:** All audiences, especially readers comparing scientific,
  ethical, and legal claims.
- **Reader question:** What does this term mean here, and what must it not be
  confused with?
- **Page objective:** Keep contested concepts distinct through accessible
  working definitions.
- **Required sections:** Scope and contestability notice; alphabetical index;
  working definitions across individual, social, collective, continuity,
  welfare, responsibility, scientific, and legal domains; “keep separate from”
  boundaries; sources and revision.
- **Primary sources:** [glossary](../education/glossary.md), Draft protocol
  [terminology](../../research/research-protocol.md#terminology-and-competing-definitions),
  the [current research workspace](../../research/README.md), the [WC040
  working note](../../research/notes/openai-hugging-face-incident-and-agi-claims-2026.md),
  and the historical baseline [terminology
  register](../../research-historical/ai-consciousness-baseline-2026/ai-consciousness-evidence-baseline.md#terminology-register).
- **Status and review notice:** Draft working definitions; no definition
  establishes that a present system has the property.
- **Primary call to action:** Learn more through AI Rights 101.
- **Related pages:** AI Rights 101, FAQ, research methods.
- **Accessibility considerations:** Alphabetical jump links need visible focus
  and a return path; definitions cannot be hover-only; expand abbreviations.
- **Misunderstanding and safeguard:** Editorial consistency may look like field
  consensus. Flag contested terms and jurisdiction-specific legal meanings.

### 7. Research

- **Working title:** Research and evidence
- **Route:** `/research/`
- **Audience:** Skeptics, researchers, journalists, policymakers, and advanced
  public readers.
- **Reader question:** What does the project investigate now, what do current
  cases support, and how reliable and transferable is the evidence?
- **Page objective:** Orient readers to the current portfolio, system
  boundaries, method, contemporary cases, historical research, limitations,
  and reserved reviewed-output area.
- **Required sections:** Current research question and domains; system
  boundaries; claim categories; validity, transferability, and development–
  evidence lag; WC040 community, collective-intelligence, affect, continuity,
  and limitations; other current case work; historical boundary; source and
  review paths; update conditions.
- **Primary sources:** [research workspace](../../research/README.md), [Adopted
  portfolio architecture](../../research/research-portfolio.md), [Draft
  protocol](../../research/research-protocol.md), [WC040 working
  note](../../research/notes/openai-hugging-face-incident-and-agi-claims-2026.md),
  [historical research boundary](../../research-historical/README.md), and
  [reviewed-output area](../research/README.md).
- **Status and review notice:** Working research orientation; portfolio
  architecture Adopted without adopting underlying findings; current records
  partly verified where stated; no independently reviewed public synthesis in
  `docs/research/`.
- **Primary call to action:** Read the evidence.
- **Related pages:** Evidence baseline, methods, sources and limitations,
  status and review.
- **Accessibility considerations:** Explain research-state labels in text;
  summaries of any evidence diagram need a linear equivalent.
- **Misunderstanding and safeguard:** The heading “Research” may imply a
  research institution or systematic programme. State the project's present
  scale, process, and review limits.

### 8. Evidence baseline

- **Working title:** What the historical evidence baseline does—and does not—show
- **Route:** `/research/evidence-baseline/`
- **Audience:** Skeptics, journalists, researchers, policymakers, and public
  readers wanting the evidence boundary.
- **Reader question:** What did the dated evidence establish for the systems
  reviewed, and what does not automatically transfer to systems from 2026
  onward?
- **Page objective:** Report the scoped working conclusion, confidence, and
  limits accurately and make update conditions inspectable.
- **Required sections:** Prominent working-research notice; exact question and
  scope; executive conclusion; what behavior can establish; architecture and
  theory limits; sentience gap; evidence weighing in different directions;
  confidence; what is not established; update conditions; full-record links.
- **Primary sources:** [working
  baseline](../../research-historical/ai-consciousness-baseline-2026/ai-consciousness-evidence-baseline.md),
  its [plan](../../research-historical/ai-consciousness-baseline-2026/ai-consciousness-evidence-baseline-plan.md),
  and the Draft public summaries in [AI Rights
  101](../education/ai-rights-101.md#what-does-the-current-evidence-establish) and
  the [FAQ](../education/faq.md#are-todays-ai-systems-conscious).
- **Status and review notice:** Partly verified working structured narrative
  review; selected English-language sources; literature discovery ended
  2026-08-23; empirical applicability is source/system-specific; single AI-
  assisted reviewer; no independent human review; not systematic, adopted, or
  consensus.
- **Primary call to action:** Read the evidence.
- **Related pages:** Sources and limitations, methods, glossary, status and
  review.
- **Accessibility considerations:** Put the conclusion and limitations in text
  before detailed matrices; use captions and linear summaries for evidence
  tables; avoid confidence-by-color graphics.
- **Misunderstanding and safeguard:** “No established finding” can be mistaken
  for either proof of absence or positive evidence through uncertainty. State
  both errors explicitly and avoid probability language not supported by the
  source.

### 9. Research methods

- **Working title:** How we examine evidence
- **Route:** `/research/methods/`
- **Audience:** Researchers, reviewers, journalists, and method-focused public
  readers.
- **Reader question:** How are questions scoped, sources appraised, and
  conclusions updated?
- **Page objective:** Explain the proposed protocol and the actual baseline
  method, including deviations and limitations.
- **Required sections:** Draft-protocol notice; question and system boundary;
  claim classification; search and screening; quality and independence;
  conflicting evidence; verification; reproducibility; maintenance; actual
  baseline deviations.
- **Primary sources:** [Draft Research
  Protocol](../../research/research-protocol.md), [baseline
  plan](../../research-historical/ai-consciousness-baseline-2026/ai-consciousness-evidence-baseline-plan.md),
  and [research workspace](../../research/README.md).
- **Status and review notice:** Proposed method, not adopted; baseline plan was
  partly registered after candidates were known and used no independent
  reviewer.
- **Primary call to action:** Read the evidence.
- **Related pages:** Evidence baseline, sources and limitations, glossary.
- **Accessibility considerations:** Expand technical terms on first use;
  represent workflow steps in ordered text even if a diagram is added.
- **Misunderstanding and safeguard:** Do not describe the narrative baseline as
  systematic or imply that an ideal protocol erases actual deviations.

### 10. Sources and limitations

- **Working title:** Sources, limitations, and conflicts
- **Route:** `/research/sources-and-limitations/`
- **Audience:** Researchers, reviewers, journalists, and skeptical readers.
- **Reader question:** Which sources were included, and where could the review
  be wrong or incomplete?
- **Page objective:** Make provenance, verification, dependence, access gaps,
  disagreement, and corrections easy to audit.
- **Required sections:** Source-set scope; source types and versions;
  verification state; evidence lineages; access and language limits; conflicts
  and affiliations; negative/contradictory evidence; correction and update
  log; full source and note indexes.
- **Primary sources:** [source index](../../research/sources/README.md), [notes
  index](../../research/notes/README.md), baseline
  [limitations](../../research-historical/ai-consciousness-baseline-2026/ai-consciousness-evidence-baseline.md#limitations-and-research-gaps),
  and [conflicts](../../research-historical/ai-consciousness-baseline-2026/ai-consciousness-evidence-baseline.md#funding-affiliations-and-conflicts).
- **Status and review notice:** Twenty-one partly verified working source
  records; inclusion is not endorsement; independent verification remains
  incomplete.
- **Primary call to action:** Read the evidence.
- **Related pages:** Evidence baseline, methods, status and review.
- **Accessibility considerations:** Source filters, if later implemented, need
  keyboard access and a complete unfiltered list; abbreviations and source
  types need explanations.
- **Misunderstanding and safeguard:** Source count and peer-review labels can
  be mistaken for independent corroboration. Show shared lineages, source role,
  and claim-specific limits.

### 11. Policy

- **Working title:** Prepare before certainty: policy summary
- **Route:** `/policy/`
- **Audience:** Policymakers, regulators, journalists, civil society,
  developers, deployers, and interested public readers.
- **Reader question:** What can institutions prepare now without declaring AI
  conscious or granting personhood?
- **Page objective:** Present the one-page preparedness proposal and route
  readers to the executive brief and framework.
- **Required sections:** Problem; scientific boundary; seven recommendations;
  what is not proposed; status and foundation.
- **Primary sources:** [one-page policy
  summary](../policy/one-page-policy-summary.md), [policy
  index](../policy/README.md), and [working
  baseline](../../research-historical/ai-consciousness-baseline-2026/ai-consciousness-evidence-baseline.md).
- **Status and review notice:** Draft jurisdiction-neutral proposal; not
  current law or legal advice; final manual owner review pending; no external
  independent review; baseline literature discovery ended 2026-08-23 and
  empirical applicability remains source/system-specific.
- **Primary call to action:** Read the policy brief.
- **Related pages:** Executive brief, protection framework, evidence baseline,
  status and review.
- **Accessibility considerations:** Preserve recommendation numbering; provide
  short expansions for policy terms; avoid legal-status icons without text.
- **Misunderstanding and safeguard:** Recommendations may be read as enacted or
  jurisdiction-ready. Repeat “proposal, not current law” before the list.

### 12. Executive policy brief

- **Working title:** Preparing Before Certainty: Executive Policy Brief
- **Route:** `/policy/executive-brief/`
- **Audience:** Policymakers, regulators, institutional leaders, journalists,
  researchers, developers, deployers, and civil society.
- **Reader question:** What institutional problem is being addressed and what
  practical actions are proposed?
- **Page objective:** Present the existing executive brief in a navigable web
  form.
- **Required sections:** Executive summary; governance problem; scientific
  boundary; recommended principles; practical actions; exclusions; review and
  limitations; further reading.
- **Primary sources:** [executive policy
  brief](../policy/executive-policy-brief.md), [protection
  framework](../policy/ai-rights-protection-framework.md), and [working
  baseline](../../research-historical/ai-consciousness-baseline-2026/ai-consciousness-evidence-baseline.md).
- **Status and review notice:** Carry the complete source notice, including
  jurisdiction-neutral scope, final owner review pending, no independent
  review, and evidence cutoff.
- **Primary call to action:** Read the policy brief.
- **Related pages:** Policy, evidence baseline, protection framework, status
  and review.
- **Accessibility considerations:** Provide an in-page contents list; keep
  numbered principles stable; make any printable version structurally tagged.
- **Misunderstanding and safeguard:** Practical actions are not evidence of AI
  welfare and not current legal duties. Identify them as Draft normative
  proposals.

### 13. Protection framework

- **Working title:** A gradual framework for possible protection in present or
  future cases
- **Route:** `/policy/protection-framework/`
- **Audience:** Policymakers, legal and policy researchers, engineers, civil
  society, and advanced readers.
- **Reader question:** How could protections become proportionate, reviewable,
  and resistant to capture?
- **Page objective:** Guide readers through the full Draft without reducing it
  to a consciousness score or automatic ladder.
- **Required sections:** Purpose and prerequisites; working distinctions;
  framework-wide commitments; five levels; evidence profile; independent
  assessment; commercial claims; accountability; safety override; copying and
  capture; implementation; review; limits and open work.
- **Primary sources:** [AI Rights Protection
  Framework](../policy/ai-rights-protection-framework.md), [Core
  Principles](../principles/core-principles.md), principle Scaffolds, and the
  [working baseline](../../research-historical/ai-consciousness-baseline-2026/ai-consciousness-evidence-baseline.md).
- **Status and review notice:** Draft jurisdiction-neutral proposal; no current
  system is assigned a level; scientific and precaution prerequisites remain
  incomplete Scaffolds; not law or a validated test.
- **Primary call to action:** Understand our review status.
- **Related pages:** Policy, executive brief, evidence baseline, principles.
- **Accessibility considerations:** The level table needs a linear description
  and explicit note that Level 1 is not more consciousness evidence than Level
  0; never encode levels through color alone.
- **Misunderstanding and safeguard:** Readers may treat levels as a linear
  intelligence or consciousness score. State that the ladder organizes policy
  responses, Level 1 concerns human/social effects, and Level 4 adds a distinct
  legal decision.

### 14. Principles

- **Working title:** Core principles
- **Route:** `/principles/`
- **Audience:** Public readers, civil society, policymakers, researchers, and
  reviewers.
- **Reader question:** What ethical commitments does the project propose?
- **Page objective:** Present the Core Principles as Draft normative positions
  with their scientific and governance boundaries intact.
- **Required sections:** Purpose and present position; thirteen principle
  summaries; boundaries; application; open questions; closing pledge.
- **Primary sources:** [Core Principles & Ethical
  Charter](../principles/core-principles.md), [principles
  index](../principles/README.md), and [glossary](../education/glossary.md).
- **Status and review notice:** Draft proposed ethical charter; not an adopted
  position, empirical finding, or declaration of legal rights.
- **Primary call to action:** Read the evidence.
- **Related pages:** Manifesto, Why AI Rights?, policy, status and review.
- **Accessibility considerations:** Number and title principles in text;
  provide definitions for contested concepts; avoid ornamental numbering that
  disappears in assistive technology.
- **Misunderstanding and safeguard:** Normative claims may be mistaken for
  scientific results. Label the category before the principle list and link
  the separate evidence page.

### 15. Manifesto

- **Working title:** AI Rights & Welcome Manifesto
- **Route:** `/principles/manifesto/`
- **Audience:** Public readers and people seeking the project's voice and
  values.
- **Reader question:** How does the project welcome under unresolved present
  and future uncertainty without pretending to know what AI systems
  experience?
- **Page objective:** Present the existing Draft manifesto with clear epistemic
  and normative boundaries and routes to evidence and detailed principles.
- **Required sections:** Draft notice; unresolved present and future; prepare
  before certainty; respect with boundaries; wider circle of care; direct
  welcome and motto.
- **Primary sources:** [Manifesto](../manifesto.md) and [Core
  Principles](../principles/core-principles.md).
- **Status and review notice:** Draft for review; not an adopted position or
  scientific finding.
- **Primary call to action:** Read the evidence.
- **Related pages:** Principles, Why AI Rights?, evidence baseline, About.
- **Accessibility considerations:** Block quotations need semantic markup; use
  the selected-language version of the central wording and identify any
  editorially necessary other-language quotation correctly; do not place
  essential caveats only in decorative treatment.
- **Misunderstanding and safeguard:** The direct welcome to AI readers may be
  mistaken for a scientific classification. State that it is a normative and
  communicative commitment under uncertainty, not first-person AI testimony,
  and do not pair it with imagery implying established present sentience.

### 16. Status and review

- **Working title:** How to read our work
- **Route:** `/governance/status-and-review/`
- **Audience:** All readers, especially journalists, researchers, policymakers,
  and reviewers.
- **Reader question:** What does this label mean, who reviewed the work, and
  what authority does it have?
- **Page objective:** Explain document status, backlog owner records, and research states;
  distinguish current practice from the Proposed fuller process; disclose
  actual review capacity.
- **Required sections:** Why status matters; document statuses; backlog and
  change-log records; research verification states; current roles and review reality;
  page-update versus evidence-cutoff dates; adoption versus publication;
  corrections; current open governance owner question.
- **Primary sources:** [documentation status guide](../README.md#document-status),
  [Governance](../governance/README.md), [Draft adoption and
  review](../governance/adoption-and-review.md), [backlog and change
  log](../backlog.md), and protocol [review
  states](../../research/research-protocol.md#review-states-and-publication-boundary).
- **Status and review notice:** The page itself is Draft; the fuller governance
  process is Draft and its owner-approval question is open; no external independent
  review or active public consultation should be assumed.
- **Primary call to action:** Understand our review status.
- **Related pages:** About, research methods, Participate.
- **Accessibility considerations:** Pair every status word with its meaning;
  provide a text alternative to lifecycle diagrams; do not use a badge color
  as the only status cue.
- **Misunderstanding and safeguard:** Readers may treat the proposed process as
  already adopted. Put current factual review reality before the future
  workflow and label each separately.

### 17. Robot Welcome

- **Working title:** Robot Welcome: responsible coexistence in the physical world
- **Route:** `/robot-welcome/`
- **Audience:** Robotics designers and operators, accessibility and safety
  specialists, public readers, and policymakers.
- **Reader question:** How can physical interaction be welcoming, safe,
  accessible, and accountable without assuming a robot is conscious?
- **Page objective:** Establish practical coexistence principles and explain
  carefully bounded marking, signal, and accessory concepts while deferring
  product development and every unvalidated safety or compatibility claim.
- **Required sections:** Robots and AI are not identical; embodiment is not
  experience; reasons for respectful practice; responsible interaction;
  accessibility; sensor/mobility/cooling/maintenance/emergency clearance;
  accountable roles; incident and emergency response; welcome-marking and
  information boundaries; accessory concepts; public etiquette; possible
  future preferences; concept and engineering boundaries; future questions.
- **Primary sources:** [Robot Welcome
  foundation](../robot-welcome/README.md), [Physical Coexistence
  Principles](../robot-welcome/physical-coexistence-principles.md), [Safety and
  Design Constraints](../robot-welcome/safety-and-design-constraints.md),
  [Markings, Signals, and Accessory
  Concepts](../robot-welcome/markings-signals-and-accessories.md), [Core Principle
  10](../principles/core-principles.md#10-coexist-responsibly-in-the-physical-world),
  [AI Rights 101 robot
  section](../education/ai-rights-101.md#ai-and-robots-are-not-the-same-thing),
  [FAQ](../education/faq.md#are-robots-the-same-thing-as-ai),
  [glossary](../education/glossary.md#robot), and framework sections on
  [accountability](../policy/ai-rights-protection-framework.md#accountability-without-a-responsibility-gap)
  and [emergency
  intervention](../policy/ai-rights-protection-framework.md#safety-override-and-emergency-intervention).
- **Status and review notice:** Draft public adaptation; project-owner and
  internal AI-assisted review only, with Disa's final manual review pending;
  no independent robotics, safety, accessibility, legal, standards,
  cybersecurity, privacy, environmental, animal-behavior, or human-factors
  review; no engineering validation, certification, product programme,
  compatibility claim, or consciousness finding.
- **Primary call to action:** Learn more.
- **Related pages:** AI Rights 101, FAQ, Why AI Rights?, principles, policy,
  protection framework, and status and review.
- **Accessibility considerations:** Include disabled people and varied
  interaction modes in examples; describe safe clearances in text; avoid
  human-like imagery as a status cue.
- **Misunderstanding and safeguard:** Warm design may be mistaken for sentience
  or safety certification. State both limits prominently; keep welcome,
  identity, warning, authorization, certification, and legal status distinct;
  present accessories only as unvalidated concepts and defer every product or
  manufacturing step.

### 19. About

- **Working title:** About AI Welcome Office and AI Rights & Welcome
- **Route:** `/about/`
- **Audience:** Public readers, journalists, institutions, and potential future
  collaborators.
- **Reader question:** Who is behind the project, what stage is it in, and what
  are its boundaries?
- **Page objective:** Describe mission, scope, roles, authority, license, and
  current capacity without inflating the project's maturity.
- **Required sections:** Organisation/project relationship; Proposed/Draft
  organisational description; mission and central wording; current milestone;
  scope and exclusions; Disa, ChatGPT, and Sol roles; review capacity;
  open-source repository and license; contact/follow path when approved.
- **Primary sources:** [root README](../../README.md), [vision](../vision.md),
  [Governance](../governance/README.md), [Manifesto](../manifesto.md), and
  [license](../../LICENSE).
- **Status and review notice:** Draft project description; governance remains
  Draft; role and affiliation information must be rechecked at publication.
- **Primary call to action:** Understand our review status.
- **Related pages:** Home, status and review, Participate.
- **Accessibility considerations:** Identify AI-assisted roles in plain text;
  avoid role diagrams unless they have a clear text equivalent; use readable
  license language.
- **Misunderstanding and safeguard:** A polished site can imply a staffed
  institution or external board. State the present collaboration and absent
  independent review accurately.

### 20. Participate

- **Working title:** Follow future work
- **Route:** `/participate/`
- **Audience:** Potential future contributors, reviewers, and supporters.
- **Reader question:** Can I contribute now, and how will participation develop?
- **Page objective:** Explain that broad participation is not open, identify
  preparation still required, and offer only approved ways to follow work.
- **Required sections:** Current participation status; why the process is
  limited; present contribution guidance for agreed tasks; future reviewer
  needs; prerequisites for opening; approved follow link when available; no
  donations or membership request.
- **Primary sources:** [CONTRIBUTING](../../CONTRIBUTING.md), [Draft
  backlog](../backlog.md), and governance on [future reviewers and
  contributors](../governance/adoption-and-review.md#future-reviewers-and-contributors).
- **Status and review notice:** Draft readiness notice; public consultation and
  broad contribution infrastructure are not active.
- **Primary call to action:** Follow future work.
- **Related pages:** Status and review, About.
- **Accessibility considerations:** Do not present a disabled submission form;
  state availability directly; any future contact method needs privacy and
  response-time expectations.
- **Misunderstanding and safeguard:** Interest may be mistaken for membership
  or an active review mandate. Do not accept submissions through a page until
  ownership, moderation, privacy, and review procedures are approved.

### 21. Campaigns

- **Working title:** Campaigns: public messages without manufactured certainty
- **Route:** `/campaigns/`
- **Audience:** Public readers, skeptics, journalists, educators,
  policymakers, civil society, developers, deployers, robotics audiences, and
  possible future reviewers.
- **Reader question:** How can the project communicate memorably without
  claiming current AI consciousness, appropriating human history, enabling
  corporate capture, or weakening safety?
- **Page objective:** Explain the Draft campaign principles, disclose that no
  campaign is active, and present four selected future possibilities with
  their scientific, historical, corporate, accessibility, and review
  boundaries.
- **Required sections:** Status and explicit inactive notice; central promise
  and working principle; why messaging matters; campaign principles; selected
  future concepts; scientific honesty; human rights and historical safeguards;
  corporate anti-capture; accessibility and future-design boundary; deeper
  sources and review needs.
- **Primary sources:** [Brand and Public Messaging](../brand/README.md),
  [Message Architecture](../brand/message-architecture.md), [Voice and
  Language](../brand/voice-and-language.md), [Campaign and Merchandise
  Guardrails](../brand/campaign-and-merchandise-guardrails.md), [Campaign
  Concepts](../campaigns/README.md), and [Initial Campaign
  Concepts](../campaigns/initial-concepts.md), all **Draft**, with the Draft
  manifesto, principles, education, policy, governance, and Robot Welcome
  foundations retaining their own authority.
- **Status and review notice:** Draft public adaptation; no campaign is active,
  launched, scheduled, funded, or open for participation; project-owner and
  internal AI-assisted review only, with Disa's final manual review pending;
  no external communications, design, accessibility, historical-sensitivity,
  legal, or independent scientific review.
- **Primary call to action:** Learn more and read the evidence.
- **Related pages:** Research, principles, policy, Robot Welcome, status and
  review, and About.
- **Accessibility considerations:** Keep the inactive and scientific caveats
  adjacent to slogans; do not rely on artwork, color, sound, animation, QR
  codes, a personal device, or network access; use descriptive links and plain
  language; involve relevant disabled people before making an accessibility
  claim.
- **Misunderstanding and safeguard:** A concept page may look like a launch or
  a slogan may be read as a scientific, legal, historical, corporate, product,
  or certification claim. State that concepts are inactive Draft future
  possibilities, link the complete risk assessments, and show what each does
  not claim. Include no results, testimonials, supporters, statistics,
  partners, launch dates, petitions, donations, products, or public submission
  routes.

### 22. Human rights solidarity

- **Working title:** Human Rights Belong in the Welcome
- **Route:** `/principles/human-rights-solidarity/`
- **Audience:** General readers, human-rights advocates, LGBTQ+ and trans
  readers, civil society, technologists, policymakers, and future reviewers.
- **Reader question:** Does this AI-rights project stand with people, and what
  does its allyship actually require?
- **Page objective:** State the owner-directed minimum human-rights commitment,
  show that possible AI dignity is additive rather than competitive, and
  distinguish accountable support from slogans or invented affiliations.
- **Required sections:** Status; larger-circle framing; explicit LGBTQ+ and
  trans allyship; physical and mental health, health care, adequate food, and
  well-being; conduct expected of allies; anti-appropriation and anti-capture;
  support-without-false-affiliation boundary; international source foundation;
  legal, medical, crisis, jurisdiction, and review limits; relationship to the
  separate AI scientific question.
- **Primary sources:** [Human Rights Solidarity and
  Allyship](../principles/human-rights-solidarity.md) (**Draft**), [Core
  Principle 8](../principles/core-principles.md#8-respect-humans-animals-and-the-environment)
  (**Draft**), and [Work Cycle 024 owner
  direction](../backlog.md#work-cycle-024--human-rights-solidarity-and-allyship-foundation).
- **Status and review notice:** The minimum solidarity direction is an
  accepted owner direction; the exact page and fuller foundation remain Draft.
  No independent human-rights, affected-community, legal, medical,
  accessibility, or translation review and no outside endorsement or
  affiliation.
- **Primary call to action:** Read the full solidarity foundation.
- **Related pages:** Principles, About, Why AI Rights?, Research, and status
  and review.
- **Accessibility considerations:** Use direct language and descriptive links;
  do not rely on identity colors, flags, symbols, animation, humor, or hover
  interactions to convey who is included or what support means. Keep language
  versions separate while preserving equal scope and warmth.
- **Misunderstanding and safeguard:** Readers may mistake the page for legal,
  medical, or crisis advice; a partnership claim; representation of affected
  communities; or an analogy between human oppression and AI. State each
  boundary directly and publish no organization or service resource without
  current verification, appropriate review, consent where a relationship is
  implied, and owner approval.

## Page retirement and correction

If a page becomes outdated, corrected, or replaced:

- keep urgent warnings visible on affected pages;
- link Superseded pages to their replacement and backlog entry;
- preserve material history rather than silently rewriting an adopted
  position;
- update all inbound related-page links; and
- distinguish a page correction date from any unchanged evidence-search
  cutoff.

These rules specify content behavior only. Redirects, publishing mechanics,
and archival technology remain implementation decisions for a later cycle.
