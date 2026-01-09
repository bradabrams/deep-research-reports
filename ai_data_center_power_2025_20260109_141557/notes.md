# Research Notes: AI Data Center Power 2025

## Collection 1 - January 9, 2025

---

## Key Statistics Summary

### Global Data Center Power Consumption
- **2024**: ~415 TWh (1.5% of global electricity)
- **2025**: ~448-536 TWh (projected 16% YoY growth)
- **2030**: ~945-980 TWh (doubling, ~3% of global electricity)
- Growth rate: 15% annually (4x faster than other sectors)

### US Data Center Power
- **2024**: 183 TWh (4% of US electricity) - equivalent to Pakistan's total demand
- **2030**: 426 TWh projected (7.8% of US electricity)
- 133% growth projected 2024-2030

### AI-Specific Power Share
- **Current (2025)**: 5-21% of data center power (estimates vary)
- **2030 Projection**: 35-50% of data center power
- AI-optimized server electricity to grow from 93 TWh (2025) to 432 TWh (2030) - nearly 5x

---

## Major Tech Company Analysis

### Microsoft
- Electricity demand projected to surge 600% by 2030 (Stand.earth report)
- Three Mile Island restart deal: $16B, 20-year, 835MW (targeting 2028)
- $100B consortium with BlackRock, GIP, MGX for datacenter/power infrastructure
- Most North American data centers still draw 50%+ from coal/gas grids
- "Plug-and-play" datacenters announced (July 2025) bypassing grid constraints

### Google
- First US corporate SMR fleet deal with Kairos Power (500MW, 2030+ target)
- Grid modernization initiative with PJM Interconnection
- Lead on geothermal power among tech companies
- 48% GHG emission increase since 2019 (mostly data centers)
- TPU pods use direct-to-chip liquid cooling

### Amazon
- Emissions rose to 68.25M metric tons in 2024 (up from 64.38M in 2023)
- First emissions increase since 2021, primarily data centers
- 500+ wind and solar projects worldwide
- $500M financing round for X-energy SMRs (targeting 5GW by 2039)
- Susquehanna nuclear conversion to AI campus ($20B+)
- FERC rejected increased electricity to Susquehanna data center (appealing)

### Meta
- RFP issued for 1-4GW of new nuclear
- 1.1GW, 20-year PPA with Clinton Clean Energy Center (Illinois)
- Air-Assisted Liquid Cooling across 40M+ sq ft
- Catalina rack design: 140kW with 72 GPUs (31% cost savings expected)

---

## GPU Power Consumption Evolution

| GPU | TDP (Watts) | Generation |
|-----|-------------|------------|
| V100 | 250-300W | Volta |
| A100 | 300-400W | Ampere |
| H100 | 700W | Hopper |
| H200 | 700W | Hopper |
| B200 | 1000W | Blackwell |
| GB200 NVL72 | 1200W/GPU | Blackwell |

**Key insight**: Power consumption is becoming critical bottleneck - 4x increase from A100 to B200

### Performance vs Power
- B200 is 57% faster for training than H100
- B200 delivers 2.2x training performance, 4x inference performance vs H100
- Real-world 8xB200 node: ~6.5-7kW total system power

---

## GPT-5 Energy Analysis

- Single GPT-5 query: 18.35 Wh average (up to 40 Wh for complex responses)
- GPT-4 query: 2.12 Wh
- GPT-5 uses 8.6x more electricity per query than GPT-4
- "Thinking mode" can use 5-10x more power than standard response

### Hypothetical Maximum
- If all 2.5B daily ChatGPT queries used GPT-5:
  - 45 GWh daily energy use
  - Equivalent to 2-3 nuclear power plants
  - Could power 1.5M US homes for a day

---

## Stargate Project Details

- **Announced**: January 21, 2025 by President Trump
- **Total Investment**: Up to $500B by 2029
- **Partners**: OpenAI (40%), SoftBank (40%), Oracle, MGX
- **Initial Capital**: $19B each from SoftBank and OpenAI, $7B each from Oracle and MGX

### Sites (as of September 2025)
1. Abilene, Texas (flagship, operational)
2. Shackelford County, Texas
3. Doña Ana County, New Mexico
4. Lordstown, Ohio
5. Milam County, Texas
6. Midwestern US site (TBD)

**Total planned capacity**: Nearly 7GW
**Projected jobs**: 100,000

### International Expansion
- **UAE Stargate**: Announced May 2025, opening 2026
- **Norway**: Launched July 2025, renewable energy focus
- **Argentina**: Up to $25B, 500MW capacity

---

## Grid Impact & Electricity Prices

### Price Increases
- Wholesale electricity up 267% in data center areas (vs 5 years ago)
- Carnegie Mellon projection: 8% average US bill increase by 2030
- Virginia/Mid-Atlantic: Could exceed 25% increase

### Capacity Market
- PJM capacity auction price: 833% increase for 2025-2026
- Cost to secure power supply: $2.2B → $14.7B (YoY)
- FERC 5-year demand forecast: 128GW peak load increase (3x previous estimate)

### Grid Strain
- 20% of planned data centers face grid connection delays (IEA)
- Virginia/Mid-Atlantic at "elevated risk" of supply shortfall
- PJM interconnection requests surged from "a few dozen to thousands annually"

---

## Regional Analysis: Virginia

### Scale
- Highest data center concentration globally
- 26% of state electricity consumed by data centers (2023)
- Energy demand projected to rise 183% by 2040

### Regulatory Response
- New electricity rate class approved November 2025
- Starting January 2027: 85% contracted distribution/transmission, 60% generation demand required
- Coalition of 50+ groups pushing for data center reform legislation

### Community Impact
- $24.7B PW Digital Gateway project delayed by local opposition
- Concerns: environmental impact, noise, grid strain, historic sites
- Cross-party opposition: GOP (tax incentives, grid), Democrats (environment)

---

## Environmental Impact

### Carbon Emissions
- AI could add 24-44M metric tons CO2 annually by 2030
- Equivalent to 5-10 million additional cars
- 60% of new data center demand met by fossil fuels (Goldman Sachs)
- Additional 220M tons CO2 emissions projected

### Corporate Emissions Trends
- Amazon: 64.38M → 68.25M metric tons (2023-2024), first increase since 2021
- Google: 48% increase since 2019
- Most Microsoft NA data centers: 50%+ coal/gas power

### Transparency Issues
- Lack of distinction between AI and non-AI workloads in reports
- Environmental disclosure often insufficient for determining total data center performance
- AI server industry "unlikely to meet net-zero aspirations by 2030" without carbon offsets

---

## Cooling Technology Trends

### Market Size
- Immersion cooling: $4.87B (2025) → $11.10B (2030), 17.91% CAGR
- Total liquid cooling: $4.9B (2024) → $21.3B (2030), 27.6% CAGR

### Adoption
- 2024: Liquid cooling at 46%, air cooling at 54%
- 2025: "Tipping point" year - liquid cooling becomes baseline for AI
- Single-phase direct-to-chip becoming standard for AI workloads

### Power Density Evolution
- Traditional max: 10-15 kW per rack
- Current AI clusters: 30-60 kW typical
- Bleeding edge: 80-120 kW per rack
- Meta Catalina racks: 140kW with 72 GPUs

### Efficiency Gains
- Liquid cooling: up to 40% reduction in cooling energy
- PUE improvement: 1.4-1.6 (air) → <1.2 (liquid)
- Microsoft reported 30% efficiency gain with two-phase immersion

### Hyperscaler Adoption
- **Meta**: Air-Assisted Liquid Cooling across 40M+ sq ft
- **Google**: Direct-to-chip for TPU pods, 4x compute density increase
- **Microsoft**: Two-phase immersion testing for AI training clusters

---

## Nuclear Power for AI

### Deal Summary (as of Dec 2025)
Big tech signed 10GW+ of new US nuclear capacity in past year

| Company | Deal | Capacity | Timeline |
|---------|------|----------|----------|
| Microsoft | Three Mile Island restart | 835MW | 2028 |
| Google | Kairos Power SMR fleet | 500MW | 2030+ |
| Amazon | X-energy SMR investment | 5GW | 2039 |
| Meta | Clinton Clean Energy PPA | 1.1GW | Active |

### SMR Pipeline
- Global pipeline: 47GW (end of Q1 2025)
- Over half of capacity in US
- Estimated $300B needed to build current pipeline

### Challenges
- No SMRs currently operate in US or Europe
- Still 5+ years from commercial operation
- First planned US SMR (NuScale) cancelled due to rising costs
- "Nuclear has had many false starts" - David Wilson, Energy Exemplar

---

## Community Opposition

### Scale of Resistance
- $64B in data center projects blocked or delayed (as of March 2025)
- Data Center Watch tracking nationwide opposition

### Notable Cases
- **PW Digital Gateway** (VA): $24.7B project delayed
- **xAI Boxtown**: Environmental racism lawsuit by SELC/NAACP
- Clean Air Act violations alleged

### Concerns Raised
- Environmental impact
- Noise pollution
- Grid strain
- Historic site damage
- Water access
- Air quality
- Energy poverty in host communities

---

## Key Quotes

> "AI is the most important driver of this growth." - IEA

> "We are effectively seeing customers across the Mid-Atlantic subsidizing the electrical infrastructure that's needed for Northern Virginia's data centers." - Energy consultant

> "Nuclear has had many false starts." - David Wilson, CEO Energy Exemplar

> "2025 marks the year when liquid cooling became unavoidable rather than optional for serious AI infrastructure." - Industry analysis

---

## Research Gaps Identified

1. Detailed breakdown of training vs inference power consumption
2. Water consumption statistics (mentioned but not detailed)
3. Specific grid connection wait times by region
4. Detailed cost-per-MW analysis for AI-ready capacity
5. International comparison (EU, China regulations)
6. Specific renewable energy percentage by company
