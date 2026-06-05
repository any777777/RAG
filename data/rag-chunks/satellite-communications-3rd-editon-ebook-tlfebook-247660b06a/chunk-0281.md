---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0281"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 281
confidence: "first-pass"
extraction_method: "structured-local"
---

shown in Fig. 12.9a. It includes the satellite transponder and transmit
antenna gains, the downlink losses, and the earth station receive
antenna gain and feeder losses.
The noise at the satellite input also appears at the earth station
input multiplied by #, and in addition, the earth station introduces
its own noise, denoted by PND. Thus the end-of-link noise is #PNU 
PND.
The C/No ratio for the downlink alone, not counting the #PNU contri-
bution, is PR/PND, and the combined C/No ratio at the ground receiver is
PR/(#PNU  PND). The power flow diagram is shown in Fig. 12.9b. The
combined carrier-to-noise ratio can be determined in terms of the indi-
vidual link values. To show this, it is more convenient to work with the
noise-to-carrier ratios rather than the carrier-to-noise ratios, and
again, these must be expressed as power ratios, not decibels. Denoting
the combined noise-to-carrier ratio value by No/C, the uplink value by
(No/C)U, and the downlink value by (No/C)D then,






 
U
 
D
(12.61)
Equation (12.61) shows that to obtain the combined value of C/No, the
reciprocals of the individual values must be added to obtain the No/C
ratio and then the reciprocal of this taken to get C/No. Looked at in
another way, the reason for this reciprocal of the sum of the reciprocals
method is that a single signal power is being transferred through the
system, while the various noise powers which are present are additive.
Similar reasoning applies to the carrier-to-noise ratio, C/N.
Example 12.18
For a satellite circuit the individual link carrier-to-noise
spectral density ratios are: uplink 100 dBHz; downlink 87 dBHz. Calculate
the combined C/No ratio.
solution
No

C
No

C
PND

PR
#PNU

PND

PR
#PNU

PR
#PNU  PND

PN

PR
No

C
336
Chapter Twelve
TLFeBOOK

## Page 351
