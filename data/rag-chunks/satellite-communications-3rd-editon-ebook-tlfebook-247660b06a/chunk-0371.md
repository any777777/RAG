---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0371"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 371
confidence: "first-pass"
extraction_method: "structured-local"
---

I Data-link layer. The function of this layer is to organize the digital
data into blocks as required by the physical layer. For example, if the
physical layer uses Asynchronous Transfer Mode (ATM) technology,
the data are organized into cells. Digital transmission by satellite
frequently uses TDMA, as described in Chap. 14, and satellite sys-
tems are being developed which transmit Internet data over ATM.
Thus the data-link layer has to organize the data into a suitable for-
mat to suit the physical layer technology. In the terrestrial Internet,
the data link converts the data into frames. The data-link layer and
the physical layer are closely interrelated, and it can be difficult
sometimes to identify the interface between these two layers
(Mackenzie, 1998).
I Network layer. This is strictly an Internet Protocol (IP) layer. The
packets are passed along the Internet from router to router and to
the host stations. No exact path is laid out beforehand, and the IP
layers in the routers must provide the destination address for the
next leg of the journey so to speak. This destination address is
part of the IP header attached to the packet. The source address
is also included as part of the IP header. The problems of lost
packets or packets arriving out of sequence are not a concern of
the IP layer, and for this reason, the IP layer is called connection-
less (i.e., it does not require a connection to be established before
sending a packet on). These problems are taken care of by the
transport layer.
I Transport layer. Two sets of protocol are provided in this layer. With
the Transmission Control Protocol (TCP), information is passed back
and forth between transport layers, which controls the information
flow. This includes such functions as the correct sequencing of pack-
ets, replacement of lost packets, and adjusting the transmission rate
of packets to prevent congestion. In the early days of the Internet
when traffic was comparatively light, these problems could be han-
dled even where satellite transmissions were involved. With the
enormous increase in traffic on the present-day Internet, these prob-
440
Chapter Fifteen
Applications & Services
TCP            UDP
IP
Data Link
Physical
Figure 15.2
Layered structure
for TCP/IP. (After Feit, 1997.)
TLFeBOOK

## Page 451
