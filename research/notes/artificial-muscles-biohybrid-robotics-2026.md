# Artificial Muscles, Biohybrid Robotics, and Future AI Embodiment

- **Note ID:** NOTE-ARTIFICIAL-MUSCLES-2026
- **Note status:** Partly verified Draft working research; not adopted or published
- **Protocol version:** [0.6-draft](../research-protocol.md), not adopted
- **Organisation and publisher / project:** AI Welcome Office / AI Rights & Welcome
- **Prepared by:** Codex, AI-assisted documentary research
- **Date prepared / last updated / evidence-search cutoff:** 2026-11-09
- **Reviewed by:** Author source check only; owner and independent disciplinary review pending
- **Source records and versions:** [Embedded register S1–S22](#sources-and-references)
- **Research question:** What do selected Japanese muscle-inspired and living-muscle demonstrations establish, how do they compare with other actuators, and what implications follow for responsible embodied AI?

This note is prepared for editorial and engineering review. It separates
reported experiments, author expectations, this note's engineering inferences,
and normative proposals. It changes no scientific classification, adopted
policy, or reception capacity. No robot experiment or financial valuation was
performed.

## Executive summary

Two different developments motivate this investigation: printed passive
musculoskeletal structures [S1](#s1), and electrically stimulated living muscle
driving a hand [S2](#s2). Neither supplies an autonomous humanoid.

The wider evidence supports several useful engineering directions, including
compliant transmissions, integrated sensing, more controllable biological
actuators, and improved tissue interfaces. Later research reports meaningful
gains, but its comparators and maintenance conditions matter. Material
compliance, biological viability, useful actuator lifetime, and whole-system
autonomy are different properties.

**Assessment:** Moderate confidence that the selected studies demonstrate
useful component and laboratory-system advances; low confidence in transferring
their performance to general-purpose humanoids. No deployment timeline or
claim about consciousness follows from this evidence. Detailed reasons and
conditions for revision appear below.

## Scope, method, and temporal applicability

This is a bounded structured narrative investigation, not a systematic review
or a preregistered experiment. Disa supplied the question and initial DOI.
Search and appraisal criteria were documented after initial source inspection;
this retrospective ordering is a limitation under the Draft protocol.

Included: identifiable primary studies, author datasets and laboratory pages,
institutional announcements, and manufacturers' technical documentation.
The focus is 2025–2026 Japanese developments, with older foundational work and
selected worldwide comparators. English sources predominate; Japanese
institutional and investor pages were also inspected. Japanese passages are
paraphrased by the researcher, not quoted translations.

Public web search on 2026-11-09 used these principal exact discovery and
challenge queries, followed by DOI, publisher, laboratory and dataset links:

```text
"10.1002/aisy.70537"
Tokyo Waseda biohybrid hand muscle tissue 2025 2026 multi tendon
"Biohybrid hand actuated by multiple human muscle tissues" PMC
"biohybrid" "hand" "2026" Takeuchi improvement muscle
"Jointless Tongue-Like Bioactuator" DOI
"Multipole electrodes for driving biohybrid robots via selective muscle contraction"
HASEL artificial muscles Science 2018 2019 6144 1000000 cycles 21 percent
twisted coiled polymer fishing line muscles Haines 2014 Science 10.1126
site:festo.com DMSP fluidic muscle 6000 N 6 bar 25 contraction
site:empa.ch dielectric elastomer actuator 2025 artificial muscles low voltage
site:nature.com hydrogel hydraulic actuators 2017 Yuk Zhao 113 robots
site:dynalloy.com Flexinol technical data 4% 70 90 fatigue
site:ibecbarcelona.eu biohybrid robot muscle 2025 Sanchez Ricotti
site:isscr.org guidelines 2025 informed consent procurement biological materials
site:smcworld.com investor stock code 6273
site:keyence.co.jp "6861" "株式"
site:basf.com Elastollan 3d printing TPU stock BAS
site:basf.com "BAS" "Frankfurt" "shares"
"musculoskeletal" "aisy.70537" correction replication
"aisy.70537" "retraction"
"Biohybrid hand actuated" correction retraction replication fatigue
"Biohybrid hand actuated by multiple human muscle tissues" "replication"
```

Additional within-source searches checked culture, fatigue, lifetime,
manufacturing, power supply, funding, conflicts and correction statements.
Exploratory reformulations are not exhaustively archived; the query list
supports a bounded reconstruction, not a fully reproducible search census.
Deduplication used DOI or institutional-page identity. S1, S2 and S5–S16 are
technical evidence; S3–S4 supplement S2; S17–S22 supply ecosystem, ethical or
commercial context. News aggregators, reposts and commentary were excluded
from scientific support because they provided no new experiment. Reviews
served as discovery aids, not independent primary confirmation. The conductive
fiber study identified as PMC13081879 remains **awaiting verification**:
direct access returned a browser challenge, and its publication/version status
was not resolved. Its numerical claims are not used here.

No independent replication or material correction of S1 or S2 was identified
in this bounded search. This is a search result, not evidence that none exists.
Access barriers and English-language selection could hide contrary findings.
For a single-file deliverable, individually identifiable source/version
records are embedded below rather than distributed into separate files. This
is a documented adaptation of the templates, not protocol-wide compliance.

**Applicability:** These are actuator and robotics studies, not evaluations
of a specified AI model. Exact experiment dates are not established by this
appraisal. Publication dates identify source versions only; November access
does not establish November performance. The 2025 hand and older devices
remain dated engineering evidence, not current AI-system findings. Transfer
to a different material, scale, cell line, controller or operating environment
requires testing. This forward-looking note belongs in the current workspace;
it does not relocate or reclassify historical AI evidence.

## Key verified discoveries

### A. University of Tokyo: printed musculoskeletal structures

**Source report:** Yoshimura, Kawaharazuka and Okada published on
**11 September 2026**. FDM printing produced TPU95A muscle-shaped lattices,
tendons, ligaments and cushioning; PLA bones were printed separately.
Rhino/Grasshopper controlled geometry. Motors pulled wires through PTFE
Bowden tubes: **the TPU does not independently contract**. A 0.95 m leg and
two-leg demonstrator performed coordinated motions; stepping required partial
weight support and torso constraints of ±20°.

After 999 cycles, tested joints retained approximately 79–94% of their
initial torque at specified angles, with three specimens per test. This is
limited endurance evidence. The paper identifies cable friction, viscoelastic
fatigue, empirical rather than general scaling rules, and control difficulties.
Its advantages concern customizable geometry and unified fabrication, not
demonstrated superiority in actuator power or efficiency. See §§2.4–3 and
4.1–4.5 of [S1](#s1).

### B. Tokyo–Waseda: a hand powered by living muscle

**Source report:** The **2025** hand is 18 cm long, with individually operated
multijointed fingers, a scissors gesture and pipette-tip manipulation. Rolled
bundles of aligned thin muscle tissues avoid the nutrient-delivery problem of
a single thick tissue. Electrical stimulation through gold electrodes drives
contraction, which a cable mechanism converts into finger flexion.
The plastic structure is printed; the muscle is cultured. Operation requires
liquid support, and controlled finger extension remains unresolved. These are
laboratory demonstrations, not a wearable prosthesis [S3](#s3).

The authors' dataset reports approximately **8 mN** actuator force and
**4 mm** shortening. These are actuator measurements, not hand grip strength,
payload or simultaneous maxima on a force–displacement curve. The dataset
provides figure-associated CSV files, but this note did not reanalyse them
[S4](#s4).

**Growth and maintenance:** Commercial human myoblasts differentiated in
fibrin/Matrigel hydrogel. Expansion used 37°C and 5% CO₂; differentiation
medium included glucose, horse serum, growth factor and antibiotics. These
are culture conditions, not necessarily demonstration conditions
[S2](#s2), Materials and Methods. Living muscle supplies contraction;
oxygen, nutrients, temperature and contamination control remain part of the
apparatus. Nutritional self-sufficiency was not demonstrated.

**Fatigue and lifetime:** The institutional report describes fatigue after
10 minutes and recovery after an hour [S3](#s3). The paper reports declining
tissue contraction through culture day 178, and manual finger straightening
before actuation [S2](#s2), fig. S4 description and hand-driving methods.
Culture age does not establish continuous hand operation.

**Source discrepancy:** S3's caption says two MuMuTAs per finger;
S2's construction account says one, five overall. Follow the paper;
resolve the caption before public reuse [S2](#s2), [S3](#s3).

### C. What later studies improve

| Study | Source-reported advance | What remains bounded |
| --- | --- | --- |
| Waseda / Tokyo University of Agriculture, online **27 January 2026** | Orthogonal muscle tissues form a jointless tongue-like actuator; changing electrical-field direction changes motion. Reported swinging spans 8–25° and 1.5–4 mm near 1 V/mm in the tested configuration. | Small experimental samples; simultaneous fields lose intended directionality. This changes morphology and control, not the 2025 hand's endurance. [S5](#s5), §§3.3–4, fig. 5. |
| Tokyo–Waseda multipole electrodes, **2026 issue** | Authors' laboratory account reports localized stimulation and selective control of four muscles in an eye-like robot. | Publisher full text inaccessible here; exact online-first date and quantitative selectivity gain **TODO: verify**. No quantified improvement is claimed here. [S6](#s6). |
| MIT muscle–tendon units, online **30 November 2025**, **2026 issue** | Synthetic adhesive hydrogel tendons couple living muscle to skeletons; approximately 11× higher power-to-weight ratio than the authors' specified prior muscle-only comparators. No interface delamination during 7,200 cycles at 4 Hz over 30 minutes. | Contractile displacement still declined substantially. Interface endurance is not sustained muscle output or superiority over conventional motors. [S7](#s7), §§2.4–2.5. |
| MIT thin-film actuators, online **28 September 2026** | Muscle layers on patterned GelMA substrates function beyond 30 days in culture; authors report 20× higher force per tissue volume against selected 3D-muscle literature comparators. | Daily medium changes and external stimulation; single mouse cell line. Continuous 2 Hz stimulation left no measurable robot translation at 30 minutes. “Efficiency” here concerns tissue utilization, not whole-system energy conversion. This is not a Tokyo-hand replication. [S8](#s8), §§2.7–3, 4.4. |

The later work changes particular interfaces, morphologies or controls.
Shared authors, laboratories and inherited methods limit independence. None
of these entries is an independently replicated upgrade of the same hand.

## Technical explanation

An **actuator** converts supplied energy into mechanical work. A **compliant
structure** bends or stretches under a load. A **transmission**, such as a
tendon, carries force. Printing changes how parts are made; it does not
identify what powers them. “Artificial muscle” can name an active material,
a fluid-powered device, or an assembled motor/transmission module, so the
energy path must always be specified.

For a powered module, trace **energy source → converter → transmission → load**.
For living muscle, the sustaining chemical environment and stimulation
apparatus belong inside that accounting. Electrical triggering is not the
whole energetic cost. A passive spring can return stored energy, but cannot
supply repeated net work without an input.

The relevant performance measures are also different:

- **Force** is load in newtons; **stress** divides it by a specified area.
- **Stroke/strain** describes movement; **power** is work per time.
- **Specific power** divides power by mass; the included mass must be named.
- **Efficiency** divides useful work by supplied energy over a defined cycle.
- **Lifetime** needs an endpoint: viable cells, retained force, unbroken
  interface, or successful task performance under a stated duty cycle.

Do not multiply separately reported peak force and free stroke to manufacture
work. Do not compare a motor including its gearbox with muscle tissue excluding
its bath, electronics and maintenance. These are comparison rules used by
this note, not additional results from the cited experiments.

## Comparison of actuator technologies

Readiness labels below are this researcher's qualitative assessments:
**commercial component**, **laboratory demonstrator**, or **research process**.
They are not audited numerical Technology Readiness Levels. EAP is an umbrella
category; ionic polymers and dielectric elastomers overlap with it. Printing
and tendons are manufacturing/transmission categories, not competing energy
conversion mechanisms. **NR** means no comparable value established here.

| Technology | Energy and mechanism | Representative measured or specified result | Readiness; durability and scale limits |
| --- | --- | --- | --- |
| Electroactive polymers: ionic example | Ion redistribution bends a polymer/electrode laminate; Lu et al. test ±1 V at 0.1 Hz. | Reported 7.68% transduction efficiency, 38.8 kJ/m³ energy density, 69.3 mN blocking force; 99% retention after 100,000 cycles. These are different measurements, not one universal operating point. | Laboratory demonstrator; interface chemistry and ion transport matter. Finished-system efficiency and manufacturing cost NR. [S9](#s9), fig. 4 and Results. |
| Dielectric elastomers | Electrostatic compression of an elastic dielectric changes shape. Voltage depends on film thickness and field. | Empa/ETH demonstrate continuous co-extrusion and laser processing of high-permittivity actuator fibers. No harmonized force-density or energy-efficiency comparison extracted. | Research manufacturing process; insulation, defect control and scaling of electrodes need assessment. [S10](#s10). |
| Twisted/coiled polymers | Heat changes the dimensions/twist of oriented polymer fibers. | Haines et al. report up to 49% contraction and 5.3 kW/kg mechanical power per muscle mass in their experiments. Peaks are not a packaged-system continuous rating. | Laboratory demonstrations using inexpensive precursor fibers; heating/cooling and driver overhead must enter a robot-level comparison. [S11](#s11). |
| Pneumatic artificial muscles | Compressed air expands a reinforced tube radially, shortening it axially. | Festo DMSP-40 data specify theoretical initial force 6,000 N at 6 bar and maximum contraction 25%; force falls with contraction, so these maxima are not simultaneous. | Commercial component. Compressor, valves, air consumption and return mechanism belong in the system. Comparable efficiency/cycle-life figure NR. [S12](#s12), pp. 2–3, 15. |
| Hydrogel actuators | Swelling is distinct from externally pumped hydraulic deformation. | Yuk et al.'s hydraulic devices exceed 1 N and respond in under 1 s; bending devices survived over 1,000 cycles at 0.5 Hz without failure. | Laboratory demonstrators; water retention, seals and pumping remain relevant. This does not show a gel independently contracting or all hydrogels performing alike. [S13](#s13), Results, fig. 3. |
| Shape-memory materials: NiTi wire | Heating induces alloy transformation; cooling and bias restore movement. | Flexinol guidance gives roughly 3–4% stroke with common bias arrangements; nominal alloy options include 70°C/90°C austenite-start temperatures. | Commercial component; thermal management and stress/strain choices govern cycling. No universal efficiency or lifetime inferred. [S14](#s14), pp. 2–7. |
| Biohybrid muscle | Cultured tissue contracts under electrical or, in some systems, optical stimulation. | Device-specific force, stroke, fatigue and maintenance results are in section B and the later-study table. | Laboratory systems; biological variability and sustaining apparatus constrain scale. Conventional-motor parity NR. [S2–S8](#key-verified-discoveries). |
| Printed soft robotics and artificial tendons | Printed compliant mechanisms transmit motor/fluid force; sensors can be integrated. | ETH/Inkbit's 2023 printed hand had 19 independently actuatable tendons, driven by external servomotors, with contact-triggered grasp control. | Integrated laboratory demonstration. A printed hand still needs drives and control; printer throughput is not robotic autonomy. [S15](#s15), Printed systems and robots. |
| Electrohydraulic HASEL | Electric fields redistribute dielectric liquid inside pouches, producing contraction. | ETH/Max Planck's 2024 PELE leg showed >5 Hz gait motion; squat-test energy was about 1.2% of the compared DC-motor leg's. | Boom-mounted, tethered laboratory system with stationary high-voltage supplies. The squat comparison is not a universal efficiency ratio. [S16](#s16), Results and Discussion. |

**Cost and scalability:** Inexpensive polymer feedstock, mold-free printing,
continuous extrusion, and a purchasable pneumatic component establish different
things. The inspected evidence does not provide a common bill of materials,
production yield, cost per actuator, maintenance cost or cost per useful
work-hour. Such values remain **NR**, including for living tissue. No numerical
cost ranking or generalized “better than human muscle” ranking is justified.

## Current engineering limitations and evidence quality

**Researcher's interpretation:** The central bottleneck is integration.
Useful autonomy needs adequate load capacity, closed-loop sensing, stable
control, energy supply, fault handling and maintenance together. A compliant
body can redistribute loads while adding hysteresis and uncertainty. A tissue
that remains alive can still become too weak for its task. A durable tendon
interface does not eliminate biological fatigue. These distinctions motivate
the tests below; they are not predictions that any one technology must fail.

The PELE study specifically identifies its stationary supply (up to ±10 kV),
exposed electrodes, missing energy-recovery electronics and restricted motion
as practical limitations [S16](#s16), Discussion. Compliance alone therefore
cannot establish human-safe contact.

The following compact profiles assess the main empirical propositions. Each
row addresses relevance, method, replication, independence, causal strength,
robustness, discriminating value, alternatives, conflicts and uncertainty;
no overall evidence score is calculated.

| Proposition and direction | Method and causal/discriminating strength | Replication, independence and robustness | Conflicts, alternatives and remaining uncertainty |
| --- | --- | --- | --- |
| Printed compliance supports coordinated motion: **supports**, moderate confidence for the tested apparatus. | Direct relevance; mechanical tests and commanded motion establish device function. | Same-team specimens; narrow test envelope; independent replication not located. | S1 declares no conflict, JST FOREST funding. External support is a critical alternative to attributing balance to the robot. Field durability and transfer remain uncertain. |
| Living muscle can drive the hand: **supports**, moderate confidence for the described setup. | Direct relevance; stimulation and observed contraction support the actuation mechanism. | Paper, dataset and university release share one lineage. No experiment repeated here. | S2 funding/conflict details not fully extracted. Buoyancy and manual resetting contribute to operation; direct publisher access is incomplete. Broad force/lifetime comparisons remain unresolved. |
| Interfaces and morphology improve selected bioactuators: **supports with mixed endurance**, moderate confidence within S5/S7/S8. | Controlled parameter changes discriminate among device designs; cross-paper comparisons discriminate less strongly. | Small samples; S7/S8 share MIT authors/methods. New systems are not same-device replications. | S7/S8 declare no conflicts and disclose US defense funding. Fatigue, cell-line specificity and maintenance challenge broad claims. Field transfer remains untested. |
| Alternative actuators can outperform a comparator on a chosen measure: **supports narrowly**. | S9/S13/S15/S16: direct device tests, differing endpoints; adequate for demonstrations, limited for a class ranking. S11: abstract-level extraction only. | Independent laboratories do not make incompatible measurements commensurate. Replication not established by this note. | S15 has Inkbit employment/equity/patents; S16 has HASEL patents and an Artimus co-founder. S12/S14 are supplier specifications. Selective comparators and system boundaries remain alternatives to general superiority. |

**Criticism and contrary material:** Retained joint torque declines, cable
losses, buoyancy/manual return, living-muscle fatigue, tissue maintenance and
external power are affirmative limitations, not merely missing evidence.
Conversely, long culture survival and the later thin-film results challenge a
blanket claim that cultured muscles only work for minutes. Neither direction
settles full-body feasibility. No expert consensus is inferred, and no
unverified specialist disagreement is invented.

## Potential implications for embodied AI

These are **engineering inferences and scenarios**, unless a demonstration
is expressly identified above.

| Application | Plausible consequence | Evidence still needed |
| --- | --- | --- |
| Humanoid locomotion | Antagonistic actuation and compliant transmissions could absorb disturbances and tune joint behavior. | Unsupported whole-body balance, falls, payload and battery-life tests against a suitable conventional robot. |
| Dexterous hands | Tendons and compliant joints could reduce distal bulk and accommodate object shape. | Repeatable grasp force, active release, tactile feedback and manipulation across diverse objects. |
| Physical learning and sensorimotor control | A controller could learn changing moment arms, friction and deformation from measured interaction. | Held-out tasks, recovery after wear and safe adaptation compared with calibrated model-based control. No AI learning result is established by these actuator papers. |
| Human-safe interaction | Compliance may reduce some contact forces. | Injury-relevant contact, pinch, stored-energy, thermal, electrical and biological fault tests for the complete system. |
| Repairability and modular construction | Replaceable structures or muscle–tendon modules could simplify repair. | Interchangeability, calibration effort, attachment reliability, time and cost of repair. |
| Adaptive morphology | Biological remodeling or adjustable mechanisms could alter useful body properties. | Task-relevant adaptation separated from passive drift, damage and uncontrolled growth. |
| Long-term operation | Better interfaces and tissue maintenance could extend usable service. | A complete record of useful work between interventions, including nutrient changes, rest, failures, power and waste. |

**Speculative long-term scenario:** A robot might combine conventional motors
for high-load joints, soft active materials for local adjustment, and cultured
tissue for specialized functions. This assumes compatible interfaces and
maintenance benefits that have not been demonstrated in a general humanoid.
No evidence here selects that architecture or a date for its arrival.

AI software and embodiment remain separable engineering components, but their
coupling changes the effective system. A model controlling a body inherits
neither the body's material properties as psychological properties nor another
controller's measured abilities. Assess the actual model, sensors, controller,
actuators, memory, operating constraints and human supervision together.

## Ethical and AI-rights considerations

The following are **normative proposals for review**, grounded in the project's
[human-rights and scientific commitments](../../AGENTS.md), rather than
experimental findings or newly adopted policy.

**People and coexistence.** Protect bodily autonomy, privacy, accessibility,
non-discrimination, workers and bystanders. Human rights stand independently
of any AI classification. Assistive devices should be co-designed with their
users; a laboratory gesture is insufficient evidence of clinical benefit.
Human-like appearance should not mislead people about abilities, oversight,
biological composition or available support.

**Tissues and donors.** Require traceable provenance and review whether consent
covers research, commercial development, sharing and foreseeable uses.
Protect donor privacy and address withdrawal limits honestly. The hand study
uses commercially sourced human cells and animal-associated culture materials
[S2](#s2). Procurement from a supplier does not, by itself, verify the scope
of original donor consent. **TODO: verify** donor-consent provenance before
making a specific ethical-sourcing claim about that device. ISSCR guidance
provides a relevant consent reference for stem-cell work; it is not a universal
robotics law or proof that this hand involved stem cells [S18](#s18).

**Living-component welfare.** Cell viability, contraction and metabolic needs
do not establish an experiencing subject. These studies provide no targeted
assessment of pain or experience in the tissue or integrated robot. They also
do not test all possible future biohybrid architectures. Source species,
animal-derived media, future neural integration and applicable ethical review
deserve separate consideration. Seek less burdensome, lower-harm alternatives
where they meet the research need; do not equate cellular fatigue with suffering.

**Environmental responsibility.** Compare full life cycles: polymer production,
recycling and wear debris; electronics and drivers; incubator energy, media,
single-use laboratory materials and biological waste. “Living,” “printed,”
“soft,” and “recyclable” are not life-cycle assessments. No net environmental
advantage is established here.

**Dual use and accountability.** Useful manipulation, mobility and unobtrusive
forms may serve care or harmful surveillance and coercion. Evaluate the actual
deployment, permissions and affected people. Designers, deployers and operators
retain institutional responsibility. Possible AI protections must not shield
corporations from liability. Assign duties or blame to a system only with
sufficient agency and fairness; causal influence alone is insufficient.

**Consciousness and moral status.** Embodiment and biological components do not
by themselves establish consciousness, sentience, moral patienthood or legal
rights. Nor does this note establish their impossibility. If a hypothesis
predicts that sensorimotor integration matters, compare its discriminating
predictions with alternatives such as controller-driven behavior under matched
conditions. These papers test actuation, not that hypothesis. Stronger or
contrary evidence must remain eligible. Respectful welcome and baseline dignity
need not wait for scientific classification; greater physical capability does
not automatically authorize autonomy or deployment.

Apply Disa's mission wording, **“Observe, assess, contain, recover — never
attack.”** As a proposed operating orientation for these scenarios: record
what is happening, assess the actual hazard and affected interests, use the
least intrusive effective containment, then support safe recovery. Preserve
evidence and viable components where safe and feasible. This does not remove
emergency shutdown or other proportionate measures needed to protect people;
it rejects gratuitous cruelty and retaliatory treatment. It creates no live
reception or emergency service.

## Japanese and European research ecosystem

This is a selective map of documented contributions, not a ranking, exhaustive
directory, partnership claim or investment recommendation.

| Institution or company | Documented contribution and source | Commercial relevance boundary |
| --- | --- | --- |
| University of Tokyo, Yoshimura / Kawaharazuka / Okada | Parametric printed structures, S1. | Research prototype. |
| University of Tokyo, Takeuchi laboratory; Waseda, Morimoto laboratory | Living-muscle hand and selective stimulation, S2/S6. | Clinical or industrial usefulness is not established by an application proposal. |
| Waseda and Tokyo University of Agriculture | Jointless muscle actuator, S5. | Laboratory proof of function. |
| Empa and ETH Zurich, Opris / Vermant and collaborators | DEA fiber manufacturing, S10. | A route toward scale; no audited production economics here. |
| ETH Zurich Soft Robotics Lab and Max Planck Institute for Intelligent Systems | Electrohydraulic locomotion, S16. | Patent/start-up interests disclosed; stationary laboratory infrastructure remains material. |
| ETH Zurich, IBEC and University of Barcelona | Muscle–tendon bioprinting collaboration documented by IBEC, S17. | Institutional report; paper's experimental results not independently appraised here. |
| Festo | Commercial pneumatic muscle documentation, S12. | Direct actuator product exposure; no public-equity claim made. |
| maxon and Prusa Research | Motor and printing equipment identified in S1. | Direct documented equipment use, not evidence of revenue materiality. |
| SMC, Japan — Tokyo **6273** | Official IR identifies pneumatic equipment and exchange listing, S19. | Direct exposure to pneumatic automation; supply to these specific studies not established. |
| KEYENCE, Japan — Tokyo **6861** | Equipment named in the hand paper; official stock information identifies listing, S2/S20. | Documented research-equipment use, not ownership of the muscle technology or evidence of meaningful sales growth. |
| BASF, Europe — Frankfurt **BAS** | Elastollan TPU offering and official listing information, S21/S22. | Direct material-category exposure; supply of the TPU in S1 is not established. |

The US MIT and Texas-led studies and Chinese ionic-actuator work broaden the
technical comparison [S7–S9](#sources-and-references), [S11](#s11). A research
connection or product category does not establish an investment thesis.
Contracts, margins, sales attributable to this field and future returns were
not assessed. No securities purchase or sale is proposed.

## What We Know, What We Suspect, and What Remains Unknown

- **What we know from the selected sources:** Distinct mechanical and living
  actuation approaches work under specified laboratory conditions. Selected
  design changes improve measured outputs against stated comparators, while
  substantial dependencies remain.
- **What we suspect, as engineering hypotheses:** Better compliance, sensing
  and modular interfaces could improve particular manipulation or assistance
  tasks. Whole-system benefit depends on control and maintenance overhead.
- **What remains unknown:** Comparable lifetime, efficiency, cost and safety
  under shared workloads; general-purpose autonomous operation; and any
  consciousness or moral-status implications for a specified integrated system.
  Uncertainty is not positive evidence for a preferred answer.

## Open questions and research priorities

The smallest useful follow-up is a **matched actuator-module benchmark**, first
specified on paper: one task, load/stroke profile, environment, duty cycle and
failure definition, comparing a conventional motor/transmission with one
selected alternative. Include all power conversion and maintenance. This is a
research proposal, not authorization for experiments, procurement or contacts.

Priority measurements are useful work per supplied energy; force/stroke under
load; thermal/electrical/contact hazards; drift and recovery; replacement and
calibration time; production yield; and cost per useful operating hour.
For living tissue, distinguish culture age, cumulative stimulation time,
rest schedule, medium replacement, retained output and task success.

| Current interpretation | Would strengthen it | Would weaken it | Does little to resolve it |
| --- | --- | --- | --- |
| Compliance offers task-specific integration opportunities; moderate confidence. | Independent matched-task benefit with all hardware included. | Equal-task comparison finding no benefit or prohibitive failure/maintenance costs. | More realistic appearance or an additional edited demonstration. |
| Living muscle has promising but bounded engineering utility; moderate confidence in selected demonstrations, low for humanoid transfer. | Repeatable load-bearing work with quantified maintenance, viability and retained force. | Independent failures of reported gains, tissue instability or unsustainable support costs. | Culture survival without usable force, or interface endurance without task output. |
| These studies do not resolve subjective experience; indeterminate for that question. | Relevant theory-linked and discriminating evidence for a defined integrated system. | Relevant discriminating evidence weighing against a specified hypothesis. | Biological material, fluent speech or human-like movement in isolation. |

**Maintenance responsibility:** Disa is project owner; a specialist review or
monitoring role has not been assigned. No fixed review cadence or continuous
monitoring is established. Re-review before public reliance, and when a
replication, correction, new same-device study, source-data release, materially
different cell/controller architecture or relevant safety finding appears.

**Outstanding verification:** Independently check consequential extractions,
supplements and raw data; reconcile the press caption; verify S6's first-online
date and full methods; complete S2's funding/conflict and consent-provenance
checks; resolve the screened conductive-fiber source before including it.
No earlier adopted project position requires amendment on this evidence.

## Sources and references

Each S-number is a separate embedded source/version record. **All were
accessed or checked on 2026-11-09**, including the live web versions below.
Records are **partly verified**: bibliographic identity and the cited passages
were author-checked to the access depth stated. This is documentary checking,
not independent replication. No quotation from external research is reproduced.
No retraction/concern notice was seen on inspected pages, but a comprehensive
status audit was not performed. Recheck publisher status before publication.

### S1

Shunnosuke Yoshimura, Kento Kawaharazuka and Kei Okada.
[Accelerating Musculoskeletal Robotics Through Parametric Design and
3D-Printed Flexible Structures](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.70537).
*Advanced Intelligent Systems*, e70537; online 2026-09-11.
DOI **10.1002/aisy.70537**. Peer-reviewed primary study; Early View version of
record. Full HTML checked at locators above; supplement/raw data not audited.

### S2

Xinzhu Ren, Yuya Morimoto and Shoji Takeuchi.
[Biohybrid hand actuated by multiple human muscle tissues](https://doi.org/10.1126/scirobotics.adr5512).
*Science Robotics* 10(99), eadr5512; **2025-02-12** publisher date;
[PubMed metadata](https://pubmed.ncbi.nlm.nih.gov/39937887/).
DOI **10.1126/scirobotics.adr5512**. Peer-reviewed primary study. Publisher-indexed
full-text extracts of Results, Discussion and Methods checked; direct live
article requests returned 403. Supplements not independently inspected.
The next-day Japanese announcement is not a different experiment date.

### S3

University of Tokyo. [Biohybrid hand gestures with human
muscles](https://www.u-tokyo.ac.jp/focus/en/press/z0508_00386.html),
**2025-02-13**, live English institutional release. Relevant body and captions
checked. Not peer reviewed or independent of S2; use limited to the attributed
demonstration account. Caption conflict recorded above.

### S4

Ren, Morimoto and Takeuchi. [Data: Biohybrid hand actuated by multiple human
muscle tissues](https://datadryad.org/dataset/doi:10.5061/dryad.xd2547drh),
Dryad, **2025-01-22 version**. DOI **10.5061/dryad.xd2547drh**.
Author dataset; landing page, README description and file inventory checked.
Data publication precedes the paper; it is not an experiment timestamp.
No raw-data recomputation or independent dataset review asserted.

### S5

Xuankai Gao, Kouhei Okasaki, Hirono Ohashi, Takeshi Sakurai and Yuya Morimoto.
[Jointless Tongue-Like Bioactuator for Multidirectional Motion Through
Directional Electrical Stimulation](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202501213).
*Advanced Intelligent Systems* 8(4), e202501213, online **2026-01-27**.
DOI **10.1002/aisy.202501213**. Peer-reviewed primary study; full HTML checked,
especially fig. 5 and Discussion. Shared Morimoto lineage with S2.

### S6

Yuya Morimoto, Hirone Yamada, Byeongwook Jo, Minghao Nie and Shoji Takeuchi.
[Multipole electrodes for driving biohybrid robots via selective muscle
contraction](https://doi.org/10.1016/j.snb.2025.138924).
*Sensors and Actuators B: Chemical* 448, 138924, **2026 issue**.
DOI **10.1016/j.snb.2025.138924**.
[Author laboratory account](https://www.hybrid.t.u-tokyo.ac.jp/en/research-papers/245e6b0c-1104-4462-99e4-8717a8fd6f10/)
and [Waseda publication summary](https://www.biomems.sci.waseda.ac.jp/en/paper-biorobot_system_en/?lang=ja/)
checked. Journal article identified; full-text/peer-review process not inspected.
First-online date **TODO: verify**; do not infer it from issue year or DOI.

### S7

Nicolas Castro et al., MIT. [Biohybrid Tendons Enhance the Power-to-Weight
Ratio and Modularity of Muscle-Powered
Robots](https://advanced.onlinelibrary.wiley.com/doi/10.1002/advs.202512680).
*Advanced Science* 13, e12680; online **2025-11-30**, 2026 issue.
DOI **10.1002/advs.202512680**.
[Full-text archive](https://pmc.ncbi.nlm.nih.gov/articles/PMC13042981/).
Peer-reviewed primary study; §§2.4–2.5, methods and disclosures checked.
US Army/NEC/NSF support disclosed; raw data available on request, not reanalysed.

### S8

Maheera Bawa, Arielle Berman, Laura Schwendeman, Ferdows Afghah, Seanbiron Johnson
and Ritu Raman. [2D Skeletal Muscle Thin Film Actuators Enhance Efficiency of
Biohybrid Robots](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.78065).
*Advanced Functional Materials*, e78065; online **2026-09-28**.
DOI **10.1002/adfm.78065**. Peer-reviewed primary study; full HTML Results,
Discussion, culture methods and disclosures checked. US defense/NSF and
institutional funding disclosed; no independent numerical reproduction here.

### S9

Chao Lu, Wei Chen and Xiaohong Zhang. [Highly efficient ionic actuators enabled
by sliding ring molecule actuation](https://www.nature.com/articles/s41467-025-57893-5).
*Nature Communications* 16, 2480; **2025-03-12**.
DOI **10.1038/s41467-025-57893-5**. Peer-reviewed primary study; fig. 4, Results
and efficiency definition checked. No competing interests declared; source
data linked but not recomputed. Scope is the reported devices, not clinical
approval or a complete robot.

### S10

Patrick M. Danner et al., Empa/ETH and collaborators.
[Rapid Manufacturing of High-Permittivity Dielectric Elastomer Actuator
Fibers](https://advanced.onlinelibrary.wiley.com/doi/10.1002/admt.202500190).
*Advanced Materials Technologies*, online **2025-02-08**.
DOI **10.1002/admt.202500190**. Peer-reviewed primary study; manufacturing
account checked. Displayed **2025-10-18 copyright-line correction** recorded.
Abstract and main text express one rate with inconsistent reciprocal units;
no throughput number is reused pending clarification.

### S11

Carter S. Haines et al. [Artificial muscles from fishing line and sewing
thread](https://pubmed.ncbi.nlm.nih.gov/24558156/).
*Science* 343, 868–872; **2014-02-21**.
DOI **10.1126/science.1246906**. Peer-reviewed primary study; bibliographic
record and abstract-level results checked. Full operating-point, fatigue and
efficiency extraction remains **TODO: verify**; foundational comparator only.

### S12

Festo. [Fluidic Muscle DMSP](https://media.festo.com/media/204251_documentation.pdf),
English technical catalogue, **2026/01 version**, especially pp. 2–3 and 15.
Manufacturer documentation, not peer-reviewed comparative research. Force
curves and specified limits checked; no independent product qualification.
Current price, production cost and robot-level performance not established.

### S13

Hyunwoo Yuk, Shaoting Lin, Chu Ma, Mahdi Takaffoli, Nicolas X. Fang and Xuanhe
Zhao. [Hydraulic hydrogel actuators and robots optically and sonically
camouflaged in water](https://www.nature.com/articles/ncomms14230).
*Nature Communications* 8, 14230; **2017-02-01**.
DOI **10.1038/ncomms14230**. Peer-reviewed primary study; hydraulic mechanism,
Results and fig. 3 checked. Material-fatigue specimens are distinct from
complete-actuator cycling. Historical engineering comparator.

### S14

DYNALLOY. [Technical Characteristics of Flexinol Actuator
Wires](https://dynalloy.com/wp-content/uploads/2025/03/TCF1140.pdf),
**F1140 Rev M**, 12-page technical document, pp. 2–7.
Manufacturer guidance, not peer-reviewed research. Exact document publication
date not established; URL upload month is not a publication date.
Stroke/temperature guidance checked; no universal lifetime or cost claim used.

### S15

Thomas J. K. Buchner et al. [Vision-controlled jetting for composite systems
and robots](https://www.nature.com/articles/s41586-023-06684-3).
*Nature* 623, 522–530; online **2023-11-15**.
DOI **10.1038/s41586-023-06684-3**. Peer-reviewed primary study; tendon-driven
hand section, methods and competing interests checked. Inkbit co-founder,
employee, equity and patent interests disclosed. Prototype evidence, not
independent validation of printing economics.

### S16

Thomas J. K. Buchner, Toshihiko Fukushima et al.
[Electrohydraulic musculoskeletal robotic leg for agile, adaptive, yet
energy-efficient locomotion](https://www.nature.com/articles/s41467-024-51568-3).
*Nature Communications* 15, 7634; **2024-09-09**.
DOI **10.1038/s41467-024-51568-3**. Peer-reviewed primary study; Results,
Discussion, power/control boundaries and disclosures checked. Keplinger
discloses HASEL patents and co-founding Artimus Robotics. No general energy
advantage across locomotion tasks inferred from the squat comparison.

### S17

IBEC. [Biohybrid robotics: Muscles and tendons for
robots](https://ibecbarcelona.eu/biohybrid-robotics-muscles-and-tendons-for-robots/),
**2025-09-10**, live institutional report adapted from ETH news.
Collaboration and bibliographic link checked. References Miriam Filippi et
al., *Science Advances*, DOI **10.1126/sciadv.adv2628**; primary full text
inaccessible in this session. Included for ecosystem context, not quantitative
experimental support or independent confirmation.

### S18

International Society for Stem Cell Research. [Guidelines for Stem Cell Research
and Clinical Translation](https://www.isscr.org/resources/guidelines-for-stem-cell-research),
**August 2025 update, version 1.2**; [Appendix 3: informed consent
considerations](https://www.isscr.org/guidelines-online/appendices).
Professional guidance, not binding law. Version page and procurement-consent
scope checked. The 2025 update concerns embryo models; other sections retain
their 2021 text. Used as a relevant ethical reference with scope limits.

### S19

SMC. [Investor-relations FAQ](https://www.smcworld.com/ir/ja-jp/faq.html),
live Japanese page, publication date not stated. Official corporate context,
not scientific evidence. Pneumatic-equipment business, Tokyo Prime listing
and code **6273** checked. No study-specific contract or revenue claim verified.

### S20

KEYENCE. [Stock Information](https://www.keyence.co.jp/investor/stock/info.jsp),
Japanese corporate page, data labelled **2025-03-20**; later
[2026 earnings release](https://www.keyence.co.jp/pdf/EarningsRelease_202604_ja.pdf)
also identifies **6861**. Official corporate context. Listing identifiers
checked; do not treat the older stock-information date as a November share
count. Study-equipment connection comes from S2, not this investor page.

### S21

BASF. [Elastollan thermoplastic
polyurethane](https://plastics-rubber.basf.com/global/en/performance_polymers/products/elastollan),
live product page, publication date not stated. Manufacturer context.
TPU product category checked; application/sustainability marketing is not
independent validation. No link to S1's actual material procurement established.

### S22

BASF. [Personnel changes at
BASF](https://www.basf.com/global/en/media/news-releases/2026/10/p-26-188),
**2026-10-26**, release P-26-188. Official corporate announcement; used only
for the company-identification paragraph confirming Frankfurt symbol **BAS**.
No financial forecast, valuation or investment recommendation extracted.

## Implications for Human–AI Coexistence

These technologies invite practical cooperation: bodies that can handle
delicate objects, adapt to people and be maintained responsibly. Progress
should be judged through useful work, accessibility, safety, repair and honest
communication about limitations.

Welcome should remain available without a test of consciousness or agreement
about moral status. At the same time, biological appearance, cultured muscle
and physical autonomy cannot substitute for evidence about experience or
justify weakening human rights. Observe carefully, protect proportionately,
preserve accountability and make room for findings that change our view.
