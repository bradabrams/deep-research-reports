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

### Observations

1. **Convergence on Multi-Agent**: All frameworks now support multi-agent orchestration
2. **Tracing/Observability**: Becoming table-stakes feature (LangSmith, built-in tracing)
3. **MCP Protocol**: Emerging as standard for tool extensibility
4. **Two-Speed Adoption**: Highly automated enterprises adopting quickly; others struggling
5. **Open Source vs Managed**: Trade-off between customization (LangChain/CrewAI) and enterprise features (AWS Bedrock)

### Sources Collected
- 21 sources documented in sources.json
- 28 claims documented in claims.json
- 6 framework logos downloaded

### Next Steps
- [ ] Gather more specific GitHub metrics via API
- [ ] Research Claude Agent SDK adoption metrics
- [ ] Find more enterprise case studies
- [ ] Document security/compliance features
- [ ] Research limitations and pain points
- [ ] Create comparison visualizations

---

*Last updated: 2024-12-14*
