---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0283"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 283
confidence: "first-pass"
extraction_method: "structured-local"
---

 1010.15  109.32  5.49  1010

	  10 log (5.49  1010)  92.6 dBHz
Again, it is seen from Example 12.19 that the combined C/No value
is close to the lowest value, which is the downlink value.
So far, only thermal and antenna noise has been taken into account
in calculating the combined value of C/N ratio. Another source of noise
which must be considered is intermodulation noise, discussed in the
next section.
12.11
Intermodulation Noise
Intermodulation occurs where multiple carriers pass through any device
with nonlinear characteristics. In satellite communications systems,
this most commonly occurs in the traveling-wave tube high-power
amplifier aboard the satellite, as described in Sec. 7.7.3. Both amplitude
and phase nonlinearities give rise to intermodulation products.
As shown in Fig. 7.20, third-order intermodulation products fall on
neighboring carrier frequencies, where they result in interference.
Where a large number of modulated carriers are present, the inter-
modulation products are not distinguishable separately but instead
appear as a type of noise which is termed intermodulation noise.
The carrier-to-intermodulation-noise ratio is usually found experi-
mentally, or in some cases it may be determined by computer 
methods. Once this ratio is known, it can be combined with the 
carrier-to-thermal-noise ratio by the addition of the reciprocals in the
manner described in Sec. 12.10. Denoting the intermodulation term
by (C/N)IM and bearing in mind that the reciprocals of the C/N power
ratios (and not the corresponding dB values) must be added, Eq.
(12.61) is extended to
 
U
 
D
 
IM
(12.62)
Example 12.20
For a satellite circuit the carrier-to-noise ratios are uplink
23 dB, downlink 20 dB, intermodulation 24 dB. Calculate the overall carri-
er-to-noise ratio in decibels.
solution
From Eq. (12.62),
 102.4  102.3  102  0.0019
N

C
No

C
No

C
No

C
No

C
C

No
No

C
338
Chapter Twelve
TLFeBOOK

## Page 353
