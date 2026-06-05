---
chunk_id: "5-48ae856785-chunk-0007"
source_id: "5-48ae856785"
source_file: "New folder (3)/5.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 7
confidence: "first-pass"
extraction_method: "structured-local"
---

Satellite Communications
Chapter 5
Worked Example
Example 5.4.1: Solution (Part II)
(c) BER in clear air
Convert C/N to linear:
C
N = 1014/10 = 25
BPSK:
Pb = Q
p
2C/N

= Q(
√
50) = Q(7.07) ≈8 × 10−11
QPSK:
QPSK requires 3 dB more C/N:
(C/N)QPSK = 11 dB ⇒C/N = 12.6
Pb = Q(
√
2 × 12.6) = Q(5.02) ≈3 × 10−7
(d) BER with 3 dB rain attenuation
New C/N = 11 dB ⇒C/N = 12.6
BPSK:
Pb ≈3 × 10−7
QPSK:
(C/N)QPSK = 8 dB ⇒C/N = 6.3
Pb = Q(3.55) ≈2.2 × 10−4
Conclusion:
• BPSK remains usable during rain
• QPSK BER degrades rapidly under fading
16

## Page 17

Satellite Communications
Chapter 5
Worked Example
Example 5.4.2: Effect of Implementation Margin (Problem)
A Ku-band satellite link uses 10 MHz of bandwidth in a transponder. The RRC
filter roll-off factor is α = 0.25.
The clear-air carrier-to-noise ratio is
(C/N)0 = 16 dB
which drops to 13 dB for 0.1% of the year.
Implementation margins:
• BPSK: 0.8 dB
• QPSK: 1.2 dB
a) Determine the symbol rate.
b) Determine the bit rate for BPSK and QPSK.
c) Compute BER in clear air and during fade.
d) Recommend a modulation scheme.
Worked Example
Example 5.4.2: Solution (Part I)
(a) Symbol rate
Rs =
B
1 + α = 10
1.25 = 8 Msps
(b) Bit rate
• BPSK: Rb = 8 Mbps
• QPSK: Rb = 16 Mbps
17

## Page 18

Satellite Communications
Chapter 5
Worked Example
Example 5.4.2: Solution (Part II)
(c) BER calculation
Clear air
• BPSK effective C/N = 15.2 dB ⇒C/N = 33.1
Pb ≈Q(
√
66.2) ≈2.5 × 10−15
• QPSK effective C/N = 14.8 dB ⇒C/N = 30.2
Pb ≈Q(
√
30.2) ≈2 × 10−8
0.1% of the year
• BPSK effective C/N = 12.2 dB ⇒C/N = 16.6
Pb ≈Q(
√
33.2) ≈5 × 10−9
• QPSK effective C/N = 11.8 dB ⇒C/N = 15.1
Pb ≈Q(
√
15.1) ≈5 × 10−5
(d) Recommendation
• BPSK provides excellent reliability year-round
• QPSK doubles throughput but suffers unacceptable BER during fades
Final decision:
BPSK is recommended unless strong FEC is used.
18
