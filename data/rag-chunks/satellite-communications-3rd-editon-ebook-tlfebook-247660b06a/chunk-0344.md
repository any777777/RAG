---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0344"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 344
confidence: "first-pass"
extraction_method: "structured-local"
---

For small satellite business systems it is desirable to be able to oper-
ate with relatively small earth stations, which suggests that FDMA
should be the mode of operation. On the other hand, TDMA permits
more efficient use of the satellite transponder by eliminating the need
for backoff. This suggests that it might be worthwhile to operate a
hybrid system in which FDMA is the uplink mode of operation, with
the individual signals converted to a time-division-multiplexed format
in the transponder before being amplified by the TWTA. This would
allow the transponder to be operated at saturation as in TDMA. Such
a hybrid mode of operation would require the use of a signal-process-
ing transponder as discussed in the next section.
14.8
On-Board Signal Processing for
FDMA/TDM Operation
As seen in the preceding section, for small earth stations carrying dig-
ital signals at relatively low data rates, there is an advantage to be
gained in terms of earth station power requirements by using FDMA.
On the other hand, TDMA signals make more efficient use of the
transponder because back-off is not required.
Market studies show that what is termed customer premises services
(CPS) will make up a significant portion of the satellite demand over
the decade 1990–2000 (Stevenson et al., 1984). Multiplexed digital
transmission will be used, most likely at the T1 rate. This bit rate pro-
vides for most of the popular services, such as voice, data, and video-
conferencing, but specifically excludes standard television signals.
Customer premises services is an ideal candidate for the FDMA/TDM
mode of operation mentioned in the preceding section. To operate in
this mode requires the use of signal-processing transponders, in which
the FDMA uplink signals are converted to the TDM format for retrans-
mission on the downlink. It also should be noted that the use of signal-
processing transponders “decouples” the uplink from the downlink.
This is important because it allows the performance of each link to be
optimized independently of the other.
A number of signal-processing methods have been proposed. One
conventional approach is illustrated in the simplified block schematic
of Fig. 14.25a. Here the individual uplink carriers at the satellite are
selected by frequency filters and detected in the normal manner. The
baseband signals are then combined in the baseband processor, where
they are converted to a time-division-multiplexed format for remodu-
lation onto a downlink carrier. More than one downlink carrier may be
provided, but only one is shown for simplicity. The disadvantages of
the conventional approach are those of excessive size, weight, and
Satellite Access
411
TLFeBOOK
