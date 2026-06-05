---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0402"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 402
confidence: "first-pass"
extraction_method: "structured-local"
---

The Y, C, and Cb signals are sampled in the digitizer shown in Fig.
16.3. It is an observed fact that the human eye is less sensitive to reso-
lution in the color components (Cr and Cb) than the luminance (Y) com-
ponent. This allows a lower sampling rate to be used for the color
components. This is referred to as chroma subsampling, and it repre-
sents one step in the compression process. For example, in the CCIR-
601-1 standard, sampling along the horizontal axis for the color
components is less by a factor 2 compared with the luminance sampling.
This is written as 4:2:2 sampling.
Following the digitizer, difference signals are formed, and the discrete
cosine transform (DCT) block converts these to a “spatial frequency”
domain. The familiar Fourier transform transforms a time signal g(t) to
a frequency domain representation G(f), allowing the signal to be filtered
in the frequency domain. Here, the variables are time t and frequency f.
In the DCT situation, the input signals are functions of the x (horizon-
tal) and y (vertical) space coordinates, g(x, y). The DCT transforms these
into a domain of new variables u and v, G(u, v). The variables are called
spatial frequencies in analogy with the time-frequency transform. It
should be noted that g(x, y) and G(u, v) are discrete functions. In the
Direct Broadcast Satellite Services
467
Digitizer
Discrete cosine
transform
(DCT)
Quantizer
Variable-
length
coding
Inverse
quantizer
Inverse
DCT
Motion
estimator
Motion
compensator
(frame delay)
Rate
controller
Buffer
Y
Cr
Cb
Sync
Elementary
stream
–
+
Motion
vectors
Reconstructed
image
Predicted
Image
Predicted
Image
Difference
image
Figure 16.3
MPEG-2 encoder paths. (From Bhatt et al., 1997. IEEE.)
TLFeBOOK

## Page 478
