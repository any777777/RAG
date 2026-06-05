---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0379"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 379
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 456

larger segments allow the congestion window to increment faster in
terms of number of bytes carried. There is a delay involved in imple-
menting Path MTU-Discovery, and of course, there is the added com-
plexity. Overall, however, it improves the performance of TCP over
satellite links.
Forward error correction (FEC).
Lost packets, whether from transmis-
sion errors or congestion, are assumed by the TCP to happen as a
result of congestion, which means that congestion control is imple-
mented, with its resulting reduction in throughput. Although there is
ongoing research into ways of identifying the mechanisms for packet
loss, the problem still remains. Application of FEC (as described in
Chap. 11) therefore should be used where possible.
Slow start and congestion avoidance.
These strategies have already
been described in Sec. 15.3, along with the problems introduced by
long RTTs. Slow start and congestion avoidance control the number of
segments transmitted, but not the size of the segments. Using Path
MTU-Discovery as described earlier can increase the size, and hence
the data throughput is improved.
Fast retransmit and fast recovery.
From the nature of the ACKs
received, the fast retransmit algorithm enables the sender to identify
and resend a lost segment before its timeout expires. Since the data
flow is not interrupted by timeouts, the sender can infer that conges-
tion is not a problem, and the fast recovery algorithm prevents the con-
gestion window from reverting to slow start. The fast retransmit
algorithm can only respond to one lost segment per send window. If
there is more than one, the others trigger the slow start mechanism.
446
Chapter Fifteen
TABLE 15.1
Summary of Objectives in RFC-2488
Mechanism
Use
RFC-2488 Section
Where Applied
Path MTU-Discovery
Recommended
3.1
Sender
FEC
Recommended
3.2
Link
TCP Congestion Control
Slow start
Required
4.1.1
Sender
Congestion avoidance
Required
4.1.1
Sender
Fast retransmit
Recommended
4.1.2
Sender
Fast recovery
Recommended
4.1.2
Sender
TCP Large Windows
Window Scaling
Recommended
4.2
Sender & Receiver
PAWS
Recommended
4.2
Sender & Receiver
RTTM
Recommended
4.2
Sender & Receiver
TCP SACKS
Recommended
4.4
Sender & Receiver
TLFeBOOK

## Page 457
