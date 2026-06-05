---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0321"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 321
confidence: "first-pass"
extraction_method: "structured-local"
---

TF before receiving the first transmitted burst. In a geostationary
satellite system, the actual propagation delay is a significant fraction
of a second, and excessive delays from other causes must be avoided.
This sets an upper limit to the frame time, although with current tech-
nology other factors restrict the frame time to well below this limit.
The frame period is usually chosen to be a multiple of 125 s, which is
the standard sampling period used in pulse-code modulation (PCM)
telephony systems, since this ensures that the PCM samples can be
distributed across successive frames at the PCM sampling rate.
Figure 14.12 shows some of the basic units in a TDMA ground station,
which for discussion purposes is labeled earth station A. Terrestrial
links coming into earth station A carry digital traffic addressed to des-
tination stations, labeled B, C, X. It is assumed that the bit rate is the
same for the digital traffic on each terrestrial link. In the units labeled
terrestrial interface modules (TIMs), the incoming continuous-bit-rate
signals are converted into the intermittent-burst-rate mode. These indi-
vidual burst-mode signals are time-division multiplexed in the time-
division multiplexer (MUX) so that the traffic for each destination
station appears in its assigned time slot within a burst.
Certain time slots at the beginning of each burst are used to carry
timing and synchronizing information. These time slots collectively
are referred to as the preamble. The complete burst containing the pre-
amble and the traffic data is used to phase modulate the radiofre-
quency (rf) carrier. Thus the composite burst which is transmitted at
rf consists of a number of time slots, as shown in Fig. 14.13. These will
be described in more detail shortly.
The received signal at an earth station consists of bursts from all
transmitting stations arranged in the frame format shown in Fig.
14.13. The rf carrier is converted to intermediate frequency (IF), which
is then demodulated. A separate preamble detector provides timing
information for transmitter and receiver along with a carrier synchro-
nizing signal for the phase demodulator, as described in the next sec-
tion. In many systems, a station receives its own transmission along
with the others in the frame, which can then be used for burst-timing
purposes.
A reference burst is required at the beginning of each frame to provide
timing information for the acquisition and synchronization of bursts
(these functions are described further in Sec. 14.7.4). In the INTELSAT
international network, at least two reference stations are used, one in
the East and one in the West. These are designated primary reference
stations, one of which is further selected as the master primary. Each
primary station is duplicated by a secondary reference station, making
four reference stations in all. The fact that all the reference stations are
identical means that any one can become the master primary. All the
Satellite Access
385
TLFeBOOK
