---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0215"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 215
confidence: "first-pass"
extraction_method: "structured-local"
---

frame timing to be established. The total number of bits in a frame is
therefore 24  8  1  193. Now, as established earlier, the sampling
frequency for voice is 8 kHz, and so the interval between PCM words
for a given channel is 1/8000  125 s. For example, the leading bit in
the PCM codewords for a given channel must be separated in time by
no more than 125 s. As can be seen from Fig. 10.7a, this is also the
frame period, and therefore, the bit rate for the T1 system is
Rb 
 1.544 Mb/s
(10.7)
Signaling information is also carried as part of the digital stream.
By signaling is meant such data as number dialed, busy signals, and
billing information. Signaling can take place at a lower bit rate, and in
the T1 system, the eighth bit for every channel, in every sixth frame,
is replaced by a signaling bit. This is illustrated in Fig. 10.7b. The time
separation between signaling bits is 6  125 s  750 s, and the sig-
naling bit rate is therefore 1/750 s  1.333 kb/s.
10.5
Bandwidth Requirements
In a satellite transmission system, the baseband signal is modulated
onto a carrier for transmission. Filtering of the signals takes place at
a number of stages. The baseband signal itself is band-limited by fil-
193

125 s
Digital Signals
261
Figure 10.7
Bell T1 PCM format.
TLFeBOOK

## Page 276
