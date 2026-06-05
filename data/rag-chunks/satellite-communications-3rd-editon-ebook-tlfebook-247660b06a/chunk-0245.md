---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0245"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 245
confidence: "first-pass"
extraction_method: "structured-local"
---

 rc
(11.3)
where Eb is the average bit energy in the uncoded bit stream (as intro-
duced in Chap. 10), and Ec is the bit energy in the coded bit stream.
Equation (10.18) gives the probability of bit error for BPSK and
QPSK modulation. With no coding applied, Eb is just the Eb of Eq.
(10.18), and the probability of bit error in the uncoded bit stream is
PeU 
erfc
(11.4)
For the coded bit stream, the bit energy is Ec  rcEb, and therefore, Eq.
(10.18) becomes
PeC 
erfc
(11.5)
This means that PeC  PeU, or the probability of bit error with coding is
worse than that without coding. It is important to note, however, that
the probability of bit error applies at the input to the decoder. For the
error control coding to be effective, the output bit error rate (BER)
should be better than that obtained without coding. More will be said
about this later.
The limitation imposed by bandwidth also must be considered. If the
time for transmission is to be the same for the coded message as for the
uncoded message, the bandwidth has to be increased to accommodate
the higher bit rate. The required bandwidth is directly proportional to
bit rate (see, for example, Eq. 10.16), and hence it has to be increased
by a factor 1/rc. If, however, the bandwidth is fixed (the system is band
limited), then the only recourse is to increase the transmission time by
the factor 1/rc. For a fixed number of bits in the original message, the
bit rate Rb entering into the encoder is reduced by a factor rc compared
with what it could have been without coding.
As an example, it is shown in Sec. 10.4 that the TI message rate is
1.544 Mb/s. When 7/8 FEC is applied, the transmission rate becomes
1.544  8/7  1.765 Mb/s. From Eq. (10.16), the required bandwidth is
BIF  1.765  (1.2)/2  1.06 MHz.
11.8
Coding Gain
As shown by Eqs. (11.4) and (11.5), the probability of bit error for a
coded message is higher (therefore, worse) than that for an uncoded
message, and therefore, to be of advantage, the coding itself must more
than offset this reduction in performance. In order to illustrate this, the
messages will be assumed to be BPSK (or QPSK) so that the expres-
rc Eb

No
1
2
Eb

No
1
2
Ec

Eb
296
Chapter Eleven
TLFeBOOK

## Page 311
