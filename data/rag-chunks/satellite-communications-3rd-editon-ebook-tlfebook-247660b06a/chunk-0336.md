---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0336"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 336
confidence: "first-pass"
extraction_method: "structured-local"
---

channels in the INTELSAT terminology, and there can be up to 128 of
these in a traffic burst. Each satellite channel is further subdivided
into 16 time slots termed terrestrial channels, each terrestrial channel
carrying one PCM sample of an analog telephone signal. QPSK modu-
lation is used, and therefore, there are 2 bits per symbol as shown.
Thus each terrestrial channel carries 4 symbols (or 8 bits). Each satel-
lite channel carries 4  16  64 symbols, and at its maximum of 128
satellite channels, the traffic burst carries 8192 symbols.
As discussed in Sec. 10.3, the PCM sampling rate is 8 kHz, and with
8 bits per sample, the PCM bit rate is 64 kb/s. Each satellite channel can
accommodate this bit rate. Where input data at a higher rate must be
transmitted, multiple satellite channels are used. The maximum input
data rate which can be handled is 128(SC)  64 kb/s  8.192 Mb/s.
The INTELSAT frame is 120,832 symbols or 241,664 bits long. The
frame period is 2 ms, and therefore, the burst bit rate is 120.832 Mb/s.
As mentioned previously, preassigned and demand-assigned voice
channels can be accommodated together in the INTELSAT frame for-
mat. The demand-assigned channels utilize a technique known as dig-
ital speech interpolation (DSI), which is described in the next section.
The preassigned channels are referred to as digital noninterpolated
(DNI) channels.
14.7.9
Demand-assigned TDMA
With TDMA, the burst and subburst assignments are under software
control, compared with hardware control of the carrier frequency
assignments in FDMA. Consequently, compared with FDMA net-
works, TDMA networks have more flexibility in reassigning channels,
and the changes can be made more quickly and easily.
A number of methods are available for providing traffic flexibility
with TDMA. The burst length assigned to a station may be varied as
the traffic demand varies. A central control station may be employed
by the network to control the assignment of burst lengths to each par-
ticipating station. Alternatively, each station may determine its own
burst-length requirements and assign these in accordance with a pre-
arranged network discipline.
As an alternative to burst-length variation, the burst length may be
kept constant and the number of bursts per frame used by a given sta-
tion varied as demand requires. In one proposed system (CCIR Report
708, 1982), the frame length is fixed at 13.5 ms. The basic burst time
slot is 62.5 s, and stations in the network transmit information
bursts varying in discrete steps over the range 0.5 ms (8 basic bursts)
to 4.5 ms (72 basic bursts) per frame. Demand assignment for speech
channels takes advantage of the intermittent nature of speech, as
described in the next section.
402
Chapter Fourteen
TLFeBOOK
