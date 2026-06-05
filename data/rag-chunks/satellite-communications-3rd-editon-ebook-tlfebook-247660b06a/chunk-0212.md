---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0212"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 212
confidence: "first-pass"
extraction_method: "structured-local"
---

This process, referred to as quantization, obviously will introduce
some distortion (termed quantization noise) into the signal. In a prop-
erly designed system, the quantization noise is kept well within
acceptable limits. The quantization steps follow a nonlinear law, with
large signals being quantized into coarser steps than small signals.
This is termed compression, and it is introduced to keep the signal-to-
quantization noise ratio reasonably constant over the full dynamic
range of the input signal while maintaining the same number of bits
per codeword. At the receiver (the D/A block in Fig. 10.4), the binary
codewords are automatically decoded into the larger quantized steps
for the larger signals, this being termed expansion. The expansion law
is the inverse of the compression law, and the combined processing is
termed companding.
Figure 10.4b shows how the MC145500 codec achieves compression
by using a chorded approximation. The leading bit of the digital code-
word is a sign bit, being 1 for positive and 0 for negative samples of the
analog signal. The next three bits are used to encode the chord in which
the analog signal falls, the three bits giving a total of eight chords. Each
chord is made to cover the same number of input steps, but the step size
increases from chord to chord. The chord bits are followed by four bits
indicating the step in which the analog value lies. The normalized deci-
sion levels shown in Fig. 10.4b are the analog levels at which the com-
parator circuits change from one chord to the next and from one step to
the next. These are normalized to a value 8159 for convenience in pre-
sentation. For example, the maximum value may be considered to be
8159 mV, and then the smallest step would be 1 mV. The first step is
shown as 1 (mV), but it should be kept in mind that the first quantized
level spans the analog zero so that 0 must be distinguished from 0.
Thus the level representing zero has in fact a step size of ±1 mV.
As an example, suppose the sampled analog signal has a value 500
mV. This falls within the normalized range 479 to 511 mV, and there-
fore, the binary code is 10111111. It should be mentioned that normal-
ly the first step in a chord would be encoded 0000, but the bits are
inverted, as noted in Fig. 10.4b. This is so because low values are more
likely than high values, and inversion increases the 1-bit density,
which helps in maintaining synchronization.
The table in Fig. 10.4b shows mu-law encode-decode characteristics.
The term mu law, usually written as  law, originated with older ana-
log compressors, where  was a parameter in the equation describing
the compression characteristic. The -law characteristic is standard in
North America and Japan, while in Europe and many other parts of the
world a similar law known as the A law is in use. Figure 10.5 shows the
curves for   255 and A  87.6, which are the standard values in use.
These are shown as smooth curves, which could be approached with the
258
Chapter Ten
TLFeBOOK
