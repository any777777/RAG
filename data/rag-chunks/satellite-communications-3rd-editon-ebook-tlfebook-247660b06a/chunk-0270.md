---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0270"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 270
confidence: "first-pass"
extraction_method: "structured-local"
---

[EIRP]  [M]  [A0]  [LOSSES]  [RFL]
(12.47)
This is for clear-sky conditions and gives the minimum value of
[EIRP] which the earth station must provide to produce a given flux
density at the satellite. Normally, the saturation flux density will be
specified. With saturation values denoted by the subscript S, Eq.
(12.47) is rewritten as
[EIRPS]U  [S]  [A0]  [LOSSES]U  [RFL]
(12.48)
Example 12.10
An uplink operates at 14 GHz, and the flux density
required to saturate the transponder is 120 dB(W/m2). The free-space loss
is 207 dB, and the other propagation losses amount to 2 dB. Calculate the
earth-station [EIRP] required for saturation, assuming clear-sky conditions.
Assume [RFL] is negligible.
solution
At 14 GHz,
[A0]   (21.45  20 log 14)  44.37 dB
The losses in the propagation path amount to 207  2  209 dB. Hence,
from Eq. (12.48),
[EIRPS]U  120  44.37  209
 44.63 dBW
12.7.2
Input backoff
As described in Sec. 12.7.3, where a number of carriers are present
simultaneously in a TWTA, the operating point must be backed off to
a linear portion of the transfer characteristic to reduce the effects of
intermodulation distortion. Such multiple carrier operation occurs
with frequency-division multiple access (FDMA) and is described in
Chap. 14. The point to be made here is that backoff must be allowed
for in the link budget calculations.
Suppose that the saturation flux density for single-carrier operation
is known. Input backoff will be specified for multiple-carrier operation,
referred to the single-carrier saturation level. The earth station EIRP
will have to be reduced by the specified backoff (BO), resulting in an
uplink value of
[EIRP]U  [EIRPS]U  [BO]i
(12.49)
Although some control of the input to the transponder power ampli-
fier is possible through the ground TT&C station, as described in Sec.
12.7.3, input backoff is normally achieved through reduction of the
[EIRP] of the earth stations actually accessing the transponder.
324
Chapter Twelve
TLFeBOOK

## Page 339
