---
chunk_id: "4-4-27ceec6dc1-chunk-0003"
source_id: "4-4-27ceec6dc1"
source_file: "New folder (3)/4.4.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

Small Receiving Antennas and Frequency Allocation
The high flux density produced by DBS-TV satellites enables the use of very small re-
ceiving antennas:
• Typical dish diameter: 0.45–0.75 m
• Beamwidth: approximately 4◦for a 0.45 m dish
Because of the wide beamwidth of small dishes:
• DBS satellites must be widely spaced in the GEO arc
• A spacing of 9◦is used in the United States
The 12-GHz DBS band is allocated exclusively to broadcasting services to prevent
interference.
Rain Attenuation and Link Availability
At Ku band, rain attenuation is a dominant impairment.
• Typical rain attenuation:
– 3 dB for 0.2% of the year (≈15 h)
– 6 dB for 0.01% of the year (≈52 min)
DBS-TV systems typically use small link margins to allow small antennas:
• Rain margin: 3–8 dB
• Annual outage time: 10–40 h
• Typical availability: > 99.7%
This represents a deliberate trade-off between link availability and user equipment
cost.
A representative downlink budget for a Ku-band GEO DBS-TV system serving
the United States is summarized in Table 1. The system employs QPSK modulation
with threshold carrier-to-noise ratio is
 C
N

th
= 8.6 dB
4

## Page 5

Table 1: Link Budget for Ku-Band DBS-TV Receiver
DBS-TV Terminal Received Signal Power
Transponder output power (160 W)
22.0 dBW
Satellite antenna on-axis gain
34.3 dB
Free-space path loss (12.2 GHz, 38,000 km)
−205.7 dB
Receiving antenna gain (0.45 m dish)
33.5 dB
Edge-of-beam loss
−3.0 dB
Clear sky atmospheric loss
−0.4 dB
Miscellaneous losses
−0.4 dB
Received carrier power, C
−119.7 dBW
DBS-TV Terminal Receiver Noise Power
Boltzmann constant, k
−228.6 dBW/K/Hz
System noise temperature (clear sky)
145 K (21.6 dBK)
Receiver noise bandwidth
20 MHz (73.0 dBHz)
Noise power, N
−134.0 dBW
Clear-sky C/N
14.3 dB
Link margin above threshold
5.7 dB
Link availability
> 99.7%
Table 4.5: Ku-Band DBS-TV Link Budget
System Description
• Transponder output power: 160 W (single-carrier, no backoff)
• Satellite antenna beamwidth: 5.5◦(E–W) × 2.5◦(N–S)
• Coverage zone: ≈4000 km (E–W) × 2000 km (N–S)
• Receiving antenna: 0.45 m offset-fed parabolic reflector
• Aperture efficiency: 67%
The offset-fed design avoids feed blockage, increasing antenna efficiency and gain.
Noise Bandwidth and Data Rate
The DBS-TV system uses:
• QPSK modulation
• Symbol rate: 20 Msps
• Receiver noise bandwidth: 20 MHz
5

## Page 6
