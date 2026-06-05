---
chunk_id: "4-4-27ceec6dc1-chunk-0005"
source_id: "4-4-27ceec6dc1"
source_file: "New folder (3)/4.4.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 5
confidence: "first-pass"
extraction_method: "structured-local"
---

(c) Receiver Noise Power Budget
System noise temperature: Ts = 110 K
k = −228.6 dBW/K/Hz
Ts = 10 log10(110) = 20.4 dBK
Bn = 20 MHz = 73.0 dBHz
N = −228.6 + 20.4 + 73.0 = −135.2 dBW
(d) Clear Air C/N and Link Margin
 C
N

clear
= −118.8 −(−135.2) = 16.4 dB
Minimum permissible C/N = 10.0 dB
Clear air link margin = 16.4 −10.0 = 6.4 dB
(e) Performance Under Rain Conditions
Given:
• Rain attenuation = 2 dB
• Noise temperature increases to 210 K
Increase in Noise Power
∆N = 10 log10
210
110

= 2.8 dB
C/N in Rain
Total degradation = 2.0 + 2.8 = 4.8 dB
 C
N

rain
= 16.4 −4.8 = 11.6 dB
9

## Page 10

Rain margin above threshold:
11.6 −10.0 = 1.6 dB
(f) Receiver on 2-dB Beam Contour
Receivers gain +1 dB compared to 3-dB contour:
 C
N

clear
= 17.4 dB
 C
N

rain
= 12.6 dB
(g) Uplink Path Loss and Antenna Gain at 17.5 GHz
Lp = 20 log10
4π × 38.5 × 106
0.01765

= 209.1 dB
Gt = 10 log10
"
0.65
 π × 6
0.01765
2#
= 58.7 dB
(h) Uplink Power Budget
Satellite receive antenna gain: 31 dB Atmospheric and other losses: 1.0 dB
Pr = Pt + 58.7 + 31.0 −209.1 −1.0 = Pt −120.4 dBW
(i) Required Uplink Transmit Power
N = −228.6 + 27.0 + 73.0 = −128.6 dBW
Pt −120.4 = −128.6 + 28 ⇒Pt = 19.8 dBW
Pt = 95.5 W
10

## Page 11

(j) Transponder Gain
Pin = −100.6 dBW,
Pout = 22.6 dBW
G = 22.6 −(−100.6) = 123.2 dB
Practical implementation:
• RF input amplifier: 30 dB
• IF amplifier: 60 dB
• RF output amplifier: 60 dB
• Controlled attenuator: −6.8 dB
(k) Uplink Link Margin
 C
N

up
= 28.0 dB ⇒Margin = 12.0 dB
(l) Overall C/N Ratio
Given:
(C/N)up = 28 dB,
(C/N)down = 15 dB
1
(C/N)o
=
1
631 +
1
31.6 = 0.03323
(C/N)o = 30.09 = 14.8 dB
11
