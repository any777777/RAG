---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0378"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 378
confidence: "first-pass"
extraction_method: "structured-local"
---

alent to 3.75  106 bytes per second (B/s) or about 3662 kilobytes per
second (kB/s). If the sender transmits at this rate, the largest packet it
can send within the RTT of 0.55 s is 3662  0.55  2014 kilobytes
approximately. This is the BDP for the two-way satellite channel. The
channel is sometimes referred to as a pipeline, and one that has a high
BDP, as a long fat pipe. Now the receive TCP layer uses a 16-bit word to
notify the send TCP layer of the size of the receive window it is going to
use. Allowing 1 byte for certain overheads, the biggest segment size that
can be declared for the receive window is 216  1  65,535 bytes, or
approximately 64 kilobytes. (Recall that 1 kilobyte is equal to 1024
bytes.) This falls well short of the 2014 kilobytes set by the BDP for the
channel, and thus the channel is very underutilized.
Variable round-trip time.
Where lower earth orbiting satellites are used
such as those in low earth orbits (LEOs) and medium earth orbits
(MEOs), the propagation delays will be much less than that for the
GEO. The slant range to LEOs is typically on the order of a few thou-
sand kilometers at most, and for MEOs, a few tens of thousand kilo-
meters. The problem with these orbits is not so much the absolute
value of delay as the variability. Because these satellites are not geo-
stationary, the slant range varies, and for continuous communications
there is the need for intersatellite links, which also adds to the delay
and the variability. For example, for LEOs, the delay can vary from a
few to about 80 ms. Whether or not this will have an impact on TCP
performance is currently an open question (RFC-2488).
15.5
Enhancing TCP Over Satellite
Channels Using Standard Mechanisms 
(RFC-2488)
In keeping with the objective that, where possible, the TCP itself
should not be modified to accommodate satellite links, the Request for
Comments 2488 (RFC-2488) describes in detail several ways in which
the performance over satellite links can be improved. These are sum-
marized in Table 15.1. The first two mechanisms listed do not require
any changes to the TCP. The others do require extensions to the TCP.
As always, any extensions to the TCP must maintain compatibility
with networks that do not employ the extensions. Brief descriptions of
the mechanisms are included, but the reader is referred to the
Requests for Comments (RFCs) for full details (see Sec. 15.6).
MTU stands for maximum transmission unit, and Path MTU-
Discovery is a method that allows the sender to find the largest packet
and hence largest TCP segment size that can be sent without frag-
mentation. The congestion window is incremented in segments; hence
Satellite Services and the Internet
445
TLFeBOOK
