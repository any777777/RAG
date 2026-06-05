---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0380"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 380
confidence: "first-pass"
extraction_method: "structured-local"
---

TCP large windows.
As shown in Sec. 15.4 in connection with the band-
width delay product, the receive window size is limited by the address
field to 64 kilobytes maximum. By introducing a window scale exten-
sion into the TCP header, the address field can be effectively increased
to 32 bits. Allowing for certain overheads, the maximum window size
that can be declared is 230  1 gigabyte (again keeping in mind that 1
gigabyte  10243 bytes). The window size and hence the scale factor
can be set locally by the receive TCP layer. Note, however, that the TCP
extension has to be implemented at the sender and the receiver.
The two mechanisms PAWS, which stands for protection against
wrapped sequence, and RTTM, which stands for round-trip time mea-
surement, are extensions that should be used with large windows.
Maintaining steady traffic flow and avoiding congestion require a cur-
rent knowledge of the RTT, which can be difficult to obtain with large
windows. By including a time stamp in the TCP header, the RTT can
be measured. Another problem that arises with large windows is that
the numbering of old sequences can overlap with new, a condition
known as wrap-around. The protection against wrapped sequences is
an algorithm that also makes use of the time stamp. These algorithms
are described fully in RFC-1323.
SACK stands for selective acknowledgment and is a strategy that
enables the receiver to inform the sender of all segments received suc-
cessfully. The sender then need only resend the missing segments.
The strategy should be used where multiple segments may be lost
during transmission, such as, for example, in a satellite link, since
clearly, retransmission of duplicate segments over long delay paths
would seriously reduce the throughput. Full details of SACK will be
found in RFC-2018.
15.6
Requests for Comments
The rapid growth of the Internet resulted in large part from the free
and open access to documentation provided by network researchers.
The ideas and proposals of researchers are circulated in memos called
Requests for Comments (RFCs). They can be accessed on the World
Wide Web at a number of sites, for example, http://www.rfc-
editor.org/. Below is a summary of some of the RFCs that relate specif-
ically to satellite links and that have been referred to in Sec. 15.5
I RFC-2760, Ongoing TCP Research Related to Satellites, February
2000. Abstract: This document outlines possible TCP enhancements
that may allow TCP to better utilize the available bandwidth pro-
vided by networks containing satellite links. The algorithms and
mechanisms outlined have not been judged to be mature enough to
Satellite Services and the Internet
447
TLFeBOOK
