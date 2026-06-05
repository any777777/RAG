---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0271"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 271
confidence: "first-pass"
extraction_method: "structured-local"
---

Equations (12.48) and (12.49) may now be substituted in Eq. (12.39)
to give

	 U
 [S]  [A0]  [BO] i   	U
 [k]  [RFL] (12.50)
Example 12.11
An uplink at 14 GHz requires a saturation flux density of
91.4 dBW/m2 and an input backoff of 11 dB. The satellite G/T is 6.7 dBK1,
and receiver feeder losses amount to 0.6 dB. Calculate the carrier-to-noise
density ratio.
solution
As in Example 12.9, the calculations are the best carried out in tab-
ular form. [A0]  44.37 dBm2 for a frequency of 14 GHz is calculated by
using Eq. (12.44) as in Example 12.10.
Quantity
Decilogs
Saturation flux density
91.4
[A0] at 14 GHz
44.4
Input backoff
11.0
Satellite saturation [G/T]
6.7
[k]
228.6
Receiver feeder loss
0.6
Total
74.5
Note that [k]  228.6 dB, so 2[k] in Eq. (12.50) becomes 228.6 dB. Also,
[RFL] and [BO]i are entered as negative numbers to take account of the
minus signs attached to them in Eq. (12.50). The total gives the carrier-to-
noise density ratio at the satellite receiver as 74.5 dBHz.
Since fade margins have not been included at this stage, Eq. (12.50)
applies for clear-sky conditions. Usually, the most serious fading is
caused by rainfall, as described in Sec. 12.9.
12.7.3
The earth station HPA
The earth station high-power amplifier has to supply the radiated
power plus the transmit feeder losses, denoted here by TFL, or [TFL]
dB. These include waveguide, filter, and coupler losses between the
HPA output and the transmit antenna. Referring back to Eq. (12.3),
the power output of the HPA is given by
[PHPA]  [EIRP]  [GT]  [TFL]
(12.51)
The [EIRP] is that given by Eq. (12.49) and thus includes any input
backoff that is required at the satellite.
The earth station itself may have to transmit multiple carriers, and
its output also will require back off, denoted by [BO]HPA. The earth sta-
tion HPA must be rated for a saturation power output given by
G

T
C

No
The Space Link
325
TLFeBOOK

## Page 340
