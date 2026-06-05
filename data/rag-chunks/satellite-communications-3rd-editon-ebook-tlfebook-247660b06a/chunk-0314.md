---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0314"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 314
confidence: "first-pass"
extraction_method: "structured-local"
---

system described in Sec. 14.3. However, the distributed-demand assign-
ment facility requires a common signaling channel (CSC). This is shown
in Fig. 14.8. The CSC bandwidth is 160 kHz, and its center frequency is
18.045 MHz below the pilot frequency, as shown in Fig. 14.8. To avoid
interference with the CSC, voice channels 1 and 2 are left vacant, and
to maintain duplex matching, the corresponding channels 1′ and 2′ are
also left vacant. Recalling from Fig. 14.5 that channel 400 also must be
left vacant, this requires that channel 800 be left vacant for duplex
matching. Thus six channels are removed from the total of 800, leaving
a total of 794 one-way or 397 full-duplex voice circuits, the frequencies
in any pair being separated by 18.045 MHz, as shown in Fig. 14.8. (An
alternative arrangement is shown in Freeman, 1981.)
All the earth stations are permanently connected through the com-
mon signaling channel (CSC). This is shown diagrammatically in Fig.
14.9 for six earth stations A, B, C, D, E, and F. Each earth station has
the facility for generating any one of the 794 carrier frequencies using
frequency synthesizers. Furthermore, each earth station has a memo-
ry containing a list of the frequencies currently available, and this list
is continuously updated through the CSC. To illustrate the procedure,
suppose that a call to station F is initiated from station C in Fig. 14.9.
Station C will first select a frequency pair at random from those cur-
rently available on the list and signal this information to station F
through the CSC. Station F must acknowledge, through the CSC, that
it can complete the circuit. Once the circuit is established, the other
earth stations are instructed, through the CSC, to remove this fre-
quency pair from the list.
The round-trip time between station C initiating the call and station
F acknowledging it is about 600 ms. During this time, the two frequen-
cies chosen at station C may be assigned to another circuit. In this
Satellite Access
377
Figure 14.8
Channeling scheme for the Spade system.
TLFeBOOK

## Page 388
