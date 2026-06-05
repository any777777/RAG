---
chunk_id: "5-48ae856785-chunk-0005"
source_id: "5-48ae856785"
source_file: "New folder (3)/5.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 5
confidence: "first-pass"
extraction_method: "structured-local"
---

Satellite Communications
Chapter 5
Rs = 1
Ts
where:
• Rs: symbol rate (symbols/s)
• Rb = NbRs: bit rate (bits/s)
Important Concept
Increasing m increases data rate, but requires higher C/N to maintain BER.
13
Bit Error Rate (BER)
Definition
The bit error rate (BER) is the probability that a received bit is incorrect.
Key points:
• BER does not depend on transmission speed
• BER depends on noise, interference, and modulation type
• BER plays the same role in digital links as S/N in analog links
Errors occur because noise corrupts symbols so that the receiver makes an incorrect
decision.
14
Energy per Symbol and Noise Density
The energy per symbol is
Es = CTs
The single-sided noise power spectral density is
N0 = N
Bn
For ideal raised-cosine (RRC) filters:
BnTs = 1
Thus:
Es
N0
= C
N
10

## Page 11

Satellite Communications
Chapter 5
Important Concept
Never use C/N in decibels inside BER equations. Always convert to a linear power
ratio first.
15
Binary Phase Shift Keying (BPSK)
15.1
BPSK Signal Model
In BPSK, each bit controls the phase of the carrier:
v(t) = Vc cos

ωct + ui
π
2

ui ∈{+1, −1}
This can be rewritten as:
v(t) = uiVc sin(ωct)
Important Concept
BPSK has constant amplitude and cannot be demodulated by envelope detection.
15.2
Coherent Detection
BPSK is demodulated using a coherent (correlation) detector:
• Multiply by a synchronized carrier
• Low-pass filter
• Sample at symbol center
• Decide based on sign of output
16
Probability of Error for BPSK
For BPSK in AWGN:
Pb = 1
2 erfc
 r
Eb
N0
!
= Q
 r
2 Eb
N0
!
With ideal RRC filtering:
Eb
N0
= C
N
Important Concept
BER formulas require linear C/N, not dB.
11

## Page 12

Satellite Communications
Chapter 5
17
Quadrature Phase Shift Keying (QPSK)
17.1
QPSK Principle
QPSK uses four phase states:
ϕ =
π
4 , 3π
4 , 5π
4 , 7π
4

The transmitted signal can be written as:
v(t) = uiV cos(ωct) + uqV sin(ωct)
Important Concept
QPSK is equivalent to two BPSK systems operating in quadrature.
17.2
Bit Rate Advantage
• Same symbol rate as BPSK
• Double the bit rate
• Requires higher C/N for same BER
17.3
BER of QPSK
In terms of Eb/N0:
P QPSK
b
= P BPSK
b
In terms of C/N:
(C/N)QPSK = 2(C/N)BPSK
Important Concept
QPSK needs 3 dB more C/N than BPSK to achieve the same BER.
18
Implementation Margin
Real systems require an additional margin:
(C/N)eff = (C/N)0 −Implementation margin
Typical values:
12

## Page 13
