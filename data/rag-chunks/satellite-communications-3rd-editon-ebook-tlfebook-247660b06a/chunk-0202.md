---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0202"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 202
confidence: "first-pass"
extraction_method: "structured-local"
---

9.6.8
Signal-to-noise ratio for TV/FM
Television performance is measured in terms of the postdetector video
signal-to-noise ratio, defined as (CCIR Recommendation 567-2, 1986)
 V

(9.21)
Because peak-to-peak video voltage is used, 2"F replaces "F in Eq.
(9.8). Also, since power is proportional to voltage squared, (S/N)V 2
replaces S/N, and Eq. (9.8) becomes
  V
2
 1.5 
(9.22)
where W is the highest video frequency. With the deviation ratio D 
"F/W, and the processing gain for TV denoted as GPV,
GPV 
 12D2 (D  1)
(9.23)
Some workers include an implementation margin to allow for non-
ideal performance of filters and demodulators (Bischof et al., 1981).
With the implementation margin denoted by [IMP], Eq. (9.15) becomes
  V
2	   	  [GP V]  [P]  [W]  [IMP]
(9.24)
Recall that this equation is in decibels. This is illustrated in the fol-
lowing example.
Example 9.6
A satellite TV link is designed to provide a video signal-to-
noise ratio of 62 dB. The peak deviation is 9 MHz, and the highest video
baseband frequency is 4.2 MHz. Calculate the carrier-to-noise ratio required
at the input to the FM detector, given that the combined noise weighting,
emphasis improvement, and implementation margin is 11.8 dB.
solution
D 
 2.143
Equation (9.23) gives
GPV  12  2.1432  (2.142  1)  173.2
Therefore,
[GPV]  10 log GPV  22.4 dB
9

4.2
C

N
S

N
(S/N)V
2

C/N
BN (2"F)2

C

N
S

N
peak-to-peak video voltage

rms noise voltage
S

N
246
Chapter Nine
TLFeBOOK

## Page 261
