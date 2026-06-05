---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0383"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 383
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 459

width*delay product. These extensions are not proposed as an
Internet standard at this time. Instead, they are intended as a basis
for further experimentation and research on TCP performance.
Distribution of this memo is unlimited.
15.7
Split TCP Connections
The Transmission Control Protocol (TCP) provides end-to-end connec-
tion. By this is meant that the TCP layers at the sender and receiver
are connected through a virtual link (see Sec. 15.3) so that such mat-
ters as congestion control, regulation of data flow, etc. can be carried
out without intervention of intermediate stages. It is to preserve this
end-to-end connection that many of the extensions to TCP described in
the preceding section have been introduced.
If, however, it is assumed that the end-to-end connectivity can be
split, new possibilities are opened up for the introduction of satellite
links as part of the overall Internet. Figure 15.5 shows one possible
arrangement (Ghani and Dixit, 1999). Breaking the network in this
way is termed spoofing. This refers to the fact that the TCP source
thinks it is connected to the TCP destination, whereas the interwork-
ing unit (IWU) performs a protocol conversion. In Fig. 15.5, TCP Reno
refers to the TCP with extensions: slow start, congestion avoidance,
fast retransmit, fast recovery, support for large windows, and delayed
ACKs. At the IWU the data are transferred from the TCP Reno to the
Satellite Services and the Internet
449
Satellite network
IWU
IWU
Link-level protocol
Improved link-layer protocol
or even TCP version
“Spoofing” endpoints
Native (legacy) TCP versions
at client desktops
TCP Reno
TCP Reno
TCP destination
TCP source
Figure 15.5
TCP/IP satellite link spoofing configuration. (From Ghani and Dixit, 1999.
© 1999 IEEE.)
TLFeBOOK

## Page 460
