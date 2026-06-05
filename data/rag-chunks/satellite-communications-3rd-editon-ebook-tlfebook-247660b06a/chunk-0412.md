---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0412"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 412
confidence: "first-pass"
extraction_method: "structured-local"
---

av : av12  
 (fD  f12)
av  0.02
bv : bv12 
 (fD  f12)
bv  1.188
Since circular polarization is used, the coefficients are found from Eq. (4.8):
Equation (4.8a):
ac : 
ac  0.021
Equation (4.8b):
bc : 
bc  1.198
Using the Method 3 curves in Fig. 4.4 for p  0.01 percent and earth station
latitude 45°, the rain height is approximately 3.5 km, and as stated in the
problem, at mean sea level ho  0,
hR : 3.5
ho : 0
Equation (4.4):
LS : 
LS  5.8
Equation (4.6):
LG : LS  cos(El)
LG  4.6
From Table 4.3,
r01 : 
r01  0.8
Equation (4.5):
L : LS  r01
L  4.8
Equation (4.2):
 : ac  R01
bc
  1.819
Equation (4.3):
AdB01 :   L
AdB01  8.8
The effect of rain is calculated as shown in Sec. 12.9.2. This requires the
attenuation to be expressed as a power ratio:
90

90  4  LG
hR  ho

sin(El)
ah  bh  av  bv

2  ac
ah  av

2
bv15  bv12

f15  f12
av15  av12

f15 f12
Direct Broadcast Satellite Services
481
TLFeBOOK

## Page 492

A : 10
A  7.5
Given:
Ta : 272K
Equation (12.58):
TRAIN : Ta  1  

TRAIN  235.9  K
For Eq. (12.60), the noise-to-signal ratios are required. These are denoted
here as NoC along with the appropriate subscript:
NoCCS:10
NoCCS  2.3109
The system noise temperature under clear-sky conditions is just TS, but the
subscript will be changed to conform with Eq. (12.60):
TSCS : TS
Equation (12.60):
NoCRAIN : NoCCS  A  (A  1)  

In dB, this is
CNodBRAIN : 10  log (NoCRAIN)
CNodBRAIN  73.8
Recalculating the [Eb/No] ratio:
Equation (10.24):
EbNodBRAIN : CNodBRAIN  RbdB
EbNodBRAIN  2.3
     
Thus the rain will completely wipe out the signal for 0.01 percent of the
time. It is left as an exercise for the reader to find the size of antenna that
would provide an adequate signal under these rain conditions.
16.12
Uplink
Ground stations that provide the uplink signals to the satellites in a
DBS system are highly complex systems in themselves, utilizing a
wide range of receiving, recording, encoding, and transmission equip-
ment. Signals will originate from many sources. Some will be analog
TV received from satellite broadcasts. Others will originate in a stu-
Ta

TSCS
CNodB

10
1

A
AdB01

10
482
Chapter Sixteen
TLFeBOOK

## Page 493
