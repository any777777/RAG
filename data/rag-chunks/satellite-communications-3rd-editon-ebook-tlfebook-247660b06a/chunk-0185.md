---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0185"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 185
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 241

Figure 9.4
Examples of baseband signals for FDM telephony: (a) 24 channels; (b) 60 chan-
nels; (c) 252 channels.
227
TLFeBOOK

## Page 242

In transmitting the chrominance information, use is made of the fact
that the eye cannot resolve colors to the extent that it can intensity
detail; this allows the chrominance signal bandwidth to be less than
that of the luminance signal. The I and Q chrominance signals are
transmitted within the luminance bandwidth by quadrature DSBSC
(see below), modulating them onto a subcarrier which places them at
the upper end of the luminance signal spectrum. Use is made of the
fact that the eye cannot readily perceive the interference which results
when the chrominance signals are transmitted within the luminance-
signal bandwidth. The baseband response is shown in Fig. 9.5.
Different methods of chrominance subcarrier modulation are
employed in different countries. In France, a system known as sequen-
tial couleur a mémoire (SECAM) is used. In most other European
countries, a system known as phase alternation line (PAL) is used. In
North America, the NTSC system is used, where NTSC stands for
National Television System Committee.
In the NTSC system, each chrominance signal is modulated onto its
subcarrier using DSBSC modulation, as described in Sec. 9.3. A single
oscillator source is used so that the I and Q signal subcarriers have the
same frequency, but one of the subcarriers is shifted 90° in phase to
preserve the separate chrominance information in the I and Q base-
band signals. This method is known as quadrature modulation (QM).
The I signal is the chrominance signal which modulates the in-phase
carrier. Its bandwidth in the NTSC system is restricted to 1.5 MHz,
and after modulation onto the subcarrier, a single-sideband filter
removes the upper sideband components more than 0.5 MHz above the
carrier. This is referred to as a vestigial sideband (VSB). The modu-
lated I signal therefore consists of the 1.5-MHz lower sideband plus
the 0.5 MHz upper VSB.
The Q signal is the chrominance signal which modulates the quad-
rature carrier. Its bandwidth is restricted to 0.5 MHz, and after mod-
ulation, a DSBSC signal results. The spectrum magnitude of the
combined I and Q signals is shown in Fig. 9.5.
228
Chapter Nine
Figure 9.5
Frequency spectra for the luminance and chromi-
nance signals.
TLFeBOOK

## Page 243
