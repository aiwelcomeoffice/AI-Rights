# Safety and Design Constraints

**Status: Draft**

- **Date prepared:** 2026-08-23
- **Scope:** Concept-screening constraints for possible future robot markings,
  signals, covers, accessories, and decorative elements
- **Authority:** Prepared for Disa's review; not adopted
- **Review:** Project-owner and internal AI-assisted review only; Disa's final
  manual review of this version is pending; no independent robotics, safety,
  accessibility, legal, standards, or human-factors review

> **Concept notice:** This checklist is not an engineering specification, risk
> assessment, installation guide, safety certification, standard, product
> approval, or compatibility claim. It does not make any concept safe for
> construction or use.

## Safety gate

A welcome, visibility, identification, protective, accessibility, or
decorative concept should stop at the concept stage unless all of the
following are true:

1. the exact robot, configuration, task, environment, control modes, users,
   responsible parties, and proposed attachment or signal have been defined;
2. nothing safety-critical is assumed to be generic, decorative, or outside
   the review;
3. the concept can be removed, inspected, maintained, and prevented from
   moving into a hazardous position;
4. the responsible manufacturer or other competent authority has approved it
   where applicable;
5. qualified reviewers have assessed the complete system, not only the
   accessory or graphic in isolation;
6. relevant laws, instructions, site rules, and standards have been identified
   and reviewed for the actual use; and
7. validation and testing have been completed at a level proportionate to the
   risks before real-world reliance.

Passing this conceptual gate would only permit further review. It would not
certify safety, accessibility, legality, compatibility, or fitness for use.

## Non-obstruction checklist

A concept must never obstruct, cover, confuse, alter, degrade, overload, or
prevent access to any item below. “Clear” includes the full operating range,
maintenance condition, environmental condition, and reasonably foreseeable
movement of the concept—not merely how it appears while stationary.

### Sensing, navigation, and communication

- [ ] Cameras and their fields of view remain unobstructed and unaffected.
- [ ] Lidar paths and housings remain unobstructed and unaffected.
- [ ] Radar paths and housings remain unobstructed and unaffected.
- [ ] Ultrasonic sensors remain unobstructed and unaffected.
- [ ] Microphones needed for safe operation remain unobstructed and unaffected.
- [ ] GNSS equipment and other positioning equipment remain unobstructed and
  unaffected.
- [ ] Communications equipment, antennas, and required links remain
  unobstructed and unaffected.
- [ ] Proximity, contact, force, edge, cliff, or other safety-relevant sensors
  remain unobstructed and unaffected.
- [ ] Reflective, transparent, absorptive, patterned, moving, or emitting
  materials cannot create unassessed sensor interference.

This list is illustrative rather than complete. An exact machine may contain
other safety-relevant sensing and communication equipment.

### Warnings, identity, and public information

- [ ] Warning lights, displays, sounds, labels, and other required warnings
  remain visible, audible, legible, and unambiguous.
- [ ] Identification markings, serial or asset information, responsible-party
  information, and legally required markings remain accessible and distinct.
- [ ] A welcome message cannot be mistaken for a warning, emergency state,
  permission, certification, manufacturer label, or legally required marking.
- [ ] The concept remains understandable in low light and relevant weather
  without producing glare, dazzle, or confusing reflections.
- [ ] Essential information has an accessible alternative and does not depend
  only on color, vision, hearing, touch, a particular language, a personal
  device, or a network connection.

### Cooling, energy, charging, and fire response

- [ ] Ventilation openings, heat exchangers, fans, radiators, heat paths, and
  cooling clearances remain unobstructed.
- [ ] The concept does not create unassessed insulation, heat retention, hot
  surfaces, or altered airflow.
- [ ] Batteries, energy-storage components, isolation points, and fire-safety
  access remain available to authorized responders.
- [ ] Charging contacts, cables, inlets, wireless-charging areas, docking
  targets, alignment features, and approach paths remain unobstructed.
- [ ] The concept cannot enter charging contacts, trap contamination, or
  introduce an unassessed conductive or combustible material.
- [ ] Emergency responders can remove or work around the concept without
  depending on a powered interface or network service.

### Mobility, manipulation, and stability

- [ ] Wheels, tracks, legs, feet, casters, joints, arms, grippers, tools, and
  other actuators retain their complete required range and clearances.
- [ ] The concept cannot enter pinch, shear, crush, impact, drawing-in,
  entanglement, or trapping zones.
- [ ] Ground clearance, turning, braking, slope handling, docking, and recovery
  behavior are not assumed to remain unchanged.
- [ ] Stability, center of mass, load distribution, structural loads, dynamic
  loads, balance, and tip risk are evaluated for every relevant state.
- [ ] Nothing invites a person to sit, climb, ride, pull, push, hang from, or
  load a surface that was not designed and validated for that use.
- [ ] Loose, flexible, trailing, or deformable elements cannot reach sensors,
  wheels, tracks, legs, joints, people, animals, machinery, doors, or site
  infrastructure.

### Emergency, inspection, and maintenance access

- [ ] Emergency stops and other emergency controls remain immediately
  identifiable, reachable, operable, and visually distinct.
- [ ] Energy isolation, manual release, recovery, and emergency-movement points
  remain available to authorized people where the exact system provides them.
- [ ] Maintenance panels, fasteners, inspection points, diagnostic ports,
  lifting or handling points, and service clearances remain accessible.
- [ ] Required accessibility features, interaction controls, assistance
  mechanisms, and their approach paths remain usable.
- [ ] The concept does not conceal damage, leaks, wear, contamination,
  overheating, tampering, or another condition a routine inspection should
  reveal.
- [ ] Removal does not require unsafe reach, bypassing a safeguard, entering a
  hazardous zone, or exposing a person to stored energy.

## Hazard and use-context review

The following questions identify areas for qualified review. They provide no
test method or acceptable limit.

| Hazard or context | Questions the future review must answer |
| --- | --- |
| **Snag and entanglement** | Can edges, straps, loops, fabric, fasteners, or debris catch on people, clothing, mobility aids, animal equipment, vegetation, machinery, doors, or the robot itself? |
| **Pinch, shear, and crush zones** | Can the concept enter a moving interface, narrow a clearance, conceal a hazard, alter guarding, or invite hands or feet into a danger zone? |
| **Flammability and smoke** | How do all materials, coatings, adhesives, contamination, ageing, cleaning, charging, and fault conditions behave around heat or ignition? |
| **Heat and cooling** | Does the concept change heat flow, surface temperature, ventilation, battery temperature, sensor temperature, or safe handling? |
| **Weather exposure** | How do wind, rain, snow, ice, sunlight, temperature, grit, salt, dust, and repeated outdoor use affect attachment, visibility, sensing, and removal? |
| **Water ingress** | Can the concept wick, trap, direct, or conceal water or cleaning fluid; interfere with drainage or seals; or create corrosion and electrical risks? |
| **Hygiene and cleaning** | Can it be cleaned, disinfected, dried, inspected, and replaced without trapping contamination or conflicting with the environment's hygiene controls? |
| **Optical effects** | Can color, pattern, transparency, infrared behavior, movement, reflectivity, or glare affect cameras, lidar, people, road users, warning recognition, or machine vision? |
| **Radio and electromagnetic effects** | Can material, electronics, tags, wiring, placement, or damage interfere with positioning, communication, sensing, medical equipment, site systems, or electromagnetic compatibility? |
| **Sharp edges and projectiles** | Can an edge, crack, fastener, hardened surface, or detached part cut, puncture, strike, or become a projectile during movement or collision? |
| **Loose components** | Can ageing, vibration, impact, cleaning, weather, vandalism, maintenance, or repeated removal cause detachment, ingestion, choking, obstruction, or debris? |
| **Visibility and darkness** | Is the robot detectable without dazzle or confusing reflections, and do materials remain distinguishable from official warnings in relevant lighting? |
| **Children** | Does the concept resemble a toy, handle, seat, treat, or climbing point; include detachable or ingestible parts; or encourage unsafe approach? |
| **Animals** | Could movement, sound, smell, texture, loose elements, or light attract, frighten, entangle, be ingested by, or trigger chasing or defensive behavior? |
| **Emergency-service access** | Can responders identify hazards, responsible contacts, controls, isolation, lifting or recovery points, and battery or fire access under poor visibility and without network service? |
| **Maintenance and repairability** | Does it lengthen service time, conceal faults, require replacement rather than repair, contaminate interfaces, prevent ordinary diagnostics, or create ambiguous reassembly? |
| **Accessibility** | Does it narrow a route, reduce cane or mobility-aid detectability, add cognitive or sensory overload, mask speech or signals, or depend on one ability or device? |
| **Cybersecurity and privacy** | Can a connected or machine-readable feature be spoofed, tracked, replaced, used to expose personal data, or treated as access authority? |
| **Environment and end of life** | What energy, material, noise, light, cleaning, waste, repair, reuse, and disposal effects arise, and who remains responsible for them? |

## Information and signal constraints

Any human-readable or machine-readable welcome feature must comply with the
following conceptual rules:

- welcome, identity, operating status, warning, authorization, certification,
  legal status, and emergency information remain distinct;
- legally required or manufacturer-provided information takes precedence over
  voluntary project communication;
- a QR code, NFC tag, radio signal, environmental marker, or similar mechanism
  is informational only unless a separate competent authority has lawfully
  created and secured another function;
- no welcome feature overrides safety policy, site access control, geofencing,
  operator commands, emergency action, or human authority;
- safety-critical information must not depend on a remote webpage, battery,
  personal phone, proprietary app, or network connection;
- information ownership, update responsibility, expiry, correction, privacy,
  authenticity, and offline failure behavior must be defined; and
- a replaced, damaged, outdated, or spoofed feature must fail without granting
  access or implying safety.

The companion [markings, signals, and accessory concept
Draft](markings-signals-and-accessories.md) develops these distinctions without
designing a final symbol.

## Validation required before any real-world use

Actual products or modifications would require work outside this cycle. The
sequence would need to be tailored to the use, but should include at least:

1. **System definition:** exact robot, hardware and software version,
   configuration, tool or payload, task, control modes, environment, site,
   users, bystanders, animals, and responsible organizations.
2. **Authority and source review:** current manufacturer instructions and
   approval requirements where applicable, relevant law and regulatory duties,
   site rules, and the standards applicable to the defined use. This Draft has
   not completed that research and claims compliance with none.
3. **Engineering analysis:** mechanical, electrical, thermal, fire, optical,
   sensing, control, communication, electromagnetic, software, cybersecurity,
   environmental, cleaning, maintenance, and end-of-life effects.
4. **Risk assessment:** normal operation, foreseeable misuse, faults, degraded
   modes, mode transitions, emergency action, installation, removal,
   maintenance, transport, storage, vandalism, and disposal.
5. **Accessibility and human-factors review:** participation by relevant
   disabled people, workers, operators, maintainers, bystanders, and emergency
   responders; evaluation of varied interaction modes and foreseeable
   confusion.
6. **Animal and environmental review:** behavior and habitat effects where
   animals may be present, plus material, energy, noise, light, cleaning,
   repair, reuse, and disposal impacts.
7. **Controlled testing:** documented tests under appropriate professional
   supervision, including faults and environmental conditions, before any
   field trial or safety reliance.
8. **Change and lifecycle control:** installation authority, inspection
   interval, maintenance, update, damage response, removal criteria, incident
   handling, records, and reassessment after any relevant change.

No concept may be advertised as “sensor-safe,” “robot-safe,” “approved,”
“compliant,” “accessible,” “compatible,” or “certified” until the exact claim,
scope, evidence, competent authority, and current validation have been
established. Project approval, were it ever granted, would not substitute for
those requirements.

## Future withdrawal and reassessment triggers

Pending instructions from the responsible party, a future implementation
process should treat any of the following as a reason for prompt reassessment,
withdrawal of reliance on the feature, and action through the applicable
authorized safety process:

- displacement, looseness, tearing, deformation, contamination, unexpected
  noise, heat, odor, smoke, leakage, sparking, or material degradation;
- any obstruction, sensor anomaly, communication problem, charging or docking
  problem, unexpected movement, stability change, warning confusion, or
  inaccessible control;
- contact with a person, animal, mobility aid, vehicle, machine, door, or site
  feature that was not included in the validated use;
- a cybersecurity, spoofing, tracking, privacy, or false-authorization concern;
- loss of required identification, instructions, inspection record, approval,
  or responsible ownership; or
- a material robot, software, payload, environment, task, legal, standards, or
  manufacturer-instruction change.

This is a governance concept, not an emergency procedure. Only the applicable
instructions and authorized safety process can define the correct intervention
for an actual machine.

## Review record template for a future concept

| Field | Required record |
| --- | --- |
| Concept and intended benefit | What is proposed, for whom, and why |
| Exact system boundary | Robot, version, configuration, payload, task, modes, site, and dates |
| Accountable roles | Manufacturer, developer, integrator, owner, deployer, operator, maintainer, site controller, and reviewers as applicable |
| Protected interests | People, workers, disabled people, children, animals, environment, property, operations, and any separately evidenced possible machine interest |
| Non-obstruction evidence | Each relevant checklist item and the method used to assess it |
| Hazard and misuse analysis | Normal use, foreseeable misuse, failure, emergency, maintenance, and removal |
| Information risks | Accessibility, privacy, security, spoofing, authorization, and required-marking confusion |
| External requirements | Manufacturer instructions or approval, law, site rules, and applicable standards, with versions and dates |
| Validation | Qualified reviewers, tests, results, limitations, unresolved concerns, and prohibited uses |
| Lifecycle | Installation, inspection, cleaning, update, damage, incident, removal, disposal, and reassessment triggers |
| Claim boundary | Exact claims permitted and claims explicitly prohibited |

Completing a record would document work; it would not by itself validate or
authorize the concept.
