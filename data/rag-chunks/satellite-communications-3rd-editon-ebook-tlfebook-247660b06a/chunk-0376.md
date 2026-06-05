---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0376"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 376
confidence: "first-pass"
extraction_method: "structured-local"
---

(some would say unacceptable) to modify it to accommodate peculiari-
ties of the physical link. The factors that can adversely affect TCP per-
formance over satellite links are as follows:
Bit error rate (BER).
Satellite links have a higher bit error rate (BER;
see Chap. 10) than the terrestrial links forming the Internet. Typically,
the satellite link BER without error control coding is around 106,
whereas a level of 108 or lower is needed for successful TCP transfer
(Chotikapong and Sun, 2000). The comparatively low BER on terres-
trial links means that most packet losses are the result of congestion,
and the TCP send layer is programmed to act on this assumption.
When packets are lost as a result of high BER, therefore, as they might
on satellite links, the TCP layer assumes that congestion is at fault
and automatically invokes the congestion control measures. This slows
the throughput.
Round-trip time (RTT).
The round-trip time (RTT) of interest here is
the time interval that elapses between sending a TCP segment and
receiving its ACK. With geostationary (GEO) satellites, the round-trip
propagation path is ground station to satellite to ground station and
back again. The range from ground station to the satellite (see Chap.
3) is on the order of 40,000 km, and therefore, the propagation path for
the round trip is 4  40,000  160,000 km. The propagation delay is
therefore 160,000/3  108  0.532 s. This is just the space propagation
delay. The total round-trip time must take into account the propaga-
tion delays on the terrestrial circuits and the delays resulting from sig-
nal processing. For order of magnitude calculations, an RTT value of
0.55 s would be appropriate. The send TCP layer must wait this length
of time to receive the ACKs, and of course, it cannot send new seg-
ments until the ACKs are received, which is going to slow the through-
put. The send TCP timeout period is also based on the RTT, and this
will be unduly lengthened. Also, with interactive applications such as
Telnet, this delay is highly undesirable.
Bandwidth-delay product (BDP).
The RTT is also used in determining an
important factor known as the bandwidth delay product (BDP). The
delay part of this refers to the RTT, since a sender has to wait this
amount of time for the ACK before sending more data. The bandwidth
refers to the channel bandwidth. As shown in Chaps. 10 and 12, band-
width and bit rate are directly related. In network terminology, the
bandwidth is usually specified in bytes per second (or multiples of this),
where it is understood that 1 byte is equal to 8 bits. For example, a satel-
lite bandwidth of 36 MHz carrying a BPSK signal could handle a bit
rate given by Eq. (14.30) as 30 megabits per second (Mb/s). This is equiv-
444
Chapter Fifteen
TLFeBOOK
