---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0318"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 318
confidence: "first-pass"
extraction_method: "structured-local"
---

[EIRP]D  [EIRPS]  [BO]O  [K]
(14.10)
The transponder bandwidth BTR will be shared between the carriers,
but not all of BTR can be utilized because of the power limitation. Let 
 represent the fraction of the total bandwidth actually occupied, such
that KB  BTR, or in terms of decilogs
[B]  []  [BTR]  [K]
(14.11)
Substituting these relationships in Eq. (14.6) gives
 	
REQ
 [EIRPS]  [BO]O   	
D
 [LOSSES]  [k]  [BTR]  [] 
(14.12)
It will be noted that the [K] term cancels out. The expression can be
rearranged as
 	REQ  [EIRPS]  	D  [LOSSES]  [k]  [BTR]   [BO]O  []
(14.13)
But as shown by Eq. (14.9), the left-hand side is equal to zero if the
single carrier access is used as reference, and hence
0   [BO]O  []
or
[]   [BO]O
(14.14)
The best that can be achieved is to make []  [BO]O, and since the
backoff is a positive number of decibels, [] must be negative, or equiv-
alently,  is fractional. The following example illustrates the limitation
imposed by backoff.
Example 14.1
A satellite transponder has a bandwidth of 36 MHz and
a saturation EIRP of 27 dBW. The earth station receiver has a G/T ratio
of 30 dB/K, and the total link losses are 196 dB. The transponder is
accessed by FDMA carriers each of 3-MHz bandwidth, and 6-dB output
backoff is employed. Calculate the downlink carrier-to-noise ratio for sin-
gle-carrier operation and the number of carriers which can be accommo-
dated in the FDMA system. Compare this with the number which could
be accommodated if no backoff were needed. The carrier-to-noise ratio
determined for single-carrier operation may be taken as the reference
value, and it may be assumed that the uplink noise and intermodulation
noise are negligible.
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
N
Satellite Access
381
TLFeBOOK

## Page 392
