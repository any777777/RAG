---
chunk_id: "cme576-exam2-11-12-2017-abet-fv-key-copy-aeb04728a5-chunk-0002"
source_id: "cme576-exam2-11-12-2017-abet-fv-key-copy-aeb04728a5"
source_file: "New folder (3)/CME576_Exam2_11_12_2017_ABET_FV_Key - Copy.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "Exams and Questions"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

3 
 
P1 (8 Marks) (2 pages available)                                                                  
Q1.1 (4 Marks: 1+3)  
(a) Why 𝐶/𝑁 ratio is used in satellite link design, not 𝑆/𝑁 ratio? 
(b) A satellite TV signal occupies the full transponder bandwidth of 36 MHz, and it must provide a C/N ratio 
at the destination Earth Station of 22 dB. Given that the total transmission losses are 200 dB and the 
destination Earth Station G/T ratio is 31 dB/K, calculate the required satellite EIRP in dB and W.     
Answer Q1.1 (1 page)   
(a) Because FM is used, where the signal amplitude is the same as the carrier, not AM.  
 
(b) Rewriting the downlink C/N equation: 
 
 
[𝐶
𝑁]
𝐷
= [𝐸𝐼𝑅𝐵]𝐷+ [𝐺
𝑇]
𝐷
−[𝐿𝑜𝑠𝑠𝑒𝑠]𝐷−𝑘−[𝐵𝑁] 
 
[𝐸𝐼𝑅𝐵]𝐷= [𝐶
𝑁]
𝐷
−[𝐺
𝑇]
𝐷
+ [𝐿𝑜𝑠𝑠𝑒𝑠]𝐷+ 𝑘+ [𝐵𝑁] 
 
Convert to dBs: 𝐵𝑁= 36 MHz    [𝐵𝑁] = 75.6 dBHz 
 
𝑘= 1.3807 × 10–23   −228.6 dBW/K/Hz 
 
 [EIR𝑃]𝐷= 22 −31 + 200 −228.6 + 75.6 = 37.96 ≈38 dBW 
= 6.31 kW 
[EIRP]𝐷= 37.96 ≈38 dBW = 6.31 kW

## Page 4

4 
 
Q1.2 (4 Marks)  A 12 GHz earth station (ES) system is receiving under a rainy sky condition with rain 
attenuation (caused by absorption) of 3 dB. The ES has an antenna with a noise temperature of 50 K, a LNA with 
a noise temperature of 100 K and a gain of 40 dB, and a mixer with a noise temperature of 1000 K.  
Find the system noise temperature 𝑇𝑠. 
 
Answer (1 page): 
System noise temperature is generally found from: 
 
𝑇𝑠 = 𝑇𝑅𝑎𝑖𝑛 + 𝑇𝐴𝑛𝑡 + 𝑇𝐿𝑁𝐴+ 𝑇𝑀𝑖𝑥𝑒𝑟
𝐺𝐿𝑁𝐴
+ …. 
𝑇𝑅𝑎𝑖𝑛= 𝑇𝑎(1 −1
𝐴) 
wher𝑒    𝐴= 10𝐴/10 = 103/10 = 1.995 
𝑇𝑅𝑎𝑖𝑛= 𝑇𝑎(1 −1
𝐴) = 𝑇𝑅𝑎𝑖𝑛= 290 (1 −
1
1.995) = 144.656 K = 21.603 dB 
For 𝐺𝐿𝑁𝐴  as a ratio:  
𝐺𝐿𝑁𝐴= 40 dB =  10,000 
Finally: 
𝑇𝑠= 𝑇𝑅𝑎𝑖𝑛 + 𝑇𝐴𝑛𝑡 + 𝑇𝐿𝑁𝐴+ 𝑇𝑀𝑖𝑥𝑒𝑟
𝐺𝐿𝑁𝐴
= 144.656 + 50 + 100 + 1000
10,000 = 294.756 K 
 
𝑇𝑠= 294.756 K  =  24.695 dB ≈24.7 dB

## Page 5
