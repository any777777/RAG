---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0175"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 175
confidence: "first-pass"
extraction_method: "structured-local"
---

redundancy means that certain units are duplicated. A duplicate, or
redundant, unit is automatically switched into a circuit to replace a
corresponding unit that has failed. Redundant units are shown by
dashed lines in Fig. 8.5.
The block diagram is shown in more detail in Fig. 8.6, where, for
clarity, redundant units are not shown. Starting at the bottom of the
diagram, the first block shows the interconnection equipment required
between satellite station and the terrestrial network. For the purpose
of explanation, telephone traffic will be assumed. This may consist of
a number of telephone channels in a multiplexed format. Multiplexing
is a method of grouping telephone channels together, usually in basic
groups of 12, without mutual interference. It is described in detail in
Chaps. 9 and 10.
It may be that groupings different from those used in the terrestri-
al network are required for satellite transmission, and the next block
shows the multiplexing equipment in which the reformatting is car-
ried out. Following along the transmit chain, the multiplexed signal
is modulated onto a carrier wave at an intermediate frequency, usu-
ally 70 MHz. Parallel IF stages are required, one for each microwave
carrier to be transmitted. After amplification at the 70-MHz IF, the
modulated signal is then upconverted to the required microwave car-
rier frequency. A number of carriers may be transmitted simultane-
ously, and although these are at different frequencies they are
generally specified by their nominal frequency, for example, as 6-GHz
or 14-GHz carriers.
It should be noted that the individual carriers may be multidestina-
tion carriers. This means that they carry traffic destined for different
stations. For example, as part of its load, a microwave carrier may
have telephone traffic for Boston and New York. The same carrier is
received at both places, and the designated traffic sorted out by filters
at the receiving earth station.
Referring again to the block diagram of Fig. 8.6, after passing
through the upconverters, the carriers are combined, and the resulting
wideband signal is amplified. The wideband power signal is fed to the
antenna through a diplexer, which allows the antenna to handle trans-
mit and receive signals simultaneously.
The station’s antenna functions in both the transmit and receive
modes, but at different frequencies. In the C band, the nominal uplink,
or transmit, frequency is 6 GHz and the downlink, or receive, frequency
is nominally 4 GHz. In the Ku band, the uplink frequency is nominally
14 GHz, and the downlink, 12 GHz. High-gain antennas are employed
in both bands, which also means narrow antenna beams. A narrow
beam is necessary to prevent interference between neighboring satellite
links. In the case of C band, interference to and from terrestrial
The Earth Segment
215
TLFeBOOK
