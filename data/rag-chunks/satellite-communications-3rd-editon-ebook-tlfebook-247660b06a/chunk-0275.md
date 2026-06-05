---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0275"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 275
confidence: "first-pass"
extraction_method: "structured-local"
---

solution
As with the uplink budget calculations, the work is best set out in
tabular form with the minus signs in Eq. (12.55) attached to the tabulated
values.
Quantity
Decilogs
Satellite saturation [EIRP]
25.0
Free-space loss
196.0
Other losses
1.5
Output backoff
6.0
Earth station [G/T]
41.0
[k]
228.6
Total
91.1
The total gives the carrier-to-noise density ratio at the earth station in
dBHz, as calculated from Eq. (12.55).
For the uplink, the saturation flux density at the satellite receiver is
a specified quantity. For the downlink, there is no need to know the
saturation flux density at the earth station receiver, since this is a ter-
minal point, and the signal is not used to saturate a power amplifier.
12.8.2
Satellite TWTA output
The satellite power amplifier, which usually is a traveling-wave tube
amplifier, has to supply the radiated power plus the transmit feeder
losses. These losses include the waveguide, filter, and coupler losses
between the TWTA output and the satellite’s transmit antenna.
Referring back to Eq. (12.3), the power output of the TWTA is given by
[PTWTA]  [EIRP]D [GT] D  [TFL] D
(12.56)
Once [PTWTA] is found, the saturated power output rating of the TWTA
is given by
[PTWTA]S  [PTWTA]  [BO]o
(12.57)
Example 12.15
A satellite is operated at an EIRP of 56 dBW with an out-
put backoff of 6 dB. The transmitter feeder losses amount to 2 dB, and the
antenna gain is 50 dB. Calculate the power output of the TWTA required for
full saturated EIRP.
solution
Equation (12.56):
[PTWTA]  [EIRP]D  [GT]D  [TFL]D
 56  50  2
 8 dBW
The Space Link
329
TLFeBOOK

## Page 344
