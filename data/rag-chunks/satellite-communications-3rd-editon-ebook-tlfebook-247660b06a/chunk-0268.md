---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0268"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 268
confidence: "first-pass"
extraction_method: "structured-local"
---

Quantity
Decilogs
Free-space loss
206.00
Atmospheric absorption loss
2.00
Antenna pointing loss
1.00
Receiver feeder losses
1.00
Polarization mismatch loss
0.00
Receiver G/T ratio
19.50
EIRP
48.00
[k]
228.60
[C/No], Eq. (12.38)
86.10
The final result, 86.10 dBHz, is the algebraic sum of the quantities as given
in Eq. (12.38).
12.7
The Uplink
The uplink of a satellite circuit is the one in which the earth station is
transmitting the signal and the satellite is receiving it. Equation
(12.38) can be applied to the uplink, but subscript U will be used to
denote specifically that the uplink is being considered. Thus Eq.
(12.38) becomes

	
U
 [EIRP]U   	 U
 [LOSSES] U  [k]
(12.39)
In Eq. (12.39) the values to be used are the earth station EIRP, the
satellite receiver feeder losses, and satellite receiver G/T. The free-
space loss and other losses which are frequency-dependent are cal-
culated for the uplink frequency. The resulting carrier-to-noise
density ratio given by Eq. (12.39) is that which appears at the satel-
lite receiver.
In some situations, the flux density appearing at the satellite receive
antenna is specified rather than the earth station EIRP, and Eq.
(12.39) is modified as explained next.
12.7.1
Saturation flux density
As explained in Sec. 7.7.3, the traveling-wave tube amplifier (TWTA)
in a satellite transponder exhibits power output saturation, as shown
in Fig. 7.21. The flux density required at the receiving antenna to pro-
duce saturation of the TWTA is termed the saturation flux density. The
saturation flux density is a specified quantity in link budget calcula-
tions, and knowing it, one can calculate the required EIRP at the earth
station. To show this, consider again Eq. (12.6) which gives the flux
density in terms of EIRP, repeated here for convenience:
G

T
C

No
322
Chapter Twelve
TLFeBOOK

## Page 337
