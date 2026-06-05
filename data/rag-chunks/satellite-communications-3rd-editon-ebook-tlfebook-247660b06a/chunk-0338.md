---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0338"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 338
confidence: "first-pass"
extraction_method: "structured-local"
---

DSI, for digital speech interpolation. These are shown by the block
labeled “interpolated” in Fig. 14.21. The first satellite channel (chan-
nel 0) in this block is an assignment channel, labeled DSI-AC. No traf-
fic is carried in the assignment channel; it is used to transmit channel
assignment information as will be described shortly.
Figure 14.22 shows in outline the DSI system. Basically, the system
allows N terrestrial channels to be carried by M satellite channels,
where N  M. For example, in the INTELSAT arrangement, N  240
and M  127.
On each incoming terrestrial channel, a speech detector senses
when speech is present, the intermittent speech signals being referred
to as speech spurts. A speech spurt lasts on average about 1.5 seconds
(Miya, 1981). A control signal from the speech detector is sent to the
channel assignment unit, which searches for an empty TDMA buffer.
Assuming that one is found, the terrestrial channel is assigned to this
satellite channel, and the speech spurt is stored in the buffer, ready for
transmission in the DSI subburst. A delay is inserted in the speech cir-
cuit, as shown in Fig. 14.22, to allow some time for the assignment
process to be completed. However, this delay cannot exactly compen-
sate for the assignment delay, and the initial part of the speech spurt
may be lost. This is termed a connect clip.
In the INTELSAT system an intermediate step occurs where the ter-
restrial channels are renamed international channels before being
assigned to a satellite channel (Pratt and Bostian, 1986). For clarity,
this step is not shown in Fig. 14.22.
At the same time as an assignment is made, an assignment message
is stored in the assignment channel buffer, which informs the receive
stations which terrestrial channel is assigned to which satellite chan-
nel. Once an assignment is made, it is not interrupted, even during
pauses between spurts, unless the pause times are required for anoth-
er DSI channel. This reduces the amount of information needed to be
transmitted over the assignment channel.
At the receive side, the traffic messages are stored in their respec-
tive satellite-channel buffers. The assignment information ensures
that the correct buffer is read out to the corresponding terrestrial
channel during its sampling time slot. During speech pauses when the
channel has been reassigned, a low-level noise signal is introduced at
the receiver to simulate a continuous connection.
It has been assumed that a free satellite channel will be found for
any incoming speech spurt, but of course there is a finite probability
that all channels will be occupied and the speech spurt lost. Losing a
speech spurt in this manner is referred to as freeze-out, and the freeze-
out fraction is the ratio of the time the speech is lost to the average
spurt duration. It is found that a design objective of 0.5 percent for a
404
Chapter Fourteen
TLFeBOOK
