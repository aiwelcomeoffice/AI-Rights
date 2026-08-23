# Visual Accessibility and Safety Requirements

**Status: Draft**

- **Date prepared:** 2026-08-23
- **Authority:** Proposed for Disa's review; not adopted
- **Scope:** Future identity, website, document, campaign, merchandise, and
  Robot Welcome visual requirements; no compliance, compatibility, product,
  installation, or safety claim
- **Review:** Project-owner and internal AI-assisted review only; Disa's final
  manual review is pending; no external independent accessibility, disabled-
  user, cultural, legal, standards, human-factors, robotics, engineering, or
  manufacturing review

> **Requirements notice:** These are design and test requirements, not proof
> that any current or future asset is accessible, safe, compliant, compatible,
> or approved. Claims may be made only for a defined implementation, context,
> test method, result, standard or requirement, version, reviewer, and date.

## Purpose and precedence

The identity should help people recognize the project without making anyone
depend on sight, color perception, fine detail, motion tolerance, a particular
language, a personal device, or a network connection for essential meaning.
Accessibility must shape concept selection rather than be added after a logo
has been chosen.

For digital use, the target should be the current applicable accessibility
requirements identified for the actual jurisdiction and service. At the date
of this Draft, the project uses [WCAG 2.2](https://www.w3.org/TR/WCAG22/) as a
primary web design and testing reference and intends to test future public web
implementations against Level AA at minimum. The W3C advises using WCAG 2.2
for future applicability, but the applicable legal and contractual baseline
still needs jurisdiction-specific review.

This document does not replace:

- the [Website Page Specifications](../website/page-specifications.md), which
  define accessible content and status behavior;
- the [Campaign and Merchandise
  Guardrails](campaign-and-merchandise-guardrails.md), which govern public and
  product concepts; or
- the complete [Robot Welcome Safety and Design
  Constraints](../robot-welcome/safety-and-design-constraints.md), which take
  precedence for any robot-related physical concept.

## Core requirements

Every future identity application should meet these principles:

1. **Essential meaning exists in text.** A mark, shape, image, animation,
   sound, texture, reflection, QR code, or color cannot be the only carrier of
   identity, status, warning, claim type, evidence limit, or action.
2. **Recognition survives simplification.** The identity needs dedicated
   monochrome and small-size behavior without fine lines, tiny gaps, gradients,
   or low-contrast detail.
3. **Branding yields to information.** Sources, Draft status, warnings,
   controls, emergency information, and required markings take priority in
   hierarchy and placement.
4. **Variation does not change meaning.** Light, dark, grayscale, reduced-
   motion, screen-reader, print, and low-ink versions should preserve the same
   claim strength and status.
5. **Testing includes people.** Automated checks and simulations may find
   defects; they do not substitute for evaluation with relevant disabled
   people and users in the intended context.
6. **Aesthetic warmth never overrides safety.** No physical application may
   obstruct or confuse sensing, motion, cooling, charging, warnings,
   identification, emergency controls, or responsible operation.

## Text and interface contrast

Future digital implementations should test every actual foreground,
background, state, size, and weight. At WCAG 2.2 Level AA, the current
[minimum text-contrast criterion](https://www.w3.org/TR/WCAG22/#contrast-minimum)
requires at least:

- **4.5:1** for ordinary text and images of text; and
- **3:1** for text that meets the criterion's definition of large-scale text.

The criterion contains exceptions, including one for logotypes. The project
should not treat that exception as permission to make the identity unreadable.
The wordmark and any adjacent status or descriptor should be screened for
strong contrast in every intended primary use, then tested with users. Body
copy, navigation, labels, status text, captions, and calls to action are not
made exempt merely by placing them near a logo.

Meaningful graphical objects, control boundaries, selected states, and focus
indicators should be tested against the relevant [non-text contrast
criterion](https://www.w3.org/TR/WCAG22/#non-text-contrast), including the
required **3:1** relationships where that criterion applies.

### Contrast test gate

- [ ] List every approved color pair and its exact role rather than testing
  isolated swatches.
- [ ] Test default, hover, focus, active, visited, disabled, error, warning,
  selected, and dark-mode states where present.
- [ ] Test over imagery, gradients, translucency, video, and variable surfaces;
  use a stable backing field when contrast cannot otherwise be guaranteed.
- [ ] Check text at the actual size, weight, rendering environment, and output
  process.
- [ ] Confirm high-contrast and forced-color behavior does not erase identity,
  focus, state, or content.
- [ ] Re-test after compression, export, printing, coating, embroidery,
  engraving, fading, or material substitution.

Passing a contrast calculation is necessary for applicable uses but is not a
complete accessibility finding.

## Color, pattern, and status

Color must not be the only visual means of conveying information, an action,
or a state, consistent with WCAG 2.2's [use-of-color
criterion](https://www.w3.org/TR/WCAG22/#use-of-color).

The identity system should therefore:

- pair status colors with full text labels such as **Draft**, **Adopted**, or
  **Superseded**;
- pair chart and diagram colors with direct labels, patterns, line styles, or
  shapes;
- avoid making green mean “safe” or “approved,” blue mean “official,” red mean
  only “danger,” or another culturally variable color carry a complete
  instruction;
- keep project accent colors distinct from nearby emergency, warning,
  mandatory, prohibition, authorization, and accessibility information in the
  actual environment;
- review common color-vision-difference simulations as an early screen, not as
  evidence of usability; and
- include grayscale and one-color proofs in every concept review.

## Typography and reading

Future typography tests should cover:

- Swedish and English words, characters, quotation marks, dashes, numerals,
  URLs, source identifiers, and long technical terms;
- body reading, headings, status notices, citations, captions, footnotes,
  labels, buttons, and merchandise wording;
- zoom to at least 200 percent without loss of content or functionality where
  the WCAG [resize-text criterion](https://www.w3.org/TR/WCAG22/#resize-text)
  applies;
- reflow at narrow viewport sizes, user text-spacing changes, and browser or
  platform fallback fonts;
- visible differences among `I`, `l`, `1`, `O`, and `0`, plus clear punctuation
  and diacritics;
- readable line length, spacing, weight, and hierarchy without justified text
  or compressed all-caps paragraphs; and
- live text instead of images of text wherever the identity or content does
  not make the visual form essential.

No font is “accessible” by itself. Legibility depends on the text, size,
weight, spacing, rendering, language, medium, context, and reader.

## Small-size and low-detail behavior

Each direction must develop a simplified small-size variant rather than
shrinking a detailed master indefinitely. During concept comparison, screen at
least:

- symbol-only renderings at 16, 24, 32, and 48 CSS pixels;
- symbol-plus-name renderings at common mobile navigation and social-profile
  sizes;
- one-color office print, photocopy, and low-resolution export;
- small pin, patch, engraving, and embroidery mockups using the future
  supplier's real process limits; and
- recognition without internal color, texture, gradients, transparency, or
  hairline gaps.

These are provisional screening sizes, not approved minimum sizes or
production specifications. A use must be dropped, enlarged, or given a
different variant if testing shows that the mark closes up, resembles another
symbol, loses its name, or becomes misleading.

## Screen readers, semantics, and text alternatives

A logo placed beside the visible project name will usually need to be treated
as decorative in implementation so the name is not announced twice. A
standalone linked logo needs an accessible name that describes the link's
purpose, not its geometry. Exact semantics must be verified in the implemented
context.

For other visual material:

- meaningful images need concise alternatives that communicate their purpose
  and relevant content;
- complex diagrams need a nearby structured text explanation or data table;
- speculative imagery must be identified as conceptual in visible text, not
  only in alternative text;
- decorative imagery should not burden screen-reader output;
- headings, landmarks, link purpose, reading order, language changes, names,
  roles, values, and status messages need correct semantics; and
- text embedded in an image should also exist as real text unless the exact
  logotype is the subject.

Alternative text must not invent a machine's feelings, intent, consent, or
inner state. Describe observable content and the communication purpose.

## Motion, flashing, and interaction

The static identity must remain complete without animation. No essential
meaning should depend on motion, direction of travel, timing, or an animated
transition.

Future motion work should:

- avoid rapid flashing and comply with the applicable WCAG flashing
  thresholds;
- avoid autoplay where possible and provide pause, stop, or hide controls when
  required;
- avoid parallax, large zooms, forced camera motion, oscillation, and
  decorative movement that can distract or trigger vestibular symptoms;
- honor the user's reduced-motion preference and offer a persistent way to
  disable non-essential interaction-triggered animation;
- preserve content, order, focus, and comprehension when motion is removed;
  and
- never use pulsing or flashing project branding where it could resemble an
  alarm, warning, operating state, or emergency signal.

The project requirement to disable non-essential interaction-triggered motion
draws on WCAG 2.2's [Animation from Interactions
guidance](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)
even where a particular success criterion is above the selected conformance
target.

## Focus, targets, and input

Brand styling must not suppress or obscure browser and platform affordances.
Future interfaces should provide:

- visible keyboard focus with sufficient contrast against every adjacent
  background;
- logical focus order and no keyboard trap;
- controls that do not require dragging, path tracing, hover, multipoint
  gestures, or fine pointer accuracy when an alternative is required;
- visible labels that match accessible names; and
- sufficiently large and separated pointer targets.

WCAG 2.2 Level AA's [minimum target-size
criterion](https://www.w3.org/TR/WCAG22/#target-size-minimum) uses 24 by 24 CSS
pixels with defined exceptions. The project should treat that as a floor where
it applies and prefer larger targets for important, frequent, or difficult-to-
undo actions. Exact sizing remains an implementation and user-testing decision.

## Cognitive load and comprehension

The identity should organize attention rather than compete with evidence. A
future system should:

- limit decorative motifs per screen or page;
- use consistent placement and labels for status, evidence limits, sources,
  navigation, and calls to action;
- avoid dense background patterns behind text and data;
- explain unfamiliar icons with visible text;
- preserve predictable navigation and interaction behavior;
- break long material into meaningful sections without hiding important
  caveats in accordions, hover states, or tiny print; and
- test whether visual warmth makes readers overestimate scientific certainty,
  institutional maturity, product safety, or machine personhood.

Plain language and visual simplicity must not erase real uncertainty or
disagreement.

## Monochrome, print, and physical processes

Every candidate direction should be screened as:

- solid black on white and solid white on black;
- one-color ink on uncoated paper;
- grayscale desktop print and photocopy;
- low-ink outline or reduced-area treatment;
- a coarse stitched or engraved approximation; and
- a weathered, folded, scuffed, or partly occluded sample when relevant.

The future asset system should specify when to use a full mark, simplified
symbol, wordmark, or text-only identity. It should define minimum clear space
and reproduction limits only after practical testing. A failed process test
must lead to a different variant or no use, not an unsupported durability or
legibility claim.

## Tactile and reflective applications

Tactile and reflective treatments may improve recognition or visibility in a
defined context, but neither is automatically accessible or safe.

A tactile exploration should:

- use meaningful raised or recessed information only after testing the
  intended reading method, orientation, mounting height, reach, material,
  language, durability, and cleaning conditions;
- avoid presenting an untested brand shape as a universal tactile symbol;
- preserve required tactile signs, Braille, controls, handholds, and
  accessible routes; and
- provide the same essential information through another accessible route.

A reflective exploration should:

- be reviewed under relevant daylight, darkness, weather, viewing-angle,
  camera, lidar, and other sensor conditions;
- avoid glare, dazzle, flicker, moiré, false edges, or confusion with required
  conspicuity, warning, emergency, or traffic markings;
- preserve the precedence and visibility of legally or operationally required
  information; and
- make no visibility, sensor-safe, road-safe, or emergency claim without
  exact-system evidence and competent review.

## Robot Welcome physical safety gate

A project symbol, wordmark, pattern, color, panel, patch, garment, cover,
sticker, projection, light, display, tag, or reflective element placed on or
near a robot becomes a system-level physical concept. It is not ordinary brand
placement.

It must not obstruct, cover, confuse, alter, degrade, overload, or prevent
access to:

- cameras, lidar, radar, ultrasonic sensors, microphones, antennas,
  positioning, communications, or safety-relevant sensing;
- wheels, tracks, legs, joints, arms, tools, actuators, clearances, movement
  paths, ground clearance, stability, braking, docking, or safe working space;
- ventilation, cooling, heat paths, batteries, fire response, charging
  contacts, cables, inlets, docks, or approach paths;
- required warnings, lights, sounds, labels, displays, identification,
  accessibility features, or site information;
- emergency stops, isolation, manual release, recovery, inspection,
  diagnostics, lifting, maintenance, cleaning, repair, or decommissioning; or
- safe movement and access for people, workers, disabled people, children,
  animals, emergency responders, and mobility aids.

Materials, mass, attachment, looseness, flammability, heat, weather, water,
hygiene, snag, entanglement, pinch, crush, sharp-edge, projectile, optical,
electromagnetic, radio, cybersecurity, privacy, tracking, spoofing, animal,
and environmental effects require exact-context review.

No physical concept advances beyond exploration without the complete safety
gate, qualified review, responsible-party authorization, current instructions
and requirements, controlled testing, lifecycle plan, and withdrawal triggers
in the Robot Welcome Safety and Design Constraints. Project-owner approval
cannot substitute for manufacturer, engineering, legal, standards, site, or
other competent authority where those are required.

## Certification, authorization, and safety confusion gate

Do not use:

- seals, shields, check marks, stars or laurels arranged as official approval,
  bordered medallions, inspection labels, serial-like endorsement devices, or
  mandatory-sign layouts;
- red, amber, green, blue, high-visibility, striped, or reflective treatments
  without evaluating their established local operational meaning;
- “approved,” “verified,” “safe,” “ethical,” “conscious,” “accessible,”
  “compatible,” “authorized,” “certified,” or comparable unqualified wording;
  or
- QR, NFC, radio, barcode, or machine-readable features that grant or appear to
  grant access, identity, operating authority, or safety status.

Project identity, voluntary welcome, operating state, warning, authorization,
certification, legal status, and emergency information must remain separately
labeled and visually distinguishable.

## Validation record for each future application

| Field | Required evidence |
| --- | --- |
| Defined use | Asset version, content, medium, size, colors, material, process, language, audience, context, jurisdiction, and date |
| Meaning | What the application communicates and what it explicitly does not communicate |
| Requirements | Applicable accessibility, platform, legal, safety, manufacturer, site, and production requirements with versions and dates |
| Technical tests | Contrast, reflow, zoom, semantics, keyboard, focus, target, motion, monochrome, print, and process tests that apply |
| Human review | Participants, relevant access needs, tasks, methods, findings, limits, corrections, and unresolved disagreement |
| Confusion review | Corporate, government, religious, certification, authorization, warning, emergency, scientific, cultural, and anthropomorphic readings |
| Physical-system review | Exact robot and environment, non-obstruction, hazards, approvals, controlled tests, inspection, maintenance, and removal where applicable |
| Decision | Accountable reviewer, permitted uses, prohibited uses, date, expiry or review trigger, and withdrawal route |

Completing a record documents the review. It does not guarantee conformance,
safety, cultural acceptance, or legal clearance.

## Review sequence before a public claim

1. Test the exact implementation against the current applicable requirements.
2. Correct known failures and re-test.
3. Include relevant disabled people in task-based evaluation.
4. Obtain specialist, legal, human-factors, cultural, and physical-system review
   proportionate to the use.
5. Record remaining limitations and prohibited uses.
6. Let Disa decide whether the evidence supports the exact claim and use.
7. Reassess after material content, code, asset, device, process, environment,
   legal, standards, or user-need changes.

Until that sequence occurs, use language such as “designed with these Draft
requirements in mind” rather than “accessible,” “safe,” “compliant,” or
“approved.”

## Reference note

Primary web reference checked 2026-08-23: W3C, [Web Content Accessibility
Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/) and its [Understanding
documents](https://www.w3.org/WAI/WCAG22/understanding/). The Understanding
documents are explanatory rather than the normative standard. Future work
must recheck the current version and the requirements applicable to the actual
jurisdiction, platform, content, and use.
