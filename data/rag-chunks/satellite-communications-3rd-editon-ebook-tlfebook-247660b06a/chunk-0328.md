---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0328"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 328
confidence: "first-pass"
extraction_method: "structured-local"
---

the earth stations in the network. A number of methods are available
for the acquisition process (see, for example, Gagliardi, 1991), but
basically, these all require some form of ranging to be carried out so
that a close estimate of the slot position can be acquired. In one
method, the traffic station transmits a low-level burst consisting of
the preamble only. The power level is 20 to 25 dB below the normal
operating level (Ha, 1990) to prevent interference with other bursts,
and the short burst is swept through the frame until it is observed to
fall within the assigned time slot for the station. The short burst is
then increased to full power, and fine adjustments in timing are
made to bring it to the beginning of the time slot. Acquisition can
take up to about 3 s in some cases. Following acquisition, the traffic
data can be added, and synchronization can be maintained by con-
tinuously monitoring the position of the loopback transmission with
reference to the SORF marker. The timing positions are reckoned
from the last bit of the unique word in the preamble (as is also the
case for the reference burst). The loopback method is also known as
direct closed-loop feedback.
Feedback timing control.
Where a traffic station lies outside the satel-
lite beam containing its own transmission, loopback of the transmis-
sion does not of course occur, and some other method must be used for
the station to receive ranging information. Where the synchronization
information is transmitted back to an earth station from a distant sta-
tion, this is termed feedback closed-loop control. The distant station
may be a reference station, as in the INTELSAT network, or it may be
another traffic station which is a designated partner. During the acqui-
sition stage, the distant station can feed back information to guide the
positioning of the short burst, and once the correct time slot is
acquired, the necessary synchronizing information can be fed back on
a continuous basis.
Figure 14.17 illustrates the feedback closed-loop control method for
two earth stations A and B. The SORF marker is used as a reference
point for the burst transmissions. However, the reference point which
denotes the start of transmit frame (SOTF) has to be delayed by a cer-
tain amount, shown as DA for earth station A and DB for earth station
B. This is necessary so that the SOTF reference points for each earth
station coincide at the satellite transponder, and the traffic bursts,
which are transmitted at their designated times after the SOTF, arrive
in their correct relative positions at the transponder, as shown in Fig.
14.17. The total time delay between any given satellite clock pulse and
the corresponding SOTF is a constant, shown as C in Fig. 14.17. C is
equal to 2tA  DA for station A and 2tB  DB for station B. In general,
for earth station i, the delay Di is determined by
Satellite Access
393
TLFeBOOK
