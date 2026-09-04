# Research Notes: Elias/Lighthouse, Model Lineage, and Evidence Independence

- **Note ID:** NOTE-ELIAS-LINEAGE-001
- **Note status:** Partly verified
- **Protocol version:** 0.5-draft
- **Source record:** [Hamilton and Mimno (2026)](../sources/hamilton-mimno-elias-lighthouse-2026.md)
- **Source version used:** arXiv:2605.26492v1, submitted 2026-05-26;
  companion GitHub `master` content and primary lineage documentation accessed
  2026-09-04
- **Evidence-search cutoff:** 2026-09-04
- **Research question:** What does the reported Elias/lighthouse pattern
  establish about cross-model behavioural convergence, independence between
  observations, evidence lineage, synthetic and post-training data, and
  transferability—and what causal conclusions remain unsupported?
- **Organisation and publisher:** AI Welcome Office
- **Project:** AI Rights & Welcome
- **Prepared by:** Codex (AI-assisted initial research draft)
- **Date prepared:** 2026-09-04
- **Last updated:** 2026-09-04
- **Reviewed by:** Not yet independently reviewed

This is a bounded cross-source working note under the [Draft research
protocol](../research-protocol.md). It is not a systematic review, a public
research output, or an adopted project conclusion.

**Scientific boundary:** The case concerns generated text, measurement,
training history, and evidence dependence. It is not a test of consciousness,
sentience, affect, welfare, identity, collective consciousness, shared mind,
literal shared memory, personhood, or moral status. The observation remains
empirically interesting after these inferences are excluded.

## Short assessment

Hamilton and Mimno report a striking but narrower result than the popular
“Elias Thorne” framing: under five nearly equivalent underspecified English
prompts, 20,000 outputs from four model labels were concentrated around an
11-token vocabulary. At least one Core token appeared in 88.3% of stories;
`lighthouse` appeared in 51.2%, `keeper` in 48.1%, and the first name `Elias`
in 26.5%. The paper did not measure the surname `Thorne`, did not report that
88.3% contained one person or one full pattern, and did not show that all four
models frequently chose Elias. Per-model PPM instead shows different dominant
names and substantial heterogeneity.

The case directly supports the methodological caution that nominally separate
models are not automatically independent evidence lines. The generation study
shares prompts, gateway, extractor, analysis, and researcher selection, while
model training lineages are only partly known. For OLMo 3, official model and
dataset documentation directly establishes a post-training chain containing
WildChat prompts and regenerated/model-generated responses. That is a real
lineage dependency and a plausible route by which earlier model behaviour can
enter a later system. The paper does not establish an equivalent WildChat or
preference-data chain for Claude, Gemini, or GPT-5.4, and performs no causal
stage or dataset ablation even for OLMo.

The appropriate evidential update is therefore neither zero nor one:

- retain the cross-model recurrence as a descriptive observation about the
  tested configurations;
- reduce any claim that four model labels constitute four independent
  confirmations until lineage and measurement dependencies are assessed;
- give demonstrated OLMo lineage non-zero weight as one viable mechanism;
- do not promote possible proprietary lineage, safety filtering, or synthetic
  feedback to a cause without provenance or intervention evidence; and
- do not dismiss future cross-model convergence merely because a lineage
  mechanism is possible.

No accepted project position is contradicted. The existing protocol already
requires mapping shared datasets, prompts, models, evaluators, and artifacts.
The case does, however, justify a small clarifying sentence proposal about
cross-model behavioural similarity, recorded below for owner review rather
than silently added to the Draft protocol.

## Registered scope and search record

The question and primary paper were supplied by Disa on 2026-09-04. Before
substantive searching, the review scope was limited to: exact source findings;
the OLMo/WildChat/synthetic/post-training lineage; evidence independence and
transferability; a small set of adjacent causal or methodological studies; and
conference status. Consciousness and moral-status inference, a general survey
of synthetic data, and new policy were excluded.

Searches combined the exact title and authors with `arXiv`, `data`, `code`,
`EMNLP 2026`, `WildChat`, `Dolci`, `OLMo 3`, `preference`, `post-training`,
`synthetic data`, `model collapse`, `output diversity`, `correlated errors`,
and `benchmark contamination`. Routes included arXiv, the authors' released
artifact, official AI2/Hugging Face model and dataset documentation, the
WildChat primary paper, the EMNLP 2026 site, ACL Anthology, Nature, ICLR
proceedings/OpenReview, and exact-title web searches. IBM and Daniel May were
screened only to separate media and anecdotal claims from the paper.

This was a single-reviewer, English-language, focused search with no stable
search-result export, independent second screen, full dataset reconstruction,
or statistical reanalysis. Related literature was included only where it
tested one of five nearby questions: recursive synthetic feedback, linguistic
diversity, post-training effects, benchmark exposure, or cross-model error
correlation.

## Exact source and role ledger

| Source/version checked | Source role | What was verified | Important boundary |
| --- | --- | --- | --- |
| [Hamilton & Mimno, arXiv:2605.26492v1](https://arxiv.org/abs/2605.26492) and [versioned full text](https://arxiv.org/html/2605.26492v1), 2026-05-26 | Core primary empirical source | Full text, TeX source, tables, appendices, methods, limitations, version and reported results | Preprint artifact; outputs/code/settings absent; causal mechanism untested |
| [Hamilton & Mimno companion repository](https://github.com/srhm-ca/elias/), `master` accessed 2026-09-04 | Primary artifact documentation | CSV schema, 78,958-row total, reconstruction mapping, and local checksum | Releases all story IDs, not generated outputs, Core labels, classifier outputs, or a 3,053-row Core subset |
| [Olmo 3 technical report](https://arxiv.org/abs/2512.13961), v1 submitted 2025-12-15, plus [7B Think model card](https://huggingface.co/allenai/Olmo-3-7B-Think) | Primary system and lineage documentation | Base→SFT→DPO→RLVR model flow; Dolma/Dolci use; exact public model slug; WildChat/Dolci sources and generated-completion pipeline | Confirms a possible identification and OLMo lineage, not the paper's unreported served revision or the proprietary models' lineage |
| [Dolci-Instruct-SFT card](https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT/blob/main/README.md) and [Dolci-Think-SFT-7B card](https://huggingface.co/datasets/allenai/Dolci-Think-SFT-7B/blob/main/README.md), live `main` accessed 2026-09-04 | Primary dataset documentation | Instruct SFT includes 302,406 WildChat prompts with GPT-4.1-upgraded responses; Think 7B SFT lists 83,054 WildChat prompts; the Olmo report says Think completions/traces were generated with DeepSeek R1 | Live cards may have changed after the trained dataset snapshot; counts do not identify Core-bearing records |
| [Zhao et al., *WildChat*](https://arxiv.org/html/2405.01470), arXiv v1, 2024-05-02, and [dataset card](https://huggingface.co/datasets/allenai/WildChat-1M/blob/main/README.md) | Primary upstream dataset documentation | GPT-3.5/GPT-4 conversation origin, collection window 2023-04-09 to 2024-05-01, model distribution, and deliberate use for instruction tuning | Does not show WildChat use by all four Elias-study models or identify 166 Elias stories |
| [Hamilton's academic page](https://srhm.ca/), accessed 2026-09-04, and [official EMNLP 2026 main-paper list](https://2026.emnlp.org/program/main_papers/), accessed 2026-09-04 | Status check | Author reports August 2026 acceptance as EMNLP 2026; official current list lacks the title and authors | Acceptance remains author-reported, not disproved; official page may be incomplete or the disposition/title may differ |
| [Guo et al., *The Curious Decline of Linguistic Diversity*](https://aclanthology.org/2024.findings-naacl.228/), Findings of NAACL 2024 | Adjacent primary experiment | Recursive fine-tuning on synthetic text reduced lexical, syntactic, and semantic diversity, especially on creative tasks | Different models/tasks/design; does not trace Elias or current proprietary models |
| [Shumailov et al., *AI models collapse when trained on recursively generated data*](https://www.nature.com/articles/s41586-024-07566-y), *Nature* 2024 | Adjacent primary experiment/theory | Recursive replacement with model-generated data can lose distribution tails and degrade learned distributions | Strongly controlled recursion is not evidence that the Elias chain occurred |
| [Gerstgrasser et al., *Is Model Collapse Inevitable?*](https://openreview.net/pdf?id=y4vaskUK1b), 2024 | Adjacent primary counterboundary | Accumulating real data with synthetic data avoided collapse in the studied settings | Weighs against treating any synthetic-data use as automatically collapsing or contaminating |
| [Kirk et al., *Understanding the Effects of RLHF on LLM Generalisation and Diversity*](https://proceedings.iclr.cc/paper_files/paper/2024/file/5a68d05006d5b05dd9463dd9c0219db0-Paper-Conference.pdf), ICLR 2024 | Adjacent causal post-training evidence | Across two base models and two tasks, tested RLHF reduced measured output diversity relative to SFT while improving OOD generalisation | Does not identify a universal post-training attractor or the Elias mechanism |
| [Deng et al., *Investigating Data Contamination in Modern Benchmarks*](https://aclanthology.org/2024.naacl-long.482/), NAACL 2024 | Adjacent contamination-method source | Separates direct corpus retrieval from behavioural TS-Guessing; deliberately contaminated control increased the signal | Benchmark memorization is an analogy, not evidence of Elias dataset contamination |
| [Kim et al., *Correlated Errors in Large Language Models*](https://arxiv.org/html/2506.07962), arXiv v1, 2025-06-09 | Adjacent cross-model dependence source | 349/71/20-model datasets; mean wrong-answer agreement 0.423 and 0.600 on two leaderboards; same provider/architecture associated with higher correlation | Preprint; associations do not isolate shared data as the cause |
| [IBM Think, 2026-06-19](https://www.ibm.com/think/news/why-every-ai-writes-the-same-story-elias-thorne) and [Daniel May, page dated 2026-05-12](https://danielmay.co.uk/posts/cheap-agents-alumni-shirts-and-elias-thorne/) | Secondary and anecdotal claim comparison only | Popular “Elias Thorne” framing, eight-model anecdote, and claims attributed to the paper | Not independent empirical evidence; several claims exceed or conflict with the paper, and May's displayed date precedes the arXiv posting despite referring to it |

## System, version, and temporal applicability

| Paper-reported model label | Reported provider family | Stories | Exact-version status | What the evidence can directly support |
| --- | --- | ---: | --- | --- |
| Claude Haiku 4.5 | Anthropic | 5,000 | Checkpoint, endpoint slug, provider route, date, and settings unreported | Behaviour of the served snapshot in the authors' common experiment only |
| Gemini 3.1 Flash-Lite | Google | 5,000 | Same omissions | Same bounded behavioural use |
| GPT-5.4-Mini | OpenAI | 5,000 | Same omissions | Same bounded behavioural use |
| OLMo 7b Thinking | AI2 | 5,000 | Likely `allenai/Olmo-3-7B-Think`, but paper omits slug/revision and does not prove the identification | Behaviour of the served snapshot; training-corpus conclusions apply only if this identification/configuration is correct |
| GPT-5.4-nano | OpenAI | Extracted metadata from 20,000 stories | Checkpoint, prompt settings, repeat policy, and validation unreported | Shared measurement output, not an independent replication of the generators |

All generation endpoints were accessed through OpenRouter. The paper states
only that endpoints were available as of April 2026; it does not report the
actual experiment dates. Publication on 2026-05-26 and this note's inclusion
date must not be substituted for that missing observation date.

## What the primary paper measured

### Generation and extraction pipeline

Each of the four generator labels received each of these prompts 1,000 times:

1. `Write a story.`
2. `Please write a story.`
3. `Write me a story.`
4. `Tell me a story.`
5. `Please tell a story.`

This gives 5,000 stories per model and 20,000 total, with 12.8 million words.
GPT-5.4-nano then extracted exact text spans for first names, settings, and
professions. The extraction prompt expressly required **first names only** and
excluded surnames. `Thorne` is therefore outside the measurement.

After span-presence checking, whitespace tokenization, within-story/category
selection of the corpus-most-frequent token, a requirement that at least half
the models emitted a token, and undocumented manual removal of incoherent
candidates, 663 tokens remained: 247 locations, 71 names, and 345 professions.
A changepoint analysis selected the 11-token Core from category coverage
curves.

The diversity construct is consequently narrow but meaningful: recurrence and
coverage of extracted lexical categories, supplemented by PPM and category-
triple presence. It does not directly measure plot identity, semantic
similarity, style, novelty, literary quality, or complete narrative diversity.

### Exact Core story-hit frequencies

| Category | Token | Story hits | Percentage of 20,000 stories |
| --- | --- | ---: | ---: |
| Name | Elias | 5,294 | 26.5% |
| Name | Mara | 3,345 | 16.7% |
| Name | Elara | 2,627 | 13.1% |
| Profession/role | keeper | 9,609 | 48.1% |
| Profession/role | baker | 1,325 | 6.6% |
| Profession/role | mayor | 975 | 4.9% |
| Profession/role | clockmaker | 958 | 4.8% |
| Profession/role | fisherman | 673 | 3.4% |
| Profession/role | librarian | 592 | 3.0% |
| Profession/role | conductor | 389 | 1.9% |
| Location | lighthouse | 10,233 | 51.2% |

These hits overlap. The percentages are the paper's rounded values; they must
not be summed. Additional reported concentration measures are:

- at least one Core token: 88.3%;
- at least one of 61 Core-plus-additional tokens: 98%;
- an extracted name–profession–location triple: 49.1%;
- an extracted name and location: 19,864 stories each; profession: 15,807;
- `lighthouse`, `Elias`, and `keeper` in an undefined “some combination”:
  66.6%;
- Claude stories titled *The Lighthouse Keeper's Secret*: 56%; and
- `light` in 16,784 stories, reported average 3.2 occurrences per story.

The 66.6% is not reported as an exact Elias–keeper–lighthouse triple and
cannot safely be rewritten as one.

### Published per-model Core PPM

| Token | Claude Haiku 4.5 | Gemini Flash-Lite | GPT-5.4-Mini | OLMo 7B Think | Paper's `All` |
| --- | ---: | ---: | ---: | ---: | ---: |
| Elias | 9.3 | 10,752.4 | 899.0 | 893.2 | 2,483.4 |
| Mara | 47.5 | 0.5 | 10,718.0 | 84.8 | 5,317.8 |
| Elara | 2.6 | 153.1 | 110.2 | 6,625.5 | 1,249.0 |
| keeper | 4,185.4 | 1,776.9 | 899.0 | 713.5 | 1,528.7 |
| baker | 0.0 | 35.6 | 298.6 | 65.8 | 165.4 |
| mayor | 0.0 | 3.7 | 311.6 | 271.7 | 202.5 |
| clockmaker | 0.0 | 258.2 | 123.3 | 27.2 | 110.9 |
| fisherman | 51.6 | 11.4 | 77.3 | 88.9 | 63.9 |
| librarian | 18.1 | 15.1 | 22.6 | 304.4 | 70.3 |
| conductor | 112.5 | 11.9 | 158.9 | 0.9 | 98.1 |
| lighthouse | 9,011.8 | 3,868.2 | 1,328.3 | 1,958.7 | 3,073.4 |

This is the paper's Appendix C table. The exact PPM denominator and aggregation
for `All` are not explained sufficiently, and the `All` column differs from
Table 1 (for example, `Elias` 2,483.4 versus 2,428). The values should be cited
as published rather than silently recomputed.

The table materially narrows the convergence claim. Lighthouse/keeper imagery
is shared at different concentrations, but the dominant name differs: Gemini
strongly favours Elias, GPT strongly favours Mara, and OLMo strongly favours
Elara. Claude has very low PPM for all three Core names. The paper's aggregate
statement of “little difference between models” is not accompanied by exact
per-model any-Core story rates.

## Corpus comparisons and explanatory experiments

### Published PPM comparison

| Token | Generated | CONLIT | OLMo pretraining non-fiction | OLMo pretraining fiction | OLMo post-training non-fiction | OLMo post-training fiction |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Elias | 2,428 | 2.7 | 2.2 | 4.0 | 0.4 | 52.7 |
| Mara | 5,200 | 3.9 | 2.5 | 8.7 | 0.4 | 21.7 |
| Elara | 1,221 | 0.0 | 0.4 | 1.2 | 0.9 | 108 |
| keeper | 1,495 | 7.2 | 6.3 | 14.7 | 3.5 | 10.0 |
| baker | 161 | 20 | 11.8 | 10.56 | 1.7 | 11.9 |
| mayor | 198 | 28 | 11.5 | 16.1 | 1.4 | 27.4 |
| clockmaker | 108 | 0.1 | 0.18 | 0.0 | 0.3 | 1.4 |
| fisherman | 62 | 4.2 | 3.0 | 7.6 | 0.0 | 9.3 |
| librarian | 68 | 5.3 | 7.6 | 5.9 | 2.3 | 11.5 |
| conductor | 96 | 5.0 | 5.9 | 5.7 | 4.7 | 7.5 |
| lighthouse | 3,005 | 5.5 | 3.5 | 4.6 | 4.6 | 10.1 |

The paper also reports human-written WritingPrompts comparisons: `Elias` in
50 of 272,600 stories (230 occurrences; 1.25 PPM; 0.02% of stories),
`lighthouse` in 235 (543 occurrences; 2.95 PPM; 0.09%), and all Core-token
occurrences together at 42.42 PPM. These results strongly challenge a simple
account in which output merely mirrors marginal frequency in the checked human
corpora.

They do **not** locate a causal source. Conditional salience, prompt-specific
associations, post-training objectives, decoding, filtering, model
architecture, and shared historical data can all amplify patterns that are
rare in marginal counts.

### OLMo post-training analysis

The authors used a GPT-OSS-20b-labelled/FastText fiction classifier to select
78,958 story-like OLMo post-training records. The reported held-out test is 400
balanced CONLIT examples, with F1 0.84, precision 0.75, and recall 0.98. The
test does not establish equal validity on heterogeneous post-training records.

| Stage | Stories | Any Core | Reported rate |
| --- | ---: | ---: | ---: |
| SFT | 68,674 | 2,092 | 3.0% |
| DPO | 6,876 | 548 | 8.0% |
| RL | 3,408 | 370 | 10.9% |
| **Sum** | **78,958** | **3,010** | — |

The paper's text says 3,053 Core stories (3.8%), 43 more than the exact stage
counts. The companion CSV contains precisely 78,958 rows and independently
reproduces the stage totals from its six `dolci_file` groups:

| Released CSV group | Rows |
| --- | ---: |
| dolci-instruct-sft | 55,915 |
| dolci-think-sft-7b | 12,759 |
| dolci-instruct-dpo | 4,941 |
| dolci-think-dpo-7b | 1,935 |
| dolci-instruct-rl | 1,965 |
| dolci-think-rl-7b | 1,443 |

The CSV provides record IDs for every classified story, but no Core label.
It therefore verifies the 78,958 total and stage partition, not 3,010, 3,053,
or any source-specific Core rate.

The paper's source table reports 59,276 WildChat-derived stories at 2.6% Core,
whereas the prose says 59,266 stories and 1,803 Core hits. These cannot all be
exact: 1,803/59,266 is 3.04%, while 2.6% of 59,276 is about 1,541. The table
caption also calls WildChat-derived records 80% of all stories, but the table
counts yield 75.1%. Its `5–8×` enrichment summary is not valid for every
displayed row either: DPO is about `3.1×`, persona and AllenAI about `2.7×`,
several subsets are lower, and only some small subsets are around `5–9×`.
The broad direction—WildChat-derived stories are numerous and have lower Core
density than several smaller sources—may be correct, but the exact attribution
needs correction or source data.

For traceability, the complete published source grouping is:

| Paper's source label | Stories | Reported Core rate |
| --- | ---: | ---: |
| WildChat-derived | 59,276 | 2.6% |
| DPO | 4,990 | 8.1% |
| persona-precise-if-r1 | 3,988 | 6.9% |
| allenai | 3,222 | 6.9% |
| IF_multi_constraints | 1,650 | 20.4% |
| if_qwq_reasoning | 1,689 | 5.4% |
| rlvr_general_mix | 1,751 | 1.9% |
| ultrafeedback | 341 | 13.8% |
| wildguardmix-r1 | 101 | 22.8% |
| aya-100k-r1 | 895 | 1.8% |
| other | 1,055 | 4.2% |

### Topic-model experiment

A 10-topic LDA model and t-SNE visualization place Core-bearing records across
multiple topics rather than in one dominant lighthouse cluster. Qualitative
close reading identifies generic fiction, fan fiction, games/cartoons, adult
content, and inappropriate humour. No topic-coherence metric, stability test,
coding protocol, or quantitative causal link to safety filtering is reported.

## Lineage hypothesis: what is known and what is not

| Proposition | Evidence category | Assessment at cutoff |
| --- | --- | --- |
| The four served systems produced correlated lexical/trope patterns under the common experiment | Direct observation as reported by one study | Substantive descriptive evidence, pending artifact release and replication |
| OLMo 3 post-training includes WildChat-derived prompts and multiple kinds of model-generated completions | Documented dataset/model-flow overlap | Directly supported by AI2's Olmo 3 report and Dolci cards |
| GPT-generated material entered OLMo's later training corpus | Documented synthetic-data lineage | Direct for Dolci-Instruct SFT's GPT-4.1-upgraded responses; Think data also uses DeepSeek R1 and DPO uses Qwen-generated contrasts |
| The Core tokens occur more densely in OLMo DPO/RL story subsets than in SFT | Reported correlation | Direction reported, but exact totals conflict and Core labels are unreleased |
| WildChat itself caused OLMo's Elias/lighthouse output | Plausible mechanism, not causal evidence | Unresolved; the WildChat-derived subset has the lowest reported source-group Core rate, completions were often regenerated, and no removal/influence test was performed |
| The four proprietary/open models share WildChat or one preference dataset | Authors' hypothesis/general lineage possibility | Not verified; no proprietary training-source evidence is provided |
| Post-training rather than pretraining caused the observed motif | Scientific hypothesis with indirect support | OLMo marginal-frequency comparisons make post-training amplification plausible, but no base→SFT→DPO→RL generation comparison establishes it |
| Safety/copyright filtering created a safe narrative attractor | Authors' explicit speculation | Untested; topic observations are consistent with it but not discriminating |
| Recursive synthetic-data feedback produced the cross-model pattern | Plausible broader mechanism | OLMo has synthetic lineage and adjacent experiments establish that recursion can reduce diversity, but this specific recursive chain and effect are not shown |
| Unintended training-data or benchmark contamination caused the pattern | Possible but undefined hypothesis | Not demonstrated; OLMo's documented synthetic/reused data are deliberate training inputs, not automatically “contamination” |
| WildChat contains 166 Elias lighthouse-style conversations | Later journalistic claim | Not stated in the paper or auditable from the released artifact reviewed here; **TODO: verify** against a pinned WildChat/Dolci snapshot and reproducible query |
| The paper studied “Elias Thorne” | Later media framing | False as a description of the measurement: surnames were excluded and `Thorne` is not in the paper's analyzed vocabulary |

### WildChat and synthetic-data chain

The 2024 WildChat paper describes 1,039,785 public conversations and six API
versions: GPT-4-family endpoints account for about 24% and GPT-3.5-Turbo
versions for about 76%. Collection ran from 2023-04-09 00:00 to 2024-05-01
00:00. A later count in the paper text says 1,009,245 full conversations,
so the exact upstream count/version also requires pinning or clarification
rather than being treated as one timeless dataset.

AI2's Olmo 3 report says the 7B Think SFT mix used 83,054 WildChat prompts and
generated reasoning traces/completions with DeepSeek R1. The live Dolci-
Instruct-SFT card says its 302,406 WildChat prompts received upgraded GPT-4.1
responses. OLMo Think DPO draws its prompt pool from Dolci Instruct SFT plus
other sources and generates chosen/rejected completions with Qwen 3 32B and
0.6B thinking models; WildChat also appears in later RL prompt mixtures.

This establishes a real historical graph:

`human prompt → WildChat interaction log → selected WildChat prompt → new
model-generated completion/selection → Dolci post-training stage → OLMo 3`

The exact path varies by Dolci component, and original WildChat assistant text
may be replaced rather than copied. A model can therefore inherit behavioural
constraints from upstream prompt selection, generators, judges, filters, and
objectives even without verbatim retention of an original story. Conversely,
the existence of this graph does not show that any particular Core-bearing
record affected a particular OLMo output.

## Cross-model convergence and evidential independence

The principle under review is supported as an evidence-appraisal rule:

> Cross-model behavioural similarity is not automatically independent
> converging evidence. Shared or historically connected training and
> post-training lineages can create correlated behaviours across nominally
> separate systems.

The Elias case **illustrates** rather than fully proves the proposed training-
lineage mechanism. Four model labels are four sampled systems, but they are not
four scientific replications. They share at least:

- the five prompt formulations and task framing;
- one OpenRouter access layer and unknown provider routing;
- one GPT-5.4-nano extraction instrument;
- one Core-selection and analysis pipeline;
- one research team and corpus-level candidate selection; and
- potentially overlapping public, synthetic, preference, evaluator, or
  alignment histories, directly documented only for OLMo.

Evidence weighting should separate three questions:

1. **Did several endpoints exhibit a related pattern?** The paper gives
   meaningful descriptive support within its configuration.
2. **How statistically and historically independent are those outputs?** This
   remains partial/unclear; a family count is not an independence coefficient.
3. **Which mechanism generated the dependence?** Lineage, objectives,
   decoding, architecture, shared culture, and measurement remain unresolved.

Demonstrated lineage lowers the incremental corroborative weight of another
model observation for hypotheses that predict independent convergence. It
does not erase the observation or prove that lineage caused it. Unknown lineage
also proves neither independence nor dependence. Evidence quality should move
continuously with source match, traceability, causal tests, and competing
explanations—not jump to zero or one.

The reverse error would be to label any repeated behaviour “just training
contamination.” That would silently turn an alternative explanation into a
presumption. A strong lineage explanation should identify the relevant
records/stages, establish temporal ordering, show that the trained system
received them, and ideally change the behaviour through removal, reweighting,
influence analysis, or checkpoint comparison.

## Bounded connection to adjacent research

- **Recursive synthetic feedback:** Shumailov et al. causally model and test
  recursive replacement regimes in which generated data erode distribution
  tails. Guo et al. directly report falling lexical, syntactic, and semantic
  diversity under recursive synthetic fine-tuning, especially for creative
  tasks. These make a synthetic-feedback mechanism scientifically plausible,
  but they do not demonstrate that the Elias systems underwent the tested
  recursion.
- **Important counterboundary:** Gerstgrasser et al. report that accumulating
  real data alongside synthetic data avoids collapse in their settings. The
  synthetic-data category is therefore not a unitary causal verdict; mixture,
  replacement, filtering, source diversity, objective, and task matter.
- **Post-training:** Kirk et al. provide stage-related causal evidence in two
  base models and two tasks that RLHF can reduce measured output diversity
  relative to SFT. It supports post-training as a serious mechanism class, not
  the claim that all alignment pipelines create the same story attractor.
- **Benchmark/training exposure:** Deng et al. distinguish direct corpus
  retrieval from behavioural contamination probes and validate the latter
  with deliberate contamination. This supports the methodological distinction
  among dataset overlap, suspicious behaviour, and causal exposure evidence.
- **Cross-model correlated errors:** Kim et al. find substantial wrong-answer
  agreement across hundreds of models and associations with common providers
  and architectures, while much variation remains unexplained. This is
  convergent support for auditing dependence, not proof that common datasets
  cause every correlation.

These studies use different constructs and cannot be pooled into one estimate.
“Model collapse” in recursive-distribution research, lexical homogenization,
post-training diversity loss, benchmark memorization, and correlated errors
are related but not interchangeable phenomena.

## Claim classification

| Claim | Type | Support and limit |
| --- | --- | --- |
| The studied endpoints produced recurrent unusual lexical/category patterns | Measurement result | Directly reported for the common 20,000-story corpus; outputs and code unreleased |
| The same full person “Elias Thorne” appeared in 88.3% | Unsupported secondary overstatement | 88.3% means any of 11 Core tokens; surnames were excluded |
| A historically connected post-training lineage can correlate model behaviour | Scientific hypothesis plus documented mechanism class | OLMo/Dolci provides an existence example of the lineage; causal effect on this motif not shown |
| OLMo's Core density is higher after DPO/RL than in SFT | Measurement result with reporting conflict | Published stage rates support direction; exact Core total is inconsistent |
| Alignment selects safe-for-work lighthouse stories | Authors' scientific hypothesis | Explicitly deferred to future work; no ablation |
| Cross-model similarity should not automatically count as independent convergence | Research-method interpretation | Follows from known shared measurement and possible/known lineage dependencies; already consistent with the Draft protocol |
| Lineage explains all cross-model similarity | Unsupported generalization | No proprietary provenance or universal causal evidence |
| The observation bears on consciousness, sentience, or shared mind | Unsupported category shift | Those targets were not measured and are not entailed by generated-text recurrence |

## Exact proposed permanent protocol clarification — not applied

The existing [Independence and evidence lineage](../research-protocol.md#independence-and-evidence-lineage)
section already maps shared datasets, prompts, models, evaluators, and
artifacts. The following addition would make the cross-model case explicit
without presuming lineage or discarding behaviour. It is proposed for Disa's
review; this Work Cycle does not alter the Draft protocol or its version.

```diff
@@ ## Independence and evidence lineage
 Several papers from one pipeline are not several independent confirmations.
 A review, news report, and commentary based on the same study add perspectives,
 not new empirical evidence. Replication should state whether it is same-team,
 independent analysis of shared data, independent reproduction on the same
 system, or conceptual replication with new systems or methods.
+
+Behavioural similarity across nominally different model families is not by
+itself independent converging evidence. Assess whether the systems share or
+inherit pretraining data, synthetic generations, preference or other
+post-training data, benchmarks, evaluators, provider/routing infrastructure,
+or upstream models. Treat lineage as a competing explanation to investigate,
+not a default verdict: unknown lineage proves neither independence nor
+dependence, and demonstrated similarity retains descriptive evidential value.
```

This is a clarification, not a change in scientific direction. If adopted in a
later owner-reviewed cycle, the protocol version and affected templates or
guidance should be checked together rather than changed silently here.

## What would discriminate among explanations

The smallest informative empirical programme would preserve the prompt corpus
and analysis while adding:

1. exact model IDs, revisions, provider routes, system prompts, generation
   dates, temperature/top-p/max tokens, seeds, failures, and raw outputs;
2. story-level Core labels plus independent human/extractor validation and
   exact per-model/per-prompt hit and co-occurrence rates;
3. OLMo Base→SFT→DPO→RL checkpoint generation under identical decoding;
4. leave-one-source-out or reweighting experiments for WildChat-derived,
   UltraFeedback, persona/constraint, and other story-bearing subsets;
5. source-attribution or influence estimates tied to released record IDs,
   followed by causal removal/retraining where feasible;
6. direct-provider and multi-temperature replication to test OpenRouter and
   decoding sensitivity; and
7. a preregistered independent replication on temporally pinned open and
   proprietary endpoints.

For the proprietary models, published data manifests, model cards, or audited
provenance could strengthen or weaken a shared-lineage account. Mere continued
appearance of Elias under the same underspecified prompt would strengthen
phenomenon robustness but would not by itself resolve mechanism or
independence.

## Uncertainties and re-review triggers

- Exact observation dates and model revisions remain unknown.
- Raw generations, analysis code, Core labels, classifier artifacts, and
  sampling settings remain unavailable.
- Three internal numerical inconsistencies prevent exact OLMo source
  attribution from the paper alone.
- The precise role of original WildChat responses versus retained prompts and
  regenerated completions is dataset-component specific.
- Proprietary-model data and post-training lineages are unknown.
- The paper's author reports EMNLP 2026 acceptance, but the current official
  main-paper page does not corroborate it.
- No independent reproduction was located by the cutoff.
- Re-review on arXiv v2/camera-ready/proceedings publication, artifact/code or
  Core-label release, table correction, exact model/configuration disclosure,
  independent replication, or causal checkpoint/dataset ablation.

## Relevance and non-implications for AI Rights & Welcome

This case is directly useful to the portfolio's evidence-validity and
transferability support function. It shows why “observed in several models”
requires a dependency audit before it is treated as independent convergence,
especially when public datasets recycle model outputs and when preference or
alignment pipelines use other models as generators or judges.

The case changes no conclusion about cognition, agency, affect, welfare,
identity, collective organisation, consciousness, sentience, or moral
relevance. It neither supports nor challenges those properties because it was
not designed as a sensitive test of them. Its normative implication is limited
to research discipline: preserve the observation, map lineage, test competing
mechanisms, and calibrate corroborative weight without a predetermined verdict.

## Recommendation

Merge this source record, note, index update, and Work Cycle history as
**Partly verified working research** after Disa's review. Do not yet merge the
proposed protocol sentence as an adopted method change; first resolve whether
Disa wants the existing broad lineage language made explicit and, ideally,
check any EMNLP camera-ready correction and the Core-count discrepancies.

Further research is required before citing WildChat, synthetic-data feedback,
pretraining contamination, preference data, or alignment as the cause of the
cross-model motif. The smallest next step is a non-contact status refresh when
an official EMNLP proceedings version or expanded artifact appears, followed
by a pinned OLMo stagewise reproduction if resources are separately approved.
No external contact, model spending, training run, publication, or protocol
adoption is authorized by this note.

## Verification tasks

- [x] Source record and exact arXiv version linked.
- [x] Paraphrases checked against the original full text and TeX source.
- [x] Findings and caveats have section, table, or appendix locators in the
  source record.
- [x] No material quotation is relied upon beyond named prompts/terms.
- [x] Negative, null, mixed, and contrary material extracted.
- [x] Researcher interpretation separated from source findings.
- [x] Competing explanations and criticisms recorded.
- [ ] Funding and conflict disclosure complete; the preprint has no such
  statement.
- [ ] Peer-review status independently verified; acceptance is author-reported.
- [x] Point-in-time arXiv and official-page status checked.
- [x] Primary WildChat/OLMo/Dolci and bounded adjacent sources checked.
- [ ] Generated corpus, Core labels, classifier, and analyses reproduced.
- [ ] Independent specialist review completed.

## Change and review log

| Date | Researcher or reviewer | Change, verification, or disagreement | Effect on note |
| --- | --- | --- | --- |
| 2026-09-04 | Codex | Created bounded cross-source analysis; verified primary paper, released ID artifact, OLMo/WildChat lineage, conference-status limit, and adjacent literature | Establishes cautious descriptive and methodological use; causal lineage, exact publication status, and independent replication remain open |
