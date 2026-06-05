---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0216"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 216
confidence: "first-pass"
extraction_method: "structured-local"
---

tering to prevent the generation of excessive sidebands in the modula-
tion process. The modulated signal undergoes bandpass filtering as
part of the amplification process in the transmitter.
Where transmission lines form the channel, the frequency response
of the lines also must be taken into account. With a satellite link, the
main channel is the radiofrequency path, which has little effect on the
frequency spectrum but does introduce a propagation delay which
must be taken into account.
At the receive end, bandpass filtering of the incoming signal is nec-
essary to limit the noise which is introduced at this stage. Thus the
signal passes through a number of filtering stages, and the effect of
these on the digital waveform must be taken into account.
The spectrum of the output pulse at the receiver is determined by
the spectrum of the input pulse Vi(f), the transmit filter response HT(f),
the channel frequency response HCH(f), and the receiver filter response
HR(f). These are shown in Fig. 10.8. Thus
V (f)  Vi (f) HT (f) HCH (f) HR (f)
(10.8)
Inductive and capacitive elements are an inherent part of the filter-
ing process. These do not dissipate power, but energy is periodically
cycled between the magnetic and electric fields and the signal. The
time required for this energy exchange results in part of the signal
being delayed so that a square pulse entering at the transmitting end
may exhibit “ringing” as it exits at the receiving end. This is illustrat-
ed in Fig. 10.9a.
Because the information is digitally encoded in the waveform, the
distortion apparent in the pulse shape is not important as long as the
receiver can distinguish the binary 1 pulse from the binary 0 pulse.
This requires the waveform to be sampled at the correct instants in
order to determine its polarity. With a continuous waveform, the “tails”
which result from the “ringing” of all the preceding pulses can combine
to interfere with the particular pulse being sampled. This is known as
intersymbol interference (ISI), and it can be severe enough to produce
an error in the detected signal polarity.
The ringing cannot be removed, but the pulses can be shaped such
that the sampling of a given pulse occurs when the tails are at zero
crossover points. This is illustrated in Fig. 10.9b, where two tails are
shown overlapping the pulse being sampled. In practice, perfect pulse
262
Chapter Ten
HT(f)
HCH(f)
HR(f)
V(f)
Vi(f)
Figure 10.8
Frequency spectrum components of
Eq. (10.8).
TLFeBOOK
