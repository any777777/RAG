---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0210"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 210
confidence: "first-pass"
extraction_method: "structured-local"
---

The symbol period is therefore
Tsym  Tbm
(10.4)
and the symbol rate in terms of bit rate is
Rsym 
(10.5)
For satellite transmission, the encoded message must be modulated
onto the microwave carrier. Before examining the modulation process,
we describe the way in which speech signals are converted to a digital
format through pulse code modulation.
10.3
Pulse Code Modulation
In the previous section describing baseband digital signals, the infor-
mation was assumed to be encoded in one of the digital waveforms
shown in Figs. 10.2 and 10.3. Speech and video appear naturally as
analog signals, and these must be converted to digital form for trans-
mission over a digital link. In Fig. 10.1 the speech and video analog
signals are shown converted to digital form through the use of analog-
to-digital converters. The particular form of A/D conversion used is
known as pulse-code modulation (PCM). Commercially available inte-
grated circuits known as PCM codecs (for coder-decoder) are used to
implement PCM. Figure 10.4a shows a block schematic for the
Motorola MC145500 series of codecs suitable for speech signals. The
analog signal enters at the Tx terminals and passes through a low-
pass filter, followed by a high-pass filter to remove any 50/60-Hz inter-
ference which may appear on the line. The low-pass filter has a cutoff
frequency of about 4 kHz, which allows for the filter rolloff above the
audio limit of 3400 Hz. As shown in connection with single-sideband
systems, a voice channel bandwidth extending from 300 to 3400 Hz is
considered satisfactory for speech. Band limiting the audio signal in
this way reduces noise. It has another important consequence associ-
ated with the analog-to-digital conversion process. The analog signal
is digitized by taking samples at periodic intervals. A theorem, known
as the sampling theorem, states in part that the sampling frequency
must be at least twice the highest frequency in the spectrum of the sig-
nal being sampled. With the upper cutoff frequency of the audio filter
at 4 kHz, the sampling frequency can be standardized at 8 kHz.
The sampled voltage levels are encoded as binary digital numbers in
the A/D converter following the high-pass filter. The binary number
which is transmitted actually represents a range of voltages, and all
samples which fall within this range are encoded as the same number.
Rb

m
256
Chapter Ten
TLFeBOOK

## Page 271
