---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0197"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 197
confidence: "first-pass"
extraction_method: "structured-local"
---

In normal operation, the operating point will always be above
threshold, the difference between the operating carrier-to-noise ratio
and the threshold level being referred to as the threshold margin. This
is also illustrated in Fig. 9.12.
Example 9.4
A 1-kHz test tone is used to produce a peak deviation of 5 kHz
in an FM system. Given that the received [C/N] is 30 dB, calculate the
receiver processing gain and the postdetector [S/N].
solution
Since the [C/N] is above threshold, Eq. (9.12) may be used. The
modulation index is ß  5 kHz/1 kHz  5. Hence
GP  3  52  (5  1)  450
and [GP]  26.5 dB. From Eq. (9.12),
[S/N]  30  26.5  56.5 dB
9.6.5
Preemphasis and deemphasis
As shown in Fig. 9.11, the noise voltage spectral density increases in
direct proportion to the demodulated noise frequency. As a result, the
signal-to-noise ratio is worse at the high-frequency end of the base-
band, a fact which is not apparent from the equation for signal-to-
noise ratio, which uses average values of signal and noise power. For
example, if a test tone is used to measure the signal-to-noise ratio in a
TV baseband channel, the result will depend on the position of the test
tone within the baseband, a better result being obtained at lower test
tone frequencies. For FDM/FM telephony, the telephone channels at
the low end of the FDM baseband would have better signal-to-noise
ratios than those at the high end.
To equalize the performance over the baseband, a deemphasis net-
work is introduced after the demodulator to attenuate the high-fre-
quency components of noise. Over most of the baseband, the
attenuation-frequency curve of the deemphasis network is the inverse
of the rising noise-frequency characteristic shown in Fig. 9.11 (for
practical reasons it is not feasible to have exact compensation over the
complete frequency range). Thus, after deemphasis, the noise-frequen-
cy characteristic is flat, as shown in Fig. 9.13d. Of course, the deem-
phasis network also will attenuate the signal, and to correct for this, a
complementary preemphasis characteristic is introduced prior to the
modulator at the transmitter. The overall effect is to leave the postde-
tection signal levels unchanged while the high-frequency noise is
attenuated. The preemphasis, deemphasis sequence is illustrated in
Fig. 9.13.
Analog Signals
241
TLFeBOOK

## Page 256
