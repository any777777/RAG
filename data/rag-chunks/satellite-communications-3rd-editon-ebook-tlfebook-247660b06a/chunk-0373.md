---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0373"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 373
confidence: "first-pass"
extraction_method: "structured-local"
---

I Byte. Common usage has established the byte (symbol B) as a unit
of 8 bits, and this practice will be followed here. It should be noted,
however, that in computer terminology, a byte can mean a unit other
than 8 bits, and the 8-bit unit may be called an octet.
I Kilobyte. The kilobyte (symbol kB) is 1024 bytes. Transmission
rates may be stated in kilobytes per second, or kB/s.
I Megabyte. The megabyte (symbol MB) is 1024 kilobytes.
Transmission rates may be stated in megabytes per second. or MB/s.
The TCP/IP suite is shown in Fig.15.4, and an excellent detailed
description of these protocols will be found in Feit (1997). The present
text will be concerned more with the special enhancements needed on
TCP/IP for successful satellite transmission.
15.3
The TCP Link
A virtual communications link exists between corresponding layers in
a network. The header in the TCP segment (see Fig. 15.3) carries
instructions that enable communication between the send and receive
TCP layers. Of course, the communication has to pass through the other
layers and along the physical link, but only the TCP layers act on the
Transmission Control Protocols (TCPs) contained in the segment
header. There is no direct physical link between the TCP layers, and
for this reason, it is called a virtual link.
The send and receive TCP layers have buffer memories (usually just
called buffers). The receive buffer holds incoming data while they are
being processed. The send buffer holds data until they are ready for
442
Chapter Fifteen
WWW
NEWS
FTP
SMTP
NFS
DNS
SNMP
Telnet
TCP
End-to-end connections
UDP
Single messages
IP
Route datagrams
Underlying communications
Point-to-
point
ATM
Frame
relay
FDDI
Token
ring
Ethernet
Figure 15.4
The TCP/IP suite. (After Feit, 1997.)
TLFeBOOK

## Page 453
