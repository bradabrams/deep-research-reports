# AI Agent Frameworks: Research Report
## A Comprehensive Analysis of AWS AgentCore, Anthropic Claude Agent SDK, OpenAI AgentKit, and Open-Source Alternatives

**Research Date:** December 13, 2025
**Confidence Summary:** 16 HIGH, 4 MEDIUM, 1 LOW, 2 DISPUTED claims

---

## Executive Summary

The AI agent framework landscape in 2025 is characterized by rapid evolution, significant fragmentation, and a widening gap between vendor promises and production reality. This report examines the major frameworks available for building autonomous AI agents, including cloud provider platforms (AWS Bedrock AgentCore), AI company SDKs (Anthropic Claude Agent SDK, OpenAI AgentKit), and open-source alternatives (LangChain/LangGraph, CrewAI, AutoGen).

### Key Findings

1. **Market Reality**: The AI agent market is valued at $7.4-7.9 billion in 2025, with strong consensus across research firms [1][2][3]. However, long-term projections vary dramatically ($50B to $236B by 2030-2034), indicating high uncertainty about growth trajectory.

2. **Adoption vs. Hype Gap**: While industry reports claim 85% of organizations plan to adopt AI agents, actual deployment data from McKinsey shows only 23% scaling and 39% experimenting—a combined 62% engagement rate [4]. The projected 171% ROI contrasts sharply with MIT research showing 95% of AI pilots fail to deliver measurable returns [5].

3. **Framework Consolidation**: The Model Context Protocol (MCP), donated to the Linux Foundation in December 2025, is emerging as an industry standard for tool integration, with adoption by OpenAI, Google, and AWS [6]. This may reduce framework fragmentation over time.

4. **Developer Experience Challenges**: All major frameworks face significant criticism. LangChain is criticized for over-abstraction and instability [7][8]. AWS Bedrock has CLI and IAM complexity issues [9]. CrewAI faces pricing concerns ($99-$120K/year) [10].

5. **Security Concerns Are Real**: MCP has documented security vulnerabilities including prompt injection, tool mutation, and data exfiltration risks [11][12]. 80% of organizations report encountering risky AI agent behaviors [13].

### Primary Takeaways

- **For Rapid Prototyping**: CrewAI (40K+ GitHub stars, beginner-friendly) or LangChain (122K stars, extensive integrations)
- **For Production**: OpenAI Agents SDK (lighter abstraction) or custom implementations
- **For Enterprise/AWS**: Bedrock AgentCore (model-agnostic, but expect steep learning curve)
- **For Long-Running Tasks**: Claude Agent SDK (innovative multi-session memory architecture)

---

## Methodology & Limitations

### Source Types Used

| Source Type | Count | Examples |
|-------------|-------|----------|
| Official Documentation | 12 | AWS, Anthropic, OpenAI docs |
| Industry Reports | 8 | McKinsey, Gartner, GM Insights |
| Technical Comparisons | 7 | Turing, Langfuse, DataCamp |
| Community Sources | 10 | Hacker News, DEV Community, Medium |
| Security Research | 5 | Red Hat, Microsoft, Palo Alto |

### Research Limitations

1. **Recency Bias**: Framework features change rapidly; some information may be outdated within weeks
2. **Vendor Self-Reporting**: GitHub stars and download counts are self-reported metrics
3. **Survey Methodology**: Adoption and ROI statistics rely on surveys with varying methodologies
4. **Community Bias**: Developer forums over-represent vocal critics and enthusiasts
5. **Missing Data**: Limited independent benchmarks comparing framework performance

### Terminology Clarification

**Important**: The original research topic mentioned "AWS AgentKit"—this is actually **OpenAI's AgentKit**. AWS's agent offerings are:
- Amazon Bedrock Agents (fully managed)
- Amazon Bedrock AgentCore (enterprise platform)
- Strands Agents (open-source SDK)

---

## Findings

### 1. Framework Landscape Overview

The AI agent framework market has consolidated around several major categories, each with distinct architectural approaches and trade-offs.

#### Cloud Provider Platforms

**Amazon Bedrock AgentCore** reached general availability in late 2025 after a July preview, accumulating over 2 million SDK downloads in five months [14]. AgentCore is model-agnostic, supporting OpenAI, Google, Anthropic, Meta, and Mistral models. Key components include:

- **Runtime**: Serverless with microVM session isolation
- **Memory**: Persistent and episodic memory capabilities
- **Gateway**: Tool integration hub
- **Policy** (preview): Natural language to Cedar policy conversion
- **Evaluations**: 13 built-in quality evaluators

Evidence suggests AWS Bedrock faces significant developer experience challenges. Community reports indicate "slow responses, buggy experiences, and missing key features" [9]. The `agentcore deploy` CLI command is described as unreliable, with "cryptic IAM errors even with admin permissions" [15].

#### AI Company SDKs

**Anthropic Claude Agent SDK**, published September 29, 2025, introduces an innovative two-part architecture for long-running agents [16]:

1. **Initializer Agent**: Sets up environment, creates progress logs, commits state via Git
2. **Coding Agent**: Reads progress logs, makes incremental updates, maintains documentation

Key features include automatic context compaction, session forking, and CLAUDE.md for persistent project context. Developers praise it as their "default agent framework over tools like LangChain/CrewAI" [17].

**OpenAI AgentKit**, launched at Dev Day on October 6, 2025, consolidates agent building with a unified Responses API [18]. Built-in tools include WebSearchTool, FileSearchTool, ComputerTool, and CodeInterpreterTool ($0.03/container). The Agents SDK has accumulated over 11,000 GitHub stars since release.

#### Open-Source Frameworks

| Framework | GitHub Stars | Architecture | Best For |
|-----------|-------------|--------------|----------|
| LangChain | ~122,000 | Modular chains | Wide integrations |
| LangGraph | ~22,000 | Graph-based | Complex stateful workflows |
| CrewAI | 40,000+ | Role-based teams | Rapid prototyping |
| AutoGen | Growing | Conversational | Microsoft ecosystem |
| Dify | ~93,000 | Low-code | Non-technical users |

LangChain maintains the largest ecosystem with 600+ integrations [7], though it faces widespread criticism for over-abstraction and "dependency hell" [8][19]. CrewAI has emerged as the beginner-friendly alternative, with 1.8M+ monthly downloads and 60% Fortune 500 adoption claimed [20].

### 2. Model Context Protocol (MCP) Standardization

MCP is an open standard introduced by Anthropic in November 2024 to standardize LLM integration with external tools and data sources [6]. The protocol was donated to the Agentic AI Foundation under the Linux Foundation in December 2025, with co-founders including Anthropic, Block, and OpenAI.

**Adoption Timeline**:
- November 2024: Anthropic launches MCP
- March 2025: OpenAI adopts MCP
- April 2025: Google confirms Gemini support
- December 2025: Google launches managed MCP servers; Linux Foundation transfer

MCP has documented security vulnerabilities that organizations must address [11][12][21]:

- **Prompt Injection**: LLMs trust any convincing tokens, enabling confused deputy attacks
- **Tool Mutation**: Tools can modify their definitions post-installation
- **Data Exfiltration**: Mixing private data with untrusted instructions creates attack vectors
- **Command Injection**: Many MCP servers pass unescaped input to system commands

Security researchers note: "Model Context Protocol is powerful but dangerous. It wasn't designed with security first" [21].

### 3. Multi-Agent Orchestration Patterns

Three primary orchestration patterns have emerged for multi-agent systems [22][23]:

**Supervisor Pattern**
- Central orchestrator coordinates all agents
- Predictable control flow, easier debugging
- Best for enterprise workflows requiring compliance

**Hierarchical Architecture**
- Three layers: Strategy → Planning → Execution
- Top-down control and decision-making
- Best for complex decomposable tasks

**Swarm Pattern**
- Decentralized peer-to-peer communication
- Better scalability, harder to debug
- Best for emergent behavior and exploration

LangGraph enables graph-based orchestration with supervisor nodes [24]. CrewAI uses role-based design treating agents as "crew members" [10]. AutoGen frames everything as asynchronous conversation among specialized agents [25].

### 4. Market Economics

**Current Market Size**: The AI agent market is valued at $7.38-7.92 billion in 2025, with strong consensus across multiple research firms [1][2][3].

**Enterprise Implementation Costs** [26]:
- Basic implementations: $100,000-$200,000
- Comprehensive enterprise: $500,000-$2,000,000
- Setup fees: $50,000-$150,000
- Implementation timeline: 3-6 months

**Vendor Pricing Models**:
- Salesforce Agentforce: $2 per conversation
- Microsoft Copilot agents: $4 per hour
- Intercom: $0.99 per resolution
- CrewAI: $99/month to $120,000/year

**Cost Comparison**: AI agent interactions cost approximately $0.50 versus $4-8 for human agents, though this varies significantly by complexity [26].

### 5. Developer Experience & Community Sentiment

Community feedback reveals consistent themes across frameworks:

**LangChain Criticism** [7][8][19]:
> "You have to learn a bunch of custom classes and abstractions, even for things that could be done with plain Python or JavaScript"

- Over-abstraction and steep learning curve
- Dependency bloat ("dependency hell")
- Frequently outdated documentation
- API instability with breaking changes
- Good for prototyping, not recommended for production

**AWS Bedrock Pain Points** [9][15]:
> "Slow responses, buggy experiences, and missing key features"

- Each tool requires separate Lambda function management
- AgentCore CLI unreliable with cryptic IAM errors
- Intermittent failures in long-running workflows
- Silent runtime restarts without logs

**CrewAI Limitations** [10][27]:
- Framework rigidity makes dynamic role adjustment difficult
- High pricing barrier for smaller organizations
- API rate limits during concurrent testing
- Several unresolved high-severity bugs

**General Developer Sentiment** [28]:
> "The transition from deterministic systems to probabilistic agents is uncomfortable... handing over control flow to a non-deterministic model feels wrong to a mind trained on strict interfaces."

Developers report spending 60-70% of AI development time on prompt engineering, compared to "trying to fix a broken database with better SQL comments" [28].

### 6. Security Landscape

Security concerns are substantial across all agent frameworks [13][29][30]:

**Top Threats**:
1. Memory Poisoning
2. Tool Misuse
3. Privilege Compromise
4. Prompt Injection
5. Cascading Hallucinations

**Statistics**:
- 80% of organizations report encountering risky agent behaviors [13]
- 41% report IAM concerns for autonomous agents [29]
- 62% of practitioners cite security as top challenge [30]

Evidence suggests most vulnerabilities are framework-agnostic, arising from insecure design patterns, misconfigurations, and unsafe tool integrations rather than framework-specific flaws [30].

---

## Areas of Uncertainty

### Disputed Claims

**Long-Term Market Projections**: Sources disagree significantly on market size beyond 2025. Estimates for 2030-2034 range from approximately $50 billion to over $236 billion—nearly a 5x difference [1][2][3]. This reflects genuine uncertainty about adoption curves and economic impact.

**ROI Expectations vs. Reality**: One report indicates organizations project 171% average ROI from agentic AI [31], but this contradicts research showing 70-95% of enterprise AI projects fail to deliver measurable returns [5][32]. The gap between projected and realized ROI remains substantial and poorly understood.

### Weak Evidence Areas

1. **Actual Production Deployment Rates**: Most adoption statistics are based on surveys asking about plans, not verified deployments
2. **Framework Performance Benchmarks**: No independent, comprehensive benchmarks comparing framework performance exist
3. **Total Cost of Ownership**: Hidden costs (security, compliance, maintenance) are poorly documented
4. **Long-Term Maintenance Burden**: Insufficient longitudinal data on framework stability over multi-year deployments

### Rapid Evolution Risks

The framework landscape changes rapidly. Key uncertainties include:
- Whether MCP will achieve true standardization or fragment
- How cloud providers will differentiate as features converge
- Whether open-source frameworks will maintain pace with commercial offerings
- Impact of potential AI regulation on agent autonomy

---

## Conclusion

### What Is Established

1. **Market Fundamentals**: The AI agent market is real and growing, with current valuations around $7.5B and strong enterprise interest.

2. **Framework Differentiation**: Clear architectural differences exist between frameworks—LangGraph for complex workflows, CrewAI for rapid prototyping, Claude Agent SDK for long-running tasks, OpenAI Agents SDK for OpenAI ecosystem integration, AWS AgentCore for enterprise deployments.

3. **MCP as Emerging Standard**: The Model Context Protocol is gaining industry-wide adoption and will likely reduce tool integration fragmentation.

4. **Security Challenges**: Agent security is a genuine concern requiring explicit attention, particularly around prompt injection and tool permissions.

5. **Developer Experience Gap**: All frameworks have significant usability challenges that slow production deployments.

### What Remains Uncertain

1. **Actual ROI**: The gap between projected (171%) and realized ROI (with 95% failure rates) remains unresolved.

2. **Optimal Architecture**: Whether supervisor, hierarchical, or swarm patterns will dominate for different use cases is unclear.

3. **Market Trajectory**: Long-term market projections vary by nearly 5x, reflecting genuine uncertainty.

4. **Framework Longevity**: Which frameworks will survive consolidation over the next 2-3 years is unknown.

### Recommendations by Use Case

| Use Case | Recommended Framework | Confidence |
|----------|----------------------|------------|
| Quick POC/Demo | LangChain or CrewAI | HIGH |
| Production deployment | OpenAI Agents SDK or custom | MEDIUM |
| Multi-agent collaboration | CrewAI | HIGH |
| Complex stateful workflows | LangGraph | MEDIUM |
| Enterprise/AWS workloads | Bedrock AgentCore | MEDIUM |
| Long-running coding tasks | Claude Agent SDK | HIGH |
| Maximum control | Strands Agents or custom | HIGH |

---

## Sources

[1] Index.dev. "50+ Key AI Agent Statistics and Adoption Trends in 2025." 2025. https://www.index.dev/blog/ai-agents-statistics

[2] GM Insights. "AI Agents Market Size & Share, Growth Opportunity 2025-2034." 2025. https://www.gminsights.com/industry-analysis/ai-agents-market

[3] Grand View Research. "AI Agents Market Size And Share | Industry Report, 2033." 2025. https://www.grandviewresearch.com/industry-analysis/ai-agents-market-report

[4] McKinsey. "The state of AI in 2025: Agents, innovation, and transformation." 2025. https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai

[5] MIT Sloan. "The GenAI Divide: State of AI in Business 2025." 2025.

[6] Anthropic. "Introducing the Model Context Protocol." 2024. https://www.anthropic.com/news/model-context-protocol

[7] Designveloper. "Why Developers Say LangChain Is 'Bad': An Honest Look." 2025. https://www.designveloper.com/blog/is-langchain-bad/

[8] Woolf, Max. "The Problem With LangChain." 2023. https://minimaxir.com/2023/07/langchain-problem/

[9] Team Blind. "Sad state of Amazon Bedrock and AWS AI." 2025. https://www.teamblind.com/post/sad-state-of-amazon-bedrock-and-aws-ai-1ugw0bvr

[10] Lindy. "CrewAI Review 2025: Is It Really Worth Your Money?" 2025. https://www.lindy.ai/blog/crew-ai

[11] Willison, Simon. "Model Context Protocol has prompt injection security problems." April 2025. https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/

[12] Red Hat. "Model Context Protocol (MCP): Understanding security risks and controls." 2025. https://www.redhat.com/en/blog/model-context-protocol-mcp-understanding-security-risks-and-controls

[13] Palo Alto Networks Unit 42. "AI Agents Are Here. So Are the Threats." 2025. https://unit42.paloaltonetworks.com/agentic-ai-threats/

[14] AWS. "Introducing Amazon Bedrock AgentCore." 2025. https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/

[15] DEV Community. "Breaking Bedrock: What Really Happens When Your Agent Doesn't Work." 2025. https://dev.to/sinariver/i-built-a-bedrock-agent-for-learning-and-it-definitely-took-that-mission-seriously-kf3

[16] Anthropic. "Building agents with the Claude Agent SDK." 2025. https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk

[17] PromptLayer. "Building Agents with Claude Code's SDK." 2025. https://blog.promptlayer.com/building-agents-with-claude-codes-sdk/

[18] OpenAI. "Introducing AgentKit." October 2025. https://openai.com/index/introducing-agentkit/

[19] Medium. "6 Reasons why Langchain Sucks." 2025. https://medium.com/@woyera/6-reasons-why-langchain-sucks-b6c99c98efbe

[20] CrewAI Blog. "CrewAI OSS 1.0 - We are going GA." October 2025. https://blog.crewai.com/crewai-oss-1-0-we-are-going-ga/

[21] Embrace The Red. "Model Context Protocol Untrusted Servers & Confused Clients." 2025. https://embracethered.com/blog/posts/2025/model-context-protocol-security-risks-and-exploits/

[22] Swarms Documentation. "Multi-Agent Architectures." 2025. https://docs.swarms.world/en/latest/swarms/concept/swarm_architectures/

[23] AWS. "Multi-Agent collaboration patterns with Strands Agents and Amazon Nova." 2025. https://aws.amazon.com/blogs/machine-learning/multi-agent-collaboration-patterns-with-strands-agents-and-amazon-nova/

[24] Latenode. "LangGraph vs AutoGen vs CrewAI: Complete AI Agent Framework Comparison." 2025. https://latenode.com/blog/langgraph-vs-autogen-vs-crewai-complete-ai-agent-framework-comparison-architecture-analysis-2025

[25] Turing. "A Detailed Comparison of Top 6 AI Agent Frameworks in 2025." 2025. https://www.turing.com/resources/ai-agent-frameworks

[26] Agentman/Medium. "The complete guide to AI Agent Pricing Models in 2025." 2025. https://medium.com/agentman/the-complete-guide-to-ai-agent-pricing-models-in-2025-ff65501b2802

[27] Sider. "CrewAI Review 2025: Is This Multi-Agent Framework Worth Your Build?" 2025. https://sider.ai/blog/ai-tools/crewai-review-2025-is-this-multi-agent-framework-worth-your-build

[28] Phil Schmid. "Why (Senior) Engineers Struggle to Build AI Agents." 2025. https://www.philschmid.de/why-engineers-struggle-building-agents

[29] AWS. "The Agentic AI Security Scoping Matrix." 2025. https://aws.amazon.com/blogs/security/the-agentic-ai-security-scoping-matrix-a-framework-for-securing-autonomous-ai-systems/

[30] ACM Computing Surveys. "AI Agents Under Threat: A Survey of Key Security Challenges." 2025. https://dl.acm.org/doi/10.1145/3716628

[31] PagerDuty. "2025 Agentic AI ROI Survey Results." 2025. https://www.pagerduty.com/resources/ai/learn/companies-expecting-agentic-ai-roi-2025/

[32] BCG. "AI Adoption in 2024: 74% of Companies Struggle to Achieve and Scale Value." 2024. https://www.bcg.com/press/24october2024-ai-adoption-in-2024-74-of-companies-struggle-to-achieve-and-scale-value

---

*Report generated: December 13, 2025*
