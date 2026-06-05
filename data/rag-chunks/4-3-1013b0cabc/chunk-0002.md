---
chunk_id: "4-3-1013b0cabc-chunk-0002"
source_id: "4-3-1013b0cabc"
source_file: "New folder (3)/4.3.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

• two uplinks
• two downlinks
For a bent-pipe transponder:
1
CNRtotal
=
1
CNRuplink
+
1
CNRdownlink
Worst-Case Assumptions
Downlink budgets are computed for worst-case conditions:
• Earth station at edge of satellite footprint (3 dB loss)
• Maximum slant range
• Lowest elevation angle
• Maximum rain attenuation
• Possible antenna mispointing
Received Power and Noise Power
Received Carrier Power
Pr = EIRP + Gr −Lp −La −Lta −Lra
(dBW)
Noise Power
Pn = k Ts Bn
(W)
In decibels:
N = k + Ts + Bn
(dBW)
Where:
• k = −228.6 dBW/K/Hz
• Ts in dBK
• Bn in dBHz
All conversions in power domain use 10 log10(·).
Path loss uses 20 log10(·) due to
squared electric field.
3

## Page 4

Example 4.6 — Clear-Air C-Band Downlink
Given Parameters
Satellite:
• Transponder saturated power = 80 W = 19 dBW
• Output backoff = 2 dB →operating power = 17 dBW
• Antenna gain = 20 dB
• Edge-of-beam loss = 3 dB
Earth Station:
• Antenna gain = 49.7 dB
• LNA noise temperature = 45 K
• Clear-sky sky noise = 13 K
• Total system noise = 58 K
• Noise bandwidth = 30 MHz
Power Budget
Table 1: C-Band Downlink Budget (Clear Air)
Quantity
Value (dB)
Transponder output power
19.0
Output backoff
-2.0
Satellite antenna gain
+20.0
Earth station antenna gain
+49.7
Free-space path loss
-196.5
Edge-of-beam loss
-3.0
Atmospheric loss
-0.2
Miscellaneous loss
-0.5
Received power Pr
-113.5 dBW
Noise Budget
Ts = 58 K ⇒17.6 dBK
Bn = 30 MHz ⇒74.8 dBHz
4

## Page 5

N = −228.6 + 17.6 + 74.8 = −136.2 dBW
CNRclear = −113.5 −(−136.2) = 22.7 dB
This far exceeds the required 14 dB, ensuring error-free performance.
Example 4.7 — Downlink CNR in Heavy Rain
Rain attenuation = 1 dB Clear-air attenuation = 0.2 dB Total = 1.2 dB →linear factor
= 1.32
Tsky,rain = 273

1 −
1
1.32

= 66 K
T rain
s
= 45 + 66 = 111 K
Increase in noise:
∆N = 10 log10
111
58

= 2.8 dB
Rain-Affected CNR
P rain
r
= −114.5 dBW
N rain = −132.7 dBW
CNRrain = 18.2 dB
Margin above minimum:
18.2 −14 = 4.2 dB
Antenna Diameter Reduction
A link has an excess margin of 4 dB in rain. If antenna gain is proportional to D2,
determine the diameter reduction factor.
5

## Page 6
