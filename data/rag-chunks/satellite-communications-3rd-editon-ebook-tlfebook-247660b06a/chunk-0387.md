---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0387"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 387
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 463

Satellite network
IWU
IWU
TCP destination
TCP source
Intersatellite links
Data packets
Large
(corporate)
transmitter
Forward
uplink/downlink
channels (Mb/s)
Small
residential
receiver
Terrestrial network
ACK packets
Reverse
channels (kb/s)
Figure 15.9
Asymmetric reverse ACK channel configuration. (From Ghani and Dixit, 1999. © 1999 IEEE.)
453
TLFeBOOK

## Page 464

ranging from Internet-only connections to a combined DirecPC and
DirecTV system.
15.9
Proposed Systems
Most of the currently employed satellites operate in what is called a
“bent pipe” mode; that is, they relay the data from one host to another
without any onboard processing. Also, many of the problems with using
geostationary satellites for Internet traffic arise because of the long
propagation delay and the resulting high delay-bandwidth product. In
some of the newer satellite systems, use is made of low and medium
earth orbiting satellites to cut down on the propagation delay time. Also,
onboard signal processing is used in many instances that may result in
the TCP/IP protocol being exchanged for propriety protocols over the
satellite links. The satellite part of the network may carry the Internet
Protocol (IP) over what is known as Asynchronous Transfer Mode
(ATM). With ATM, the data are partitioned into fixed-length packets,
called cells, of length 53 bytes total. Five bytes form the header for the
cell, and the remaining 48 bytes are the payload. However, with ATM,
the “payload” also carries additional overhead bytes, specifically bytes
for what is called the ATM adaptation layer. The asynchronous part of
the ATM refers to the fact that cells are transmitted asynchronously;
that is, they do not need to be assigned regular time slots. The cell size
of 53 bytes is a compromise between what is suitable for time-sensitive
traffic such as voice and video and what is suitable for non-time-
sensitive data. For high-bit-rate traffic, many cells can be trans-
454
Chapter Fifteen
Information
is transferred
to and from the
INTERNET
DirecPC satellites
Web sites are
zipped at speeds
up to 400 kbps
straight to your
DirecPC dish
and satellite modem
START
Your PC
sends a
request
through your
telephone
modem
to your
ISP
which
routes
it to
DirecPC Network
Operations Center
(NOC)
The NOC sends
the data to
Figure 15.10
DirecPC turbo Webcast. (From http://direcpc.com/consumer/what/ser-
vices.html.)
TLFeBOOK

## Page 465
