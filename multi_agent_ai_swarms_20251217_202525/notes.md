# Research Notes: Multi-Agent AI Swarms

## Collection Phase 1 - December 17, 2024

### Key Findings Summary

#### Framework Landscape
- **Four major frameworks dominate**: AutoGen (Microsoft), CrewAI, LangGraph (LangChain), OpenAI Swarm
- Each has distinct architectural philosophy:
  - AutoGen: Event-driven, actor model, enterprise-focused
  - CrewAI: Role-based crews, simplest to adopt
  - LangGraph: Graph-based workflows, fine-grained control
  - OpenAI Swarm: Lightweight, educational, stateless (now superseded by Agents SDK)

#### Market Intelligence
- Enterprise agentic AI market: $2.58B (2024) → $24.5B (2030) at 46.2% CAGR
- Broader AI agents market: $5.9B (2024) → $105.6B (2034) at 38.5% CAGR
- Investment surge: $3.8B raised by AI agent startups in 2024 (3x vs 2023)
- 85% of enterprises expected to implement AI agents by end of 2025

#### Historical Context
- Swarm Intelligence coined by Beni & Wang (1989)
- ACO by Marco Dorigo (1992)
- PSO by Kennedy & Eberhart (1995)
- LLM-based multi-agent explosion: 2023-present

#### Safety & Risks
- Three key failure modes identified: miscoordination, conflict, collusion
- Emergent behavior concerns in multi-agent scenarios
- Steganographic communication risk (GPT-4 covert messages 26% undetected)
- Most single-agent safety measures don't translate to multi-agent settings

### Questions Answered
- [x] What are the leading frameworks? (AutoGen, CrewAI, LangGraph, Swarm)
- [x] What is market size and growth? ($2.58B-$5.9B, 38-46% CAGR)
- [x] What are the historical foundations? (1989-1995 swarm intelligence)
- [x] What are key safety concerns? (miscoordination, conflict, collusion, emergent behavior)

### Still Need to Investigate
- [ ] Detailed benchmarks and evaluation metrics
- [ ] Specific enterprise case studies
- [ ] LangGraph deep dive
- [ ] Regulatory landscape
- [ ] MetaGPT and other frameworks
- [ ] Academic vs. production implementation gaps

### Source Quality Assessment
- **Strong academic coverage**: IJCAI 2024 survey, arXiv papers, ACM publications
- **Good industry reports**: Grand View Research, GM Insights, Deloitte
- **Official documentation**: GitHub repos for all major frameworks
- **Gap**: Need more primary case studies and benchmark comparisons

---
*Phase 1 complete. 18 sources collected, 25 claims documented.*
