---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0323"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 323
confidence: "first-pass"
extraction_method: "structured-local"
---

Carrier and bit-timing recovery (CBR). To perform coherent demod-
ulation of the phase-modulated carrier as described in Secs. 10.7 and
10.8, a coherent carrier signal must first be recovered from the
burst. An unmodulated carrier wave is provided during the first part
of the CBR time slot. This is used as a synchronizing signal for a
local oscillator at the detector, which then produces an output coher-
ent with the carrier wave. The carrier in the subsequent part of the
CBR time slot is modulated by a known phase-change sequence
which enables the bit timing to be recovered. Accurate bit timing is
needed for the operation of the sample-and-hold function in the
detector circuit (see Figs. 10.13 and 10.23). Carrier recovery is
described in more detail in Sec. 14.7.3.
Burst code word (BCW). (Also known as a unique word.) This is a
binary word, a copy of which is stored at each earth station. By com-
paring the incoming bits in a burst with the stored version of the
BCW, the receiver can detect when a group of received bits matches
the BCW, and this in turn provides an accurate time reference for
the burst position in the frame. A known bit sequence is also carried
in the BCW, which enables the phase ambiguity associated with
coherent detection to be resolved.
Station identification code (SIC). This identifies the transmitting
station.
Figure 14.14 shows the makeup of the reference bursts used in cer-
tain of the INTELSAT networks. The numbers of symbols and the cor-
responding time intervals allocated to the various functions are
shown. In addition to the channels already described, a coordination
and delay channel (sometimes referred to as the control and delay
channel) is provided. This channel carries the identification number of
the earth station being addressed and various codes used in connection
with the acquisition and synchronization of bursts at the addressed
earth station. It is also necessary for an earth station to know the
propagation time delay to the satellite to implement burst acquisition
and synchronization. In the INTELSAT system, the propagation delay
is computed from measurements made at the reference station and
transmitted to the earth station in question through the coordination
and delay channel.
The other channels in the INTELSAT reference burst are the fol-
lowing:
TTY: telegraph order-wire channel, used to provide telegraph com-
munications between earth stations.
SC: service channel which carries various network protocol and
alarm messages.
388
Chapter Fourteen
TLFeBOOK
