---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0303"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 303
confidence: "first-pass"
extraction_method: "structured-local"
---

The resulting equivalent noise-temperature rise at the earth station E
receive antenna output is 4.57  4.57  9.14K.
13.4.4
Coordination criterion
CCIR Report 454–3 (1982) specifies that the equivalent noise-temper-
ature rise should be no more than 4 percent of the equivalent thermal
noise temperature of the satellite link. The equivalent thermal noise
temperature is defined in the CCIR Radio Regulations, App. 29.
As an example, the CCIR Recommendations for FM Telephony
allows up to 10,000 pW0p total noise in a telephone channel. The
abbreviation pW0p stands for picowatts at a zero-level test point,
psophometrically weighted, as already defined in connection with
Table 13.1. The 10,000-pW0p total includes a 1000-pW0p allowance for
terrestrial station interference and 1000 pW0p for interference from
other satellite links. Thus the thermal noise allowance is 10,000 
2000  8000 pW0p. Four percent of this is 320 pW0p. Assuming that
this is over a 3.1-kHz bandwidth, the spectrum density is 320/3100 or
approximately 0.1 pJ0p (pW0p/Hz). In decibels, this is 130 dBJ. This
is output noise, and to relate it back to the noise temperature at the
antenna, the overall gain of the receiver from antenna to output,
including the processing gain discussed in Sec. 9.6.3, must be known.
For illustration purposes, assume that the gain is 90 dB, so the anten-
na noise is 130  90  220 dBJ. The noise-temperature rise corre-
sponding to this is 220  228.6  8.6 dBK. Converting this to kelvins
gives 7.25 K.
13.4.5
Noise power spectral density
The concept of noise power spectral density was introduced in Sec.
12.5 for a flat frequency spectrum. Where the spectrum is not flat,
an average value for the spectral density can be calculated. To illus-
trate this, the very much simplified spectrum curve of Fig. 13.10 will
be used. The maximum spectrum density is flat at 3 W/Hz from 0 to
2 kHz and then slopes linearly down to zero over the range from 2 to
8 kHz.
The noise power in any given bandwidth is calculated as the area
under the curve, whose width is the value of the bandwidth. Thus, for
the first 2 kHz, the noise power is 3 W/Hz  2000  6000 W. From 2
to 8 kHz, the noise power is 3  (8  2)  1000/2  9000 W. The total
power is therefore 15,000 W, and the average spectral density is
15,000/8000  1.875 W/Hz.
The noise power spectral density over the worst 4-kHz bandwidth
must include the highest part of the curve and is therefore calculated
for the 0- to 4-kHz band. The power over this band is seen to be the
364
Chapter Thirteen
TLFeBOOK
