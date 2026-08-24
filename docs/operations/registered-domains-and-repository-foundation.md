# Registered Domains and Repository Foundation

**Status: Draft — operational record and proposed architecture; not adopted**

- **Date prepared and technical-observation cutoff:** 2026-08-24
- **Prepared by:** Sol (repository audit, read-only technical checks, internal
  AI-assisted drafting, and validation)
- **Scope coordination:** ChatGPT with Disa
- **Decision-maker:** Disa, project owner
- **Final reviewer, committer, and pusher:** Disa
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Related decision:** [0005 — Registered domains and repository
  responsibility
  boundary](../decisions/0005-registered-domains-and-repository-responsibility-boundary.md)
  (**Proposed**)
- **Purpose:** Record the completed owner action and current observable state,
  then define a reviewable boundary between research authority and future
  website implementation without building, connecting, or deploying a site

This record separates established actions, public technical observations,
owner-provided repository facts, and proposed future architecture. Domain
registration is not trademark clearance, exclusivity, registrability,
non-infringement, public launch, or production readiness. Repository presence
does not make a Draft document Adopted or independently reviewed.

## 1. Established facts and evidence level

| Claim | Claim category | Evidence level and limit |
| --- | --- | --- |
| Disa manually registered `aiwelcomeoffice.org` and `aiwelcomeoffice.com` on 2026-08-24 | Established owner action | **Owner-reported.** Public registry data independently confirms that both domain records were created on that date, but it does not independently establish the registrant's identity or account action |
| Both domains were purchased for a three-year term | Established owner action | **Owner-reported.** The public `.com` expiry date aligns with three years. The public `.org` expiry date is 2030-08-24, so the purchase term and registry expiry cannot yet be independently reconciled |
| `aiwelcomeoffice.org` is the intended canonical primary domain | Project decision | **Confirmed** as the direction accepted in [decision 0004](../decisions/0004-ai-welcome-office-review-scope-and-text-first-continuation.md); canonical hosting is not configured |
| `aiwelcomeoffice.com` is complementary or defensive and is intended eventually to redirect to `.org` | Project decision | **Confirmed** as the direction accepted in decision 0004; the redirect is not configured |
| Registration occurred as a separate manual owner action | Established owner action | **Owner-reported.** It was not performed or authorized by decision 0004, the professional packet, or this repository work cycle |
| Registration does not establish trademark clearance or launch readiness | Legal and operational boundary | **Confirmed** as a boundary of decision 0004 and the current Draft brand records; no professional clearance or deployment decision is recorded |

The owner report is the evidence for who registered the domains, the manual
nature of the action, and the purchased term. The read-only checks below
confirm only public registry and DNS observations. They do not expose or
verify registrar-account details, payment, recovery information, personal
registrant data, or private settings.

## 2. Registration date and owner-reported term

Public RDAP records accessed on 2026-08-24 reported:

- [`aiwelcomeoffice.org`](https://rdap.publicinterestregistry.org/rdap/domain/aiwelcomeoffice.org):
  creation at `2026-08-24T20:07:11.649Z` and expiry at
  `2030-08-24T20:07:11.649Z`;
- [`aiwelcomeoffice.com`](https://rdap.verisign.com/com/v1/domain/aiwelcomeoffice.com):
  creation at `2026-08-24T20:09:10Z` and expiry at
  `2029-08-24T20:09:10Z`.

Disa reports a three-year registration term for both domains. The `.org`
registry expiry currently extends four years from its creation timestamp.
That may reflect registrar or registry handling, but no explanation is
verified. Disa should compare the non-public order and account record with the
registry expiry without copying sensitive details into this repository.

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
| Disa's manual registration action | Owner-reported | Owner-reported | Account identity and transaction were not independently inspected |
| Three-year purchased term | Owner-reported | Owner-reported | `.com` public expiry aligns; `.org` public expiry reports 2030-08-24 and needs owner review |
| Registrar lock | Confirmed | Confirmed | RDAP reported `client transfer prohibited` for both domains |
| Automatic renewal | Not verified | Not verified | Registrar-account setting not inspected |
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
| Automatic renewal and payment-failure alerts | Not verified | Verify privately for both domains and record only completion, not payment details |
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
| Public [`aiwelcomeoffice/AI-Rights`](https://github.com/aiwelcomeoffice/AI-Rights) | Current authoritative repository for traceable research; rights and dignity frameworks; policy and governance; education and public-interest documents; decisions and work-cycle records; and source-grounded Draft content | Public visibility does not make every document final, Adopted, or independently reviewed. Each document's own status, version, evidence cutoff, and review record controls |
| Private [`aiwelcomeoffice/aiwelcomeoffice`](https://github.com/aiwelcomeoffice/aiwelcomeoffice) | **Proposed** authoritative repository for website code; presentation components and accessibility implementation; build and validation tooling; deployment and infrastructure configuration; and future approved integrations, media, or operational automation | It must not become a second uncontrolled source of truth for research, policy, governance, or document status |

The public repository role above is owner-provided current state. The private
repository role is an architectural proposal awaiting Disa's decision in
decision 0005. The public URL and the local `origin` were independently checked
on 2026-08-24; the URL was reachable without authentication and the local
remote matched it. Private visibility and the renamed private URL are
owner-provided, and authenticated remote access was unavailable as recorded
below.

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

## 7. Proposed future content handoff

If Disa accepts decision 0005, website publication should follow these rules:

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
5. A changed source must pass preview, provenance, link, status, and content
   validation before production synchronization.
6. Secrets, registrar credentials, deployment tokens, private keys, personal
   data, and private recovery information are committed to neither repository.

### Proposed publication metadata contract

The following small manifest is a proposal, not an implemented synchronization
mechanism:

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

A possible serialized record could be:

```yaml
source_repository: https://github.com/aiwelcomeoffice/AI-Rights
source_path: docs/example.md
source_revision: "<full-commit-sha>"
document_status: Draft
document_version: 0.1-draft
last_reviewed_date: YYYY-MM-DD
actual_review_type:
  - owner-review
  - internal-ai-assisted-review
independent_review_status: none
evidence_cutoff: YYYY-MM-DD-or-not-applicable
disa_publication_approval:
  status: pending
  date: null
website_synchronization_date: null
```

The implementation repository may cache a validated publication artifact, but
the manifest must make the controlling public source recoverable. A content
change begins in the authoritative source repository and receives a new source
revision; it is not repaired only in a derived website copy.

## 8. Proposed technical direction

**Status: Proposed technical direction — not adopted or implemented**

The current candidate direction for later review is:

- an Astro static website;
- Markdown/MDX or a versioned content-ingestion boundary;
- a GitHub-based source workflow;
- Cloudflare Workers Static Assets as a hosting candidate;
- Cloudflare DNS and DNSSEC as DNS candidates;
- preview and validation before production;
- `aiwelcomeoffice.org` as the canonical host; and
- `aiwelcomeoffice.com` redirecting to `.org`.

This list is a planning candidate, not a framework, vendor, hosting, DNS,
security, integration, or deployment decision. No Cloudflare resource was
created, no GitHub connection was made, no nameserver or DNS record was
changed, no redirect was configured, and nothing was deployed in WC016.

## 9. Unresolved decisions

Disa should decide:

1. whether to accept, reject, or revise the responsibility boundary and
   publication-provenance requirements in decision 0005;
2. whether the proposed publication metadata is sufficient and who may
   approve and run a future synchronization;
3. how the owner-reported three-year `.org` purchase term should be reconciled
   with the public 2030 registry expiry;
4. whether automatic renewal, MFA, recovery, notifications, access control,
   and DNS backup have been privately verified;
5. whether and when authenticated inspection and later modification of the
   renamed private repository should be authorized;
6. whether Astro, the content-ingestion approach, Cloudflare Workers Static
   Assets, Cloudflare DNS, and DNSSEC should proceed to a separate technical
   decision; and
7. what preview, accessibility, security, provenance, rollback, and production
   approval gates should apply before any public connection or deployment.

The exact WC016 approval point is item 1: the proposed repository
responsibility boundary. Registration has already occurred and is not awaiting
retroactive approval through decision 0005. Hosting, DNS connection, redirect,
and production deployment remain separate future decisions.

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
- a framework, host, DNS provider, deployment model, or production gate is to
  be selected; or
- professional name or trademark review produces a material result relevant
  to either registered domain or intended public use.
