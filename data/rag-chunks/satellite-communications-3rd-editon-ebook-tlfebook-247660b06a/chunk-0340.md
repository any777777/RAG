---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0340"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 340
confidence: "first-pass"
extraction_method: "structured-local"
---

stated above. Typically, DSI gains somewhat greater than 2 can be
achieved in practice.
Speech predictive encoded communications (SPEC).
The block diagram
for the SPEC system is shown in Fig. 14.23 (Sciulli and Campanella,
1973). In this method, the incoming speech signals are converted to a
PCM multiplexed signal using 8 bits per sample quantization. With 64
input lines and sampling at 125 s, the output bit rate from the mul-
tiplexer is 8  64/125  4.096 Mb/s.
The digital voice switch following the PCM multiplexer is timeshared
between the input signals. It is voice-activated to prevent transmission
of noise during silent intervals. When the zero-order predictor receives
a new sample, it compares it with the previous sample for that voice
channel, which it has stored, and transmits the new sample only if it dif-
fers from the preceding one by a predetermined amount. These new
samples are labeled unpredictable PCM samples in Fig. 14.23a.
For the 64 channels a 64-bit assignment word is also sent. A logic 1
in the channel for the assignment word means that a new sample was
sent for that channel, and a logic 0 means that the sample was
unchanged. At the receiver, the sample assignment word either directs
the new (unpredictable) sample into the correct channel slot, or it
results in the previous sample being regenerated in the reconstruction
decoder. The output from this is a 4.096-Mb/s PCM multiplexed signal
which is demultiplexed in the PCM decoder.
406
Chapter Fourteen
Figure 14.23
(a) SPEC transmitter, (b) SPEC receiver. (From Sciulli and Campanella,
1973. © 1973—IEEE.)
TLFeBOOK

## Page 417
