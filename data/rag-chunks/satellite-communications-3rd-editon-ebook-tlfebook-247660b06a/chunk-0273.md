---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0273"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 273
confidence: "first-pass"
extraction_method: "structured-local"
---

[EIRP]D   	
D
  	
D
 [LOSSES]D  [k]  [B]
Setting this up in tabular form, and keeping in mind that [k]  228.6 dB
and that losses are numerically equal to 200 dB, we obtain
Quantity
Decilogs
[C/N]
22
[G/T]
31
[LOSSES]
200
[k]
228.6
[B]
75.6
[EIRP]
38
The required EIRP is 38 dBW or, equivalently, 6.3 kW.
Example 12.12 illustrates the use of Eq. (12.54). Example 12.13
shows the use of Eq. (12.53) applied to a digital link.
Example 12.13
A QPSK signal is transmitted by satellite. Raised-cosine
filtering is used, for which the rolloff factor is 0.2 and a BER of 105 is
required. For the satellite downlink, the losses amount to 200 dB, the
receiving earth station G/T ratio is 32 dBK1, and the transponder band-
width is 36 MHz. Calculate (a) the bit rate which can be accommodated, and
(b) the EIRP required.
solution
Given data:
B:  36  MHz
:  0.2
GTRdB:  31
LOSSESdB:  200
kdB:  228.6
Given that   0.2, Eq. (10.16) gives
Rb: 
Rb  6  107  s1

for BER  105, Fig. 10.17 gives an Eb/No ratio of
EbNoRdB:  9.6
Converting Rb to decilogs:
RbdB:  10  log 

From Eq. (10.24) the required C/No ratio is
CNoRdB:  EbNoRdB  RbdB
Rb

sec1
2  B

1  
G

T
C

N
The Space Link
327
TLFeBOOK

## Page 342
