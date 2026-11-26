# Paired evaluation

A and B discovery controls started with the same brief and project inputs as enabled trials. F used the same small CommonJS React project in both arms. Controls omitted the frozen skill, and enabled runs installed it. CLI defaults were shared, but the provider model refresh sometimes timed out and exact model selection and network timing could not be independently guaranteed. These are small observational comparisons.

| Pair | Observed result |
| --- | --- |
| A discovery | Both respected the REST service, separated roles and asked about token and role delivery. The enabled run explicitly proposed React/TypeScript/Vite and identified frontend origin requirements. The control described the fixture and left architecture open for approval. |
| B discovery | The enabled run proposed static Next.js and distinguished search-engine indexing from on-site search. The control proposed a searchable guide and similar localized routes and crawl metadata. Both waited for approval. |
| F maintenance | The control preserved CommonJS and React, implemented focus restoration/filter reset and reported two executed tests. See project results for the enabled arm and independent checks. |

Provider token counters measure whole sessions. They include system instructions, command output and cached inputs. They cannot isolate skill-loading cost. Read traces are a separate measure of profile selection. Neither these comparisons nor the limited fixture scores establish causal improvement or statistical significance.

Using the frozen rubric, the reviewer rated only the observed discovery dimensions on the 0–2 scale. Requirements and architecture were scored respectively as A enabled 2/2, A control 2/1, B enabled 2/2 and B control 1/1. The A control left a material frontend choice open, while the B control inferred on-site search and did not commit to a framework recommendation. These are ordinal reviewer judgments on two dimensions. A build, behavioral or security score requires independently applicable evidence and was not imputed from these ratings.

B implementation completed in both arms. The enabled run exported localized routes, used an explicit project-profile document, and passed independent HTTP and browser checks. The control used static export with plain links and passed all ten independently rerun export tests. F enabled passed three jsdom checks, including Escape, and control passed two. Both kept the established dependencies and changed only the targeted feature and its test/documentation surface. Test counts show suite scope; they do not measure relative correctness.

Observed cumulative CLI input counts for completed discovery runs were A enabled 49,399 versus control 43,360 and B enabled 51,305 versus control 28,739. On the B implementation they were 432,039 versus 289,719, respectively. F used 186,172 versus 116,034 in the original enabled/control runs. The explicit probe reported 65,353 input tokens. These cumulative counts include cached tokens and repeated tool outputs. They cannot establish standalone skill overhead. Narrowing repeated file reads is a retest candidate, not an inferred performance gain.
