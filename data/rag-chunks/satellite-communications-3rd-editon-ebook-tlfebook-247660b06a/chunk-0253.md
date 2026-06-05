---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0253"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 253
confidence: "first-pass"
extraction_method: "structured-local"
---

EIRP  GPS
(12.2)
EIRP is often expressed in decibels relative to one watt, or dBW. Let
PS be in watts; then
[EIRP]  [PS]  [G]
dBW
(12.3)
where [PS] is also in dBW and [G] is in dB.
Example 12.1
A satellite downlink at 12 GHz operates with a transmit
power of 6 W and an antenna gain of 48.2 dB. Calculate the EIRP in dBW.
solution
[EIRP]  10 log 6  48.2
 56 dBW
For a paraboloidal antenna, the isotropic power gain is given by Eq.
(6.32). This equation may be rewritten in terms of frequency, since this
is the quantity which is usually known:
G   (10.472fD)2
(12.4)
where f is the carrier frequency in gigahertz, D is the reflector diame-
ter in meters, and  is the aperture efficiency. A typical value for aper-
ture efficiency is 0.55, although values as high as 0.73 have been
specified (Andrew Antenna, 1985).
With the diameter D in feet and all other quantities as before, the
equation for power gain becomes
G   (3.192fD)2
(12.5)
Example 12.2
Calculate the gain of a 3-m paraboloidal antenna operating
at a frequency of 12 GHz. Assume an aperture efficiency of 0.55.
solution
G  0.55  (10.472  12  3)2 
 78,168
Hence
[G]  10 log 78,168  48.9 dB
12.3
Transmission Losses
The [EIRP] may be thought of as the power input to one end of the
transmission link, and the problem is to find the power received at the
other end. Losses will occur along the way, some of which are constant.
306
Chapter Twelve
TLFeBOOK

## Page 321
