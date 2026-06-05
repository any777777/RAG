---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0357"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 357
confidence: "first-pass"
extraction_method: "structured-local"
---

Once the threshold has been reached or exceeded, the system switch-
es from acquisition mode to tracking mode.
One form of tracking circuit, the delay lock loop, is shown in Fig.
14.37. Here, two correlators are used, but the local signal to one is
advanced by half a chip period relative to the desired code waveform,
and the other is delayed by the same amount. The outputs from the
correlators are subtracted, and this difference signal provides the con-
trol voltage for the voltage-controlled oscillator (VCO) that drives the
shift register clock. With the control voltage at the zero crossover
point, the locally generated code signal is in phase with the received
code signal. Any tendency to drift out of phase changes the VCO in
such a way as to bring the control voltage back to the zero crossover
point, thus maintaining synchronism.
The acquisition and tracking circuits also will attempt to correlate
the stored version of c(t) at the receiver with all the other waveforms
being received. Such correlations are termed cross-correlations. It is
essential that the cross-correlation function not show a similar peak as
426
Chapter Fourteen
X
X
+
c(t-!-      )
Tch
2
c(t-!-      )
Tch
2
BPF
Envelope
detector
Envelope
detector
+
–
e(!)
e(!)
Loop
filter
Clock
P.N.
generator
RPF
+
–
+
0
–
!
(a)
(b)
Figure 14.37
(a) The delay lock loop; (b) the waveform at the adder.
TLFeBOOK

## Page 437
