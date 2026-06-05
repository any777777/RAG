---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0352"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 352
confidence: "first-pass"
extraction_method: "structured-local"
---

quency. For clarity, it is assumed that the carrier is the uplink fre-
quency, and hence the uplink carrier is described by
eU(t)  c(t)p(t) cos 
Ut
(14.33)
The corresponding downlink carrier is
eD(t)  c(t)p(t) cos 
Dt
(14.34)
At the receiver, an identical c(t) generator is synchronized to the c(t)
of the downlink carrier. This synchronization is carried out in the
acquisition and tracking block. With c(t) a polar NRZ type waveform,
and with the locally generated c(t) exactly in synchronism with the
transmitted c(t), the product c2(t)  1. Thus the output from the mul-
tiplier is
c(t) eD(t)  c 2(t)p(t) cos 
Dt
 p(t) cos 
Dt
(14.35)
This is identical to the conventional BPSK signal given by Eq.(10.14),
and hence detection proceeds in the normal manner.
14.10.2
The code signal c(t)
The code signal c(t) carries a binary code that has special properties
needed for successful implementation of CDMA. The binary symbols
used in the codes are referred to as chips rather than bits to avoid con-
fusion with the information bits that also will be present. Chip gener-
ation is controlled by a clock, and the chip rate, in chips per second, is
given by the clock speed. Denoting the clock speed by Rch, the chip peri-
od is the reciprocal of the clock speed:
Tch 
(14.36)
The waveform c(t) is periodic, in that each period is a repetition of a
given sequence of N chips. The sequence itself exhibits random prop-
erties, which will be described shortly. The periodic time for the wave-
form is
TN  NTch
(14.37)
The codes are generated using binary shift registers and associated
linear logic circuits. The circuit for a three-stage shift register that
generates a sequence of N  7 chips is shown in Fig.14.34a. Feedback
occurs from stages 1 and 3 as inputs to the exclusive OR gate. This pro-
1

Rch
Satellite Access
421
TLFeBOOK

## Page 432
