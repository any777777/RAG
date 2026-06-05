---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0232"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 232
confidence: "first-pass"
extraction_method: "structured-local"
---

283
Error Control Coding
11.1
Introduction
As shown by Fig. 10.17, the probability of bit error (Pe) in a digital trans-
mission can be reduced by increasing [Eb/No], but there are practical
limits to this approach. Equation (10.24) shows that for a given bit rate
Rb, [Eb/No] is directly proportional to [C/No]. An increase in [C/No] can
be achieved by increasing transmitted power and/or reducing the sys-
tem noise temperature (to reduce No). Both these measures are limited
by cost and, in the case of the onboard satellite equipment, size. In
practical terms, a probability of bit error (Pe of Eq. 10.18) of about 104,
which is satisfactory for voice transmissions, can be achieved with off-
the-shelf equipment. For lower Pe values such as required for some
data, error control coding must be used. Error control performs two
functions, error detection and error correction. Most codes can perform
both functions, but not necessarily together. In general, a code is capa-
ble of detecting more errors than it can correct. Where error detection
only is employed, the receiver can request a repeat transmission (a
technique referred to as automatic repeat request, or ARQ). This is only
of limited use in satellite communications because of the long trans-
mission delay time associated with geostationary satellites. What is
termed forward error correction (FEC) allows errors to be corrected
without the need for retransmission, but this is more difficult and
costly to implement than ARQ.
A Pe value of 104 represents an average error rate of 1 bit in 104, and
the error performance is sometimes specified as the bit error rate (BER).
It should be recognized, however, that the probability of bit error Pe
occurs as a result of noise at the input to the receiver, while the BER is
the actual error rate at the output of the detector. When error control
Chapter11
Copyright 2001 The McGraw-Hill Companies   Click Here for Terms of Use
TLFeBOOK

## Page 298
