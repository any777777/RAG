---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0247"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 247
confidence: "first-pass"
extraction_method: "structured-local"
---

produce a binary 1 as output. In other words, a firm or hard decision is
made on each bit at the threshold detector.
With soft decision decoding (Fig. 11.9b), the received codeword is
compared in total with the known codewords in the set, 111 and 000 in
this example. The comparison is made on the basis of minimum dis-
tance. To illustrate this, consider first two points in an x, y, z coordinate
system. Let point P1 have coordinates x1, y1, z1 and point P2 have coor-
dinates x2, y2, z2. From the geometry of the situation, the distance d
between the points is obtained from
d2  (x1  x2)2  (y1  y2)2  (z1  z2)2
298
Chapter Eleven
A
Uncoded
Coded
2
4
6
8
9
9.6 10
Eb
No
dB
1•10 –7
1•10 –6
1•10 –5
1•10 –4
0.001
0.01
0.1
BER
Figure 11.8
Plot of BER versus [Eb/N0] for coded and uncoded signals.
TLFeBOOK

## Page 313

Treating the codewords as vectors and comparing the received code-
word on this basis with the stored version of 111 results in
(0.5  1)2  (0.7  1)2  (2  1)2  9.34
Comparing it with the stored version of 000 results in
[0.5  (1) ]2  [0.7  (1) ]2  [2  (1) ]2  6.14
The distance determined in this manner is often referred to as the
Euclidean distance in acknowledgment of its geometric origins, and the
distance squared is known as the Euclidean distance metric. On this
basis, the received codeword is closest to the 000 codeword, and the
decoder would produce a binary 0 output.
Soft decision decoding results in about a 2-dB reduction in the
[Eb/No] required for a given BER (Taub and Schilling, 1986). This ref-
erence also gives a table of comparative values for soft and hard deci-
sion coding for various block and convolutional codes. Clearly, soft
Error Control Coding
299
Optimum
demodulator
Soft
decision
decoder
Binary 0
output
Noisy signal
.5V .7V –2V
Optimum
demodulator
Threshold
detector
Hard
decision
decoder
Binary 1
output
Noisy signal
.5V .7V –2V
Clean signal
1V 1V –1V
Threshold
level 0V
(a)
(b)
Figure 11.9
(a) Hard decision and (b) soft decision decoding.
TLFeBOOK

## Page 314
