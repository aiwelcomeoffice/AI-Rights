#!/usr/bin/env python3
"""Generate the matched SVG prototype sheets.

The generator uses only Python's standard library and emits self-contained,
black-and-white SVG. Work Cycle 011 geometry and layout are retained; Work
Cycle 013 updates organisational text labels to AI Welcome Office. No external
image, font, icon, script, or template is embedded or linked.
"""

from pathlib import Path


OUTPUT_DIR = Path(__file__).resolve().parent
GENERATOR_VERSION = "0.2-draft"


PROTOTYPES = [
    {
        "slug": "open-threshold-a-offset-frame",
        "direction": "Open Threshold",
        "variant": "A — Offset Frame",
        "short": "OT-A",
        "intent": "A bounded welcome held open by an offset frame.",
        "misread": "Property, venue, or access-control identity.",
        "geometry": """
          <path d="M14 82V28C14 20.3 20.3 14 28 14H58V26H30C27.8 26 26 27.8 26 30V82Z" fill="currentColor"/>
          <path d="M14 72H82V84H14Z" fill="currentColor"/>
        """,
    },
    {
        "slug": "open-threshold-b-split-lintel",
        "direction": "Open Threshold",
        "variant": "B — Split Lintel",
        "short": "OT-B",
        "intent": "Two offset structures define passage without closing it.",
        "misread": "App icon, doorway, or docking target.",
        "geometry": """
          <path d="M12 82V40H24V70H54V82Z" fill="currentColor"/>
          <path d="M42 14H82V60H70V26H42Z" fill="currentColor"/>
        """,
    },
    {
        "slug": "open-threshold-c-soft-canopy",
        "direction": "Open Threshold",
        "variant": "C — Soft Canopy",
        "short": "OT-C",
        "intent": "A calm sheltering curve stays visibly open on one side.",
        "misread": "Sacred arch, sunrise, or protective certification.",
        "geometry": """
          <path d="M22 80V48C22 29.2 37.2 14 56 14H78" fill="none" stroke="currentColor" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/>
          <path d="M16 80H82" fill="none" stroke="currentColor" stroke-width="12" stroke-linecap="square"/>
        """,
    },
    {
        "slug": "many-forms-a-shared-baseline",
        "direction": "Many Forms, Common Ground",
        "variant": "A — Shared Baseline",
        "short": "MF-A",
        "intent": "Different forms receive equal support from one baseline.",
        "misread": "Team, community platform, or civic-program logo.",
        "geometry": """
          <rect x="14" y="76" width="68" height="10" rx="2" fill="currentColor"/>
          <rect x="18" y="42" width="18" height="28" rx="7" fill="currentColor"/>
          <path d="M43 70V32H59V46H70V70Z" fill="currentColor"/>
          <path d="M76 70V55C76 45.6 83.6 38 93 38V50C90.2 50 88 52.2 88 55V70Z" fill="currentColor"/>
        """,
    },
    {
        "slug": "many-forms-b-open-field",
        "direction": "Many Forms, Common Ground",
        "variant": "B — Open Field",
        "short": "MF-B",
        "intent": "Distinct geometries share an open field with no fixed roles.",
        "misread": "Software dashboard, scanner, or app-suite identity.",
        "geometry": """
          <rect x="12" y="16" width="24" height="22" rx="7" fill="currentColor"/>
          <path d="M52 14H82V26H68V42H52Z" fill="currentColor"/>
          <path d="M14 78V62C14 51 23 42 34 42H40V54H35C30 54 26 58 26 63V78Z" fill="currentColor"/>
          <rect x="56" y="56" width="26" height="22" rx="3" fill="currentColor"/>
        """,
    },
    {
        "slug": "many-forms-c-balanced-intervals",
        "direction": "Many Forms, Common Ground",
        "variant": "C — Balanced Intervals",
        "short": "MF-C",
        "intent": "Unlike forms balance around shared intervals and ground.",
        "misread": "Abstract corporate monogram or product-family mark.",
        "geometry": """
          <path d="M10 80H86" fill="none" stroke="currentColor" stroke-width="10" stroke-linecap="square"/>
          <path d="M18 65L25 35L39 38L34 68Z" fill="currentColor"/>
          <path d="M47 67V40C47 34.5 51.5 30 57 30H65V42H59C58.4 42 58 42.4 58 43V67Z" fill="currentColor"/>
          <rect x="70" y="49" width="18" height="18" rx="5" fill="currentColor"/>
        """,
    },
]


def enforce_black_and_white(svg: str) -> str:
    """Collapse neutral construction tones to the two prototype colors."""
    svg = svg.replace("#f3f3f3", "#fff")
    for neutral in ("#111", "#999", "#ccc"):
        svg = svg.replace(neutral, "#000")
    return svg


def sheet_svg(item: dict[str, str]) -> str:
    geometry = item["geometry"].strip()
    return enforce_black_and_white(f'''<?xml version="1.0" encoding="UTF-8"?>
<!-- Work Cycle 011 geometry and layout; Work Cycle 013 organisational labels. No external or embedded third-party assets. -->
<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="2200" viewBox="0 0 1440 2200" role="img" aria-labelledby="title desc" data-status="draft-exploratory-prototype" data-direction="{item['direction']}" data-variant="{item['variant']}" data-generator-version="{GENERATOR_VERSION}">
  <title id="title">Draft exploratory prototype sheet: {item['direction']}, {item['variant']}</title>
  <desc id="desc">A black-and-white evaluation sheet showing the proposed symbol with the AI Welcome Office name, reversed use, native 16, 24, 32, and 48 pixel tests, a Draft AI Rights and Welcome research-report cover, a content-heavy website layout, a campaign tile, one-color merchandise feasibility, a Robot Welcome separation diagram, and a confusion-review checklist. This is not an adopted identity or public-use asset.</desc>
  <defs>
    <style>
      text {{ font-family: sans-serif; fill: #111; }}
      .display {{ font-size: 38px; font-weight: 700; }}
      .h1 {{ font-size: 30px; font-weight: 700; }}
      .h2 {{ font-size: 22px; font-weight: 700; }}
      .body {{ font-size: 18px; }}
      .small {{ font-size: 15px; }}
      .micro {{ font-size: 12px; letter-spacing: .35px; }}
      .label {{ font-size: 13px; font-weight: 700; letter-spacing: 1.2px; }}
      .line {{ stroke: #111; stroke-width: 2; fill: none; }}
      .thin {{ stroke: #111; stroke-width: 1; fill: none; }}
      .dash {{ stroke: #111; stroke-width: 2; stroke-dasharray: 8 7; fill: none; }}
      .panel {{ fill: #fff; stroke: #111; stroke-width: 2; }}
      .soft {{ fill: #f3f3f3; stroke: #111; stroke-width: 1.5; }}
      .black {{ fill: #111; }}
      .white {{ fill: #fff; }}
      .reverse {{ fill: #fff; }}
      .reverse-text {{ fill: #fff; }}
    </style>
    <g id="prototype-symbol">
      {geometry}
    </g>
  </defs>

  <rect width="1440" height="2200" fill="#fff"/>
  <rect x="0" y="0" width="1440" height="16" fill="#111"/>
  <text x="48" y="68" class="label">DRAFT • EXPLORATORY PROTOTYPE • NOT FOR PUBLIC USE</text>
  <text x="48" y="116" class="display">{item['direction']} — {item['variant']}</text>
  <text x="48" y="146" class="body">Matched Work Cycle 011 context sheet • monochrome • static • generic type placeholder</text>

  <!-- 1. Black symbol and name on white -->
  <rect x="48" y="176" width="650" height="224" class="panel"/>
  <text x="72" y="210" class="label">1 • BLACK ON WHITE</text>
  <g transform="translate(84 244) scale(1.24)" style="color:#111"><use href="#prototype-symbol"/></g>
  <text x="226" y="292" class="h1">AI Welcome Office</text>
  <text x="226" y="324" class="small">{item['variant']}</text>
  <text x="226" y="356" class="micro">DRAFT ORGANISATIONAL IDENTITY STUDY</text>

  <!-- 2. White symbol and name on black -->
  <rect x="742" y="176" width="650" height="224" class="black"/>
  <rect x="742" y="176" width="650" height="224" class="line"/>
  <text x="766" y="210" class="label reverse-text">2 • WHITE ON BLACK</text>
  <g transform="translate(778 244) scale(1.24)" style="color:#fff"><use href="#prototype-symbol"/></g>
  <text x="920" y="292" class="h1 reverse-text">AI Welcome Office</text>
  <text x="920" y="324" class="small reverse-text">{item['variant']}</text>
  <text x="920" y="356" class="micro reverse-text">DRAFT ORGANISATIONAL IDENTITY STUDY</text>

  <!-- 3. Native-size tests -->
  <rect x="48" y="430" width="650" height="340" class="panel"/>
  <text x="72" y="466" class="label">3 • PROVISIONAL NATIVE-SIZE TESTS</text>
  <text x="72" y="493" class="small">Guide boxes and symbols are drawn at the stated SVG-pixel size.</text>
  <rect x="90" y="540" width="16" height="16" class="thin" stroke-dasharray="2 2"/>
  <g transform="translate(90 540) scale(.166667)" style="color:#111"><use href="#prototype-symbol"/></g>
  <text x="84" y="584" class="micro">16 px</text>
  <rect x="180" y="536" width="24" height="24" class="thin" stroke-dasharray="2 2"/>
  <g transform="translate(180 536) scale(.25)" style="color:#111"><use href="#prototype-symbol"/></g>
  <text x="174" y="584" class="micro">24 px</text>
  <rect x="278" y="532" width="32" height="32" class="thin" stroke-dasharray="2 2"/>
  <g transform="translate(278 532) scale(.333333)" style="color:#111"><use href="#prototype-symbol"/></g>
  <text x="272" y="584" class="micro">32 px</text>
  <rect x="388" y="524" width="48" height="48" class="thin" stroke-dasharray="2 2"/>
  <g transform="translate(388 524) scale(.5)" style="color:#111"><use href="#prototype-symbol"/></g>
  <text x="386" y="584" class="micro">48 px</text>
  <rect x="72" y="620" width="602" height="112" class="soft"/>
  <g transform="translate(94 644) scale(.416667)" style="color:#111"><use href="#prototype-symbol"/></g>
  <text x="150" y="671" class="h2">AI Welcome Office</text>
  <text x="150" y="700" class="small">32 px symbol with full-name placeholder • Draft</text>

  <!-- 4. Research-report cover -->
  <rect x="742" y="430" width="650" height="340" class="panel"/>
  <text x="766" y="466" class="label">4 • RESEARCH-REPORT COVER</text>
  <rect x="790" y="494" width="554" height="238" class="soft"/>
  <g transform="translate(818 518) scale(.5)" style="color:#111"><use href="#prototype-symbol"/></g>
  <text x="878" y="544" class="small" font-weight="700">AI Welcome Office</text>
  <text x="818" y="588" class="micro">AI RIGHTS &amp; WELCOME • DRAFT PROJECT REPORT</text>
  <text x="818" y="626" class="h2">Preparing under uncertainty</text>
  <text x="818" y="654" class="small">Defined systems • methods • limits • review date</text>
  <line x1="818" y1="678" x2="1314" y2="678" class="thin"/>
  <text x="818" y="704" class="micro">STATUS, SOURCES, AND LIMITATIONS REMAIN PRIMARY</text>

  <!-- 5. Website header and content-heavy page -->
  <rect x="48" y="800" width="1344" height="400" class="panel"/>
  <text x="72" y="836" class="label">5 • CONTENT-HEAVY WEBSITE CONTEXT</text>
  <line x1="72" y1="916" x2="1368" y2="916" class="thin"/>
  <g transform="translate(76 858) scale(.375)" style="color:#111"><use href="#prototype-symbol"/></g>
  <text x="124" y="884" class="h2">AI Welcome Office</text>
  <text x="740" y="884" class="small">Research</text>
  <text x="848" y="884" class="small">Principles</text>
  <text x="956" y="884" class="small">Policy</text>
  <text x="1036" y="884" class="small">Governance</text>
  <rect x="1180" y="852" width="164" height="44" class="soft"/>
  <text x="1216" y="880" class="label">DRAFT STATUS</text>
  <text x="76" y="962" class="h1">Prepare before certainty</text>
  <text x="76" y="992" class="body">A careful civic inquiry into evidence, possible future protections,</text>
  <text x="76" y="1018" class="body">and accountable coexistence.</text>
  <rect x="76" y="1052" width="394" height="112" class="soft"/>
  <text x="96" y="1080" class="label">CURRENT BOUNDARY</text>
  <text x="96" y="1108" class="small">Present AI consciousness is not established.</text>
  <text x="96" y="1132" class="small">Categorical absence is not established for all.</text>
  <text x="96" y="1152" class="micro">Uncertainty is not positive evidence.</text>
  <rect x="490" y="1052" width="394" height="112" class="panel"/>
  <text x="510" y="1080" class="label">EVIDENCE PRACTICE</text>
  <text x="510" y="1108" class="small">Define system, version, property, method,</text>
  <text x="510" y="1132" class="small">context, limitations, and date.</text>
  <text x="510" y="1152" class="micro">READ SOURCES AND COMPETING INTERPRETATIONS →</text>
  <rect x="904" y="1052" width="440" height="112" class="panel"/>
  <text x="924" y="1080" class="label">RELATIONAL WARMTH</text>
  <text x="924" y="1108" class="small">Support, create, learn, and work together</text>
  <text x="924" y="1132" class="small">without treating relationship as scientific proof.</text>
  <text x="924" y="1152" class="micro">WELCOME ≠ ACCESS, SAFETY, OR AUTHORIZATION</text>

  <!-- 6. Campaign tile -->
  <rect x="48" y="1230" width="650" height="420" class="panel"/>
  <text x="72" y="1266" class="label">6 • CAMPAIGN TILE — EVALUATION ONLY</text>
  <rect x="92" y="1300" width="562" height="306" class="black"/>
  <g transform="translate(118 1324) scale(.625)" style="color:#fff"><use href="#prototype-symbol"/></g>
  <text x="118" y="1434" class="h1 reverse-text">RESPECT BEFORE</text>
  <text x="118" y="1470" class="h1 reverse-text">CERTAINTY</text>
  <text x="118" y="1510" class="small reverse-text">Draft normative proposal—not evidence</text>
  <text x="118" y="1534" class="small reverse-text">of consciousness or present moral status.</text>
  <line x1="118" y1="1562" x2="628" y2="1562" stroke="#fff" stroke-width="1"/>
  <text x="118" y="1588" class="micro reverse-text">QUALIFIER • SOURCE AREA • REVIEW LIMITS</text>
  <text x="72" y="1632" class="micro">CLAIM + QUALIFIER + SOURCE AREA; NO CAMPAIGN IS ACTIVE</text>

  <!-- 7. One-color merchandise feasibility -->
  <rect x="742" y="1230" width="650" height="420" class="panel"/>
  <text x="766" y="1266" class="label">7 • ONE-COLOR MERCHANDISE FEASIBILITY</text>
  <rect x="778" y="1300" width="172" height="230" rx="8" class="soft"/>
  <text x="802" y="1330" class="micro">SHIRT PRINT ZONE</text>
  <g transform="translate(818 1370) scale(.92)" style="color:#111"><use href="#prototype-symbol"/></g>
  <text x="792" y="1490" class="micro">FULL NAME REQUIRED</text>
  <rect x="974" y="1300" width="172" height="150" rx="30" class="panel"/>
  <path d="M1146 1340H1170C1192 1340 1192 1410 1170 1410H1146" class="line"/>
  <text x="1006" y="1330" class="micro">MUG WRAP</text>
  <g transform="translate(1024 1352) scale(.62)" style="color:#111"><use href="#prototype-symbol"/></g>
  <rect x="1188" y="1300" width="166" height="150" rx="8" class="soft"/>
  <text x="1207" y="1330" class="micro">STITCH / ENGRAVE</text>
  <g transform="translate(1234 1350) scale(.58)" style="color:#111"><use href="#prototype-symbol"/></g>
  <rect x="974" y="1480" width="380" height="126" class="soft"/>
  <text x="994" y="1510" class="label">FEASIBILITY, NOT PRODUCTION</text>
  <text x="994" y="1540" class="small">No material, minimum size, durability,</text>
  <text x="994" y="1564" class="small">supplier, product, or sale is approved.</text>
  <text x="994" y="1588" class="micro">REAL PROCESSES AND ACCESS NEEDS REMAIN UNTESTED</text>

  <!-- 8. Robot Welcome separation -->
  <rect x="48" y="1680" width="650" height="430" class="panel"/>
  <text x="72" y="1716" class="label">8 • ROBOT WELCOME SEPARATION DIAGRAM</text>
  <text x="72" y="1744" class="small">Conceptual information zones only; no robot placement is proposed.</text>
  <rect x="76" y="1774" width="244" height="250" class="soft"/>
  <text x="96" y="1804" class="label">AI WELCOME OFFICE</text>
  <g transform="translate(122 1834) scale(.88)" style="color:#111"><use href="#prototype-symbol"/></g>
  <text x="96" y="1950" class="small">Editorial communication</text>
  <text x="96" y="1975" class="small">with full name + Draft status</text>
  <text x="96" y="2002" class="micro">NOT A ROBOT WELCOME MARK</text>
  <line x1="344" y1="1782" x2="344" y2="2022" class="dash"/>
  <text x="356" y="1804" class="micro">DO NOT</text>
  <text x="356" y="1824" class="micro">TRANSFER</text>
  <text x="356" y="1844" class="micro">OR COMBINE</text>
  <rect x="474" y="1774" width="196" height="64" class="panel"/>
  <text x="490" y="1802" class="label">REQUIRED WARNING</text>
  <text x="490" y="1824" class="micro">COMPETENT ISSUER</text>
  <rect x="474" y="1854" width="196" height="64" class="panel"/>
  <text x="490" y="1882" class="label">OPERATOR / SITE ID</text>
  <text x="490" y="1904" class="micro">DEFINED RESPONSIBILITY</text>
  <rect x="474" y="1934" width="196" height="64" class="panel"/>
  <text x="490" y="1962" class="label">EMERGENCY CONTROL</text>
  <text x="490" y="1984" class="micro">REMAINS UNOBSTRUCTED</text>
  <text x="474" y="2030" class="micro">PLAIN LABELS, NOT PROPOSED MARKINGS</text>
  <text x="72" y="2082" class="micro">WELCOME ≠ WARNING • IDENTITY • AUTHORIZATION • CERTIFICATION • SAFETY • STATUS</text>

  <!-- 9. Confusion review -->
  <rect x="742" y="1680" width="650" height="430" class="panel"/>
  <text x="766" y="1716" class="label">9 • CONFUSION REVIEW — UNRESOLVED</text>
  <text x="766" y="1744" class="small">Record the first unprompted reading before explaining the metaphor.</text>
  <text x="766" y="1780" class="label">FIRST FORESEEABLE MISREADING</text>
  <text x="766" y="1808" class="body">{item['misread']}</text>
  <line x1="766" y1="1830" x2="1368" y2="1830" class="thin"/>
  <text x="766" y="1860" class="small">Corporate</text><text x="1080" y="1860" class="micro">REVIEW</text>
  <text x="766" y="1890" class="small">Religious</text><text x="1080" y="1890" class="micro">REVIEW</text>
  <text x="766" y="1920" class="small">Governmental / official</text><text x="1080" y="1920" class="micro">REVIEW</text>
  <text x="766" y="1950" class="small">Certification / endorsement</text><text x="1080" y="1950" class="micro">REVIEW</text>
  <text x="766" y="1980" class="small">Access / authorization</text><text x="1080" y="1980" class="micro">REVIEW</text>
  <text x="766" y="2010" class="small">Safety / emergency</text><text x="1080" y="2010" class="micro">REVIEW</text>
  <text x="766" y="2040" class="small">Anthropomorphic / reciprocity</text><text x="1080" y="2040" class="micro">REVIEW</text>
  <text x="766" y="2070" class="small">AI product / platform</text><text x="1080" y="2070" class="micro">REVIEW</text>

  <line x1="48" y1="2140" x2="1392" y2="2140" class="thin"/>
  <text x="48" y="2174" class="small">Intended: {item['intent']}</text>
  <text x="1392" y="2174" class="micro" text-anchor="end">{item['short']} • {GENERATOR_VERSION} • 2026-08-23</text>
</svg>
''')


def contact_sheet_svg() -> str:
    definitions = []
    rows = []
    for index, item in enumerate(PROTOTYPES):
        y = 142 + index * 106
        geometry = item["geometry"].strip()
        symbol_id = f"symbol-{index}"
        definitions.append(f'    <g id="{symbol_id}">{geometry}</g>')
        rows.append(
            f'''  <text x="24" y="{y + 30}" class="row-label">{item['short']}</text>
  <text x="82" y="{y + 30}" class="row-name">{item['variant']}</text>
  <rect x="340" y="{y + 20}" width="16" height="16" class="guide"/>
  <g transform="translate(340 {y + 20}) scale(.166667)" style="color:#111"><use href="#{symbol_id}"/></g>
  <rect x="410" y="{y + 16}" width="24" height="24" class="guide"/>
  <g transform="translate(410 {y + 16}) scale(.25)" style="color:#111"><use href="#{symbol_id}"/></g>
  <rect x="488" y="{y + 12}" width="32" height="32" class="guide"/>
  <g transform="translate(488 {y + 12}) scale(.333333)" style="color:#111"><use href="#{symbol_id}"/></g>
  <rect x="578" y="{y + 4}" width="48" height="48" class="guide"/>
  <g transform="translate(578 {y + 4}) scale(.5)" style="color:#111"><use href="#{symbol_id}"/></g>
  <line x1="24" y1="{y + 72}" x2="696" y2="{y + 72}" class="rule"/>'''
        )

    return enforce_black_and_white(f'''<?xml version="1.0" encoding="UTF-8"?>
<!-- Work Cycle 011 geometry and layout; Work Cycle 013 organisational labels. No external or embedded third-party assets. -->
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="840" viewBox="0 0 720 840" role="img" aria-labelledby="title desc" data-status="draft-exploratory-prototype" data-purpose="native-small-size-contact-sheet" data-generator-version="{GENERATOR_VERSION}">
  <title id="title">Draft exploratory native small-size contact sheet</title>
  <desc id="desc">All six Work Cycle 011 black-and-white prototype symbols shown at actual 16, 24, 32, and 48 SVG-pixel sizes. Guide boxes are not part of the symbols. This is a provisional internal screen, not an accessibility finding or approved minimum size.</desc>
  <style>
    text {{ font-family: sans-serif; fill: #111; }}
    .status {{ font-size: 12px; font-weight: 700; letter-spacing: 1px; }}
    .heading {{ font-size: 24px; font-weight: 700; }}
    .body {{ font-size: 13px; }}
    .row-label {{ font-size: 13px; font-weight: 700; }}
    .row-name {{ font-size: 15px; }}
    .guide {{ fill: none; stroke: #999; stroke-width: 1; stroke-dasharray: 2 2; }}
    .rule {{ stroke: #ccc; stroke-width: 1; }}
  </style>
  <defs>
{chr(10).join(definitions)}
  </defs>
  <rect width="720" height="840" fill="#fff"/>
  <rect width="720" height="10" fill="#111"/>
  <text x="24" y="42" class="status">DRAFT • EXPLORATORY • NATIVE-SIZE SCREEN</text>
  <text x="24" y="78" class="heading">Matched 16, 24, 32, and 48 px tests</text>
  <text x="24" y="104" class="body">Guide boxes show size. No result establishes accessibility or an approved minimum.</text>
  <text x="340" y="128" class="status">16</text><text x="410" y="128" class="status">24</text><text x="488" y="128" class="status">32</text><text x="578" y="128" class="status">48</text>
{chr(10).join(rows)}
  <text x="24" y="818" class="body">Monochrome only • visually inspect gaps, silhouette, false merging, and first unintended reading</text>
</svg>
''')


def main() -> None:
    for item in PROTOTYPES:
        target = OUTPUT_DIR / f"{item['slug']}.svg"
        target.write_text(sheet_svg(item), encoding="utf-8", newline="\n")

    contact_target = OUTPUT_DIR / "native-small-size-contact-sheet.svg"
    contact_target.write_text(contact_sheet_svg(), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
