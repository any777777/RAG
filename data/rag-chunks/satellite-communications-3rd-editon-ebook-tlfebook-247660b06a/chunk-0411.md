---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0411"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 411
confidence: "first-pass"
extraction_method: "structured-local"
---

Equation (10.53):
CNodB : EIRPdBW  GTdB  LOSSESdB  kdB
CNodB  86.3
The downlink bit rate in dB relative to 1 bps is
RbdB : 10  log 

RbdB  76
Equation (10.24):
EbNodB : CNodB  RbdB
EbNodB  10.3
As noted in Sec. 16.8, a [Eb/No] of at least 6 dB is required. The value
obtained provides a margin of 4.3 dB under clear-sky conditions.
Example 16.2
Table 16.2 and Fig. 16.8 show the rainfall intensity in mm/h
exceeded for given percentages of time. Calculate the upper limit for [Eb/No]
set by the rainfall for the percentage of time equal to 0.01 percent. The earth
station is at mean sea level, and the rain attenuation may be assumed
entirely absorptive, and the apparent absorber temperature may be taken
as 272 K.
solution
It is first necessary to calculate the attenuation resulting from the
rain. The given data are shown below. Because the CCIR formula contains
hidden conversion factors, units will not be attached to the data, and it is
understood that all lengths and heights are in km, and rain rate is in mm/h.
The elevation angle, however, must be stated in degrees in order for
Mathcad to correctly evaluate the sine and cosine functions.
From Fig. 16.8, the earth station is seen to be located within region K.
From the accompanying Table 16.2, the rainfall exceeds 42 mm/h for 0.01
percent of the time.
R01 : 42
Table 4.2 does not give the coefficients for 12.5 GHz; therefore, the values
must be found by linear interpolation between 12 and 15 GHz. Denoting the
12-GHz values with subscript 12 and the 15-GHz values with subscript 15,
then from Table 4.2,
f12:12GHz
ah12:.0188
av12:.0168
bh12:1.217
bv12:1.2
f15:15GHz
ah15:.0367
av15:.0335
bh15:1.154
bv15:1.128
Using linear interpolation, the values at 12.5 GHz are found as
ah : ah12 
 (fD  f12)
ah  0.022
bh : bh12 
 (fD  f12)
bh  1.207
bh15  bh12

f15  f12
ah15  ah12

f15  f12
Rb

sec1
480
Chapter Sixteen
TLFeBOOK

## Page 491
