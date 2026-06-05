---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0189"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 189
confidence: "first-pass"
extraction_method: "structured-local"
---

take place through optical image processing or by conversion of the elec-
tronic signal format. The latter can be further subdivided into analog
and digital techniques. The digital converter, referred to as digital inter-
continental conversion equipment (DICE), is favored because of its good
performance and lower cost (see Miya, 1981).
9.6
Frequency Modulation
The analog signals discussed in the previous sections are transferred
to the microwave carrier by means of frequency modulation (FM).
Instead of being done in one step, as shown in Fig. 9.8b, this modula-
tion usually takes place at an intermediate frequency, as shown in Fig.
8.6. This signal is then frequency multiplied up to the required uplink
microwave frequency. In the receive branch of Fig. 8.6, the incoming
(downlink) FM microwave signal is downconverted to an intermediate
frequency, and the “baseband” signal is recovered from the IF carrier
in the demodulator. The actual baseband video signal is now available
directly via a low-pass filter, but the audio channels must each under-
go an additional step of FM demodulation to recover the baseband
audio signals.
A major advantage associated with frequency modulation is the
improvement in the postdetection signal-to-noise ratio at the receiver
output compared with other analog modulation methods. This
improvement can be attributed to three factors: (1) amplitude limiting,
(2) a property of FM which allows an exchange between signal-to-noise
ratio and bandwidth, and (3) a noise reduction inherent in the way
noise phase modulates a carrier. These factors are discussed in more
detail in the following sections.
Figure 9.9 shows the basic circuit blocks of an FM receiver. The
receiver noise, including that from the antenna, can be lumped into
one equivalent noise source at the receiver input, as described in Sec.
12.5. It is emphasized at this point that thermal-like noise only is
being considered, the main characteristic of which is that the spectral
density of the noise power is constant, as given by Eq. (12.15). This is
referred to as a flat spectrum. (This type of noise is also referred to as
white noise in analogy to white light, which contains a uniform spec-
trum of colors.) Both the signal spectrum and the noise spectrum are
Analog Signals
233
Figure 9.9
Elements of an FM receiver. Figures shown in parentheses are typical.
TLFeBOOK

## Page 248
