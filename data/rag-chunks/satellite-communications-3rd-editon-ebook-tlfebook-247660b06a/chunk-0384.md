---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0384"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 384
confidence: "first-pass"
extraction_method: "structured-local"
---

data-link protocol. As shown in the figure, any one of a number of link
layer protocols may be used. At the destination end, the IWU performs
the conversion back to TCP Reno.
One approach developed at Roke Manor Research, Ltd. (West and
McCann, 2000) illustrates some of the possibilities and problems asso-
ciated with splitting. The two key issues are setup and teardown (West
and McCann, 2000). To illustrate the process, consider a connection
being set up between host A and host B. In setting up the connection,
host A sends a synchronizing segment, labeled SYN in the TCP/IP
scheme, which specifies certain protocols to be followed. Host B
responds with its own SYN, which contains its protocol requirements,
also an ACK signal that carries the number to be used by host A for
the first data byte it sends. Host A then responds with an ACK signal
that carries the number to be used by host B for the first data byte it
sends. The three signals, SYN, SYN/ACK, and ACK, constitute what is
known as a three-way handshake.
A three-way handshake is also used to close (teardown). Suppose
host B wishes to close. It sends a final segment (FIN). Host A acknowl-
edges the FIN with an ACK and follows this with its own final segment
(FIN). Host B acknowledges the FIN with an ACK. On connections
with long RTTs, it will be seen that these three-way handshakes will
be very time-consuming.
Figure 15.6 shows the system developed at Roke Manor. The
enhancers perform the same function as the IWUs in Fig. 15.5 in that
they terminate the Internet connections and do not require any modi-
fications to the TCP/IP. A propriety protocol is used over the satellite
link. Figure 15.7 illustrates a situation where both setup and tear-
down are spoofed. In this illustration, host B refuses the connection,
but host A receives the RESET signal too late. The spoofed FIN ACK
tells host A that the data transfer was successful.
Figure 15.8 shows a more appropriate strategy. In this case, the FIN
sent by host A is not spoofed. Since host B has refused the connection,
host A receives no FIN, ACK back from host B. Therefore, host A can
450
Chapter Fifteen
INTERNET
Enhancer
INTERNET
Enhancer
Figure 15.6
Physical architecture incorporating enhancer technology. (From West and
McCann, 2000.)
TLFeBOOK

## Page 461
