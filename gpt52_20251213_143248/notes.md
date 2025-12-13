# GPT-5.2 Research Notes

## Research Iteration 1 - December 13, 2025

---

## Key Findings Summary

### 1. Release Details
- **Release Date:** December 11, 2025
- **Internal Codename:** "Garlic"
- **Context:** Released amid intense "code red" response to Google Gemini 3

### 2. Technical Specifications
- **Context Window:** 400,000 tokens (5x GPT-4's capacity)
- **Max Output:** 128,000 tokens
- **Knowledge Cutoff:** August 31, 2025
- **Architecture:** Transformer-based with chain-of-thought reasoning (o1-style)
- **Parameter Count:** Not disclosed

### 3. Model Variants

| Variant | Use Case | Key Strength |
|---------|----------|--------------|
| **Instant** | Fast tasks, writing, translation | Low latency, speed |
| **Thinking** | Coding, math, planning, long docs | Deep reasoning chains |
| **Pro** | Mission-critical (legal, finance, drug discovery) | Maximum accuracy |

### 4. Benchmark Performance

#### Key Scores:
| Benchmark | GPT-5.2 Score | Comparison |
|-----------|---------------|------------|
| GPQA Diamond | 92.4% (Thinking), 93.2% (Pro) | Beats Gemini 3 Pro (91.9%) |
| ARC-AGI-2 | 52.9% (Thinking), 54.2% (Pro) | Crushes Gemini 3 Pro (31.1%), Claude 4.5 (37.6%) |
| AIME 2025 | 100% (no tools) | First model to achieve perfect score |
| FrontierMath T1-3 | 40.3% | ~10% improvement over GPT-5.1 |
| SWE-Bench Pro | 55.6% | New state of the art |
| SWE-Bench Verified | 80.0% | Near Claude 4.5's 80.9% |
| GDPval | 70.9% beat/tie rate | First model at/above human expert |
| CharXiv (Python) | 88.7% | Beats Gemini 3 Pro (81.4%) |
| Tau2-bench Telecom | 94.5% | Tool-use benchmark |

#### Hallucination Rates:
- GPT-5.2 Thinking: 10.9%
- GPT-5.1 Thinking: 12.7%
- GPT-5 Thinking: 16.8%

### 5. Pricing

| Tier | Input (per 1M) | Output (per 1M) | Notes |
|------|----------------|-----------------|-------|
| Base | $1.75 | $14.00 | 40% increase over GPT-5.1 |
| Pro | $21.00 | $168.00 | Premium tier |
| Cached | 90% discount | - | For repeated inputs |

#### Competitor Comparison:
- **Claude Opus 4.5:** $15/1M input, $75/1M output (most expensive)
- **Gemini 3 Pro:** $1.25-2.50/1M input, $10-15/1M output (tiered)
- **GPT-5.2:** $1.75/1M input, $14/1M output (competitive)

### 6. Competitive Context: "Code Red"

#### Timeline:
1. **Mid-November 2025:** Google releases Gemini 3 Pro
2. **November 24, 2025:** Anthropic releases Claude Opus 4.5
3. **Early December 2025:** Sam Altman issues internal "code red" memo
4. **December 2, 2025:** Code red reported by Fortune, CNBC
5. **December 11, 2025:** GPT-5.2 released

#### Key Factors:
- Google Gemini reached 650 million monthly users in October 2025
- Gemini 3 topped multiple AI benchmarks
- OpenAI deprioritized health, shopping, advertising projects
- Focus shifted entirely to ChatGPT improvements
- Altman expects to exit code red by January 2026

### 7. Availability

- **ChatGPT:** Rolling out to Plus ($20/mo), Pro ($200/mo), Go, Business, Enterprise
- **API:** Available to all developers
- **GitHub Copilot:** Public preview for Pro, Pro+, Business, Enterprise
- **GPT-5.1 Sunset:** 3 months from December 11, 2025

### 8. Safety & Concerns

#### Improvements:
- 38% fewer errors than predecessor
- 8x reduction in hallucinations vs o3
- 50x reduction in errors in urgent situations vs GPT-4o
- Chain-of-thought reasoning helps resist jailbreaks

#### Concerns:
- Security researchers bypassed GPT-5 safety within 24 hours
- SPLX testing showed poor scores on default configuration
- NeuralTrust jailbroke using "Echo Chamber" technique
- Critics note rapid pace may compromise safety priorities
- "Value lock-in" concerns about AI companies embedding their values

### 9. Historical Context

#### GPT Evolution:
| Model | Date | Parameters | Key Advance |
|-------|------|------------|-------------|
| GPT-1 | June 2018 | 117M | Transformer architecture |
| GPT-2 | Feb 2019 | 1.5B | Coherent text generation |
| GPT-3 | May 2020 | 175B | Few-shot learning |
| GPT-3.5/ChatGPT | Nov 2022 | - | Instruction tuning, RLHF |
| GPT-4 | Mar 2023 | ~1-1.8T | Multimodal, reliability |
| GPT-4o | May 2024 | - | Unified multimodal |
| GPT-5 | Aug 2025 | - | Router architecture, 256K context |
| GPT-5.1 | ~Oct 2025 | - | Conversational improvements |
| GPT-5.2 | Dec 2025 | - | Professional knowledge work |

---

## Questions Addressed This Iteration

### Fully Addressed:
- [x] Q1: Technical specifications (context window, tokens, cutoff)
- [x] Q2: Variant differences (Instant, Thinking, Pro)
- [x] Q3: Benchmark scores (GPQA, FrontierMath, AIME, etc.)
- [x] Q5: Multimodal capabilities (vision, documents)
- [x] Q7: Pricing structure and competitor comparison
- [x] Q9: Platform availability
- [x] Q12: Code red triggers
- [x] Q13: Competitor benchmark comparisons
- [x] Q16: GPT model timeline

### Partially Addressed:
- [ ] Q4: GPT-5.1 to 5.2 improvements (need more detail)
- [ ] Q6: Safety measures (have high-level, need system card details)
- [ ] Q8: Price increase impact on adoption
- [ ] Q14: Market positioning analysis
- [ ] Q17: Microsoft partnership evolution
- [ ] Q18: OpenAI organizational context

### Not Yet Addressed:
- [ ] Q10: Market share/revenue implications
- [ ] Q11: GPT-5.1 sunset impact on businesses
- [ ] Q15: 2025 release cadence analysis
- [ ] Q19-22: Critical perspectives and regulatory response

---

## Follow-up Questions Discovered

1. What is the internal "Garlic" codename about?
2. How does ChatGPT's 700M weekly users compare to competitors?
3. What specific projects were deprioritized in code red?
4. How did Claude Opus 4.5 release factor into the competitive response?
5. What are the specific API rate limits for GPT-5.2?
6. What enterprise contracts has OpenAI recently secured?

---

## Sources Used This Iteration

- 20 sources identified and catalogued
- 4 primary sources (OpenAI official)
- 8 major news outlets
- 8 analysis/technical sources

---

## Images Needed

1. Benchmark comparison chart (priority)
2. GPT model evolution timeline
3. Pricing comparison table
4. Sam Altman / OpenAI leadership photo
5. Code red timeline visualization

---

---

## Research Iteration 1 - Completed

### New Findings This Iteration

#### Microsoft/Enterprise Integration
- GPT-5.2 generally available in Microsoft Foundry (Azure AI Foundry)
- Enterprise features: managed identities, policy enforcement, telemetry
- Use cases: financial services, healthcare, manufacturing, customer support
- Quota management: TPM and RPM controls at deployment level

#### EU AI Act Compliance
- OpenAI signed EU Code of Practice in July 2025
- GPT-5 likely qualifies for "systemic risk" classification
- Models released after Aug 2, 2025 must comply immediately
- Concerns raised about training data transparency

#### Additional Competitive Context
- Internal codename for GPT-5.2 was "Garlic"
- Accelerated release: less than 1 month after GPT-5.1 (Nov 12 → Dec 11)
- Gemini 3 Pro first to break 1500 LMArena Elo rating
- No new image generator in GPT-5.2 despite code red emphasis on images

#### Executive Quotes
- Fidji Simo (CPO): "We designed 5.2 to unlock even more economic value"
- Aidan Clark (Research): Math reasoning "a proxy for whether a model can follow multi-step logic"

### Updated Statistics
- **Sources collected:** 25 (5 primary, 8 news, 12 analysis)
- **Claims documented:** 45 (35 high confidence, 10 medium)
- **Images downloaded:** 2 (OpenAI logo, ChatGPT logo)

---

*Notes updated: December 13, 2025*
