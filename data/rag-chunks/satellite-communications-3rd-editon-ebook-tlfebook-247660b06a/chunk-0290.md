---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0290"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 290
confidence: "first-pass"
extraction_method: "structured-local"
---

[I]  [EIRP] 2  3  [GB () ]  [FSL]  [Y] D
(13.2)
It is assumed that the free-space loss is the same for both paths.
These two equations may be combined to give
[C]  [I]  [EIRP]1  [EIRP]2  [GB]  [GB () ]  [Y] D
or
 	
D
 " [E]  [GB]  [GB () ]  [Y]D
(13.3)
The subscript D is used to denote downlink, and "[E] is the difference
in dB between the [EIRP]s of the two satellites.
Example 13.1
The desired carrier [EIRP] from a satellite is 34 dBW, and
the ground station receiving antenna gain is 44 dB in the desired direc-
tion and 24.47 dB toward the interfering satellite. The interfering satel-
lite also radiates an [EIRP] of 34 dBW. The polarization discrimination is
4 dB. Determine the carrier-to-interference ratio at the ground receiving
antenna.
solution
From Eq. (13.3),
 	
D
 (34  34)  44  24.47  4
 23.53 dB
13.2.2
Uplink
A result similar to Eq. (13.3) can be derived for the uplink. In this sit-
uation, however, it is desirable to work with the radiated powers and
the antenna transmit gains rather than the EIRPs of the two earth
stations. Equation (12.3) may be used to substitute power and gain for
EIRP. Also, for the uplink, GB and GB() are replaced by the satellite
receive antenna gains, both of which are assumed to be given by the
3-dB contour. Denoting by "[P] the difference in dB between wanted
and interfering transmit powers, [GA] the boresight transmit antenna
gain at A, and [GC()] the off-axis transmit gain at C, it is left as an
exercise for the reader to show that Eq. (13.3) is modified to
 	
U
 " [P]  [GA]  [GC () ]  [Y]U
(13.4)
Example 13.2
Station A transmits at 24 dBW with an antenna gain of 54
dB, and station C transmits at 30 dBW. The off-axis gain in the S1 direction
C
I
C
I
C
I
350
Chapter Thirteen
TLFeBOOK

## Page 361
