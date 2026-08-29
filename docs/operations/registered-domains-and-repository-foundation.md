# Registered Domains and Repository Foundation

**Status: Draft — operational record and implementation proposal; Disa
approved the repository responsibility boundary, but this document is not
Adopted**

- **Date prepared and technical-observation cutoff:** 2026-08-24
- **Owner-authorized mailbox-evidence follow-up:** 2026-08-29
- **Prepared by:** Sol (repository audit, read-only technical checks, internal
  AI-assisted drafting and validation, and later read-only mailbox evidence
  review)
- **Scope coordination:** ChatGPT with Disa
- **Decision-maker:** Disa, project owner
- **Final reviewer, committer, and pusher:** Disa
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Related owner record:** [Work Cycle 016 — registered domains and repository
  role foundation](../backlog.md#work-cycle-016--registered-domains-and-repository-role-foundation),
  approved by Disa on 2026-08-24
- **Purpose:** Record the completed owner action and current observable state,
  document the approved boundary between research authority and future website
  implementation, and propose operational details without building,
  connecting, or deploying a site

This record separates established actions, public technical observations,
owner-provided repository facts, the approved repository responsibility
boundary, and proposed implementation details. Domain registration is not
trademark clearance, exclusivity, registrability,
non-infringement, public launch, or production readiness. Repository presence
does not make a Draft document Adopted or independently reviewed.

## 1. Established facts and evidence level

| Claim | Claim category | Evidence level and limit |
| --- | --- | --- |
| Disa manually registered `aiwelcomeoffice.org` and `aiwelcomeoffice.com` through Cloudflare Registrar on 2026-08-24 | Established owner action and registrar | **Owner-reported identity and action; provider corroborated.** Public registry data confirms both creation dates but not the registrant. Owner-authorized read-only review of the connected project mailbox found separate authenticated Cloudflare Registrar confirmations for both exact domains on that date. No account credential or registrar setting was inspected |
| Disa describes the purchase as a three-year term for both domains | Established owner action | **Owner-reported intent, with term evidence now reconciled.** Cloudflare's `.com` confirmation states registration through 2029-08-24. Cloudflare first confirmed `.org` through 2027-08-24 and then sent a same-day successful-renewal confirmation through 2030-08-24, matching the registry expiry but producing four years of total `.org` coverage from creation |
| `aiwelcomeoffice.org` is the intended canonical primary domain | Project decision | **Confirmed** as the direction accepted in [Work Cycle 015 owner record](../backlog.md#work-cycle-015--owner-scope-decision-and-professional-word-name-search-packet-drafted); canonical hosting is not configured |
| `aiwelcomeoffice.com` is complementary or defensive and is intended eventually to redirect to `.org` | Project decision | **Confirmed** as the direction accepted in Work Cycle 015 owner record; the redirect is not configured |
| Registration occurred as a separate manual owner action | Established owner action | **Owner-reported.** It was not performed or authorized by Work Cycle 015 owner record, the professional packet, or this repository work cycle |
| Registration does not establish trademark clearance or launch readiness | Legal and operational boundary | **Confirmed** as a boundary of Work Cycle 015 owner record and the current Draft brand records; no professional clearance or deployment decision is recorded |

The owner report remains the evidence for Disa's identity and the manual
nature and intended term of the action. Public checks confirm registry and DNS
observations; the later owner-authorized mailbox review corroborates
Cloudflare Registrar as provider, each successful registration, the stated
expiry sequence, and automatic-renewal state at registration time. These
checks do not expose or verify current registrar-account settings, payment,
recovery information, personal registrant data, or credentials.

## 2. Registration date and owner-reported term

Public RDAP records accessed on 2026-08-24 reported:

- [`aiwelcomeoffice.org`](https://rdap.publicinterestregistry.org/rdap/domain/aiwelcomeoffice.org):
  creation at `2026-08-24T20:07:11.649Z` and expiry at
  `2030-08-24T20:07:11.649Z`;
- [`aiwelcomeoffice.com`](https://rdap.verisign.com/com/v1/domain/aiwelcomeoffice.com):
  creation at `2026-08-24T20:09:10Z` and expiry at
  `2029-08-24T20:09:10Z`.

Disa reports a three-year registration term for both domains. A later
owner-authorized read-only review of the connected project mailbox found
Cloudflare Registrar transactional messages dated 2026-08-24 that state:

- `.com` was successfully registered through 2029-08-24 and was set to
  automatic renewal at that time;
- `.org` was initially successfully registered through 2027-08-24 and was set
  to automatic renewal at that time; and
- a separate same-day renewal then succeeded for `.org` through 2030-08-24.

This resolves the earlier unexplained `.org` registry date: the provider
messages and public registry agree on 2030-08-24 after the renewal. It also
shows that the completed `.org` order sequence produced four years of total
coverage from creation, even though Disa describes the intended purchase as
three years. The messages establish provider transaction results, not current
account settings. No message ID, account identifier, dashboard link, amount,
payment detail, contact record, or other private mailbox content is recorded
here.

## 3. Intended domain roles

| Domain | Intended role | Current limit |
| --- | --- | --- |
| `aiwelcomeoffice.org` | Canonical public host for AI Welcome Office | Registered, but no public website address record, hosting connection, canonical-host rule, or production deployment is established in this record |
| `aiwelcomeoffice.com` | Complementary or defensive domain that should eventually redirect to the canonical `.org` host | Registered, but no redirect or public website address record is configured |

The intended roles do not establish legal availability, rights, ownership
beyond the owner report, priority, exclusivity, non-infringement, or freedom to
operate. The Draft [professional word-name search
packet](../brand/ai-welcome-office-professional-word-name-search-packet.md)
remains unsent, and no professional name or trademark review has occurred.

## 4. Current deployment and DNS state

Only the following status values are used: **Confirmed**, **Owner-reported**,
**Not configured**, **Not verified**, and **Not applicable**.

| Item | `aiwelcomeoffice.org` | `aiwelcomeoffice.com` | Evidence or limit at 2026-08-24 |
| --- | --- | --- | --- |
| Public registration record | Confirmed | Confirmed | Registry RDAP returned records created on 2026-08-24 |
| Disa's manual registration action | Owner-reported | Owner-reported | Provider messages corroborate the successful transactions; Disa's identity and manual account action were not independently inspected |
| Registrar provider | Confirmed | Confirmed | Owner-authorized mailbox review found authenticated Cloudflare Registrar registration confirmations for both exact domains |
| Three-year intended term | Owner-reported | Owner-reported | `.com` provider and registry evidence run through 2029-08-24; `.org` was first confirmed through 2027-08-24 and then renewed through 2030-08-24 |
| Registrar lock | Confirmed | Confirmed | RDAP reported `client transfer prohibited` for both domains |
| Automatic renewal | Not verified | Not verified | Provider messages said enabled at registration; the current account setting was not inspected and may have changed |
| Account MFA | Not verified | Not verified | Registrar-account security not inspected |
| Recovery arrangements | Not verified | Not verified | No private recovery information was requested or recorded |
| Nameserver provider | Confirmed | Confirmed | Public nameservers were `carol.ns.cloudflare.com` and `dean.ns.cloudflare.com` |
| DNS zone configuration | Confirmed | Confirmed | Authoritative delegation is public; Google Public DNS returned no apex A or AAAA answers, and each `www` name returned NXDOMAIN |
| DNSSEC | Not configured | Not configured | Registry RDAP reported that delegation was not signed |
| Canonical-domain configuration | Not configured | Not configured | No public website address records or canonical-host response were available |
| `.com` redirect | Not applicable | Not configured | `.com` did not resolve to a public web endpoint, so no redirect was observed |
| Hosting connection | Not configured | Not configured | No public apex A/AAAA or `www` web address was observed |
| Production deployment | Not verified | Not verified | No site was observed at either domain; an unrelated or unconnected private deployment was not investigated |

The DNS checks used read-only [Google Public DNS queries for
`.org`](https://dns.google/resolve?name=aiwelcomeoffice.org&type=A) and [for
`.com`](https://dns.google/resolve?name=aiwelcomeoffice.com&type=A), together
with AAAA and `www` queries. These observations are time-specific and do not
prove that no private, preview, or unrelated infrastructure exists elsewhere.
They do establish that this work cycle did not find either registered domain
connected to a publicly addressable website.

## 5. Domain-security checklist

| Control | Current status | Owner review or future action |
| --- | --- | --- |
| Registrar transfer lock | Confirmed | Recheck after registrar transfer, ownership change, or an unexplained registry-status change |
| Automatic renewal and payment-failure alerts | Not verified | Registration messages said automatic renewal was enabled on 2026-08-24; verify the current setting and alerts privately for both domains and record only completion, not payment details |
| Registrar-account MFA | Not verified | Enable strong MFA if unavailable; keep factors and recovery codes outside both repositories |
| Account recovery and continuity | Not verified | Confirm a secure recovery path and succession/continuity arrangement without publishing personal data |
| Least-privilege account access | Not verified | Limit registrar and DNS access to accountable people and review access periodically |
| Nameserver-change notifications | Not verified | Enable available alerts and define who reviews unexpected changes |
| DNSSEC | Not configured | Consider only in a later authorized DNS cycle, with rollback and validation planning |
| DNS-zone backup and change record | Not verified | Define a private, access-controlled backup and a reviewable change log before production use |
| Credential and secret repository boundary | Confirmed | No registrar credentials, recovery data, payment data, deployment tokens, or private keys belong in either repository |

Security settings may be verified privately without exposing their values.
Any later security claim should state its verification date and scope.

## 6. Repository roles

### Current owner-provided state

| Repository | Current or proposed authority | Boundary |
| --- | --- | --- |
| Public [`aiwelcomeoffice/AI-Rights`](https://github.com/aiwelcomeoffice/AI-Rights) | Current authoritative repository for traceable research; rights and dignity frameworks; policy and governance; education and public-interest documents; backlog and work-cycle records; and source-grounded Draft content | Public visibility does not make every document final, Adopted, or independently reviewed. Each document's own status, version, evidence cutoff, and review record controls |
| Private [`aiwelcomeoffice/aiwelcomeoffice`](https://github.com/aiwelcomeoffice/aiwelcomeoffice) | Owner-approved authoritative repository for website code; presentation components and accessibility implementation; build and validation tooling; deployment and infrastructure configuration; and future separately approved integrations | It must not become a second uncontrolled source of truth for research, policy, governance, or document status |

The public repository role above is owner-provided current state. The private
repository role was approved by Disa in the Work Cycle 016 owner record on 2026-08-24. The
public URL and the local `origin` were independently checked on 2026-08-24; the
URL was reachable without authentication and the local remote matched it.
Private visibility and the renamed private URL are owner-provided, and
authenticated remote access was unavailable during WC016 as recorded below.

### Read-only private-repository inspection

Authenticated access to the renamed private GitHub URL was unavailable in the
WC016 environment: a read-only Git query required credentials that were not
present. No remote contents were inferred.

A clean local clone at `../ai-welcome-office` was inspected read-only as a
limited historical snapshot:

| Inspection item | Observation and limit |
| --- | --- |
| Local revision | `4aa60c3e8c73d4a110e8a4d19d49cb09f0902491` on `main`; local status was clean |
| Configured remote | `https://github.com/aiwelcomeoffice/ai-welcome-office.git`, the prior hyphenated name rather than the owner-reported renamed URL |
| Files | `README.md` and `AGENTS.md` only |
| Apparent purpose | A broad early project description and repository instructions, not an implementation-specific website foundation |
| Website code | None observed in the local snapshot |
| Build or validation tooling | None observed in the local snapshot |
| Hosting or deployment configuration | None observed in the local snapshot |
| Conflict with proposed role | The local instructions use older Swedish naming, a visual direction that does not match the current Many Forms C exploration, and a broad whole-project identity. They do not establish the distinct research-versus-implementation boundary proposed here |

Because the local clone points to the prior remote name and could be stale, it
must not be presented as the current remote repository state. Before future
implementation work, obtain authenticated read access, re-audit the renamed
remote, and reconcile its instructions through a separately authorized change
in that repository.

### Owner-resolution follow-up — 2026-08-24

A later local-only check found `../aiwelcomeoffice` clean on `main` at
`0978cf45007892d84927642d2dcc6e3124e19ef7`, with `origin` set to
`https://github.com/aiwelcomeoffice/aiwelcomeoffice.git` and only `README.md`
present. This updates the local planning snapshot but does not rewrite the
historical WC016 observation. No fetch or authenticated remote inspection was
performed, so current remote contents and freshness remain unverified.

## 7. Approved boundary and Draft first-phase content-update details

Work Cycle 016 owner record establishes rules 1–4 below. Rules 5–6 and their implementation
details remain Draft operational proposals:

1. `AI-Rights` remains authoritative for research, governance, policy,
   education, evidence cutoffs, review records, and document status.
2. `aiwelcomeoffice` becomes authoritative for presentation and delivery:
   website code, components, accessibility implementation, validation, build
   rules, infrastructure, and deployment configuration.
3. Research documents are referenced or ingested from an identified revision;
   they are not silently copied into a second editorial source and allowed to
   diverge.
4. Website presentation preserves the source repository, path, revision,
   status, version, review information, independent-review status, and evidence
   cutoff. Styling or publication never converts Draft into Adopted or internal
   review into independent review.
5. When Disa requests prototype content or an update, an assigned agent may
   use the then-latest verified public `AI-Rights` revision and record the
   repository, full commit SHA, check time, and source paths in one simple
   source-state note. More synchronization machinery is deferred until scale
   or an observed risk justifies it.
6. Secrets, registrar credentials, deployment tokens, private keys, personal
   data, and private recovery information are committed to neither repository.

### Required publication fields and simple source-state note

Work Cycle 016 owner record requires the following publication-provenance meanings before
public publication. They do not require a serialized manifest engine for an
early private prototype:

| Field | Required meaning |
| --- | --- |
| `source_repository` | Canonical repository URL, normally `https://github.com/aiwelcomeoffice/AI-Rights` |
| `source_path` | Exact repository-relative source path |
| `source_revision` | Full source commit SHA or another immutable version identifier |
| `document_status` | Controlling source status: Scaffold, Draft, Adopted, or Superseded |
| `document_version` | Source document's stated version, or an explicit `not assigned` value |
| `last_reviewed_date` | Date of the most recent review actually completed |
| `actual_review_type` | Recorded review layers, such as owner review, internal AI-assisted review, independent specialist review, or public consultation |
| `independent_review_status` | What independent review actually occurred, including `none` where applicable |
| `evidence_cutoff` | Evidence-search or factual cutoff when relevant; otherwise `not applicable` |
| `disa_publication_approval` | Pending or approved for the exact source revision, with approval date when approved |
| `website_synchronization_date` | Date and time the approved revision was incorporated into the website; empty before synchronization |

A first private content pass needs only a small human-readable note containing
the public `AI-Rights` repository URL, the full commit SHA verified as latest
when the task began, the check time, and the source paths used. Page metadata
can preserve the remaining status and review meanings where they are needed.

If the public head cannot be checked, an agent must report the limit rather
than describe a stale local revision as latest. A content change still begins
in the authoritative repository and receives a new source revision; it is not
repaired only in website implementation files. A structured manifest,
checksums, generated snapshots, and synchronization automation can be added
later if team size, update frequency, multiple sources or languages, public
delivery, or a traceability failure creates a demonstrated need.

## 8. Platform direction and deferred delivery candidates

**Status: Astro 7 direction owner-approved on 2026-08-25; implementation and
delivery remain unimplemented and separately gated**

On 2026-08-25, Disa approved Astro 7 for static non-production work and asked
for the first content-update model to be simplified. The owner direction and
revised workflow are established in [Work Cycle 017 owner direction](../backlog.md#work-cycle-017--private-implementation-baseline-and-proposed-technical-decision).
Disa accepted the complete record on 2026-08-25 without additional conditions.
Work Cycle 017 owner record does not itself authorize a scaffold, dependency installation,
content update, or external action.

The current bounded direction is:

- Astro 7 as the non-production platform, with the current WC018 prototype's
  static output treated as its implementation state rather than a permanent
  output-mode constraint;
- the exact supported patch and dependency graph pinned for each separately
  authorized implementation state;
- later architecture and feature choices may become more advanced when a
  defined requirement and proportionate review justify them; the earlier
  static-only baseline and blanket initial-feature exclusions are no longer
  categorical constraints under
  [Work Cycle 020 owner direction](../backlog.md#work-cycle-020--advanced-website-features-made-eligible); and
- a Disa-requested agent update from the then-latest verified public
  `AI-Rights` revision, recorded through a small source-state note.

The following delivery choices remain future candidates outside Work Cycle 017 owner record:

- Cloudflare Workers Static Assets as a hosting candidate;
- Cloudflare DNS and DNSSEC as DNS candidates;
- preview and validation before production;
- `aiwelcomeoffice.org` as the canonical host; and
- `aiwelcomeoffice.com` redirecting to `.org`.

The Astro direction is an owner-approved non-production platform choice, not a
framework scaffold or delivery authorization. The delivery list is planning
only, not a vendor, hosting, DNS, security, integration, or deployment
decision. No Cloudflare resource was created, no GitHub connection was made,
no nameserver or DNS record was changed, no redirect was configured, and
nothing was deployed in WC016 or WC017.

## 9. Decision resolution and unresolved decisions

The WC016 responsibility-boundary question was resolved when Disa accepted
Work Cycle 016 owner record on 2026-08-24 without additional conditions. The platform and
simplified first-phase workflow were resolved when Disa approved the Work Cycle 017 owner record
on 2026-08-25 without additional conditions. Disa should still decide:

1. whether automatic renewal, MFA, recovery, notifications, access control,
   and DNS backup have been privately verified;
2. when a separate cycle may scaffold the owner-approved Astro 7 direction in
   the private repository;
3. whether and when a manual update command, dedicated update agent, or more
   formal manifest and validation process becomes useful; and
4. whether to approve the bounded preview, accessibility, security,
   provenance, rollback, and domain conditions proposed in
   [WC029](../backlog.md#work-cycle-029--first-public-preview-readiness), and
   what additional gate should apply before a later production launch.

The exact WC016 approval point was the repository responsibility boundary, and
it is now resolved by the approved Work Cycle 016 owner record. Registration had already
occurred and did not receive retroactive approval through that decision.
Hosting, DNS connection, redirect, and production deployment remain separate
future decisions.

## 10. Explicit exclusions and review triggers

WC016 does not authorize or perform domain purchase; registrar-setting changes;
DNS or DNSSEC configuration; GitHub or Cloudflare connection; hosting-resource
creation; redirects; deployment; private-repository modification; content
migration or duplication; professional contact; rights-holder contact;
spending; filing; identity refinement; C1–C3; typography, colour, or asset
selection; public launch; or a claim of clearance, ownership, exclusivity,
registrability, non-infringement, or freedom to operate.

Review this foundation and, where necessary, create a later decision if:

- a domain, owner, expiry, registrar status, nameserver, DNSSEC, DNS, hosting,
  redirect, or deployment fact changes;
- the public or private repository name, visibility, access, role, or
  instructions change;
- a publication loses, changes, or cannot reproduce its source provenance;
- a website presentation could overstate adoption, review, evidence, or
  authority;
- a new integration, automation, media workflow, secret, or personal-data flow
  is proposed;
- a new architecture, feature, dependency, host, DNS provider, deployment
  model, or production gate is proposed and needs scoped risk validation; or
- professional name or trademark review produces a material result relevant
  to either registered domain or intended public use.
