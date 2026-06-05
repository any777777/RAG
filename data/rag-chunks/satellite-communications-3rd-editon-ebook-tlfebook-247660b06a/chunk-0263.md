---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0263"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 263
confidence: "first-pass"
extraction_method: "structured-local"
---

TS  Tant  Te1 

 ...
(12.24)
12.5.4
Noise factor
An alternative way of representing amplifier noise is by means of its
noise factor F. In defining the noise factor of an amplifier, the source is
taken to be at room temperature, denoted by T0, usually taken as 290
K. The input noise from such a source is kT0, and the output noise from
the amplifier is
N0,out  FGkT0
(12.25)
Here, G is the available power gain of the amplifier as before, and F is
its noise factor.
A simple relationship between noise temperature and noise factor
can be derived. Let Te be the noise temperature of the amplifier, and
let the source be at room temperature as required by the definition of
F. This means that Tant  T0. Since the same noise output must be
available whatever the representation, it follows that
Gk (T0  Te)  FGkT0
or
Te  (F  1) T0
(12.26)
This shows the direct equivalence between noise factor and noise
temperature. As a matter of convenience, in a practical satellite receiv-
ing system, noise temperature is specified for low-noise amplifiers and
converters, while noise factor is specified for the main receiver unit.
The noise figure is simply F expressed in decibels:
Noise figure  [F]  10 log F
(12.27)
Example 12.6
An LNA is connected to a receiver which has a noise figure
of 12 dB. The gain of the LNA is 40 dB, and its noise temperature is 120 K.
Calculate the overall noise temperature referred to the LNA input.
solution
12 dB is a power ratio of 15.85:1, and therefore,
Te2  (15.85  1)  290  4306 K
A gain of 40 dB is a power ratio of 104:1, and therefore,
Tin  120 
 120.43 K
4306

104
Te3

G1G2
Te2

G1
The Space Link
317
TLFeBOOK

## Page 332
