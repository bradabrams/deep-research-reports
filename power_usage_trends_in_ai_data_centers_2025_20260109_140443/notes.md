# Research Notes: AI Data Center Power Usage Trends 2025

## Collection 1 - Key Findings Summary

### Global Consumption Baseline & Projections

| Year | Total DC Consumption | AI Share | Source |
|------|---------------------|----------|--------|
| 2024 | 415 TWh (1.5% global) | 5-15% | IEA |
| 2025 | 448-536 TWh (2% global) | ~21% | Gartner/Deloitte |
| 2030 | 945-1,000 TWh (3% global) | 35-50% | IEA/Gartner |

### US-Specific Data
- **2024**: 183 TWh (4%+ of US electricity)
- **2030 Projection**: 426 TWh (133% growth)
- **Grid Capacity**: 61.8 GW (2025) → 134.4 GW (2030)
- **Regional Concentration**: Virginia (26% of state electricity), North Dakota (15%)

### AI-Optimized Servers
- **2025**: 93 TWh
- **2030**: 432 TWh (nearly 5x increase)

### Major Tech Company Consumption (2024-2025)
- **Google**: ~32 TWh (27% YoY growth, doubled since 2020)
- **Microsoft**: ~30 TWh (27% YoY growth)
- Combined with Meta: +17 TWh additional demand in 2024

### Energy Per AI Query
- **ChatGPT**: 0.34 Wh (OpenAI official) to 2.9 Wh (IEA estimate)
- **Google Search**: 0.3 Wh
- **AI vs Search**: ~10x more energy for AI queries
- **ChatGPT Scale**: 2.5 billion queries/day = ~850 MWh daily

### GPU Power Consumption
| GPU | TDP | Efficiency vs Prior |
|-----|-----|---------------------|
| A100 | 400W | Baseline |
| H100 | 700W | 2x efficiency, 4x faster training |
| B200 | ~600W actual (1000W spec) | 57% faster than H100 |

- H100 fleet projected: 13.8 TWh annual consumption

### PUE Metrics
- **Industry Average**: 1.56
- **Best Practice Target**: ≤1.2
- **Google**: 1.20 TTM average
- **Liquid Cooling Impact**: Up to 45% PUE improvement

### Energy Sources (US Data Centers 2024)
- Natural Gas: 40%+
- Renewables (solar/wind): 24%
- Nuclear: 20%
- Coal: 15%

### Investment & Infrastructure
- **Global DC Investment 2024**: ~$500 billion (doubled since 2022)
- **Grid Upgrades Needed**: $720 billion through 2030 (Goldman Sachs)
- **Clean Energy Contracted**: 50GW by Q3 2024 (US only)

### Grid Strain Indicators
- PJM (largest US grid): 6GW reliability shortfall projected by 2027
- Interconnection queues causing multi-year delays
- Texas SB-6: New requirements for loads >75MW

### Nuclear Commitments
- Microsoft: 837MW from Three Mile Island (20-year PPA)
- Meta: RFP for 1.4GW new nuclear
- Amazon: SMR agreements for 320-960MW

---

## Key Tensions & Debates

1. **Forecast Divergence**: Wide range in projections (600-1,300 TWh by 2030)
2. **Efficiency vs Demand**: Hardware improvements offset by explosive growth
3. **Renewable Claims**: State AGs investigating RECs/carbon accounting
4. **Grid Readiness**: Supply infrastructure lagging demand growth
5. **Carbon-Free Claims**: Google at 66% 24/7 carbon-free vs 100% annual matching

---

## Questions for Further Research

1. Detailed breakdown of training vs inference energy
2. Regional policy responses beyond Texas
3. SMR deployment timelines and capacity
4. Water usage trends (cooling)
5. Embodied carbon in hardware manufacturing

---

*Last Updated: 2026-01-09*
*Collection: 1 of 2*
