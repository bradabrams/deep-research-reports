# Research Notes: AI Agent Frameworks
## Collection Date: December 13, 2025

---

## Key Findings Summary

### 1. Framework Landscape Clarification
**IMPORTANT**: "AWS AgentKit" is actually **OpenAI's AgentKit**. AWS offers:
- **Bedrock Agents** - Fully managed, config-based (Bedrock models only)
- **Bedrock AgentCore** - Enterprise platform, model-agnostic (GA late 2025)
- **Strands Agents** - Open-source Python SDK for custom implementations

### 2. Major Framework Comparison

| Framework | Architecture | Best For | Learning Curve |
|-----------|-------------|----------|----------------|
| **LangGraph** | Graph-based workflows | Complex stateful workflows | Steep |
| **CrewAI** | Role-based teams | Rapid prototyping | Beginner-friendly |
| **AutoGen** | Conversational multi-agent | Enterprise/Microsoft ecosystem | Moderate |
| **Claude Agent SDK** | Session-based harness | Long-running tasks | Moderate |
| **OpenAI Agents SDK** | Response API + tools | OpenAI ecosystem | Easy |
| **AWS AgentCore** | Modular services | Enterprise production | Moderate |

### 3. GitHub Popularity (Dec 2025)
1. **Dify**: ~93,000 stars (low-code platform)
2. **CrewAI**: 30,000+ stars, ~1M monthly downloads
3. **LangGraph**: 14,000+ stars, 4.2M monthly downloads
4. **OpenAI Agents SDK**: 11,000+ stars (since March 2025)
5. **Google ADK**: ~10,000 stars (since April 2025)

### 4. Multi-Agent Orchestration Patterns

**Supervisor Pattern**
- Central orchestrator coordinates all agents
- Predictable control flow, easier debugging
- Best for: enterprise workflows, compliance-heavy tasks

**Hierarchical Architecture**
- Three layers: Strategy → Planning → Execution
- Top-down control and decision-making
- Best for: complex decomposable tasks

**Swarm Pattern**
- Decentralized peer-to-peer communication
- Better scalability, harder to debug
- Best for: emergent behavior, exploration tasks

---

## Vendor-Specific Deep Dives

### Anthropic Claude Agent SDK
**Launch**: September 29, 2025
**Key Innovation**: Multi-session memory solution

**Two-Part Architecture**:
1. **Initializer Agent**: Sets up environment, creates `claude-progress.txt`, commits state via Git
2. **Coding Agent**: Reads progress logs, makes incremental updates, updates documentation

**Key Features**:
- CLAUDE.md for persistent project context
- Automatic context compaction
- Session forking
- Python & TypeScript SDKs
- Built on Claude Code harness

**Limitation**: Memory based on explicit scaffolding (logs, commits) - not episodic recall

### OpenAI AgentKit / Agents SDK
**Launch**: October 6, 2025 (Dev Day)
**Key Innovation**: Unified Responses API

**Components**:
- Agent Builder (visual)
- ChatKit (embeddable UI)
- Agents SDK (Node, Python, Go)
- Expanded Evals

**Built-in Tools**:
- WebSearchTool
- FileSearchTool
- ComputerTool (computer use)
- CodeInterpreterTool ($0.03/container)
- ImageGenerationTool
- HostedMCPTool

**Pricing**:
- Code Interpreter: $0.03/container
- File Search: $0.10/GB/day + $2.50/1k calls
- MCP tool calls: Token cost only

### AWS Bedrock AgentCore
**Preview**: July 16, 2025
**GA**: Late 2025
**Downloads**: 2M+ in 5 months

**Components**:
- **Runtime**: Serverless, microVM isolation per session
- **Memory**: Persistent + episodic memory
- **Gateway**: Tool integration hub
- **Browser Runtime**: Complex web workflows
- **Code Interpreter**: Sandboxed execution
- **Policy** (preview): Natural language → Cedar policies
- **Evaluations** (preview): 13 built-in evaluators

**Key Differentiator**: Model-agnostic - works with OpenAI, Google, Anthropic, Meta, Mistral

### Model Context Protocol (MCP)
**Origin**: Anthropic, November 2024
**Foundation**: Donated to Agentic AI Foundation (Linux Foundation) December 2025
**Co-founders**: Anthropic, Block, OpenAI
**Supporters**: Google, Microsoft, AWS, Cloudflare, Bloomberg

**Adoption Timeline**:
- March 2025: OpenAI adopts MCP
- April 2025: Google confirms Gemini support
- December 2025: Google launches managed MCP servers

**Technical Details**:
- Based on Language Server Protocol (LSP) patterns
- Transport: JSON-RPC 2.0 over stdio or HTTP/SSE
- Pre-built servers: Slack, GitHub, Google Drive, Postgres, Puppeteer

---

## Pricing & Economics

### Enterprise Implementation Costs
- Basic: $100,000-$200,000
- Comprehensive: $500,000-$2,000,000
- Setup fees: $50,000-$150,000
- Implementation time: 3-6 months

### Vendor Pricing Models
| Vendor | Model | Price |
|--------|-------|-------|
| Salesforce | Per conversation | $2 |
| Microsoft | Per hour | $4 |
| Intercom | Per resolution | $0.99 |

### ROI Statistics
- Average projected ROI: 171%
- US enterprises: 192%
- Cost reduction: 10-25% operational workflows
- Marketing cost reduction: up to 37%
- AI vs human interaction: $0.50 vs $4-8

### Monthly Operating Costs
- Basic: $100-$2,000/month
- Enterprise: $500+/month (100k+ interactions)
- Security/compliance: +20-40% of platform costs

---

## Market Statistics (2025)

### Market Size
- 2025: $7.38-7.92 billion
- 2030 projection: $50.31 billion (CAGR 45.8%)
- 2032 projection: $103.6 billion
- 2034 projection: $236 billion

### Adoption Rates
- 85% organizations using AI agents in at least one workflow
- 79% (PwC) implemented at some level
- 23% scaling agentic AI
- 39% experimenting
- 96% IT leaders plan expansion in 2025
- 72% enterprises deployed/experimented (2024)

### Industry Distribution
- Banking/Financial Services: Leading
- Retail: High adoption
- Manufacturing: High adoption
- 70% of POCs from these three sectors

---

## Security Concerns

### Top Threats
1. Memory Poisoning
2. Tool Misuse
3. Privilege Compromise
4. Prompt Injection
5. Cascading Hallucinations

### Statistics
- 80% encountered risky agent behaviors
- 41% IAM concerns for agents
- 62% practitioners cite security as top challenge
- 53% leadership cite security as top challenge

### Framework-Agnostic Issues
Most vulnerabilities arise from:
- Insecure design patterns
- Misconfigurations
- Unsafe tool integrations
- NOT framework-specific flaws

---

## Gartner Insights (2025)

### Key Reports
- **AI Application Development Platforms**: Google, IBM named Leaders
- **Conversational AI Platforms**: Google top-right, Kore.ai and Cognigy Leaders
- **Data Science/ML Platforms**: Databricks edges out Big 3 clouds

### Predictions
- By 2027: 70% customer support automated (up from 50% in 2025)
- By 2028: 33% enterprise software will incorporate agentic AI

---

## Technical Architecture Notes

### Framework Selection Matrix
| Need | Recommended Framework |
|------|----------------------|
| Complex workflows | LangGraph |
| Rapid prototyping | CrewAI |
| Microsoft ecosystem | AutoGen |
| Long-running tasks | Claude Agent SDK |
| OpenAI ecosystem | OpenAI Agents SDK |
| Enterprise/AWS | Bedrock AgentCore |
| Full control | Strands Agents |

### Key Trade-offs
- **LangGraph**: Power vs complexity
- **CrewAI**: Simplicity vs enterprise features
- **AutoGen**: Flexibility vs learning curve
- **Managed platforms**: Ease vs vendor lock-in

---

## Community & Social Insights

### Hacker News Discussions

**Key Thread: "Sick of AI Agent Frameworks"**
- Developers express frustration with framework fragmentation
- Common complaint: "5 layers of abstraction just to change a minute detail"
- AutoGen noted as popular but "not production-ready, undergoing rapid changes"

**Key Thread: "Which agentic framework/tool do you prefer?"**
- Community consensus: CrewAI for multi-agent collaboration ease, OpenAI SDK for lean production
- LangGraph praised for complex workflows but criticized for steep learning curve
- Many prefer rolling own solutions over framework lock-in

### LangChain Criticism (Common Themes)

**Over-Abstraction**
> "You have to learn a bunch of custom classes and abstractions, even for things that could be done with plain Python or JavaScript"

**Dependency Bloat**
- Described as "bloated" and prone to "dependency hell"
- Even basic features require installing many dependencies

**Documentation Issues**
- Frequently outdated documentation
- Missing explanations of default parameters
- Developers "scavenge through various resources"

**Instability**
> "It's unstable, the interface constantly changes, the documentation is regularly out of date..."

**Production Concerns**
- Good for prototyping, not recommended for production
- Code gets messy, hard to scale and maintain

**Vendor Lock-in**
- Creates inherent lock-in to only use LangChain-based code
- "$30 million" VC investment creates misaligned incentives

### CrewAI Criticism

**Pricing Concerns**
- Starting at $99/month, up to $120,000/year for enterprise
- Considered "expensive" for smaller businesses

**Technical Limitations**
- Framework rigidity makes dynamic role adjustment difficult
- Inconsistent results for specific use cases
- Several unresolved high-severity bugs

**Resource Issues**
- API rate limits hit during concurrent agent testing
- Context window constraints limit scalability

### AWS Bedrock Agents Pain Points

**Developer Experience**
> "Slow responses, buggy experiences, and missing key features"

**Complexity**
- Each tool requires separate Lambda function management
- "Code-intensive" compared to alternatives
- Very large learning curve with confusing terminology

**AgentCore CLI Issues**
- `agentcore deploy` command unreliable
- Cryptic IAM errors even with admin permissions
- Broken deployments hard to clean up

**Debugging Challenges**
- Intermittent failures in long-running workflows
- No clear explanation when agents stop mid-execution
- Silent runtime restarts with no logs

### Developer Sentiment (General)

**The Paradigm Shift Problem**
> "The transition from deterministic systems to probabilistic agents is uncomfortable... handing over control flow to a non-deterministic model feels wrong to a mind trained on strict interfaces."

**Overengineering by AI**
> "Like asking someone for a cup of tea and getting a 12-piece tea set, imported leaves, a handwritten guide on brewing, and a three-course snack pairing."

**Time Sink**
- 60-70% of AI development time spent on prompt engineering
- Compared to "trying to fix a broken database with better SQL comments"

**New Developer Role**
> "I've promoted myself from coder to manager of robots... Managing those robots isn't a simple task."

### Positive Community Feedback

**Claude Agent SDK**
- Developers praise: "I use it as my default agent framework over tools like LangChain/CrewAI"
- Time savings: "23 hours to 5 hours for complex content"
- Good for rapid prototyping of agentic tasks

**OpenAI Agents SDK**
- Lighter than LangChain's abstractions
- Better debugging than Auto-GPT
- Guardrails add safety absent in earlier autonomous agents

**CrewAI**
- Excellent for rapid prototyping
- Beginner-friendly documentation
- Clean API design

### Community Recommendations Summary

| Use Case | Community Preference |
|----------|---------------------|
| Quick POC/Demo | LangChain (despite criticisms) |
| Production deployment | OpenAI Agents SDK, custom code |
| Multi-agent collaboration | CrewAI |
| Complex stateful workflows | LangGraph (if you accept learning curve) |
| Enterprise/compliance | AWS AgentCore (with patience) |
| Coding/development agents | Claude Agent SDK |

---

## Images Downloaded
- `json_logo.png` - For MCP JSON-RPC documentation
- `langgraph_logo.svg` - LangGraph branding
- `crewai_logo.png` - CrewAI branding

---

*Last updated: December 13, 2025*
