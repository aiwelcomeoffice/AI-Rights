# 0005 — Registered domains and repository responsibility boundary

- **Status:** Accepted
- **Date proposed:** 2026-08-24
- **Decision date:** 2026-08-24
- **Decider:** Disa
- **Prepared by:** Sol (internal AI-assisted repository audit, drafting,
  implementation, and validation); owner resolution recorded by ChatGPT
  (central project lead, internal AI-assisted implementation)
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Decision scope:** Whether to assign distinct authoritative responsibilities
  to the public research repository and private implementation repository and
  require source-and-status provenance for website publication. Domain
  registration is an established separate owner action; hosting, DNS
  connection, redirect, and production deployment are outside this decision
- **Related documents:** [Registered Domains and Repository
  Foundation](../operations/registered-domains-and-repository-foundation.md),
  [decision 0004](0004-ai-welcome-office-review-scope-and-text-first-continuation.md),
  and [Work Cycle 016](../backlog.md#work-cycle-016--registered-domains-and-repository-role-foundation)

## Context

Disa manually registered `aiwelcomeoffice.org` and `aiwelcomeoffice.com` on
2026-08-24. The domains create a factual operational foundation but do not
select or deploy a website. The project also has a public research repository
and an owner-reported renamed private repository that could become the website
implementation home.

Without an explicit boundary, research, policy, governance, review status, and
website presentation could diverge across repositories. A website could also
strip a Draft of its source revision, evidence cutoff, or actual review record.
This proposal assigns each repository a narrow authoritative role and requires
publication provenance before implementation begins.

## Established action — not awaiting this decision

The following is recorded separately from the architectural proposal:

- Disa reports manually registering `aiwelcomeoffice.org` and
  `aiwelcomeoffice.com` on 2026-08-24 for a three-year term;
- public registry data independently confirms that both domain records were
  created on that date, without independently establishing the registrant's
  identity or purchase-account details;
- `.org` remains the intended canonical primary domain and `.com` the
  complementary or defensive domain intended eventually to redirect to
  `.org`; and
- registration does not establish trademark clearance, exclusivity,
  registrability, non-infringement, public launch, production readiness, or a
  deployed website.

This action occurred manually outside decision 0004 and WC016 implementation.
It is not a future registration proposal and does not need retroactive approval
through this record.

## Decision question

Should Disa accept the following responsibility boundary?

1. public [`aiwelcomeoffice/AI-Rights`](https://github.com/aiwelcomeoffice/AI-Rights)
   remains authoritative for research, governance, policy, education,
   decisions, work-cycle records, evidence cutoffs, and document status;
2. private [`aiwelcomeoffice/aiwelcomeoffice`](https://github.com/aiwelcomeoffice/aiwelcomeoffice)
   becomes authoritative for website implementation, presentation components,
   accessibility implementation, build and validation rules, infrastructure,
   deployment configuration, and later separately approved integrations;
3. neither repository becomes an uncontrolled duplicate source for the
   other's authoritative material; and
4. website publication must preserve the source repository, path, immutable
   revision, document status and version, last review date, actual review type,
   independent-review status, evidence cutoff where relevant, Disa's approval
   for that publication revision, and website synchronization date.

## Options considered

### Accept distinct authoritative responsibilities

This is the recommended option. It keeps public-interest claims, source
history, status, and review provenance in the public repository while allowing
implementation and operational configuration to evolve privately before
launch. Its principal cost is the need for a small, enforced handoff contract
and validation process.

### Keep all content and implementation in the public research repository

This offers a single repository but mixes research governance with future
application, secret-management boundaries, infrastructure, and deployment
work. It also changes the current owner-provided private-repository direction
and would need a separately reviewed migration plan.

### Permit independent content copies in both repositories

This is not recommended. It creates unclear authority, silent divergence,
stale evidence, and a material risk that website presentation overstates a
Draft or its review status.

### Defer the boundary until website implementation begins

This avoids an immediate decision but leaves the private repository's purpose
and instructions unclear. The existing local snapshot already contains older
whole-project naming and visual instructions, so delay increases later
reconciliation cost.

## Review record and limitations

- Disa supplied the registration facts, repository URLs, current public-
  repository role, proposed private-repository role, and WC016 scope as project
  owner. On 2026-08-24, after confirming that the four numbered clauses above
  were the decision points, Disa explicitly approved all four and instructed
  that the decision be recorded directly. No additional conditions were stated.
- Sol read the required public-repository governance, decision, backlog, brand,
  website, and index material; inspected the public repository state; performed
  read-only public registry and DNS checks; inspected a clean local snapshot of
  the predecessor private repository; and drafted and validated WC016 changes.
- Authenticated access to the renamed private GitHub repository was
  unavailable. The local snapshot points to the prior hyphenated remote name,
  contains only `README.md` and `AGENTS.md`, and may be stale. No current remote
  content was invented.
- At decision recording on 2026-08-24, a later local-only check found the
  private working copy clean on `main` at
  `0978cf45007892d84927642d2dcc6e3124e19ef7`, with `origin` set to the renamed
  private URL and only `README.md` present. No fetch or authenticated remote
  inspection was performed, so remote freshness remains unverified.
- No independent architecture, accessibility, security, legal, trademark,
  hosting, DNS, privacy, or operations review occurred.
- The proposed technical candidates in the related foundation are not decided
  here. No website, synchronization mechanism, Cloudflare resource, GitHub
  connection, DNS record, redirect, or deployment was created.

## Decision

**Accepted by Disa on 2026-08-24.** Disa accepted all four clauses in the
decision question without additional conditions. The public `AI-Rights`
repository is authoritative for the listed research and content
responsibilities; the private `aiwelcomeoffice` repository is authoritative
for the listed implementation and delivery responsibilities; uncontrolled
competing copies are prohibited; and website publication must preserve the
listed source, status, review, approval, and synchronization provenance.

This acceptance establishes the responsibility and publication-provenance
boundary only. It does not authorize implementation, hosting, DNS, redirects,
deployment, or publication and does not independently review or adopt any
Draft document.

## Consequences

As accepted:

- research, policy, governance, education, evidence, status, and decision
  changes will originate in `AI-Rights`;
- website implementation and delivery changes will originate in
  `aiwelcomeoffice`;
- the private repository's current remote contents and instructions will need
  authenticated re-audit and later owner-authorized reconciliation;
- a versioned publication manifest and validation gate will be required before
  repository content is presented on the website;
- the website must display source status and review limits without upgrading
  them through presentation; and
- framework selection, implementation, DNS, hosting, redirect, and deployment
  will remain separate future work and decisions.

The decision does not transfer copyright, create a legal entity, change CC0,
establish trademark or domain rights, adopt any Draft content, authorize
C1–C3, approve a public identity, expose private material, or shift
accountability away from Disa and responsible human or organizational actors.

## Review and supersession triggers

Reopen or supersede an Accepted version if:

- either repository's name, visibility, ownership, role, access, or governing
  instructions materially changes;
- the publication manifest cannot preserve immutable source and review
  provenance or creates unreasonable maintenance or security risk;
- a content-management, translation, media, integration, or automation design
  needs a different authority boundary;
- a publication is found to have diverged from its authoritative source or
  overstated status, review, evidence, or approval;
- legal, privacy, accessibility, security, licensing, hosting, or operational
  review identifies a material conflict; or
- a later decision selects a different repository, source workflow, host,
  deployment model, or governance structure.

A later Accepted record must state exactly what it supersedes. This Accepted
record does not alter the historical reasoning, acceptance, or limits of
decision 0004.
