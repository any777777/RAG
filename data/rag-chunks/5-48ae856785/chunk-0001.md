---
chunk_id: "5-48ae856785-chunk-0001"
source_id: "5-48ae856785"
source_file: "New folder (3)/5.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1

Satellite Communications
Chapter 5
Chapter 5
Modulation and Multiplexing Techniques
for Satellite Links
Chapter Overview
This chapter introduces modulation and multiplexing techniques used in satellite links.
Although modern links are predominantly digital, analog FM remains important because
it illustrates the tradeoff between bandwidth and noise performance.
1
Multiplexing in Satellite Systems
Analog FDM has mostly disappeared, but FDMA remains widely used in satellite sys-
tems.
Definition
FDMA divides the transponder bandwidth into smaller frequency channels, each
allocated to a user on a fixed or demand basis.
FDMA is common in:
• SCPC systems
• VSAT networks
Single Channel Per Carrier (SCPC)
Single Channel Per Carrier (SCPC) is a satellite multiple access technique in which
one radio-frequency (RF) carrier is assigned to a single communication channel, typically
carrying one voice circuit or a low-rate data stream.
• Each user occupies a dedicated carrier frequency.
• SCPC is commonly implemented using FDMA.
• It provides low delay and simple terminal design.
• Spectral efficiency is lower compared to burst-access schemes.
Typical applications:
1

## Page 2

Satellite Communications
Chapter 5
• Satellite telephony
• VSAT voice channels
• Point-to-point data links
• Backup and emergency communications
Very Small Aperture Terminal (VSAT)
Very Small Aperture Terminal (VSAT) is a small, two-way satellite earth station
that uses a compact antenna, typically in the range of 0.6–2.4 m in diameter, to provide
voice, data, and video communication services via satellite.
• Operates mainly in C-band, Ku-band, and Ka-band.
• Communicates with a central hub station or directly with other VSATs.
• Supports star, mesh, or hybrid network topologies.
• Employs access schemes such as TDMA, FDMA (including SCPC), or hybrid tech-
niques.
Typical applications:
• Corporate data networks
• Banking and ATM connectivity
• Remote Internet access
• Oil, gas, maritime, and rural communications
2
Frequency Modulation (FM)
2.1
Why FM is Used
Satellite links often have low carrier-to-noise ratios (5–25 dB), while analog TV/voice
requires higher baseband S/N ratios.
Important Concept
FM can produce baseband S/N ratios much higher than the RF/IF C/N ratio, but
requires wider bandwidth (WBFM).
2

## Page 3
