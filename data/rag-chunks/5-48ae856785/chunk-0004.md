---
chunk_id: "5-48ae856785-chunk-0004"
source_id: "5-48ae856785"
source_file: "New folder (3)/5.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

Satellite Communications
Chapter 5
Worked Example
Problem 6: CPFSK/Low-Rate Data Over FM Channel (Carson Check)
A digital link sends Rb = 9.6 kbps. With tight filtering, baseband bandwidth is
fmax = 0.5Rb = 4.8 kHz. Choose ∆fpk = 3.6 kHz.
a) Estimate BRF using Carson’s rule.
b) If receiver (C/N) = 10 dB, estimate (S/N)out (ignore de-emphasis).
Solution:
(a) Carson:
BRF ≈2(∆fpk + fmax) = 2(3.6 + 4.8) = 16.8 kHz.
(b) Unweighted S/N:
(S/N)out = (C/N) + 10 log10
BRF
fmax

+ 20 log10
∆fpk
fmax

+ 1.8
Compute:
10 log10
16.8
4.8

= 10 log10(3.5) ≈5.44 dB
20 log10
3.6
4.8

= 20 log10(0.75) ≈−2.50 dB
Hence:
(S/N)out ≈10 + 5.44 −2.50 + 1.8 = 14.74 dB
Answers:
(a) BRF ≈16.8 kHz.
(b) (S/N)out ≈14.7 dB.
8

## Page 9

Satellite Communications
Chapter 5
10
Digital Modulation and Demodulation
Introduction
This section introduces the principles of digital modulation and demodulation used in
satellite communication systems. Unlike analog systems, the quality of a digital satellite
link is measured by its bit error rate (BER) rather than signal-to-noise ratio.
In satellite systems, phase modulation is almost universally used. For historical
reasons, digital phase modulation is called Phase Shift Keying (PSK).
We focus on:
• BPSK and QPSK modulation
• Symbol and bit error rates
• Relationship between C/N, Eb/N0, and BER
• Practical satellite link performance
11
Basic Terminology
Definition
Phase Shift Keying (PSK) is a digital modulation technique in which the phase
of a carrier is switched among a finite number of values.
Common PSK types:
• BPSK: Binary PSK (2 phase states)
• QPSK: Quadrature PSK (4 phase states)
If a modulation scheme uses m phase states, the number of bits per symbol is
Nb = log2 m
Important Concept
BPSK carries 1 bit per symbol, while QPSK carries 2 bits per symbol.
12
Symbols, Bit Rate, and Symbol Rate
Definition
A symbol is the waveform transmitted during one symbol period Ts.
9

## Page 10
