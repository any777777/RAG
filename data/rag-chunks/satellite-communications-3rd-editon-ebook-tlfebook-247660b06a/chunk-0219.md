---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0219"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 219
confidence: "first-pass"
extraction_method: "structured-local"
---

When the binary signal is 1, the carrier sinusoid is unchanged, and
when it is 1, the carrier sinusoid is changed in phase by 180°. Binary
phase-shift keying is also known as phase-reversal keying (PRK). The
binary signal may be filtered at baseband before modulation, to limit
the sidebands produced, and as part of the filtering needed for the
reduction of ISI, as described in Sec. 10.5. The resulting modulated
waveform is sketched in Fig. 10.11.
Differential phase-shift keying (DPSK).
This is phase-shift keying in
which the phase of the carrier is changed only if the current bit differs
from the previous one. A reference bit must be sent at the start of mes-
sage, but otherwise the method has the advantage of not requiring a
reference carrier at the receiver for demodulation.
Quadrature phase-shift keying (QPSK).
This is phase-shift keying for a
4-symbol waveform, adjacent phase shifts being equispaced by 90°.
The concept can be extended to more than four levels, when it is denot-
ed as MPSK for M-ary phase-shift keying.
Quadrature amplitude modulation (QAM).
This is also a multilevel
(meaning higher than binary) modulation method in which the ampli-
tude and the phase of the carrier are modulated.
Although all the methods mentioned find specific applications in
practice, only BPSK and QPSK will be described here, since many of
the general properties can be illustrated through these methods, and
they are widely used.
10.6.1
Binary phase-shift keying
Binary phase-shift keying may be achieved by using the binary polar
NRZ signal to multiply the carrier, as shown in Fig. 10.12a. For a bina-
ry signal p(t), the modulated wave may be written as
e (t)  p (t) cos 
0t
(10.14)
When p(t)   1, e(t)  cos 
0t, and when p(t)  1, e(t)  cos 
0t,
which is equivalent to cos (
0t ± 180°). Bandpass filtering (BPF) of the
modulated wave may be used instead of baseband filtering to limit the
radiated spectrum. The bandpass filter also may incorporate the
square root of the raised-cosine rolloff, described in Sec. 10.5, required
to reduce ISI (see, for example, Pratt and Bostian, 1986).
At the receiver (Fig. 10.12b), the received modulated carrier will
undergo further bandpass filtering to complete the raised-cosine
response and to limit input noise. The filtered modulated wave, e′(t) 
266
Chapter Ten
TLFeBOOK

## Page 281
