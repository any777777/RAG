---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0316"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 316
confidence: "first-pass"
extraction_method: "structured-local"
---

14.6
Bandwidth-Limited and Power-Limited
TWT Amplifier Operation
A transponder will have a total bandwidth BTR, and it is apparent that
this can impose a limitation on the number of carriers which can
access the transponder in an FDMA mode. For example, if there are K
carriers each of bandwidth B, then the best that can be achieved is 
K  BTR/B. Any increase in the transponder EIRP will not improve on
this, and the system is said to be bandwidth-limited. Likewise, for dig-
ital systems, the bit rate is determined by the bandwidth, which again
will be limited to some maximum value by BTR.
Power limitation occurs where the EIRP is insufficient to meet the
[C/N] requirements, as shown by Eq. (12.34). The signal bandwidth
will be approximately equal to the noise bandwidth, and if the EIRP is
below a certain level, the bandwidth will have to be correspondingly
reduced to maintain the [C/N] at the required value. These limitations
are discussed in more detail in the next two sections.
14.6.1
FDMA downlink analysis
To see the effects of intermodulation noise which results with FDMA
operation, consider the overall carrier-to-noise ratio as given by Eq.
(12.62). In terms of noise power rather than noise power density, 
Eq. (12.62) states
    
U
  
D
  
IM
(14.1)
A certain value of carrier-to-noise ratio will be needed, as specified
in the system design, and this will be denoted by the subscript REQ.
The overall C/N must be at least as great as the required value, a con-
dition which can therefore be stated as
 
REQ
  
(14.2)
Note that because the noise-to-carrier ratio rather than the carrier-
to-noise ratio is involved, the actual value is equal to or less than the
required value. Using Eq. (14.1), the condition can be rewritten as
 
REQ
  
U
  
D
  
IM
(14.3)
The right-hand side of Eq. (14.3) is usually dominated by the down-
link ratio. With FDMA, backoff is utilized to reduce the intermodula-
tion noise to an acceptable level, and as shown in Sec. 12.10, the
N

C
N

C
N

C
N

C
N

C
N

C
N

C
N

C
N

C
N

C
Satellite Access
379
TLFeBOOK

## Page 390
