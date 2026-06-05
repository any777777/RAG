---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0372"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 372
confidence: "first-pass"
extraction_method: "structured-local"
---

lems require special solutions where satellite systems are used,
which are discussed in later sections. The TCP layer is termed con-
nection-oriented (compared with the connectionless service men-
tioned above) because sender and receiver must be in
communication with each other to implement the protocol. There are
situations where a simple standalone message may need to be sent
which does not require the more complex TCP. For these types of
message, another transport layer protocol called the User Datagram
Protocol (UDP) is used. The UDP provides a connectionless service,
similar to IP. The UDP header adds the port numbers for the source
and destination applications.
The term packet has been used somewhat loosely up to this point. A
more precise terminology is used for packets at the various layers, and
this is shown in Fig. 15.3. At the application level the packet is simply
referred to as data. The packet comprising the TCP header, and the
data are a TCP segment. The packet comprising the UDP header and
the data is a UDP message. The packet comprising the IP header, the
TCP or UDP header, and the data is an IP datagram. Finally, the pack-
et comprising the data-link frame header, the frame trailer (used for
error control), and the IP datagram is a frame.
It should be noted here that the preceding definitions are those used
in version 4 of the Internet Protocol (IPv4). Internet Protocol version 6
(IPv6) is a more recent version being brought on-stream in which the
IP datagram is in fact called an IP packet.
Some of the units used in data transmission are
Satellite Services and the Internet
441
Data
Data
TCP
header
Data
UDP
header
Data
TCP or
UDP
header
IP
header
Data
TCP or
UDP
header
IP
header
Frame
header
Frame
trailer
Application – data
Data link
frame
Network
IP datagram
UDP message
Transport
TCP segment
Figure 15.3
Packet terminology. (After Feit, 1997.)
TLFeBOOK

## Page 452
