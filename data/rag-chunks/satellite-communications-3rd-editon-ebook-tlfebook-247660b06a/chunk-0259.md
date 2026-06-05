---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0259"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 259
confidence: "first-pass"
extraction_method: "structured-local"
---

at the input, and unless the signal is significantly greater than the
noise, amplification will be of no help because it will amplify signal
and noise to the same extent. In fact, the situation will be worsened by
the noise added by the amplifier.
The major source of electrical noise in equipment is that which aris-
es from the random thermal motion of electrons in various resistive
and active devices in the receiver. Thermal noise is also generated in
the lossy components of antennas, and thermal-like noise is picked up
by the antennas as radiation.
The available noise power from a thermal noise source is given by
PN  kTNBN
(12.14)
Here, TN is known as the equivalent noise temperature, BN is the
equivalent noise bandwidth, and k  1.38  1023 J/K is Boltzmann’s
constant. With the temperature in kelvins and bandwidth in hertz, the
noise power will be in watts. The noise power bandwidth is always
wider than the 3-dB bandwidth determined from the amplitude-fre-
quency response curve, and a useful rule of thumb is that the noise
bandwidth is equal to 1.12 times the 3-dB bandwidth, or BN 
 1.12
 B3 dB.
The main characteristic of thermal noise is that it has a flat fre-
quency spectrum; that is, the noise power per unit bandwidth is a con-
stant. The noise power per unit bandwidth is termed the noise power
spectral density. Denoting this by N0, then from Eq. (12.14),
N0 
 kTN joules
(12.15)
The noise temperature is directly related to the physical tempera-
ture of the noise source but is not always equal to it. This is discussed
more fully in the following sections. The noise temperatures of various
sources which are connected together can be added directly to give the
total noise.
Example 12.5
An antenna has a noise temperature of 35 K and is matched
into a receiver which has a noise temperature of 100 K. Calculate (a) the
noise power density and (b) the noise power for a bandwidth of 36 MHz.
solution
(a)
N0  (35  100)  1.38  1023  1.86  1021 J
(b)
PN  1.86  1021  36  106  0.067 pW
In addition to these thermal noise sources, intermodulation distor-
tion in high-power amplifiers (see, for example, Sec. 12.7.3) can result
PN

BN
312
Chapter Twelve
TLFeBOOK

## Page 327
