---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0201"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 201
confidence: "first-pass"
extraction_method: "structured-local"
---

The required IF bandwidth can now be found using Carson’s rule,
Eq. (9.1), and the processing gain from Eq. (9.16). The following exam-
ple illustrates the procedure.
Example 9.5
The carrier-to-noise ratio at the input to the demodulator of
an FDM/FM receiver is 25 dB. Calculate the signal-to-noise ratio for the top
channel in a 24-channel FDM baseband signal, evaluated under test condi-
tions for which Table 9.1 applies. The emphasis improvement is 4 dB, noise
weighting improvement is 2.5 dB, and the peak/rms factor is 13.57 dB. The
audio channel bandwidth may be taken as 3.1 kHz.
solution
Given data:
n:  24
gdB:  13.57
b:  3.1  103  Hz
PdB:  4
WdB:  2.5
CNRdB:  25
L:  10
L  1.683
…Eq. (9.19)
g:  10
g  4.77
…Eq. (9.17)
From Table 9.1, for 24 channels
"Frms:  35  103  Hz
Using Eq. (9.20),
"F:  g  "Frms  L
"F  2.809  105  Hz
Assuming that the baseband spectrum is as shown in Fig. 9.4a, the top fre-
quency is 108 kHz:
fm:  108  103  Hz
Carson’s rule gives
BIF:  2  ("F  fm)
From Eq. (9.16),
GP: 
 

2
GP  26.353
From Eq. (9.15),
SNRdB:  CNRdB  10  log (GP)  PdB  WdB
SNRdB  45.7
     
"Frms

fm
BIF

b
gdB

20
1  4  log (n)

20
Analog Signals
245
TLFeBOOK

## Page 260
