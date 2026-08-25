# 0006 — Non-production website platform and simple content updates

- **Status:** Accepted
- **Date proposed:** 2026-08-25
- **Date revised:** 2026-08-25 after Disa's owner direction
- **Decision date:** 2026-08-25
- **Decider:** Disa
- **Prepared by:** Sol with Disa (internal AI-assisted repository audit,
  technical comparison, revision, and validation)
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Decision scope:** Record Disa's approved Astro 7 direction and decide a
  simple first-phase content-update method, minimum local prototype checks,
  and the triggers for a later more formal delivery process
- **Related documents:** [Accepted decision
  0005](0005-registered-domains-and-repository-responsibility-boundary.md),
  [Registered Domains and Repository
  Foundation](../operations/registered-domains-and-repository-foundation.md),
  [Draft public website content architecture](../website/README.md), and [Work
  Cycle 017](../backlog.md#work-cycle-017--private-implementation-baseline-and-proposed-technical-decision)

## Context

[Decision
0005](0005-registered-domains-and-repository-responsibility-boundary.md)
establishes that `AI-Rights` controls research, policy, governance, education,
decisions, evidence boundaries, review records, and document status. The
private `aiwelcomeoffice` repository controls website implementation,
presentation, accessibility implementation, and build and validation rules.
It may present identified source material but must not become a competing
editorial authority.

The first version of this proposal added a manifest schema, per-file
checksums, generated read-only snapshots, separate synchronization roles, and
five detailed gate groups. On 2026-08-25, Disa approved Astro 7 and asked for a
simpler early delivery model: the assigned agent should use the latest
information in the published `AI-Rights` repository when a website update is
requested. A manual trigger or dedicated update agent can be added later. A
more formal process should wait until more humans, agents, sources, languages,
or automation make it useful.

This revision removes the early manifest, checksum, snapshot, and operator
machinery. It keeps a small source record because “latest” is a moving state
and a later reviewer must be able to identify what the agent actually used.
It also preserves decision 0005's publication-provenance requirements without
requiring a particular serialization or automation design now.

In this record, **non-production** means local implementation, static build,
and local preview for review. It does not include an external preview service,
hosting, DNS, redirect, deployment, publication, or public launch.

## Owner direction already received

**Astro 7 is approved by Disa as the non-production website platform
direction.** The later scaffold should:

- use Astro 7 in static-output mode;
- pin the exact supported Astro 7 patch and dependency graph at the separately
  authorized scaffold date;
- start without a client UI framework, server adapter, server-side rendering,
  actions, live content loading, MDX, third-party scripts, or experimental
  Astro features; and
- reopen the choice if Astro 7 is unsupported or a small representative build
  shows disproportionate complexity, accessibility problems, or unacceptable
  dependency risk.

No scaffold or dependency installation is authorized by this recorded
platform approval alone.

## Accepted first-phase workflow

Disa accepted the following simplified first-phase workflow as the rest of
decision 0006:

1. **Use the latest published source when an update is requested.** When Disa
   requests the first prototype content or a later content update, the assigned
   agent performs a current read-only check of the public `AI-Rights` default
   branch and uses that then-latest published revision. The agent records the
   repository URL, full commit SHA, checked date and time, and source paths in
   one small human-readable source-state record. If the current public revision
   cannot be verified, the agent reports that limit and must not describe a
   stale local copy as latest.
2. **Keep authority simple.** Disa's instruction is enough for an assigned
   agent to perform a private non-production content update from that verified
   source. Disa remains the only person who may approve an exact website
   revision for public publication. No recurring automatic synchronization is
   created now. A manual update command or dedicated update agent may be added
   later through a separately reviewed change.
3. **Use minimum local checks.** Before a private prototype or content update
   is handed back for review, require a successful static build, local-link
   check, visible source and status check, basic automated and manual
   accessibility review, secret and personal-data scan, full diff review, and
   a Git-recoverable prior version. These checks establish only local review
   readiness, not publication or production readiness.
4. **Add process only when needed.** Introduce a structured manifest,
   checksums, generated source snapshots, separate approver/operator roles, or
   automated synchronization only when team size, update frequency, multiple
   languages or sources, public delivery, or an observed provenance failure
   justifies the extra process.

Disa explicitly confirmed all four simplified clauses on 2026-08-25 without
additional conditions. Together with her earlier Astro 7 approval, that
confirmation makes the complete record Accepted. It does not by itself
authorize a scaffold, dependency installation, content update, external
service, deployment, or publication.

## Platform comparison retained from the first proposal

This is an internal technical assessment, not a project benchmark or
independent architecture, accessibility, or security review. No framework
guarantees accessible output.

| Criterion | Astro 7, static only | Framework-free static HTML/CSS | Eleventy |
| --- | --- | --- | --- |
| Accessibility | Semantic HTML and shared components can keep navigation, status notices, and landmarks consistent; rendered output still needs automated and human review. | Direct control and no required runtime JavaScript, but repeated status and navigation markup can drift. | Static output with no client JavaScript by default; templates and rendered output still need review. |
| Maintenance | One documented system for routes, layouts, components, build, and preview, at the cost of a larger toolchain. | Smallest initial toolchain, but reusable layout and source handling soon become local scripts or repetition. | A flexible middle option with fewer framework assumptions, but project-specific source and status rules remain necessary. |
| Source handling | Can consume simple local content and metadata without requiring a custom synchronization platform. | Content can be copied directly into pages, but source and status consistency rely more heavily on review. | Handles Markdown and data well, but does not remove the need to record the `AI-Rights` revision actually used. |
| Preview and testing | Standard local development, static build, and preview commands. | Simple browser preview, but multi-page build and test commands must be assembled locally. | Standard static build and local development workflow. |
| Security and dependency risk | Static-only output keeps runtime risk small; Node, Astro, and build dependencies still need pinning and review. | Lowest dependency surface. | Static runtime with an npm build dependency and optional plugin risk. |
| Reversibility | Static output and a small source record are portable; `.astro` templates would need migration. | Highest direct portability. | Good portability through independent template formats and incremental adoption. |

Astro 7 remains proportionate because the website material has shared layouts,
status notices, sources, and routes, while the simplified workflow avoids
building a content-delivery subsystem before it is needed. Framework-free
output remains the lowest-dependency fallback, and Eleventy remains the
relevant generator fallback.

## Simple first-phase source handling

### At the first prototype or a requested update

The assigned agent should:

1. check the public `AI-Rights` default branch read-only at the start of the
   task;
2. record its full commit SHA and the check time;
3. read the relevant current source documents and their statuses;
4. update the private website implementation without independently changing
   research, policy, governance, evidence limits, review descriptions, or
   document status;
5. record the source paths used in one human-readable source-state file; and
6. run the minimum local checks before returning the diff to Disa.

The source-state record is an audit note, not a new content authority. It does
not need a schema version, per-file checksum, generated snapshot tree,
synchronization operator field, or automation system in the first phase.

If `AI-Rights` changes after the recorded check, the current website work is
simply based on the recorded SHA until Disa requests another update. It must
not be called current beyond that recorded synchronization point.

### Before any future public publication

Decision 0005 still requires the published presentation to preserve source
repository, path, immutable revision, document status and version, last review
date, actual review type, independent-review status, relevant evidence cutoff,
Disa's approval for that exact publication revision, and website
synchronization date.

Those meanings may initially be recorded and rendered through simple page
metadata and the source-state note. Decision 0005 does not require WC017 to
build a separate manifest engine. Missing or inaccurate publication
provenance remains a blocker to publication even if a local prototype builds.

## Minimum local review checks

The early private workflow needs only a small, repeatable review set:

- the pinned Astro version installs and produces static output;
- the local preview opens and all local routes and links resolve;
- pages preserve the controlling source status, review limits, evidence cutoff
  where relevant, and a discoverable source reference;
- semantic structure, keyboard navigation, visible focus, reflow, contrast,
  text alternatives, and reduced motion receive proportionate automated and
  manual accessibility checks;
- source and output contain no secret, private personal data, unexpected
  external request, tracking, form submission, third-party script, or remote
  font;
- the complete diff is reviewed for accidental substantive editing; and
- the previous private-repository Git revision remains available as the local
  rollback path.

No formal WCAG conformance, security certification, production rollback test,
or deployment approval may be inferred from these checks. More complete gates
belong in a later public-delivery decision.

## Growth triggers for a more formal delivery cycle

Revisit the simple workflow when any of the following occurs:

- more than one person or agent regularly edits or updates website content;
- a dedicated agent, scheduled job, webhook, or other automatic update path is
  proposed;
- update frequency makes manual source recording unreliable;
- content comes from more than one repository, branch, language, or approval
  stream;
- a public preview, staging environment, deployment, or production release is
  proposed;
- a website revision is stale, cannot be traced, changes source meaning, or
  misses required decision-0005 provenance; or
- audit, accessibility, security, privacy, legal, or operations review needs a
  stronger separation of duties.

At that point, a later decision can add only the controls the observed scale or
risk requires. Possible controls include a structured manifest, checksums,
generated immutable snapshots, review queues, named update roles, and automated
validation. They are deferred, not prohibited.

## Explicitly outside this decision

This record does not authorize a website scaffold, dependency installation,
content update, source copy, external preview, hosting provider, Cloudflare,
DNS, DNSSEC, nameserver change, redirect, TLS configuration, deployment,
publication, production, professional contact, spending, C1–C3, or identity
refinement. Each implementation or external action still needs a separately
scoped instruction from Disa.

## Review record and limitations

- Disa defined WC017's original scope. On 2026-08-25 she explicitly approved
  Astro 7 and directed Sol to simplify the first delivery model so an assigned
  agent uses the latest published `AI-Rights` information, with manual or
  agent-triggered updates and more structure only when collaboration grows.
- Later on 2026-08-25, Disa explicitly confirmed all four simplified workflow
  clauses and instructed that the complete record be marked approved by her.
  No additional conditions were stated.
- Sol revised the proposal to remove the early manifest, checksum, snapshot,
  and separate synchronization-role requirements while retaining the
  responsibility and publication-provenance boundary in decision 0005.
- Before WC017 edits, local `AI-Rights` was clean on `main` at
  `3db4bb86d8cb4df5a5db20ffcff205ffa828da8e`; local `aiwelcomeoffice` was
  clean on `main` at `0978cf45007892d84927642d2dcc6e3124e19ef7`. Both matched
  their locally stored `origin/main` references. No fetch, pull, merge, or
  authenticated remote inspection occurred, so remote freshness remains
  unverified.
- Official technical sources checked on 2026-08-25 remain the [Astro 7.2
  release](https://astro.build/blog/astro-720/), Astro's [configuration
  reference](https://docs.astro.build/en/reference/configuration-reference/),
  Eleventy's [official overview](https://www.11ty.dev/), [WCAG
  2.2](https://www.w3.org/TR/WCAG22/), and W3C WAI's [evaluation
  guidance](https://www.w3.org/WAI/test-evaluate/).
- No candidate was installed, built, benchmarked, or tested with project
  content. No independent human architecture, accessibility, security,
  privacy, content-design, or operations review occurred.

## Decision

**Accepted by Disa on 2026-08-25.** Disa approved Astro 7 as the
non-production platform direction and accepted all four simplified workflow
clauses without additional conditions. The accepted scope is limited to the
platform direction, private first-phase content-update method, minimum local
prototype checks, and triggers for adding a more formal delivery process.
External preview, hosting, DNS, deployment, publication, and production remain
separately gated.

## Consequences

- a later separately instructed cycle may create a minimal Astro 7 static
  scaffold;
- an assigned agent may use the then-latest verified public `AI-Rights`
  revision when Disa requests prototype content or an update;
- one small source-state record replaces an early manifest, checksum, and
  snapshot subsystem;
- Disa remains the only public publication approver, but private implementation
  work does not require separate manifest or per-file approval;
- Git history supplies the early rollback path;
- more formal delivery controls are added only when a recorded growth trigger
  occurs; and
- no external preview, hosting, DNS, deployment, or publication becomes
  authorized.

## Review and supersession triggers

Reopen or supersede an Accepted version if Astro 7 is unsupported or
disproportionate; an agent cannot reliably identify the latest published
source; the simple source record loses traceability; decision 0005 is
superseded; collaboration or automation crosses a growth trigger; or public
preview, hosting, DNS, deployment, or production is proposed.

A later Accepted decision must state exactly what it supersedes rather than
silently expanding this record into production authority.
