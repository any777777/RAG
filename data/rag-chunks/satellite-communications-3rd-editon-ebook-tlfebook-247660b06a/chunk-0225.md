---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0225"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 225
confidence: "first-pass"
extraction_method: "structured-local"
---

solution
Given data:
PR:  102  watt
Tb:  104  s
No:  107  joule
Computations:
Eb:  P R  Tb
BER:  .5  1  erf  
BER  3.9  106
          
Eb

No
Digital Signals
273
Figure 10.17
BER versus (Eb/No) for baseband signaling using a binary
polar NRZ waveform. The curve also applies for BPSK and QPSK mod-
ulated waveforms.
TLFeBOOK

## Page 288

Equation (10.18) is sometimes expressed in the alternative form
Pe  Q 
(10.20)
Here, the Q() function is simply an alternative way of expressing the
complementary error function, and in general
erfc (x)  2Q 2 x
(10.21)
These relationships are given for reference only and will not be used
further in this book.
An important parameter for carrier systems is the ratio of the
average carrier power to the noise power density, usually denoted
by [C/No]. The [Eb/No] and [C/No] ratios can be related as follows.
The average carrier power at the receiver is PR watts. The energy
per symbol is therefore PR/Rsym joules, with Rsym in symbols per sec-
ond. Since each symbol contains m bits, the energy per bit is
PR/mRsym joules. But mRsym  Rb, and therefore, the energy per bit
Eb is
Eb 
(10.22)
As before, let No represent the noise power density. Then Eb/No 
PR/RbNo. But PR/No is the carrier-to-noise density ratio, usually denoted
by C/No, and therefore,

(10.23)
Rearranging this and putting it in decibel notation gives

	  
	  [Rb]
(10.24)
It should be noted that whereas Eb/No has units of decibels, C/No has
units of dBHz, as explained in App. G.
Example 10.2
The downlink transmission rate in a satellite circuit is 61
Mb/s, and the required [Eb/No] at the ground station receiver is 9.5 dB.
Calculate the required [C/No].
solution
The transmission rate in decibels is
[Rb]  10 log 61  106  77.85 dBb/s
Eb

No
C

No
C/No

Rb
Eb

No
PR

Rb
2Eb

No
274
Chapter Ten
TLFeBOOK

## Page 289
