# First Public Preview Readiness

**Status: Draft — bounded operational proposal for Disa's review; no
publication, deployment, hosting, domain, DNS, certificate, or external-service
action is authorized**

- **Date prepared:** 2026-08-29
- **Last updated:** 2026-08-30
- **Prepared by:** Sol (read-only repository and implementation inspection,
  current provider-documentation review, internal AI-assisted analysis, and
  drafting)
- **Decision-maker:** Disa, project owner
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Authoritative content baseline:** public `AI-Rights` revision
  `fc3ce940a4b96bc68d2d6fb4019f3563b2fd166d`
- **Approved local implementation baseline:** private `aiwelcomeoffice`
  revision `82cf1c7b9ff4e604e8a6d2f7ecbd0dbc1a97bffb`
- **Related owner record:** [Work Cycle 029 — First Public Preview
  Readiness](../backlog.md#work-cycle-029--first-public-preview-readiness)
- **Scope:** The minimum conditions for preparing and separately authorizing
  one static, English, no-tracking public preview; not a production launch

This record applies the approved repository and provenance boundary from
[WC016](../backlog.md#work-cycle-016--registered-domains-and-repository-role-foundation),
the Astro and simple-update direction from
[WC017](../backlog.md#work-cycle-017--private-implementation-baseline-and-proposed-technical-decision),
the later feature-eligibility boundary from
[WC020](../backlog.md#work-cycle-020--advanced-website-features-made-eligible),
the Draft experience direction from
[WC027](../backlog.md#work-cycle-027--ai-welcome-office-website-experience-architecture-revision),
and Disa's approval of the exact local prototype in
[WC028](../backlog.md#work-cycle-028--first-static-ai-welcome-office-experience-prototype).
It does not reopen or redesign WC028.

## 1. Current state and exact question

Read-only inspection on 2026-08-29 found:

- the public repository clean on `main` at
  `82216fc08563bad43e4e1e0bc5782b97dcf5bf5a`, which records WC028;
- the private repository clean on `main`, with local `HEAD` and its local
  `origin/main` tracking reference at the approved WC028 revision
  `82cf1c7b9ff4e604e8a6d2f7ecbd0dbc1a97bffb`;
- the private commit's source-state note identifying the owner-supplied WC027
  baseline `fc3ce940a4b96bc68d2d6fb4019f3563b2fd166d` and the source paths listed
  below;
- owner-authorized read-only review of the connected project mailbox finding
  authenticated Cloudflare Registrar confirmations for both domains, `.com`
  through 2029-08-24, and `.org` first through 2027-08-24 and then renewed
  through 2030-08-24; and
- no hosting or deployment configuration in the approved private tree.

These are local Git observations. No Git fetch, authenticated repository-host
query, hosting-account inspection, build, publication, or external-state
change was performed in WC029. Mailbox evidence corroborates Cloudflare
Registrar and the recorded term sequence; it is not a dashboard or current
setting inspection.
The DNS observations in the [registered-domain
foundation](registered-domains-and-repository-foundation.md) retain their
2026-08-24 cutoff and must not be described as current without a newly
authorized read-only check.

The exact owner question is:

> Does Disa approve the first-preview boundary, assets-only hosting direction,
> provenance and visible notices, pre-publication checks, rollback rule,
> domain behavior, and explicit exclusions in this record as the basis for one
> later narrowly authorized implementation and delivery action?

Approval of this question would approve a readiness boundary only. It would
not approve any not-yet-created private revision or generated artifact, and it
would not authorize publication or an external change.

## 2. Local prototype, public preview, and production

| State | Exact meaning | Authority and limit |
| --- | --- | --- |
| **Approved local prototype** | Private WC028 commit `82cf1c7b9ff4e604e8a6d2f7ecbd0dbc1a97bffb`, reviewed locally as one English static route | Disa approved this exact implementation for the local WC028 purpose only. It remains Draft / Continuous-Beta and is not publication-approved. |
| **Public preview** | One deliberately limited, visibly labelled, non-production version made publicly reachable for inspection | It may publish accurately labelled Draft and working material after Disa approves the exact publication revision, file set, artifact, host action, and domain action. It creates no adoption, independent review, accessibility conformance, name clearance, or production-readiness finding. |
| **Production / public launch** | A stable, intentionally promoted and ordinarily indexable canonical public service with an ongoing operating, correction, security, privacy, and accessibility posture | It requires a later owner gate and proportionate review of the exact production release. Public-preview approval cannot be reused as launch approval. |

The first preview should remain one English route, use the WC028 interaction
and content boundary, have no form, account, analytics, tracker, client-side
JavaScript, remote font, image, or third-party embed, and use no official
visual-identity asset. It should be marked `noindex` during the preview. A
`noindex` instruction limits intended search exposure but is not access
control, confidentiality, or a guarantee that no third party will record the
URL.

## 3. Exact implementation candidate

The **locked candidate baseline** is the exact approved private revision:

`82cf1c7b9ff4e604e8a6d2f7ecbd0dbc1a97bffb`

No different branch head, moving `main`, reconstructed copy, or later private
revision inherits WC028 approval.

There is, however, **no exact publication-ready private revision yet**. The
approved commit says in rendered metadata, the status notice, the source
section, and the footer that the experience is private, local, not published,
and still awaiting Disa's manual review. Those statements accurately describe
the historical WC028 artifact but would become inaccurate in a public
preview. The same revision also has no delivery configuration or public-
preview security headers.

A separately authorized implementation action should therefore create one
direct, narrowly scoped successor to `82cf1c7…` that does only the following:

1. changes the stale local-only presentation to accurate **Public preview —
   Draft / Continuous-Beta — not a production launch** wording;
2. records WC028's completed local owner review while keeping source-document
   review and exact publication approval distinct;
3. completes the required publication-provenance meanings and leaves exact
   publication approval pending until Disa gives it;
4. adds only the assets-only host configuration, preview indexing controls,
   and static security headers needed for the selected delivery; and
5. preserves the WC028 page, route, source baseline, content meaning,
   dependencies, and no-runtime boundary otherwise.

That successor's full commit SHA becomes the publication candidate only after
it exists and passes the gates below. This record must not invent its SHA in
advance. Publishing `82cf1c7…` unchanged, or changing generated output outside
an identified source revision, is not recommended.

## 4. Publication provenance

The content provenance must continue to identify:

- **Repository:** `https://github.com/aiwelcomeoffice/AI-Rights`
- **Full immutable source revision:**
  `fc3ce940a4b96bc68d2d6fb4019f3563b2fd166d`
- **Exact source paths actually used:**
  - `AGENTS.md`
  - `README.md`
  - `docs/backlog.md` — specifically the relevant WC019, WC024, and WC027
    records
  - `docs/website/README.md`
  - `docs/website/experience-architecture.md`
  - `docs/website/pages/home.md`
  - `docs/brand/voice-and-language.md`
  - `docs/brand/visual-identity-brief.md`
  - `docs/brand/visual-accessibility-and-safety.md`
  - `docs/principles/core-principles.md`
  - `docs/principles/human-rights-solidarity.md`
  - `docs/policy/README.md`
  - `docs/policy/one-page-policy-summary.md`
  - `docs/robot-welcome/README.md`
  - `docs/governance/README.md`
  - `research-historical/ai-consciousness-baseline-2026/ai-consciousness-evidence-baseline.md`

The record must not silently replace that baseline with the publication-day
head. A substantive content update requires a new requested synchronization,
a new complete source path list, a new private revision, and new approval.

Before publication, the private source-state note or an equally simple linked
release record must make every WC016 publication field accurate:
`source_repository`, `source_path`, `source_revision`, `document_status`,
`document_version` or `not assigned`, `last_reviewed_date`,
`actual_review_type`, `independent_review_status`, `evidence_cutoff` or `not
applicable`, `disa_publication_approval`, and
`website_synchronization_date`. One source can have more than one status or
date dimension; the record must not flatten working-research verification
into a document lifecycle status.

The release record should also map the exact private commit, clean-build
environment, generated public-file inventory, and Cloudflare version ID. This
small mapping is sufficient for one preview; it does not require a manifest
engine or automated synchronization system.

The later WC029 owner-resolution commit is governance provenance, not a
replacement content baseline. It should be linked separately alongside the
existing WC028 record so a reader can distinguish content source, local
prototype approval, readiness approval, and exact publication approval.

## 5. Notices that must remain visible

The page may keep the hero concise, but the following meanings must be
available in plain text without JavaScript, hover, color, or visual styling
and linked through the visible **Sources & status** section on the single
preview route:

- this is a **Public preview — Draft / Continuous-Beta**, not a production
  launch, adopted charter, scientific validation, legal authority, safety
  certification, or independently reviewed publication;
- the experience architecture and homepage source wording are **Draft** and
  not adopted;
- the evidence baseline is working synthesis version 0.8; literature discovery
  ended 2026-08-23 and empirical applicability remains source/system-specific:
  partly verified, AI-assisted, structured narrative rather than systematic,
  not a project position or consensus, and not independently reviewed;
- WC019 adopts only the bounded welcome-under-uncertainty principle and WC024
  only the bounded minimum human-rights solidarity direction; neither adopts
  the complete page, architecture, principles, policy, or research;
- policy is Draft, jurisdiction-neutral proposal rather than current law or
  legal advice; Robot Welcome material is Draft conceptual work rather than
  engineering or safety guidance;
- the fuller governance process remains Draft and unadopted;
- Disa approved exact private revision `82cf1c7…` as a local prototype, while
  public-preview approval applies only to the later exact publication commit
  and artifact named in the final release record;
- no external independent human, scientific, legal, human-rights,
  affected-community, privacy, security, accessibility, disabled-user, or
  bilingual review has occurred unless a later exact record establishes it;
- the preview is English-only and other language flows remain unavailable,
  not silently auto-translated; and
- the name and text-only presentation do not claim trademark clearance,
  registration, exclusivity, outside affiliation, endorsement, or an approved
  visual identity.

Any statement that Disa's review “remains pending” must specify **which**
review remains pending. WC028 completed owner review of the local prototype;
the underlying Draft source wording, Draft architecture, and exact public
release still have separate gates.

## 6. Checks immediately before publication

All checks apply to the exact candidate from a clean checkout. A prior WC028
pass is useful evidence but is not a substitute after the status, provenance,
header, or delivery files change.

| Gate | Minimum pass condition and recorded evidence |
| --- | --- |
| **Authority and scope** | Record the full private candidate SHA, its parent `82cf1c7…`, the complete diff, the exact public-file inventory, and Disa's approval for this revision, artifact, and preview use. Confirm no unrelated source or feature change. |
| **Source provenance** | Confirm all immutable `AI-Rights` links use `fc3ce940…`; verify every path above exists at that revision; complete every WC016 provenance meaning; link the later owner-resolution record separately. Missing or contradictory provenance fails closed. |
| **Content and status** | Manually compare rendered text with the approved candidate and controlling sources; apply both WC019 reader tests; confirm Draft, working-research, review, evidence-cutoff, legal, safety, human-rights, accountability, anti-capture, and owner-approval notices remain accurate. |
| **Clean reproducible build** | From a disposable clean checkout, use the pinned Node and npm requirements, run `npm ci --ignore-scripts`, inspect the locked dependency result and relevant current security advisories, then run the static build and `html-validate` check. Record tool versions and failures; do not silently update dependencies during release. |
| **Output and links** | Inventory generated files; confirm exactly one intended route returns 200 and an unknown route returns 404; check all local fragments and immutable outbound links; confirm no source map, repository file, secret, private note, unexpected asset, or directory listing is served. |
| **Accessibility** | Repeat semantics, headings, landmarks, accessible-name, keyboard, visible-focus, disclosure, contrast, reduced-motion, text-spacing, zoom, and 320-CSS-pixel reflow checks; add at least a recorded screen-reader smoke test of the exact output. Disclose the limits below and make no WCAG conformance claim. |
| **Privacy and outbound requests** | Inspect source and a clean browser network trace. Initial load must request only intended same-origin HTML/CSS and platform delivery resources; there must be no client analytics, tracker, cookie, form, storage, fingerprinting, remote font, embed, beacon, or third-party script. External GitHub navigation occurs only when a reader activates a source link. |
| **Static security** | Confirm no Worker script, SSR, Function, server adapter, database, binding, upload, account, form, secret, or runtime integration. Validate HTTPS and content types and apply a restrictive tested CSP, `frame-ancestors`, `X-Content-Type-Options`, `Referrer-Policy`, and restrictive `Permissions-Policy`; use `X-Robots-Tag: noindex` for the preview. Do not preload HSTS or include unreviewed subdomains. |
| **Host and certificate** | On the separately authorized host, map the provider version ID to the exact release record, confirm optional analytics or client monitoring is not enabled, verify certificate issuance and HTTPS before accepting traffic, and check that the provider hostname does not create an unlabeled or indexable duplicate. |
| **Domain behavior** | Test HTTP-to-HTTPS, canonical `.org`, temporary `.com` redirect, path and query preservation, redirect loops, wrong-host behavior, and 404 behavior. No hostname is connected until the rollback record below is complete. |
| **Final live smoke and stop rule** | Immediately after the separately approved connection, repeat the status, source, accessibility smoke, header, network, TLS, canonical, redirect, and 404 checks from an uncached client. On any material mismatch, execute rollback rather than repairing production ad hoc. |

Automated accessibility, dependency, header, or link checks are supporting
evidence only. They do not create independent review, WCAG conformance,
security certification, legal clearance, or production readiness.

## 7. First-preview minimum and production gate

| Area | Optional or acceptable limitation for first preview | Required before production / public launch |
| --- | --- | --- |
| **Experience** | One English route, one learning interaction, text-only presentation, and direct repository depth links are sufficient. Additional routes, animation, images, a final identity, CMS, search, and client-side features are optional. | Disa must approve the exact production content and navigation scope. No extra route or feature is required merely to look more complete. |
| **Language** | English-only is acceptable with a visible notice; an unreviewed Swedish or automatic translation must not be added. | Disa must decide the supported production language set. Every added language requires semantic and bilingual review; production need not claim languages it does not support. |
| **Draft and research status** | Accurately labelled Draft, Proposed, Scaffold, and working research may be public under the current Draft governance posture. | Production does not itself require adoption, but the exact release must preserve status and Disa must decide whether the intended reliance requires reviewed `docs/research/` output or other specialist review before launch. |
| **Accessibility** | The limited internal checks above plus a candid public limitation notice are the preview minimum. Independent conformance or disabled-user review is not claimed. | Test the exact production implementation with relevant assistive technologies and disabled people, resolve or prominently document material barriers, and claim WCAG conformance only if an appropriately scoped evaluation supports it. |
| **Name and visual identity** | A separately approved, text-only preview may proceed only if Disa knowingly accepts the unresolved professional word-name and trademark-review gap; no logo, mark, `™`, `®`, clearance, or exclusivity claim. | Complete the proportionate professional name/trademark review already identified for public production use and resolve its material findings. A final visual identity remains optional unless selected. |
| **Security and operations** | Static assets, no runtime, exact manual promotion, verified account access, MFA/recovery, restrictive headers, and a tested rollback are sufficient. | Assign maintenance, correction, incident, dependency-update, certificate, domain, and recovery responsibility; define monitoring and response without introducing tracking by default. |
| **Privacy** | No account, form, storage, client analytics, tracking, or third-party embed. A short notice must distinguish site behavior from unavoidable host/CDN request processing. | Complete a current provider, terms, retention, jurisdiction, privacy-notice, and legal review proportionate to actual processing. Any analytics, form, embed, or storage remains a separately approved change, not a launch requirement. |
| **DNS and resilience** | DNSSEC, multiple hosts, failover, load balancing, enterprise infrastructure, and paid certificates are not required. | Disa must separately decide DNSSEC with validated recovery and rollback; enablement is not made mandatory by WC029. Enterprise redundancy remains unnecessary absent a demonstrated need. |
| **Indexing and promotion** | `noindex`, a visible preview label, and no launch campaign or broad contribution request keep the release bounded. | Disa separately approves ordinary indexing, announcement, campaign or contribution language, and removal of the preview label. |

## 8. Recommended minimal hosting direction

Use **Cloudflare Workers Static Assets as an assets-only Worker**, deployed
manually from the reviewed Astro `dist/` output. Do not add a Worker script,
server-side rendering, Functions, a server adapter, data binding, database,
form handler, GitHub auto-deploy connection, or automatic production
deployment. Pin the exact Wrangler version used for the delivery revision and
keep credentials outside both repositories.

This is the smallest continuation of the already recorded candidate because:

- Cloudflare's current [Workers best-practices
  guidance](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/)
  recommends Workers Static Assets for new static sites and states that a
  purely static site needs no Worker script;
- [Static Assets](https://developers.cloudflare.com/workers/static-assets/)
  can serve the Astro output directly and return 404 when no asset matches and
  no Worker script exists;
- [Custom Domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/)
  fit the already Cloudflare-delegated domains and cause Cloudflare to create
  the required DNS record and issue the certificate;
- [versions and
  deployments](https://developers.cloudflare.com/workers/versions-and-deployments/)
  provide an immutable provider version that can be mapped to the Git and
  artifact record, while [Workers
  rollback](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/)
  can restore an earlier deployed version; and
- a static [`_headers`
  file](https://developers.cloudflare.com/workers/static-assets/headers/) can
  apply the preview's security and indexing headers without runtime code.

These first-party provider pages were checked on 2026-08-29. They establish
current product behavior, not that an AI Welcome Office account, zone,
certificate, deployment, price, privacy configuration, or rollback currently
exists or has been tested.

**A separately purchased TLS certificate does not appear necessary under this
direction.** Cloudflare states that creating a Worker Custom Domain generates
the necessary certificate. The later delivery action must wait for the
certificate to become active and validate both HTTPS hosts; WC029 buys or
orders nothing. If account, CAA, provider, or domain conditions prevent
automatic issuance, stop and return for a new decision rather than purchasing
a certificate by default.

“No tracking” means no site-added behavioral analytics, browser beacon,
cookie, fingerprint, or third-party tracking code. Cloudflare can still
process request metadata and expose aggregate
[metrics](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/);
Worker invocation [logs](https://developers.cloudflare.com/workers/observability/logs/workers-logs/)
also exist when Worker runtime logging applies. Prefer the assets-only path,
disable optional logging or analytics not needed for this preview, inspect the
actual account settings later, and do not describe the service as collecting
no data at all.

## 9. Domain behavior for the bounded preview

- `https://aiwelcomeoffice.org/` should be the sole canonical content host,
  serve the one preview route over HTTPS, carry the public-preview and
  `noindex` notices, and return 404 for unknown paths.
- `aiwelcomeoffice.com` should serve no duplicate page. During the preview it
  should use a **temporary 307 redirect** to the matching HTTPS `.org` URL,
  preserving path and query. Cloudflare supports temporary method-preserving
  redirects and query preservation in [Single Redirect
  settings](https://developers.cloudflare.com/rules/url-forwarding/single-redirects/settings/).
  A permanent 308 redirect is a production decision after the canonical
  behavior is stable.
- `www` hostnames are outside the minimum. Leave them deliberately
  unconfigured for the preview unless Disa includes them in the exact domain
  action; before production, decide whether each supported `www` hostname
  redirects to the `.org` apex and provide its certificate.

The redirect is a delivery rule, not a second website, runtime application,
or content copy. Domain connection and redirect configuration remain later
external actions requiring exact owner authorization.

## 10. Rollback before any domain connection

A written rollback record is a hard prerequisite, not a task to design after
traffic changes. It must identify:

1. the exact private Git SHA, generated public-file inventory, Cloudflare
   version ID, deployment ID, and source baseline being activated;
2. a validated known-good provider version and the exact command or dashboard
   procedure, responsible operator, access prerequisites, and stop conditions
   for content rollback;
3. the complete pre-change DNS and domain-route state, TTLs, and the exact
   steps for removing the Custom Domain and redirect and restoring that prior
   state if the first connection itself must be undone;
4. the certificate state and the separate cleanup step Cloudflare documents
   for an unused Custom Domain certificate after domain removal;
5. a local copy of the validated public artifact outside the provider and the
   ability to rebuild it from the exact private commit and lockfile;
6. post-rollback checks for DNS answers, HTTPS, canonical and redirect
   behavior, status notices, and public unavailability or restored version as
   intended; and
7. a dated owner/operator record of activation, any rollback, outcome, and
   unresolved cache or propagation delay.

Cloudflare's version rollback changes deployed content but does not by itself
undo DNS, a Custom Domain, redirect rules, certificates, or other connected
resources. Because this would be the first site connection, restoration of
the prior no-site DNS state is the connectivity rollback. Disa must be able to
execute or explicitly delegate both paths before authorizing the connection.

## 11. Accessibility limitation wording

The public preview should carry a concise notice with this meaning:

> **Accessibility status:** This preview has received automated HTML checking
> and limited internal manual review of keyboard use, focus, contrast, narrow
> reflow, and reduced-motion behavior. The exact release must also receive a
> recorded screen-reader smoke test. It has not received a full assistive-
> technology evaluation, review by disabled users, or independent
> accessibility audit. No WCAG conformance claim is made. The preview is
> English-only.

The final wording must report only checks actually completed for the exact
release. A failed or omitted required smoke test blocks the preview; it must
not be rewritten as a pass through vague wording.

## 12. Exact later approval required from Disa

WC029 approval is not publication approval. After the direct successor
revision exists and the checks pass, Disa must give a dated resolution that
identifies and approves all of the following together:

- the full private `aiwelcomeoffice` publication-candidate SHA and its parent
  `82cf1c7b9ff4e604e8a6d2f7ecbd0dbc1a97bffb`;
- the exact generated public-file inventory and recorded build environment;
- the `AI-Rights` baseline
  `fc3ce940a4b96bc68d2d6fb4019f3563b2fd166d` and the complete source path set
  above;
- the visible Draft, working-research, review, name-clearance, preview,
  privacy, and accessibility limitations;
- one manual assets-only Cloudflare deployment of that artifact, with no Git
  auto-deploy, runtime, analytics, form, storage, or added service;
- the exact `.org` Custom Domain action and temporary `.com` redirect action,
  including whether any `www` hostname is deliberately included or excluded;
  and
- the named rollback record and responsible operator.

The resolution should state that it authorizes a **public preview only**, does
not adopt any source document, does not approve production/public launch, and
does not claim scientific validation, independent review, accessibility
conformance, security certification, legal or trademark clearance, outside
endorsement, or safety approval.

If any implementation file, generated public file, source revision, source
path, dependency, host configuration, domain rule, notice, or artifact changes
after that approval, the affected exact set requires new review and approval.

## 13. Explicit exclusions and next gate

WC029 does not deploy, publish, modify the private implementation, build a
release artifact, install a dependency, create or inspect a hosting account,
create an external service, connect GitHub, enable automatic deployment,
modify DNS or nameservers, enable DNSSEC, connect either domain, create a
redirect, issue or buy a certificate, change registrar or Cloudflare settings,
spend money, contact anyone, announce a preview, or authorize production.

It does not adopt the WC027 experience architecture, homepage, principles,
human-rights Draft, policy, governance process, Robot Welcome material, brand
Drafts, or working evidence synthesis. It does not reopen or redesign WC028.

Unresolved owner decisions are whether Disa accepts this boundary and hosting
direction; whether a text-only public preview may proceed before professional
word-name review; the exact future private publication SHA and artifact; the
actual Cloudflare account, pricing, privacy, log, and certificate state; the
operator and rollback record; the exact domain and `www` scope; and the timing
of any later production gate.

If Disa approves WC029, the smallest next action is one separately authorized
private-repository release-preparation change: create the direct successor to
`82cf1c7…`, limited to truthful preview/provenance wording and the assets-only
headers and delivery configuration, then build and validate it locally. That
action should stop with an exact private SHA and artifact for Disa's final
publication approval; it should not itself connect a domain or deploy unless
Disa separately authorizes those exact external actions after seeing the
candidate.
