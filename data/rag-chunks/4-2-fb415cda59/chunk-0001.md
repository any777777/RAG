---
chunk_id: "4-2-fb415cda59-chunk-0001"
source_id: "4-2-fb415cda59"
source_file: "New folder (3)/4.2.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 1
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1

Handout: System Noise Temperature and G/T Ratio
Satellite Communication Systems
1
Introduction
Noise is one of the most important performance-limiting factors in satellite communica-
tion receivers. To evaluate receiver quality, two key parameters are used:
• System Noise Temperature, Ts
• G/T Ratio (Gain-to-Noise-Temperature ratio)
These parameters directly determine the carrier-to-noise ratio (C/N) at the demodu-
lator input and are therefore central to satellite link budget design.
2
Thermal Noise and Noise Temperature
Any physical object at temperature greater than 0 K generates electrical noise power.
The available thermal noise power in a bandwidth B is
Pn = kTB
(1)
where
• k = 1.38 × 10−23 J/K is Boltzmann’s constant,
• T is the noise temperature in Kelvin,
• B is the bandwidth in Hz.
In dB units,
k = −228.6 dBW/K/Hz
Noise temperature provides a convenient way to describe noise contributions of an-
tennas, amplifiers, mixers, and lossy components.
3
System Noise Temperature
3.1
Equivalent Noise Model
A practical receiver contains multiple elements such as:
• RF amplifier
• Downconverter/mixer
• IF amplifier
1

## Page 2

Each device adds noise. To simplify analysis, each noisy device is replaced by:
1. A noiseless device with the same gain.
2. An equivalent input noise generator with noise temperature equal to the device’s
noise temperature.
All individual noise contributions are then referred to the input of the receiver by
dividing by the preceding gains.
3.2
General Expression for System Noise Temperature
If the receiver consists of stages with noise temperatures T1, T2, . . . and gains G1, G2, . . . ,
then the total system noise temperature at the input is
Ts = T1 + T2
G1
+
T3
G1G2
+ · · ·
(2)
Noise contribution from later stages is reduced by the gain of earlier stages.
3.3
Example: Three-Stage Receiver
For an RF amplifier, mixer, and IF amplifier:
Ts = TRF + Tm
GRF
+
TIF
GRFGm
(3)
3.4
Example 4.2.1
Given:
Tant = 50 K, TRF = 50 K, Tm = 500 K, TIF = 1000 K
GRF = 23 dB ≈200, Gm = 0 dB = 1
Compute:
Ts = 50 + 50 + 500
200 + 1000
200
Ts = 107.5 K
If the mixer has 10 dB loss (Gm = 0.1), then:
Ts = 50 + 50 + 2.5 +
1000
200 × 0.1 = 152.5 K
4
Effect of Waveguide Loss
If a lossy device with gain Gl < 1 and physical temperature Tp is placed ahead of the
LNA, the equivalent noise temperature is
Tl = Tp
 1
Gl
−1

(4)
2

## Page 3
