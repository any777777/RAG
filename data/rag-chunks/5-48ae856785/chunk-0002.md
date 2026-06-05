---
chunk_id: "5-48ae856785-chunk-0002"
source_id: "5-48ae856785"
source_file: "New folder (3)/5.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

Satellite Communications
Chapter 5
2.2
Instantaneous Frequency
fi(t) = fc + ∆f = fc + kfm(t)
Important Concept
In FM, amplitude is (approximately) constant; information is carried by frequency
deviation.
2.3
FM Waveform Equation
VFM(t) = A cos

2πfct + 2πkf
Z t
0
m(τ) dτ + ϕ0

FM is nonlinear, producing many sidebands and a complex spectrum.
3
Bandwidth of FM Signals
3.1
Carson’s Rule
BRF ≈2(∆fpk + fmax)
Important Concept
Carson’s rule is the practical method engineers use to estimate FM bandwidth.
4
FM S/N Improvement (Unweighted)
A widely used practical expression for baseband S/N is:
(S/N)out = (C/N) + 10 log10
BRF
fmax

+ 20 log10
∆fpk
fmax

+ 1.8
Deviation ratio:
D = ∆fpk
fmax
Important Concept
Larger deviation ratio increases S/N improvement but consumes more RF band-
width.
3

## Page 4

Satellite Communications
Chapter 5
5
Pre-emphasis and De-emphasis
FM demodulator noise increases with baseband frequency. De-emphasis (receiver) reduces
high-frequency noise, while pre-emphasis (transmitter) boosts high-frequency signal com-
ponents so the overall signal is not distorted.
Typical improvement values:
• Video: P ≈9 dB
• Voice: P ≈5–10 dB
With de-emphasis, the unweighted S/N becomes:
(S/N)U = (C/N) + 10 log10
BRF
fmax

+ 20 log10
∆fpk
fmax

+ 1.8 + P
6
Analog FM Transmission by Satellite
6.1
FM Television
A typical NTSC signal:
• Baseband bandwidth: fmax = 4.2 MHz
• RF bandwidth: BRF ≈30 MHz
7
Subjective Video S/N (Weighted)
Video quality also depends on human perception. A subjective improvement factor Q is
often added (typical Q ≈8 dB):
(S/N)W = (C/N) + 10 log10
BRF
fmax

+ 20 log10
∆fpk
fmax

+ 1.8 + P + Q
8
FM Threshold Effect
Important Concept
FM demodulators exhibit a threshold: below a certain input C/N, output noise
increases rapidly (“clicks” in audio, “sparklies” in TV).
4

## Page 5
