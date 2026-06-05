---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0334"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 334
confidence: "first-pass"
extraction_method: "structured-local"
---

Example 14.4
Calculate the frame efficiency for an INTELSAT frame giv-
en the following information:
Total frame length  120,832 symbols
Traffic bursts per frame  14
Reference bursts per frame  2
Guard interval  103 symbols
solution
From Fig. 14.14, the preamble symbols add up to
P  176  24  8  8  32  32
 280
With addition of the CDC channel, the reference channel symbols add 
up to
R  280  8
 288
Therefore, the overhead symbols are
OH  2  (103  288)  14  (103  280)
 6144 symbols
Therefore, from Eq. (14.27),
F  1 
 0.949
The voice-channel capacity of a frame, which is also the voice-chan-
nel capacity of the transponder being accessed by the frame, can be
found from a knowledge of the frame efficiency and the bit rates. Let
Rb be the bit rate of a voice channel, and let there be a total of n voice
channels shared between all the earth stations accessing the transpon-
der. The total incoming traffic bit rate to a frame is nRb. The traffic bit
rate of the frame is FRT, and therefore
nRb  FRTDMA
or
n 
(14.28)
FRTDMA

Rb
6144

120,832
Satellite Access
399
TLFeBOOK

## Page 410

Example 14.5
Calculate the voice-channel capacity for the INTELSAT
frame in Example 14.2, given that the voice-channel bit rate is 64 kb/s and
that QPSK modulation is used. The frame period is 2 ms.
solution
The number of symbols per frame is 120,832, and the frame period
is 2 ms. Therefore, the symbol rate is 120,832/2 ms  60.416 megasym-
bols/s. QPSK modulation utilizes 2 bits per symbol, and therefore, the trans-
mission rate is RT  60.416  2  120.832 Mb/s.
Using Eq. (14.28) and the efficiency as calculated in Example 14.4,
n  0.949  120.832 
 1792
14.7.8
Preassigned TDMA
An example of a preassigned TDMA network is the common signaling
channel (CSC) for the Spade network described in Sec. 14.5. The frame
and burst formats are shown in Fig. 14.19. The CSC can accommodate
up to 49 earth stations in the network plus one reference station, mak-
ing a maximum of 50 bursts in a frame.
103

64
400
Chapter Fourteen
Figure 14.19
Frame and bit formats for the common signaling channel (CSC) used with
the Spade system. (Data from Miya, 1981.)
TLFeBOOK

## Page 411
