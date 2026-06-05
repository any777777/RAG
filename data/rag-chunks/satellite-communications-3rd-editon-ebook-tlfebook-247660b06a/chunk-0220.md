---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0220"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 220
confidence: "first-pass"
extraction_method: "structured-local"
---

p′(t) cos 
0t, is passed into another multiplier circuit, where it is multi-
plied by a replica of the carrier wave cos 
0t. The output from the mul-
tiplier is therefore equal to p′(t) cos2
0t. This can be expanded as p′(t)(0.5
 0.5 cos 2
0t). The low-pass filter is used to remove the second har-
monic component of the carrier, leaving the low-frequency output, which
is 0.5p′(t), where p′(t) is the filtered version of the input binary wave p(t).
It will be seen that the modulator is basically the same as that used to
produce the DSBSC signal described in Sec. 9.3. In the present instance,
the bandpass filter following the modulator is used to select the com-
plete DSBSC signal rather than a single sideband.
The receiver is shown in more detail in Fig. 10.13. As shown, a local-
ly generated version of the unmodulated carrier wave is required as
one of the inputs to the multiplier. The locally generated carrier has to
be exactly in phase with the incoming carrier, and hence this type of
detection is termed coherent detection. Coherent detection necessitates
recovering the unmodulated carrier phase information from the incom-
ing modulated wave, and this is achieved in the carrier recovery (CR)
section shown in Fig. 10.13.
As discussed in Sec. 10.5, to avoid ISI, sampling must be carried out at
the bit rate and at the peaks of the output pulses. This requires the sam-
ple-and-hold circuit to be accurately synchronized to the bit rate, which
necessitates a bit timing recovery (BTR) section, as shown in Fig. 10.13.
Thermal noise at the receiver will result in noise phase modulation
of the carrier, and so the demodulated waveform p′(t) will be accompa-
nied by noise. The noisy p′(t) signal is passed into the threshold detec-
tor which regenerates a noise-free output but one containing some bit
errors as a result of the noise already present on the waveform.
Digital Signals
267
Figure 10.12
(a) BPSK modulator; (b) coherent detection of a BPSK signal.
TLFeBOOK

## Page 282
