---
chunk_id: "4-3-1013b0cabc-chunk-0006"
source_id: "4-3-1013b0cabc"
source_file: "New folder (3)/4.3.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 6
confidence: "first-pass"
extraction_method: "structured-local"
---

Example 4.6.1: Uplink Design and Required Trans-
mitter Power
Problem Statement
A Ku-band satellite transponder has:
• Linear gain: 127 dB
• Saturation output power: 5 W
• Receive antenna gain at 14 GHz: 26 dB
An uplink at 14.45 GHz uses an earth station antenna with gain 50 dB, a waveguide
loss of 1.5 dB, atmospheric loss of 0.5 dB, and the station lies on the 2 dB contour
of the satellite beam.
Compute the required transmitter power to obtain:
1. 1 W output from the satellite transponder under clear sky.
2. The transmitter rating needed to maintain 1 W output for 99.99% of the
year, given 7 dB rain attenuation.
Solution
1. Required Input Power to the Transponder
The transponder gain is 127 dB, so to obtain 1 W = 0 dBW output:
Pin = Pout −Gtrans = 0 −127 = −127 dBW.
2. Uplink Budget
The uplink power equation is:
Pr = EIRP + Gr −Lp −Lat −Lta −Lpt.
Rearranged to solve for transmitter power:
Pt = Pr −Gt −Gr + Lp + Lta + Lat + Lpt.
10

## Page 11

Given:
Pr = −127 dBW,
Gt = 50 dB,
Gr = 26 dB,
Lta = 1.5 dB,
Lat = 0.5 dB,
Lpt = 2.0 dB,
Lp ≈207.2 dB
(path loss at 38,500 km).
Compute:
Pt = −127 + 50 + 26 + 207.2 −1.5 −0.5 −2.0
= 7.2 dBW.
Convert to watts:
Pt = 107.2/10 = 5.2 W.
3. Required Power Under Rain Fade
Rain attenuation = 7 dB:
Pt,rain = 7.2 + 7 = 14.2 dBW.
Convert to watts:
Pt,rain = 1014.2/10 = 26.3 W.
Final Answers
Pt = 5.2 W
(clear sky)
Pt,rain = 26.3 W
(to guarantee 99.99% availability)
11

## Page 12

Example 4.7.1: Combining C/N and C/I Values
Problem Statement
An earth station experiences:
(C/N)dn = 20 dB,
(C/N)up = 20 dB.
For a bent-pipe transponder:
• Find the overall (C/N)0.
• If the transponder generates intermodulation with (C/I) = 24 dB, find the
new overall (C/N)0.
Solution
Convert to linear values:
(C/N)up = (C/N)dn = 1020/10 = 100.
Use the reciprocal formula:
1
(C/N)0
=
1
(C/N)up
+
1
(C/N)dn
.
Compute:
1
(C/N)0
= 0.01 + 0.01 = 0.02.
Thus:
(C/N)0 = 50
⇒
10 log10(50) = 17.0 dB.
Including Intermodulation Interference
Convert:
(C/I) = 1024/10 = 251.2.
Include third term:
1
(C/N)0
= 0.01 + 0.01 +
1
251.2 = 0.020 + 0.00398 = 0.02398.
So:
(C/N)0 =
1
0.02398 = 41.7.
12

## Page 13
