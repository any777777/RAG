---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0258"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 258
confidence: "first-pass"
extraction_method: "structured-local"
---

12.4
The Link-Power Budget Equation
As mentioned at the beginning of Sec. 12.3, the [EIRP] can be consid-
ered as the input power to a transmission link. Now that the losses for
the link have been identified, the power at the receiver, which is the
power output of the link, may be calculated simply as [EIRP]  [LOSS-
ES]  [GR], where the last quantity is the receiver antenna gain. Note
carefully that decibel addition must be used.
The major source of loss in any ground-satellite link is the free-space
spreading loss [FSL], as shown in Sec. 12.3.1, where Eq. (12.13) is the
basic link-power budget equation taking into account this loss only.
However, the other losses also must be taken into account, and these
are simply added to [FSL]. The losses for clear-sky conditions are
[LOSSES]  [FSL]  [RFL]  [AML]  [AA]  [PL]
(12.12)
The decibel equation for the received power is then
[PR]  [EIRP]  [GR]  [LOSSES]
(12.13)
where
[PR]
 received power, dBW
[EIRP]
 equivalent isotropic radiated power, dBW
[FSL]
 free-space spreading loss, dB
[RFL]
 receiver feeder loss, dB
[AML]
 antenna misalignment loss, dB
[AA]
 atmospheric absorption loss, dB
[PL]
 polarization mismatch loss, dB
Example 12.4
A satellite link operating at 14 GHz has receiver feeder loss-
es of 1.5 dB and a free-space loss of 207 dB. The atmospheric absorption loss
is 0.5 dB, and the antenna pointing loss is 0.5 dB. Depolarization losses may
be neglected. Calculate the total link loss for clear-sky conditions.
solution
The total link loss is the sum of all the losses:
[LOSSES]  [FSL]  [RFL]  [AA]  [AML]  207  1.5  0.5  0.5 
 209.5 dB
12.5
System Noise
It is shown in Sec. 12.3 that the receiver power in a satellite link is
very small, on the order of picowatts. This by itself would be no prob-
lem because amplification could be used to bring the signal strength
up to an acceptable level. However, electrical noise is always present
The Space Link
311
TLFeBOOK

## Page 326
