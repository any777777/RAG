---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0274"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 274
confidence: "first-pass"
extraction_method: "structured-local"
---

From Eq. (12.53),
eirpdBW:  CNoRdB GTRdB  LOSSESdB  kdB
eirpdBW  27.8

12.8.1
Output back-off
Where input back-off is employed as described in Sec. 12.7.2, a corre-
sponding output back-off must be allowed for in the satellite EIRP. As
the curve of Fig. 7.21 shows, output back-off is not linearly related to
input backoff. A rule of thumb frequently used is to take the output
backoff as the point on the curve which is 5 dB below the extrapolated
linear portion, as shown in Fig. 12.7. Since the linear portion gives a
1:1 change in decibels, the relationship between input and output
backoff is [BO]o  [BO]i  5 dB. For example, with an input back-off
of [BO]i  11 dB, the corresponding output back-off is [BO]o  11  5
 6 dB.
If the satellite EIRP for saturation conditions is specified as
[EIRPS]D, then [EIRP]D  [EIRPS]D  [BO]o and Eq. (12.53) becomes

	
D
 [EIRPS]D  [BO] o   	
D
 [LOSSES] D  [k]         (12.55)
Example 12.14
The specified parameters for a downlink are satellite sat-
uration value of EIRP, 25 dBW; output backoff, 6 dB; free-space loss, 196 dB;
allowance for other downlink losses, 1.5 dB; and earth station G/T, 41
dBK1. Calculate the carrier-to-noise density ratio at the earth station.
G

T
C

No
328
Chapter Twelve
Figure 12.7
Input and output back-off relationship for the satel-
lite traveling-wave-tube amplifier; [BO]i  [BO]0  5 dB.
TLFeBOOK

## Page 343
