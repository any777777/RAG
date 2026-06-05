---
chunk_id: "5-48ae856785-chunk-0003"
source_id: "5-48ae856785"
source_file: "New folder (3)/5.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

Satellite Communications
Chapter 5
9
SCPC-FM Voice Links
Typical voice channel:
• Baseband: fmax ≈3.4 kHz
• RF channel BW: 30–45 kHz
With de-emphasis:
(S/N)voice = (C/N) + 10 log10
BRF
fmax

+ 20 log10
∆fpk
fmax

+ 1.8 + P
Worked Example
Problem 1:
A signal with maximum baseband frequency fmax = 5 kHz frequency modulates a
carrier with peak deviation ∆fpk = 12 kHz. Find the required RF bandwidth.
Solution:
Carson’s rule:
BRF ≈2(∆fpk + fmax) = 2(12 + 5) kHz = 34 kHz.
Answer: BRF ≈34 kHz.
Worked Example
Problem 2:
An FM satellite voice channel occupies BRF = 40 kHz. The baseband extends to
fmax = 3.4 kHz. Estimate ∆fpk.
Solution:
From Carson’s rule:
BRF = 2(∆fpk + fmax) ⇒∆fpk = BRF
2
−fmax = 40
2 −3.4 = 20 −3.4 = 16.6 kHz.
Answer: ∆fpk ≈16.6 kHz.
5

## Page 6

Satellite Communications
Chapter 5
Worked Example
Problem 3:
An FM link has BRF = 30 MHz, fmax = 4.2 MHz, ∆fpk = 10.8 MHz, and receiver
(C/N) = 15 dB. Compute the unweighted baseband (S/N)out.
Solution:
Use:
(S/N)out = (C/N) + 10 log10
BRF
fmax

+ 20 log10
∆fpk
fmax

+ 1.8
Compute each term:
10 log10
 30
4.2

= 10 log10(7.1429) ≈8.54 dB
20 log10
10.8
4.2

= 20 log10(2.5714) ≈8.20 dB
Hence:
(S/N)out ≈15 + 8.54 + 8.20 + 1.8 = 33.54 dB
Answer: (S/N)out ≈33.5 dB.
Worked Example
Problem 4:
Using Problem 3 results, assume de-emphasis improvement P = 9 dB and subjec-
tive weighting Q = 8 dB. Find (S/N)W.
Solution:
Weighted S/N:
(S/N)W = (S/N)out + P + Q
(S/N)W ≈33.54 + 9 + 8 = 50.54 dB
Answer: (S/N)W ≈50.5 dB (very good TV quality).
6

## Page 7

Satellite Communications
Chapter 5
Worked Example
Problem 5:
A SCPC-FM link has BRF = 45 kHz, fmax = 3.4 kHz, receiver (C/N) = 13 dB,
and de-emphasis improvement P = 7 dB. The FM demodulator threshold is 6 dB.
a) Find ∆fpk.
b) Find baseband (S/N)voice.
c) Find link margin.
Solution:
(a) From Carson:
∆fpk = BRF
2
−fmax = 22.5 −3.4 = 19.1 kHz.
(b) Voice S/N:
(S/N)voice = (C/N) + 10 log10
BRF
fmax

+ 20 log10
∆fpk
fmax

+ 1.8 + P
Compute:
10 log10
 45
3.4

= 10 log10(13.235) ≈11.22 dB
20 log10
19.1
3.4

= 20 log10(5.618) ≈14.99 dB
So:
(S/N)voice ≈13 + 11.22 + 14.99 + 1.8 + 7 = 48.01 dB
(c) Link margin:
Margin = (C/N)clear −(C/N)th = 13 −6 = 7 dB.
Answers:
(a) ∆fpk ≈19.1 kHz.
(b) (S/N)voice ≈48.0 dB.
(c) Margin = 7 dB.
7

## Page 8
