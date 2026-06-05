---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0267"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 267
confidence: "first-pass"
extraction_method: "structured-local"
---

The G/T ratio is a key parameter in specifying the receiving system
performance. The antenna gain GR and the system noise temperature
TS can be combined in Eq. (12.34) as
[G/T]  [GR]  [TS]
dBK1
(12.35)
Therefore, the link equation [Eq. (12.34)] becomes
 	  [EIRP]   	  [LOSSES]  [k]  [BN]
(12.36)
The ratio of carrier power to noise power density PR/No may be the
quantity actually required. Since PN  kTNBN  NoBN, then
 	  
	
 
	  [BN]
and therefore

	   	  [BN]
(12.37)
[C/N] is a true power ratio in units of decibels, and [BN] is in decibels
relative to one hertz, or dBHz. Thus the units for [C/No] are dBHz.
Substituting Eq. (12.37) for [C/N] gives

	  [EIRP]   	  [LOSSES]  [k]
dBHz
(12.38)
Example 12.9
In a link budget calculation at 12 GHz, the free-space loss is
206 dB, the antenna pointing loss is 1 dB, and the atmospheric absorption is
2 dB. The receiver G/T ratio is 19.5 dB/K, and receiver feeder losses are 1 dB.
The EIRP is 48 dBW. Calculate the carrier-to-noise spectral density ratio.
solution
The data are best presented in tabular form and in fact lend them-
selves readily to spreadsheet-type computations. For brevity, the units are
shown as decilogs, and losses are entered as negative numbers to take
account of the minus sign in Eq. (12.38). Recall that Boltzmann’s constant
equates to 228.6 decilogs, so [k]  228.6 decilogs, as shown in the table.
Entering data in this way allows the final result to be entered in a table cell
as the sum of the terms in the rows above the cell, a feature usually incor-
porated in spreadsheets and word processors. This is illustrated in the fol-
lowing table. 
G

T
C

No
C

N
C

No
C

No
C

NoBN
C

N
G

T
C

N
The Space Link
321
TLFeBOOK

## Page 336
