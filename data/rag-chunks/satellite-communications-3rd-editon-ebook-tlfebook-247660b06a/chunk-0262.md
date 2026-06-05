---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0262"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 262
confidence: "first-pass"
extraction_method: "structured-local"
---

which is simply noise energy in joules as shown by Eq. (12.15). The
input noise energy coming from the antenna is
No,ant  kTant
(12.16)
The output noise energy No,out will be GNo,ant plus the contribution
made by the amplifier. Now all the amplifier noise, wherever it occurs
in the amplifier, may be referred to the input in terms of an equivalent
input noise temperature for the amplifier Te. This allows the output
noise to be written as
No,out  Gk (Tant  Te)
(12.17)
The total noise referred to the input is simply No,out/G, or
No,in  k (Tant  Te)
(12.18)
Te can be obtained by measurement, a typical value being in the range
35 to 100 K. Typical values for Tant are given in Sec. 12.5.1.
12.5.3
Amplifiers in cascade
The cascade connection is shown in Fig. 12.4b. For this arrangement,
the overall gain is
G  G1G2
(12.19)
The noise energy of amplifier 2 referred to its own input is simply
kTe2. The noise input to amplifier 2 from the preceding stages is
G1k(Tant  Te1), and thus the total noise energy referred to amplifier 2
input is
The Space Link
315
Figure 12.3
Antenna noise temperature as a function of elevation for 1.8-m antenna
characteristics. (Andrew Bulletin 1206; courtesy Andrew Antenna Company, Limited.)
TLFeBOOK

## Page 330

N0,2  G1k (Tant  Te1)  kTe2
(12.20)
This noise energy may be referred to amplifier 1 input by dividing
by the available power gain of amplifier 1:
N0,1 
 k Tant  Te1 

(12.21)
A system noise temperature may now be defined as TS by
N0,1  kTS
(12.22)
and hence it will be seen that TS is given by
TS  Tant  Te1 
(12.23)
This is a very important result. It shows that the noise temperature
of the second stage is divided by the power gain of the first stage when
referred to the input. Therefore, in order to keep the overall system
noise as low as possible, the first stage (usually an LNA) should have
high power gain as well as low noise temperature.
This result may be generalized to any number of stages in cascade,
giving
Te2

G1
Te2

G1
N0,2

G1
316
Chapter Twelve
Figure 12.4
Circuit used in finding equivalent noise temper-
ature of (a) an amplifier and (b) two amplifiers in cascade.
TLFeBOOK

## Page 331
