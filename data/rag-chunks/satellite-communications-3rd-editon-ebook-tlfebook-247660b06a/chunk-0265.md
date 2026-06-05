---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0265"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 265
confidence: "first-pass"
extraction_method: "structured-local"
---

TNW,o  Tx 1  
(12.29)
This is the equivalent noise temperature of the network referred to the
output terminals of the network. The equivalent noise at the output
can be transferred to the input on dividing by the network power gain,
which by definition is 1/L. Thus the equivalent noise temperature of
the network referred to the network input is
TNW,i  Tx (L  1)
(12.30)
Since the network is bilateral, Eqs. (12.29) and (12.30) apply for sig-
nal flow in either direction. Thus Eq. (12.30) gives the equivalent noise
temperature of a lossy network referred to the input at the antenna
when the antenna is used in receiving mode.
If the lossy network should happen to be at room temperature, that
is, Tx  T0, then a comparison of Eqs. (12.26) and (12.30) shows that
F  L
(12.31)
This shows that at room temperature the noise factor of a lossy net-
work is equal to its power loss.
12.5.6
Overall system noise temperature
Figure 12.6a shows a typical receiving system. Applying the results of
the previous sections yields, for the system noise temperature referred
to the input,
TS  Tant  Te1 

(12.32)
The significance of the individual terms is illustrated in the following
examples.
Example 12.7
For the system shown in Fig. 12.6a, the receiver noise fig-
ure is 12 dB, the cable loss is 5 dB, the LNA gain is 50 dB, and its noise tem-
perature 150 K. The antenna noise temperature is 35 K. Calculate the noise
temperature referred to the input.
solution
For the main receiver, F  101.2  15.85. For the cable, L  100.5 
3.16. For the LNA, G  105. Hence
TS  35  150 

 185 K
3.16 	 (15.85  1) 	 290

105
(3.16  1) 	 290

105
L (F  1) T0

G1
(L  1) T0

G1
1
L
The Space Link
319
TLFeBOOK

## Page 334
