---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0214"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 214
confidence: "first-pass"
extraction_method: "structured-local"
---

The frequency spectrum occupied by a digital signal is proportion-
al to the bit rate, and in order to conserve bandwidth, it may be nec-
essary to reduce the bit rate. For example, if 7-bit codewords were to
be used, the bit rate would be 56 kb/s. Various data reduction
schemes are in use which give much greater reductions, and some of
these can achieve bit rates as low as 2400 b/s (Hassanein et al., 1989
and 1992).
10.4
Time-Division Multiplexing
A number of signals in binary digital form can be transmitted through
a common channel by interleaving the pulses in time, this being
referred to as time-division multiplexing (TDM). For speech signals, a
separate codec may be used for each voice channel, the outputs from
these being combined to form a TDM baseband signal, as shown in Fig.
10.6. At the baseband level in the receiver, the TDM signal is demulti-
plexed, the PCM signals being routed to separate codecs for decoding.
In satellite systems, the TDM waveform is used to modulate the carri-
er wave, as described later.
The time-division multiplexed signal format is best described with
reference to the widely used Bell T1 system. The signal format is illus-
trated in Fig. 10.7a. Each PCM word contains 8 bits, and a frame con-
tains 24 PCM channels. In addition, a periodic frame synchronizing
signal must be transmitted, and this is achieved by inserting a bit from
the frame synchronizing codeword at the beginning of every frame. At
the receiver, a special detector termed a correlator is used to detect the
frame synchronizing codeword in the bit stream, which enables the
260
Chapter Ten
CODEC
1
CODEC
1
TDM
D
E
M
U
L
T
I
P
L
E
X
E
R
CODEC
1
CODEC
1
Analog
inputs
Analog
outputs
CODEC
1
CODEC
1
•
•
•
Figure 10.6
A basic TDM system.
TLFeBOOK

## Page 275
