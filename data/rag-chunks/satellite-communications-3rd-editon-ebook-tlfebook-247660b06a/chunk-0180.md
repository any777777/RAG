---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0180"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 180
confidence: "first-pass"
extraction_method: "structured-local"
---

speech baseband. In practice, some variations occur in the basebands
used by different telephone companies. The telephone channel is often
referred to as a voice frequency (VF) channel, and in this book this will
be taken to mean the frequency range of 300 to 3400 Hz.
There are good reasons for limiting the frequency range. Noise,
which covers a very wide frequency spectrum, is reduced by reducing
the bandwidth. Also, reducing the bandwidth allows more telephone
channels to be carried over a given type of circuit, as will be described
in Sec. 9.4.
The signal levels encountered within telephone networks vary con-
siderably. Audio signal levels are often measured in volume units (VU).
For a sinusoidal signal within the voice frequency range, 0 VU corre-
sponds to 1 mW of power, or 0 dBm. No simple relationship exists
between volume units and power for speech signals, but as a rough
guide, the power level in dBm of normal speech is given by 1.4 VU.
As a rule of thumb, the average voice level on a telephone circuit (or
mean talker level) is defined as 13 VU (see Freeman, 1981).
9.3
Single-Sideband Telephony
Figure 9.1a shows how the VF baseband may be represented in the
frequency domain. In some cases, the triangular representation has
the small end of the triangle at 0 Hz, even though frequency compo-
nents below 300 Hz actually may not be present. Also, in some cases,
the upper end is set at 4 kHz to indicate allowance for a guard band,
the need for which will be described later.
When the telephone signal is multiplied in the time domain with a
sinusoidal carrier of frequency fc, a new spectrum results, in which the
original baseband appears on either side of the carrier frequency. This
is illustrated in Fig. 9.1b for a carrier of 20 kHz, where the band of fre-
quencies below the carrier is referred to as the lower sideband and the
band above the carrier as the upper sideband. To avoid distortion
which would occur with sideband overlap, the carrier frequency must
be greater than the highest frequency in the baseband.
The result of this multiplication process is referred to as double-side-
band suppressed-carrier (DSBSC) modulation, since only the side-
bands, and not the carrier, appear in the spectrum. Now, all the
information in the original telephone signal is contained in either of
the two sidebands, and therefore, it is necessary to transmit only one
of these. A filter may be used to select either one and reject the other.
The resulting output is termed a single-sideband (SSB) signal.
The SSB process utilizing the lower sideband is illustrated in Fig.
9.2, where a 20-kHz carrier is used as an example. It will be seen that
for the lower sideband, the frequencies have been inverted, the 
222
Chapter Nine
TLFeBOOK
