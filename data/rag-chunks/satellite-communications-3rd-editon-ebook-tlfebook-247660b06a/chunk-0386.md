---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0386"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 386
confidence: "first-pass"
extraction_method: "structured-local"
---

data segments on the forward link and 40 bytes for ACKs on the
reverse link are given in RFC-2760.
Asymmetry is also used to describe the physical capacities of the
links. For small earth stations (e.g., VSATs), transmit power and
antenna size (in effect, the EIRP) limit the uplink data rate, which
therefore may be much less than the downlink data rate. Such asym-
metry can result in ACK congestion. Again, using some values given in
RFC-2760, for a 1.5 Mb/s data link a reverse link of less than 20 kb/s
can result in ACK congestion. The levels of asymmetry that lead to
ACK congestion are readily encountered in VSAT networks that share
the uplink through multiple access.
In some situations, the reverse link may be completed through a ter-
restrial circuit, as shown in Fig. 15.9 (Ghani and Dixit, 1999). Here,
the TCP source is connected to the satellite uplink through an IWU as
before. The downlink signal feeds the small residential receiver, which
is a receive-only earth station. An IWU on the receive side converts the
data to the TCP format and sends them on to the destination. The ACK
packets from the TCP destination are returned to the TCP source
through a terrestrial network. As pointed out in RFC-2760, the reverse
link capacity is limited not only by its bandwidth but also by queue
lengths at routers, which again can result in ACK congestion. Some of
the proposed methods of handling asymmetry problems and ongoing
research are described in Ghani and Dixit (1999).
DirecPC (http://www.direcpc.com/), a product and service of
Hughes Network Systems, takes advantage of asymmetric channels
to provide satellite transfer of Internet data to the individual con-
sumer and homeowner. The system as shown in Fig. 15.10 can be used
for all TCP/IP-based software applications such as email, Telnet, and
the World Wide Web (WWW). A customer URL (uniform, or universal
resource locator) request goes out through a modem to the Internet
service provider (ISP) at normal modem speeds (typically in the range
28.6 to 56 kb/s). Before sending the URL, the DirecPC software
installed in the customer’s PC attaches what is termed a tunneling
code to the URL. This instructs the ISP to forward the request to the
DirecPC network operations center (NOC) instead of to the Internet
server. At the NOC, the tunneling code is stripped away, and the
request is forwarded to the Internet site through high-speed lines.
The requested content is returned to the NOC, which then downloads
it to the customer through the satellite link, at a bit rate of up to 400
kb/s. The advantage of the system, therefore, is that the large data
files are returned over a high-speed link rather than back through the
low-speed modem.
Hughes 601 spacecraft are used, and the downlink is in the Ka band
(20 to 30 GHz). The company offers a variety of system configurations,
452
Chapter Fifteen
TLFeBOOK
