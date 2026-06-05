---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0319"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 319
confidence: "first-pass"
extraction_method: "structured-local"
---

solution
Note: For convenience in the Mathcad solution, decibel or decilog
values will be indicated by dB. For example, the output backoff in decibels
is shown as BOdBO.
Transponder bandwidth:
BTR:  36  MHz
BdBTR:  10  log 

Carrier bandwidth:
B:  3  MHz
BdB:  10  log 

Saturation eirp:
eirpdBWS:  27
Output backoff:
BOdBO:  6
Total losses:
LOSSESdB :  196
Ground station G/T:
GTRdB :  30
CNRdBD:  eirpdBWS  GTRdB  LOSSESdB  228.6  BdBTR
Eq. (12.54)
CNRdBD  14

dB:  BOdBO
Eq. (14.14)
KdB:  dB  BdBTR  BdB
Eq. (14.11)
K:  10
K  3

If backoff was not required, the number of carriers which could be accom-
modated would be
KdB

10
B

Hz
BTR

Hz
382
Chapter Fourteen
TLFeBOOK

## Page 393

 12
14.7
TDMA
With time-division multiple access, only one carrier uses the transpon-
der at any one time, and therefore, intermodulation products, which
result from the nonlinear amplification of multiple carriers, are
absent. This leads to one of the most significant advantages of TDMA,
which is that the transponder traveling-wave tube (TWT) can be oper-
ated at maximum power output or saturation level.
Because the signal information is transmitted in bursts, TDMA is
only suited to digital signals. Digital data can be assembled into burst
format for transmission and reassembled from the received bursts
through the use of digital buffer memories.
Figure 14.10 illustrates the basic TDMA concept, in which the sta-
tions transmit bursts in sequence. Burst synchronization is required,
and in the system illustrated in Fig. 14.10, one station is assigned sole-
BTR

B
Satellite Access
383
Figure 14.10
Time-division multiple access (TDMA) using a ref-
erence station for burst synchronization.
TLFeBOOK

## Page 394
