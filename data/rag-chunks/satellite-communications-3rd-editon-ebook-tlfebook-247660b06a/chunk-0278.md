---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0278"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 278
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 346

power output from the satellite may be monitored by a central control
station or in some cases by each earth station, and the power output
from any given earth station may be increased if required to compen-
sate for fading. Thus the earth-station HPA must have sufficient
reserve power to meet the fade margin requirement.
Some typical rain-fade margins are shown in Table 12.2. As an
example, for Ottawa, the rain attenuation exceeds 1.9 dB for 0.1 per-
cent of the time. This means that to meet the specified power require-
ments at the input to the satellite for 99.9 percent of the time, the
earth station must be capable of providing a 1.9-dB margin over the
clear-sky conditions.
12.9.2
Downlink rain-fade margin
The results given by Eqs. (12.53) and (12.54) are for clear-sky condi-
tions. Rainfall introduces attenuation by absorption and scattering of
signal energy, and the absorptive attenuation introduces noise as dis-
cussed in Sec. 12.5.5. Let [A] dB represent the rain attenuation caused
by absorption. The corresponding power loss ratio is A  10[A]/10, and
substituting this for L in Eq. (12.29) gives the effective noise tempera-
ture of the rain as
Train  Ta 1  
(12.58)
Here, Ta, which takes the place of Tx in Eq. (12.29), is known as the
apparent absorber temperature. It is a measured parameter which is a
function of many factors including the physical temperature of the
rain and the scattering effect of the rain cell on the thermal noise inci-
dent upon it (Hogg and Chu, 1975). The value of the apparent absorber
temperature lies between 270 and 290 K, with measured values for
North America lying close to or just below freezing (273 K). For exam-
ple, the measured value given by Webber et al. (1986) is 272 K.
The total sky-noise temperature is the clear-sky temperature TCS
plus the rain temperature:
Tsky  TCS  Train
(12.59)
Rainfall therefore degrades the received [C/No] in two ways: by atten-
uating the carrier wave and by increasing the sky-noise temperature.
Example 12.16
Under clear-sky conditions, the downlink [C/N] is 20 dB,
the effective noise temperature of the receiving system being 400 K. If rain
attenuation exceeds 1.9 dB for 0.1 percent of the time, calculate the value
below which [C/N] falls for 0.1 percent of the time. Assume Ta  280 K.
1
A
332
Chapter Twelve
TLFeBOOK

## Page 347
