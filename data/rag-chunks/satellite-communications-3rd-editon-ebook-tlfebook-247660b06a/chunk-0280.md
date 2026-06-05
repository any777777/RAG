---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0280"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 280
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 348

(b) The rain attenuation can reduce the [C/N] to the threshold level of 10
dB (i.e., it reduces the margin to zero), which is a (C/N) power ratio of 10:1
or a downlink N/C power ratio of 1/10.
For clear-sky conditions, [C/N]CS  17.4 dB, which gives an N/C ratio of
0.0182. Substituting these values in Eq. (12.60) gives
0.1  0.0182 A 

Solving this equation for A gives A  4, or approximately 6 dB. From the
curve of Fig. 12.8, the probability of exceeding the 6-dB value is 2.5  104,
and therefore, the availability is 1  2.5  104  0.99975, or 99.975 per-
cent.
For digital signals, the required [C/N0] ratio is determined by the
acceptable bit error rate (BER), which must not be exceeded for more
than a specified percentage of the time. Figure 10.17 relates the BER
to the [Eb/No] ratio, and this in turn is related to the [C/No] by Eq.
(10.24), as discussed in Sec. 10.6.4.
(A  1)  272

544
334
Chapter Twelve
Figure 12.8
Typical rain attenuation curve used in Ex.
(12.17).
TLFeBOOK

## Page 349

For the downlink, the user does not have control of the satellite
[EIRP], and thus the downlink equivalent of uplink power control,
described in Sec. 12.9.1, cannot be used. In order to provide the rain-
fade margin needed, the gain of the receiving antenna may be
increased by using a larger dish and/or a receiver front end having a
lower noise temperature. Both measures increase the receiver [G/T]
ratio and thus increase [C/No] as shown by Eq. (12.53).
12.10
Combined Uplink and Downlink C/N
Ratio
The complete satellite circuit consists of an uplink and a downlink, as
sketched in Fig. 12.9a. Noise will be introduced on the uplink at the
satellite receiver input. Denoting the noise power per unit bandwidth
by PNU and the average carrier at the same point by PRU, the carrier-
to-noise ratio on the uplink is (C/No)U  (PRU/PNU). It is important to
note that power levels, and not decibels, are being used here.
The carrier power at the end of the space link is shown as PR, which
of course is also the received carrier power for the downlink. This is
equal to # times the carrier power input at the satellite, where # is the
system power gain from satellite input to earth station input, as
The Space Link
335
Figure 12.9
(a) Combined uplink and downlink; (b) power flow diagram for (a).
TLFeBOOK

## Page 350
