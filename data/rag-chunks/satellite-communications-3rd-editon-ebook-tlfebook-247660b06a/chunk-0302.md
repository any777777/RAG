---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0302"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 302
confidence: "first-pass"
extraction_method: "structured-local"
---

The transmission gain for network R is then defined as
[#]  [URE]  [URS]
(13.16)
Note that this is the same transmission gain shown in Fig. 12.9.
Using the transmission gain, the interference I2 at the satellite may
be referred to the earth station receiver as #I2, and hence the noise-
temperature rise at the satellite receiver input may be referred to the
earth station receiver input as #"TS. This is illustrated in Fig. 13.9b.
Expressed in decibel units, the relationship is
["TS  E]  [#]  ["TS]
(13.17)
13.4.3
Resulting noise-temperature rise
The overall equivalent rise in noise temperature at earth station E as
a result of interference signals B1 and B2 is then
"T  "TS  E  "TE
(13.18)
In this final calculation the dBK values must first be converted to
degrees, which are then added to give the resulting equivalent noise-
temperature rise at the earth station E receive antenna output.
362
Chapter Thirteen
Figure 13.9
(a) Defining the
transmission gain #
in Sec.
13.4.2. (b) Use of transmission
gain to refer satellite noise tem-
perature to an earth-station.
TLFeBOOK

## Page 373

Example 13.6
Given that LU  200 dB, LD  196 dB, GE  G′E  25 dB,
GS  G′S  9 dB, GTE  GRE  48 dB, GRS  GTS  19 dB, US  U′S  1 J,
and U′E  10 J, calculate the transmission gain [#], the interference levels
[I1] and [I2], and the equivalent temperature rise overall.
solution
Using Eq. (13.14) gives
[URS]  50  48  19  200
 183 dBJ
Using Eq. (13.15) gives
[URE]  60  19  48  196
 189 dBJ
Therefore,
[#]  189  (183)
 6 dB
From Eq. (13.10),
[I1]  60  9  25  196
 222 dBJ
From Eq. (13.12),
[I2]  50  25  9  200
 216 dBJ
From Eq. (13.11),
["TE]  222  228.6
 6.6 dBK
or
"TE  4.57 K
From Eq. (13.13),
["TS]  216  228.6
 12.6 dBK
From Eq. (13.17),
["TS  E]  6  12.6
 6.6 dBK
or
"TS  E  4.57 K
Interference
363
TLFeBOOK

## Page 374
