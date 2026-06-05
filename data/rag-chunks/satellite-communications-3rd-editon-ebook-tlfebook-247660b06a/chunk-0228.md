---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0228"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 228
confidence: "first-pass"
extraction_method: "structured-local"
---

Note that with p(t) equal to ±1, the square is just 1. The bandpass
filter following the frequency multiplier is tuned to the carrier second
harmonic, which provides one of the inputs to the phase detector of the
phase-locked loop. The voltage-controlled oscillator (VCO) in the
phase-locked loop (PLL) operates at the carrier frequency. The second
frequency multiplier provides the second harmonic of this as the other
input to the phase detector. The phase difference between these two
inputs generates a bias voltage that brings the frequency of the VCO
into synchronism with the carrier frequency as derived from the BPSK
signal.
With QPSK, the signal can be represented by the formulas given in
Table 10.1, which may be written generally as
e (t)  2 cos (
0t ±
)
(10.27)
Quadrupling this, followed by some trigonometric simplification,
results in
e4 (t) 
 2 cos 2 
0t ±
 
cos 4 (
0t ±
) (10.28)
The last term on the right-hand side is selected by the bandpass filter
and is
cos 4 
0t ±
 
cos (4
0t ± n	)
(10.29)
This is seen to consist of the fourth harmonic of the carrier, including
a constant-phase term that can be ignored. The fourth harmonic is
selected by the bandpass filter, and the operation of the circuit pro-
ceeds in a similar manner to that for the BPSK signal.
Frequency multiplication can be avoided by use of a method known
as the Costas loop. Details of this, along with an analysis of the effects
of noise on the squaring loop and the Costas loop methods, will be
found in Gagliardi (1991). Other methods are also described in detail
in Franks (1980).
10.8
Bit Timing Recovery
Accurate bit timing is needed at the receiver in order to be able to
sample the received waveform at the optimal points. In the most com-
mon arrangements, the clocking signal is recovered from the demod-
ulated waveform, these being known as self-clocking or self-
synchronizing systems. Where the waveform has a high density of
12
n	

12
n	

4
12
n	

32
n	

4
278
Chapter Ten
TLFeBOOK

## Page 293
