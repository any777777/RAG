---
chunk_id: "reference-777408ef16-chunk-0085"
source_id: "reference-777408ef16"
source_file: "New folder (3)/Reference.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 85
confidence: "first-pass"
extraction_method: "structured-local"
---

The reduction factors are given in Table 4.3. With all these factors
together into one equation, the rain attenuation in decibels is given by
Ap  aRp
bLSrp dB
(4.7)
Interpolation formulas which depend on the climatic zone being con-
sidered are available for values of p other than those quoted above
(see, for example, Ippolito, 1986). Polarization shifts resulting from
rain are described in Sec. 5.6.
Example 4.1
Calculate, for a frequency of 12 GHz and for horizontal and
vertical polarizations, the rain attenuation which is exceeded for 0.01 per-
cent of the time in any year, for a point rain rate of 10 mm/h. The earth sta-
tion altitude is 600 m, and the antenna elevation angle is 50 degrees. The
rain height is 3 km.
solution
The given data are shown below. Because the CCIR formula con-
tains hidden conversion factors, units will not be attached to the data, and
it is understood that all lengths and heights are in kilometers, and rain rate
is in millimeters per hour. The elevation angle, however, must be stated in
degrees in order for Mathcad to correctly evaluate the sine and cosine func-
tions.
El :  50  deg
hO :  .6
hr:  3
R01 :  10
Although the Mathcad vec operator could be used to carry out all calcula-
tions in a compact form, the individual calculations are shown for illustra-
tion purposes. The factors that are independent of polarization will be
calculated first.
Equation (4.4):
LS : 
LS  3.133
hr  hO

sin (El)
Radio Wave Propagation
97
TABLE 4.3
Reduction Factors
For p  0.001%
r0.001 
For p  0.01%
r0.01 
For p  0.1%
r0.1 
For p  1%
r1  1
SOURCE: Ippolito, 1986.
180

180  LG
90

90  4LG
10

10  LG
TLFeBOOK

## Page 108

Equation (4.6):
LG :  LS 	 cos (El)
LG  2.014
From Table 4.3, the rate reduction factor is
r01 : 
r01  0.918
Equation (4.5):
L :  LS 	 r01
L  2.876
For horizontal polarization, from Table 3.2 at f  12 GHz:
ah :  .0188
bh :  1.217
Equation (4.2):
 :  ah 	 R01
bh
  0.31
dB/m
Equation (4.3):
AdB :   	 L
AdB  0.89
    
For vertical polarization, from Table 3.2 at f  12 GHz:
av :  .0168
bv :  1.2
Equation (4.2):
 :  av 	 R01
bv
  0.266
dB/m
Equation (4.3):
AdB :   	 L
AdB  0.77
    
The corresponding equations for circular polarization are
ac 
(4.8a)
bc 
(4.8b)
The attenuation for circular polarization is compared with that for
linear polarization in the following example.
ahbh 
 avbv

2ac
ah 
 av

2
90

90 
 4 	 LG
98
Chapter Four
TLFeBOOK

## Page 109
