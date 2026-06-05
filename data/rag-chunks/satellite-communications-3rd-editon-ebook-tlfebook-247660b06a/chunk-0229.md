---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0229"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 229
confidence: "first-pass"
extraction_method: "structured-local"
---

zero crossings, a zero-crossing detector can be used to recover the
clocking signal. In practice, the received waveform is often badly dis-
torted by the frequency response of the transmission link and by
noise, and the design of the bit timing recovery circuit is quite com-
plicated. In most instances, the spectrum of the received waveform
will not contain a discrete component at the clock frequency. However,
it can be shown that a periodic component at the clocking frequency
is present in the squared waveform for digital signals (unless the
received pulses are exactly rectangular, in which case squaring sim-
ply produces a dc level for a binary waveform). A commonly used base-
band scheme is shown in block schematic form in Fig. 10.21 (Franks,
1980). The filters A and B form part of the normal signal filtering
(e.g., raised-cosine filtering). The signal for the bit timing recovery is
tapped from the junction between A and B and passed along a sepa-
rate branch which consists of a filter, a squaring circuit, and a band-
pass filter which is sharply tuned to the clock frequency component
present in the spectrum of the squared signal. This is then used to
synchronize the clocking circuit, the output of which clocks the sam-
pler in the detector branch.
The early-late gate circuit provides a method of recovering bit timing
which does not rely on a clocking component in the spectrum of the
received waveform. The circuit utilizes a feedback loop in which the
magnitude changes in the outputs from matched filters control the fre-
quency of a local clocking circuit (for an elementary description see, for
example, Roddy and Coolen, 1995). Detailed analyses of these and oth-
er methods will be found in Franks (1980) and Gagliardi (1991).
10.9
Problems
10.1.
For a test pattern consisting of alternating binary 1s and 0s, deter-
mine the frequency spectra in terms of the bit period Tb for the following sig-
nal formats: (a) unipolar; (b) polar NRZ; (c) polar RZ; (d) Manchester.
Digital Signals
279
Figure 10.21
Functional block diagram for bit-timing recovery.
Sampler
BPF
LPF
B
A
Demodulated
signal
Detector
output
Squarer
(  )2
Threshold
decision
circuit
Zero-
crossing
detector
and clock
circuit
TLFeBOOK

## Page 294
