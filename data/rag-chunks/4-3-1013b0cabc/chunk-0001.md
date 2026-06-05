---
chunk_id: "4-3-1013b0cabc-chunk-0001"
source_id: "4-3-1013b0cabc"
source_file: "New folder (3)/4.3.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1

Downlink Design and Link Budgets
Satellite Communications – Chapter 4
4.4 Design of Downlinks
The design of a satellite downlink must satisfy two key engineering objectives:
1. Meet a minimum required CNR for a specified percentage of time.
2. Carry maximum revenue-generating traffic at minimum cost.
A well-known engineering principle applies:
“An engineer is someone who can do for a dollar what any fool can do for one hundred
dollars.”
While any link can be made extremely reliable by using very large antennas and high
power, this approach is prohibitively expensive. Good system design requires balancing:
• antenna size
• amplifier power
• rain margin
• modulation and coding
For example, designing a link to withstand a 20 dB rain fade instead of a natural
3 dB fade requires an earth station antenna with ≈7 times larger diameter, which is
rarely economical.
Rain Attenuation and Link Availability
All downlinks experience rain attenuation, with severity increasing with frequency:
• C-band (6/4 GHz): typically 1–2 dB
• Ku-band (14/11 GHz): moderate (5–10 dB)
• Ka-band (30/20 GHz): severe and dominant impairment
1

## Page 2

Satellite links are usually designed for annual availability in the range:
99.5% to 99.99%
This means the CNR will fall below the permissible value for:
0.5% to 0.01% of the year
Examples:
0.01% of a year = 52 minutes
0.5% of a year = 43.8 hours
Rain is highly variable. A link designed for 52 minutes of outage may experience
hours of outage in one rainy year and none the next.
Applications with strict availability requirements:
• Voice circuits
• Corporate and financial data links
• Intercontinental backbone connections
Internet access can tolerate several hours of degraded quality, making it suitable for
Ku/Ka-band consumer terminals.
4.4.1 Link Budgets
A link budget is a structured table where:
• Gains are entered as positive quantities.
• Losses are entered as negative quantities.
Key benefits:
• Easy recalculation when parameters change.
• Works for uplinks, downlinks, and full system analysis.
• Simplifies verification of required CNR.
A two-way satellite link requires four separate link budgets:
2

## Page 3
