---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0264"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 264
confidence: "first-pass"
extraction_method: "structured-local"
---

In Example 12.6 it will be seen that the decibel quantities must be
converted to power ratios. Also, even though the main receiver has a
very high noise temperature, its effect is made negligible by the high
gain of the LNA.
12.5.5
Noise temperature of absorptive
networks
An absorptive network is one which contains resistive elements. These
introduce losses by absorbing energy from the signal and converting it
to heat. Resistive attenuators, transmission lines, and waveguides are
all examples of absorptive networks, and even rainfall, which absorbs
energy from radio signals passing through it, can be considered a form
of absorptive network. Because an absorptive network contains resis-
tance it generates thermal noise.
Consider an absorptive network which has a power loss L. The pow-
er loss is simply the ratio of input power to output power and will
always be greater than unity. Let the network be matched at both
ends, to a terminating resistor RT at one end and an antenna at the
other, as shown in Fig. 12.5, and let the system be at some ambient
temperature Tx. The noise energy transferred from RT into the net-
work is kTx. Let the network noise be represented at the output ter-
minals (the terminals connected to the antenna in this instance) by an
equivalent noise temperature TNW,o. Then the noise energy radiated by
the antenna is
Nrad 
 kTNW,o
(12.28)
Because the antenna is matched to a resistive source at temperature
Tx, the available noise energy which is fed into the antenna and radi-
ated is Nrad  kTx. Keep in mind that the antenna resistance to which
the network is matched is fictitious in the sense that it represents
radiated power, but it does not generate noise power. This expression
for Nrad can be substituted into Eq. (12.28) to give
kTx

L
318
Chapter Twelve
RT
Lossy network
power loss L : 1
Ambient temperature
TX
NRAD
Figure 12.5
Network matched at both ends, to a terminating resistor RT
at one end and an antenna at the other.
TLFeBOOK

## Page 333
