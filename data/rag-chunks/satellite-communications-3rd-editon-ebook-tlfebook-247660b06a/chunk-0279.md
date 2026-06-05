---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0279"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 279
confidence: "first-pass"
extraction_method: "structured-local"
---

solution
1.9 dB attenuation is equivalent to a 1.55:1 power loss. The equiv-
alent noise temperature of the rain is therefore
Train  280 (1  1/1.55)  99.2 K
The new system noise temperature is 400  99.2  499.2 K. The decibel
increase in noise power is therefore [499.2]  [400]  0.96 dB. At the same
time, the carrier is reduced by 1.9 dB, and therefore, the [C/N] with 1.9-dB
rain attenuation drops to 20  1.9  0.96  17.14 dB. This is the value
below which [C/N] drops for 0.1 percent of the time.
It is left as an exercise for the student to show that where the rain
power attenuation A (not dB) is entirely absorptive, the downlink C/N
power ratios (not dBs) are related to the clear-sky value by
 rain  CSA  (A  1) 

(12.60)
where the subscript CS is used to indicate clear-sky conditions and
TS,CS is the system noise temperature under clear-sky conditions.
For low frequencies (6/4 GHz) and low rainfall rates (below about 1
mm/h), the rain attenuation is almost entirely absorptive. At higher
rainfall rates, scattering becomes significant, especially at the higher
frequencies. When scattering and absorption are both significant, the
total attenuation must be used to calculate the reduction in carrier
power and the absorptive attenuation to calculate the increase in noise
temperature.
As discussed in Chap. 9, a minimum value of [C/N] is required for
satisfactory reception. In the case of frequency modulation, the mini-
mum value is set by the threshold level of the FM detector, and a
threshold margin is normally allowed, as shown in Fig. 9.12. Sufficient
margin must be allowed so that rain-induced fades do not take the
[C/N] below threshold more than a specified percentage of the time, as
shown in Example 12.17.
Example 12.17
In an FM satellite system, the clear-sky downlink [C/N]
ratio is 17.4 dB and the FM detector threshold is 10 dB, as shown in Fig.
9.12. (a) Calculate the threshold margin at the FM detector, assuming the
threshold [C/N] is determined solely by the downlink value. (b) Given that
Ta  272 K and that TS,CS  544 K, calculate the percentage of time the sys-
tem stays above threshold. The curve of Fig. 12.8 may be used for the down-
link, and it may be assumed that the rain attenuation is entirely absorptive.
solution
(a) Since it is assumed that the overall [C/N] ratio is equal to the
downlink value, the clear-sky input [C/N] to the FM detector is 17.4 dB. The
threshold level for the detector is 10 dB, and therefore, the rain-fade mar-
gin is 17.4  10  7.4 dB.
Ta

TS,CS
N

C
N

C
The Space Link
333
TLFeBOOK
