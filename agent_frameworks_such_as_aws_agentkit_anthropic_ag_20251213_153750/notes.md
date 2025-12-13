# Research Notes: AI Agent Frameworks

## Initial Observations (December 13, 2025)

### Framework Landscape
- Clear divide between **proprietary** (OpenAI, Anthropic, AWS) and **open-source** (LangChain, CrewAI, AutoGen)
- Rapid consolidation happening - major launches in Sept-Oct 2025
- MCP (Model Context Protocol) emerging as potential standard from Anthropic

### Key Differentiators Identified
1. **OpenAI AgentKit**: Speed/managed infrastructure focus
2. **Anthropic Agent SDK**: Developer control/MCP protocol/security
3. **AWS Bedrock Agents**: Enterprise integration/guardrails
4. **LangChain/LangGraph**: Ecosystem breadth/community
5. **AutoGen**: Multi-agent conversations/Microsoft stack
6. **CrewAI**: Beginner-friendly/role-based agents

---

## Research Iteration 1 Findings (December 13, 2025)

### Major Development: Agentic AI Foundation (AAIF)
- **Launched**: December 9, 2025 under Linux Foundation
- **Founding members**: Anthropic, OpenAI, Block (co-founders)
- **Platinum supporters**: AWS, Google, Microsoft, Bloomberg, Cloudflare
- **Three founding projects**:
  1. **MCP** (Anthropic) - universal protocol for AI-tool connections
  2. **goose** (Block) - local-first AI agent framework
  3. **AGENTS.md** (OpenAI) - project-specific guidance standard

### MCP Protocol Deep Dive
- Released November 2024, now industry standard
- **10,000+ published MCP servers** as of Dec 2025
- Architecture: Host → MCP Client → MCP Server
- Transport: JSON-RPC 2.0 over stdio or HTTP/SSE
- Three primitives: **tools** (model-controlled), **resources** (app-controlled), **prompts** (user-controlled)
- Adopted by: OpenAI (March 2025), Google Gemini (April 2025)
- **Security concerns**: Prompt injection, tool permissions, lookalike tools (April 2025 analysis)

### OpenAI AgentKit Details (Oct 6, 2025)
- **Agent Builder**: Visual drag-and-drop canvas ("Canva for agents")
  - Nodes for models, tools, rules, guardrails, branching logic
  - Preview runs, inline eval config, full versioning
  - Built-in PII filtering, jailbreak protection
- **Connector Registry**: Centralized enterprise tool management
  - Pre-built connectors: Dropbox, Google Drive, SharePoint, Teams, GitHub
  - Access control policies, rate limits, audit trails
  - Supports third-party MCP servers
- **ChatKit**: Embeddable chat interfaces
- **Evals for Agents**: Step-by-step trace grading, automated prompt optimization
- Status: ChatKit/Evals GA, Agent Builder beta, Connector Registry rolling out

### AWS Bedrock Agents Update
- **Multi-agent collaboration GA**: March 10, 2025
- Two collaboration modes:
  1. **Supervisor mode**: Orchestrates subagents serially/in parallel
  2. **Supervisor with routing**: Routes simple requests directly, escalates complex ones
- Features: Action groups, knowledge bases, guardrails, memory retention
- **A2A Protocol**: Agent-to-agent communication (vs MCP for agent-to-tool)

### Framework Comparison Matrix (AWS Analysis)
| Framework | AWS Integration | Multi-Agent | Workflow Complexity | Learning Curve |
|-----------|-----------------|-------------|---------------------|----------------|
| Bedrock Agents | Strongest | Adequate | Adequate | Low |
| AutoGen | Weak | Strong | Strong | Steep |
| CrewAI | Weak | Strong | Adequate | Moderate |
| LangGraph | Adequate | Strong | Strongest | Steep |
| Strands Agents | Strongest | Strong | Strongest | Moderate |

### Open-Source Framework Comparisons

**LangGraph**:
- Best for: Complex, non-linear stateful workflows
- Architecture: Graph-based with nodes (compute) and edges (transitions)
- Strength: Sophisticated state transitions, parallel execution
- Weakness: Steep learning curve

**AutoGen (Microsoft)**:
- Best for: Enterprise deployments, dynamic multi-agent conversations
- Architecture: Actor model with asynchronous conversations
- Strength: Declarative serialization (agents → JSON), scalability
- Weakness: Confusing versioning, manual setup

**CrewAI**:
- Best for: Rapid prototyping, role-based teamwork
- Architecture: Crews (autonomous) + Flows (deterministic)
- Strength: Beginner-friendly, quick startup
- Weakness: Poor logging for complex systems

### Enterprise Case Studies

**Klarna** (2024):
- AI assistant handled 2.3M conversations in first month
- Resolution time: 11 min → under 2 min
- ~$40M profit improvement attributed to AI efficiencies

**Equinix**:
- 68% deflection on employee requests
- 43% autonomous resolution via E-Bot

**ServiceNow**:
- 54% deflection on "Report an issue" form
- 12-17 minutes saved per case
- ~$5.5M annualized savings

---

## Key Statistics Summary

| Metric | Value | Source Confidence |
|--------|-------|-------------------|
| 2025 Market Size | $7-8B | HIGH |
| 2032 Projection | $93-107B | HIGH |
| Enterprise Adoption | 79-85% | MEDIUM |
| IT Leader Plans | 93% | MEDIUM |
| Average ROI | 171% | MEDIUM |
| 2024 Startup Funding | $3.8B | MEDIUM |
| MCP Servers | 10,000+ | HIGH |
| AGENTS.md Adoption | 60,000+ projects | HIGH |

---

## Research Gaps Still to Address
- [ ] Detailed latency/cost benchmarks in production
- [ ] Framework migration case studies
- [ ] Computer Use capabilities comparison
- [ ] Developer satisfaction surveys
- [ ] Enterprise TCO analysis

---

*Notes updated: 2025-12-13*
