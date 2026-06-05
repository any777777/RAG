---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0227"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 227
confidence: "first-pass"
extraction_method: "structured-local"
---

With purely digital systems, the BER will be directly reflected in
errors in the data being transmitted. With analog signals which have
been converted to digital form through PCM, the BER contributes to
the output signal-to-noise ratio, along with the quantization noise, as
described in Sec. 10.3. Curves showing the contributions of thermal
noise and quantization noise to the signal-to-noise output for analog
systems are in Fig. 10.19. The signal-to-noise power ratio is given by
(Taub and Schilling, 1986)

(10.25)
where Q  2n is the number of quantized steps, and n is the number
of bits per sample.
The BER can be improved through the use of error control coding.
This is the topic of Chap. 11.
10.7
Carrier Recovery Circuits
To implement coherent detection, a local oscillator that is exactly syn-
chronized to the carrier must be provided at the receiver. As shown in
Sec. 10.6.1, a BPSK signal is a double sideband suppressed carrier
(DSBSC) type of signal, and therefore, the carrier is not directly avail-
able in the BPSK signal. The carrier can be recovered using a squar-
ing loop, as shown in Fig.10.20. Consider first the situation where the
input is a BPSK signal. The frequency multiplier is a nonlinear circuit,
which squares the signal. Squaring Eq. (10.14) results in
e2 (t)  p2 (t) cos2 
0t
 12  12 cos 2
0t
(10.26)
Q2

1  4Q2Pe
S

N
Digital Signals
277
Frequency
multiplier
xm
BPSK
QPSK
m = 2
m = 4
Phase
detector
Frequency
multiplier
xm
PSK
BPF
VCO
Recovered
carrier
Figure 10.20
Functional block diagram for carrier recovery.
TLFeBOOK

## Page 292
