# Research Notes: Agentic AI Framework Comparison

## Session Log

### 2024-12-14 - Research Initiated

**Frameworks Under Study:**
1. LangChain
2. CrewAI
3. AutoGen (Microsoft)
4. OpenAI Agents SDK
5. Claude Agent SDK (Anthropic)
6. AWS Bedrock Agents

---

## Iteration 1 - Initial Data Collection

### Key Findings Summary

#### GitHub Stars (approximate, as of late 2024/early 2025)
| Framework | Stars | Monthly Downloads |
|-----------|-------|-------------------|
| LangChain | ~99K | 28M |
| AutoGen | ~33-43K | 890K+ |
| CrewAI | ~41K | ~1M |
| LangGraph | ~11.7K | 4.2M |
| OpenAI Agents SDK | ~9.3K | TBD |
| Claude Agent SDK | TBD | TBD |

#### Architecture Patterns Identified

**LangChain/LangGraph**
- DAG-inspired workflow design
- Nodes represent tasks/functions
- Fine-grained control over flow and state
- 600+ integrations
- Highest learning curve but most resources

**AutoGen (Microsoft)**
- Conversational multi-agent paradigm
- Agents "talk" to solve problems
- Excels at code generation with self-correction
- #1 on GAIA benchmark (March 2024)
- Event-driven, distributed architecture in v0.4

**CrewAI**
- Role-based "crew" metaphor
- Explicit process concept (sequential/parallel)
- Built on top of LangChain
- Easiest learning curve
- Rapid prototyping focus

**OpenAI Agents SDK**
- Lightweight design with few abstractions
- Core primitives: Agents, Handoffs, Guardrails, Sessions, Function Tools
- Provider-agnostic (100+ LLMs supported)
- Built-in tracing and observability
- Temporal integration for durable workflows

**Claude Agent SDK**
- "Give agents a computer" philosophy
- Renamed from Claude Code SDK
- Automatic context compaction
- MCP extensibility
- File operations, code execution, web search

**AWS Bedrock Agents**
- Enterprise-grade managed service
- AgentCore services: Runtime, Gateway, Memory, Identity, Browser, Code Interpreter
- Multi-agent collaboration with supervisor
- RAG integration built-in
- Framework-agnostic (works with CrewAI, LangGraph, etc.)

#### Enterprise Adoption Highlights

- **CrewAI**: 60% Fortune 500 adoption (claimed), customers include IBM, Microsoft, Walmart, SAP
- **AutoGen**: 40% Fortune 100 adoption for internal agentic systems
- **AWS Bedrock**: Robinhood case study - scaled to 5B tokens/day, 80% cost reduction
- **LangChain**: 132K+ applications built, customers include Klarna, Snowflake, BCG

#### Market Context

- 79% of organizations report AI agent adoption
- Market projected to reach $199B by 2034 (from $5.25B in 2024)
- 96% of IT leaders plan to expand AI agent usage in 2025
- Gartner: 33% of enterprise software will have agentic AI by 2028
- Warning: 40% of agentic AI projects projected to fail by 2027

---

## Iteration 2 - Community & Social Insights

### LangChain Community Sentiment

**Criticisms (widespread)**
- "LangChain is where good AI projects go to die" - Kieran Klaassen, Every Inc
- Frequent breaking changes and API instability (pre-v0.1)
- Documentation described as "atrocious and inconsistent"
- Over-complicated abstractions adding unnecessary layers
- Token inefficiency: 166% higher token usage vs manual RAG in one test
- Confusing package structure (langchain_core, langchain_community)
- Hidden behaviors making debugging difficult

**Counter-arguments**
- v0.1.0 (January 2024) marked first "stable" release
- Still best for rapid prototyping with pre-built components
- 600+ integrations unmatched by competitors
- Strong community and ecosystem tools (LangSmith, LangServe)

### CrewAI Community Sentiment

**Praise**
- "Like a well-organized team ready to go" vs "box of Lego" (OpenAI SDK)
- Easiest framework for beginners
- Good for POCs and rapid prototyping
- Active community (100K+ developers)

**Criticisms**
- Production deployment issues (1GB virtual environments)
- Lack of observability and debugging tools
- Memory feature inconsistent - sometimes better without it
- Not suitable for complex production use cases
- Pricing concerns ($99/mo for basic, $6,000/year for enterprise)

**Community Advice**
- Use CrewAI when you know how to solve a problem and want to automate
- Use AutoGen when you don't know and want experts to collaborate on solution

### AutoGen Community Sentiment (HackerNews)

**Praise**
- "Step ahead of LangChain agents"
- Good modularization for complex tasks
- Docker container isolation for safety
- Practical for data analytics, software development

**Criticisms**
- Questions about whether multi-agent truly provides emergent properties
- Performance sometimes doesn't match direct GPT-4 prompts
- Plagiarism controversy (disputed)
- Microsoft naming conventions criticized

**Notable Discussion Points**
- Top trending GitHub repo (October 2023)
- Mentioned by Satya Nadella in fireside chat
- DeepLearning.ai course collaboration

### AWS Bedrock Agents Community Sentiment

**Enterprise Feedback**
- Cox Automotive: "Strategic platform for deploying AI agents at scale"
- Ericsson: "AI agents of unprecedented capability" for R&D
- Epsilon: 30% reduced campaign setup, 8 hours saved weekly
- AgentCore SDK downloaded over 1 million times

**Key Differentiator**
- Framework-agnostic: works with CrewAI, LangGraph, OpenAI SDK
- Enterprise-grade security and compliance built-in
- Model flexibility (not locked to AWS models)

### OpenAI Agents SDK Community Sentiment

**Early Reception**
- "Game-changer for developers wanting AI to actually do things"
- Lightweight design praised vs. heavier frameworks
- Coinbase: Built AgentKit in "just a few hours"

**Developer Positioning**
- "OpenAI SDK for lean production deployments"
- Best for general-purpose prototyping
- Provider-agnostic despite OpenAI branding

### Claude Agent SDK Community Sentiment

**Feedback Themes**
- Focus on feedback loops: gather context -> take action -> verify -> repeat
- Best form of feedback: clearly defined rules + explanation of failures
- IDE integration (JetBrains) well-received
- Python-only currently (covers most AI/ML developers)

---

## Key Community Themes

### 1. Framework Selection Heuristics
| Scenario | Recommended Framework |
|----------|----------------------|
| Know solution, want automation | CrewAI |
| Dynamic problem-solving | AutoGen |
| Complex integrations | LangChain |
| Lean production | OpenAI Agents SDK |
| Enterprise compliance | AWS Bedrock Agents |
| Code-centric tasks | Claude Agent SDK |

### 2. Common Pain Points Across Frameworks
- Debugging/observability challenges
- Production deployment complexity
- Breaking changes and versioning issues
- Documentation lag
- Learning curve vs. flexibility trade-off

### 3. Emerging Consensus
- Multi-agent is becoming standard
- MCP protocol gaining traction
- Tracing/observability now table-stakes
- Enterprise adoption accelerating rapidly
- 40% failure rate prediction raises concerns

---

## Sources Summary
- 34 sources documented
- 21 official/industry sources (high credibility)
- 13 community sources (low credibility, valuable color)
- 6 framework logos downloaded

---

*Last updated: 2024-12-14*
