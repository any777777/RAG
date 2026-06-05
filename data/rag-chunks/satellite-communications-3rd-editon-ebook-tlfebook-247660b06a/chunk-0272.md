---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0272"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 272
confidence: "first-pass"
extraction_method: "structured-local"
---

[PHPA,sat]  [PHPA]  [BO]HPA
(12.52)
Of course, the HPA will be operated at the backed-off power level so
that it provides the required power output [PHPA]. To ensure operation
well into the linear region, an HPA with a comparatively high satura-
tion level can be used and a high degree of backoff introduced. The
large physical size and high power consumption associated with larg-
er tubes do not carry the same penalties they would if used aboard the
satellite. Again, it is emphasized that backoff at the earth station may
be required quite independently of any backoff requirements at the
satellite transponder. The power rating of the earth station HPA also
should be sufficient to provide a fade margin, as discussed in Sec.
12.9.1.
12.8
Downlink
The downlink of a satellite circuit is the one in which the satellite is
transmitting the signal and the earth station is receiving it. Equation
(12.38) can be applied to the downlink, but subscript D will be used to
denote specifically that the downlink is being considered. Thus Eq.
(12.38) becomes

	D
 [EIRP]D   	D
 [LOSSES]D  [k]
(12.53)
In Eq. (12.53) the values to be used are the satellite EIRP, the earth
station receiver feeder losses, and the earth station receiver G/T. The
free-space and other losses are calculated for the downlink frequency.
The resulting carrier-to-noise density ratio given by Eq. (12.53) is that
which appears at the detector of the earth station receiver.
Where the carrier-to-noise ratio is the specified quantity rather than
carrier-to-noise density ratio, Eq. (12.38) is used. This becomes, on
assuming that the signal bandwidth B is equal to the noise bandwidth
BN:
 	D
 [EIRP]D   	 D
 [LOSSES]D  [k]  [B]
(12.54)
Example 12.12
A satellite TV signal occupies the full transponder band-
width of 36 MHz, and it must provide a C/N ratio at the destination earth
station of 22 dB. Given that the total transmission losses are 200 dB and the
destination earth station G/T ratio is 31 dB/K, calculate the satellite EIRP
required.
solution
Equation (12.54) can be rearranged as
G

T
C

N
G

T
C

No
326
Chapter Twelve
TLFeBOOK

## Page 341
