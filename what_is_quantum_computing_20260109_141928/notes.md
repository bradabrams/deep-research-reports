# Research Notes: What is Quantum Computing?

## Research Iteration 1 - January 9, 2026

### Key Findings Summary

#### Foundational Concepts
- **Quantum computing** uses qubits that leverage superposition, entanglement, and interference
- **Qubits** can exist in multiple states simultaneously (n qubits = 2^n states)
- **Bloch sphere** provides geometric visualization of qubit states
- **Decoherence** is the fundamental challenge - qubits lose quantum properties when interacting with environment

#### Hardware Landscape (2025)
| Approach | Key Players | Coherence | Temperature | Strengths |
|----------|-------------|-----------|-------------|-----------|
| Superconducting | IBM, Google, Rigetti | ~300 μs | ~15 mK | Fast gates |
| Trapped Ion | IonQ, Quantinuum | 0.2-600 s | Room temp (laser) | High fidelity |
| Photonic | Xanadu, PsiQuantum | N/A | Room temp | No cooling needed |
| Neutral Atom | QuEra, Pasqal | Variable | μK | Scalability |

#### Major 2025 Breakthroughs
1. **Google Willow**: Error correction below threshold (2.14x improvement with distance)
2. **IonQ**: 99.99% two-qubit gate accuracy, $39.9M revenue in Q3
3. **Quantinuum**: 50 entangled logical qubits, 98%+ gate fidelity
4. **IBM Nighthawk**: 120 qubits, 30% more complex circuits
5. **QuEra**: 96 logical qubits with below-threshold performance

#### Market Data
- 2025 market size: $1.4-3.5 billion (estimates vary)
- 2030 projections: $12-20 billion
- CAGR: 20-42%
- Potential value creation: $250 billion across industries (Bain)

#### Key Algorithms
- **Shor's**: Factoring (exponential speedup) - cryptography threat
- **Grover's**: Search (quadratic speedup - √N)
- **VQE**: Chemistry/molecular simulation (NISQ-era)
- **QAOA**: Optimization problems (NISQ-era)

#### Real-World Applications Already Deployed
1. HSBC: 34% improvement in bond trading predictions (IBM Heron)
2. Ford Otosan: Scheduling reduced from 30 min to <5 min (D-Wave)
3. IonQ: Quantum advantage in drug discovery simulations

#### Cryptography Implications
- NIST released 3 post-quantum standards (August 2024): ML-KEM, ML-DSA, SLH-DSA
- "Harvest now, decrypt later" threat is real
- Migration to PQC may take 10-20 years
- RSA-2048 potentially breakable by 2030

#### Challenges & Limitations
- NISQ devices: 50-1,000 qubits with high error rates
- Error correction overhead: ~1,000 physical qubits per logical qubit
- Gate fidelity: 95-99% for 2-qubit gates (need >99.9%)
- ~1,000 gate limit before noise overwhelms signal

#### Industry Roadmaps
| Company | 2028-2029 Target |
|---------|------------------|
| IBM | 200 logical qubits, 100M gates (Starling) |
| IonQ | 20,000 physical qubits, CRQC |
| Google | Continued Willow scaling |

### Historical Context
- 1981-82: Feynman proposes quantum simulation
- 1985: Deutsch defines universal quantum computer
- 1994: Shor's algorithm revolutionizes the field
- 1996: Grover's algorithm
- 2019: Google claims quantum supremacy (disputed by IBM)
- 2023: IBM Condor breaks 1,000 qubits
- 2024: Google Willow error correction breakthrough
- 2025: Industry inflection point - commercial reality begins

### Sources Consulted
- 20 sources identified (16 HIGH credibility, 4 MEDIUM)
- Mix of: IBM/Google official, academic (Nature), industry analysis (TQI, Bain, Deloitte), news, NIST

### Still To Research
- [ ] Deeper dive on quantum networking / quantum internet
- [ ] Geopolitical aspects (US-China race, export controls)
- [ ] Educational pathways / skills development
- [ ] Specific company case studies
- [ ] More visual assets

---
*Last updated: January 9, 2026*
