---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0406"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 406
confidence: "first-pass"
extraction_method: "structured-local"
---

affect the signal much more severely than they would in a noncom-
pressed bit stream. As a result, forward error correction is a must.
Concatenated coding is used (see Sec. 11.6). The outer code is a Reed-
Solomon code that corrects for block errors, and the inner code is a con-
volution code that corrects for random errors. The inner decoder
utilizes the Viterbi decoding algorithm. These FEC bits, of course, add
overhead to the bit stream. Typically, for a 240-W transponder (see
Sec. 16.3), the bit capacity of 40 Mb/s (see Sec. 16.5) may have a pay-
load of 30 Mb/s and coding overheads of 10 Mb/s. The lower-power 120-
W transponders require higher coding overheads to make up for the
reduction in power and have a payload of 23 Mb/s and coding over-
heads of 17 Mb/s. More exact figures are given in Mead (2000) for
DirecTV, where the overall code rates are given as 0.5896 for the 120-
W transponder and 0.758 for the 240-W transponder.
Mead (2000) has shown that with FEC there is a very rapid transi-
tion in BER for values of [Eb/No] between 5.5 and 6 dB. For [Eb/No] val-
ues greater than 6 dB, the BER is negligible, and for values less than
5.5 dB, the BER is high enough to render the system useless.
Advances in coding techniques promise a further increase in transpon-
der capacity. A system patented by France Telecom (see Vollmer, 2000),
when used with 8-PSK, should realize a 50 percent increase in the bit
rate capacity of a transponder. The new codes are called Turbo codes, and
details will be found in Hewitt and Thesling (2000).
16.9
The Home Receiver Outdoor Unit
(ODU)
The home receiver consists of two units, an outdoor unit and an indoor
unit. Commercial brochures refer to the complete receiver as an inte-
grated receiver decoder (IRD). Figure 16.5 is a block schematic for the
outdoor unit (ODU). This will be seen to be similar to the outdoor unit
shown in Fig. 8.1. The downlink signal, covering the frequency range
12.2 to 12.7 GHz, is focused by the antenna into the receive horn. The
horn feeds into a polarizer that can be switched to pass either left-
hand circular to right-hand circular polarized signals. The low-noise
block that follows the polarizer contains a low-noise amplifier (LNA)
and a downconverter. The function of the LNA is described in Sec. 12.5.
The downconverter converts the 12.2- to 12.7-GHz band to 950 to 1450
MHz, a frequency range better suited to transmission through the con-
necting cable to the indoor unit.
The antenna usually works with an offset feed (see Sec. 6.14), and a
typical antenna structure is shown in Fig. 16.6. It is important that
the antenna have an unobstructed view of the satellite cluster to
Direct Broadcast Satellite Services
471
TLFeBOOK
