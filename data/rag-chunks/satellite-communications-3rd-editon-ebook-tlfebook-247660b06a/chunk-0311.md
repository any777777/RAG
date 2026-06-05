---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0311"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 311
confidence: "first-pass"
extraction_method: "structured-local"
---

Figure 14.5 shows the INTELSAT SCPC channeling scheme for a
36-MHz transponder. The transponder bandwidth is subdivided into
800 channels each 45 kHz wide. The 45 kHz, which includes a guard-
band, is required for each digitized voice channel, which utilizes QPSK
modulation. The channel information signal may be digital data or
PCM voice signals (see Chap. 10). A pilot frequency is transmitted for
the purpose of frequency control, and the adjacent channel slots on
either side of the pilot are left vacant to avoid interference. The
scheme therefore provides a total of 798 one-way channels or up to 399
full-duplex voice circuits. In duplex operation, the frequency pairs are
separated by 18.045 MHz, as shown in Fig. 14.5.
The frequency tolerance relative to the assigned values is within 
±1 kHz for the received SCPC carrier and must be within ±250 Hz for
the transmitted SCPC carrier (Miya, 1981). The pilot frequency is trans-
mitted by one of the earth stations designated as a primary station. This
provides a reference for automatic frequency control (AFC) (usually
through the use of phase-locked loops) of the transmitter frequency syn-
thesizers and receiver local oscillators. In the event of failure of the pri-
mary station, the pilot frequency is transmitted from a designated
backup station.
An important feature of the INTELSAT SCPC system is that each
channel is voice-activated. This means that on a two-way telephone
conversation, only one carrier is operative at any one time. Also, in
long pauses between speech, the carriers are switched off. It has been
estimated that for telephone calls, the one-way utilization time is 40
percent of the call duration. Using voice activation, the average num-
ber of carriers being amplified at any one time by the transponder
traveling-wave tube (TWT) is reduced. For a given level of intermodu-
lation distortion (see Secs. 7.7.3 and 12.10), the TWT power output per
FDMA carrier therefore can be increased.
374
Chapter Fourteen
Figure 14.5
Channeling arrangement for Intelsat SCPC system.
TLFeBOOK

## Page 385
