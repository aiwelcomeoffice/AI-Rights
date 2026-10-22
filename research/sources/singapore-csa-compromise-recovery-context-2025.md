# Source Record: Singapore CSA compromise-recovery guidance

- **Record ID / status:** SRC-PHP2SHELL-2026-11; Partly verified Draft
- **Protocol version:** 0.6-draft
- **Created / updated / accessed / status checked:** 2026-10-22
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted research intake)
- **Reviewed by:** Not yet independently reviewed

## Bibliographic record and inclusion

- **Title:** Remediation Guide for a Compromised SharePoint Environment related to CVE-2025-53770 and CVE-2025-53771
- **Author / issuing authority:** Cyber Security Agency of Singapore (CSA)
- **Publication date:** 2025-07-24
- **Original:** <https://www.csa.gov.sg/alerts-and-advisories/advisories/ad-2025-016/>
- **Version:** Live English advisory accessed 2026-10-22; immutable revision not pinned.
- **Source type / peer review:** Official operational recommendations; not an empirical AI study or independent scholarly review.
- **Correction status:** Page describes a developing situation; no separate correction notice observed in the inspected sections. Revision history unverified.
- **Disposition:** Contextual guidance for the [PHP2Shell addendum](../notes/php2shell-ai-assisted-vulnerability-discovery-2026-10-21.md#retrospective-compromise-persistence-and-cryptographic-key-exposure); not evidence of PHP2Shell incidents, RSA-key theft or current AI capability.

## Source report and critical appraisal

**Locators:** Executive Summary; Phases 1–4 of the Structured Incident Response Plan. CSA distinguishes patching from removing persistence, replacing exposed secrets and restoring system integrity. The note uses these response distinctions, not SharePoint-specific commands or incident counts.

**Evidence profile:** Direct for CSA's published recommendations; indirect for PHP response. Documentary method is adequate for attribution; effectiveness, completeness and replication are not assessed. This is institutional guidance, not a causal experiment. CSA controls publication; underlying incident reporting includes secondary sources and was excluded from evidential use. No funding audit or independent validation was performed. The guidance's strong rebuild assurance is not adopted as a guarantee. Portability is limited to general recovery reasoning; mechanisms and product-specific procedures differ.

**Temporal applicability:** A 2025 non-AI response document used as contextual guidance in 2026; access date does not refresh its incidents or establish present PHP compromise. No AI model/version fields apply.

## Verification and review log

**Discovery / screening, 2026-10-22:** Web queries were `site.cisa.gov web shells patching rebuild credentials incident response persistent access`, `site:cisa.gov web shells patching rebuild credentials incident response persistent access`, `site:cisa.gov "Federal Government Cybersecurity" "Rebuild" "credentials" playbooks`, and `site:cisa.gov "Federal Government Cybersecurity" "Playbooks" 2021`. The first query's malformed site expression provided no reliable domain restriction. CSA was included for its original recommendations. The CISA playbook and AA20-245A were inaccessible (403); Microsoft and NSA background accounts were not used as additional evidential support. Unrelated search hits and secondary incident claims were excluded.

2026-10-22, Codex: title, date, issuing authority and scoped recommendations checked. **TODO: verify:** immutable revision, later corrections and environment-specific applicability before operational reliance. No incident investigation, recovery action or independent security review occurred.
