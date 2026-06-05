---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0382"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 382
confidence: "first-pass"
extraction_method: "structured-local"
---

be recommended by the IETF. The goal of this document is to edu-
cate researchers as to the current work and progress being done in
TCP research related to satellite networks.
I RFC-2488, Enhancing TCP Over Satellite Channels Using Standard
Mechanisms, January 1999. Abstract: The Transmission Control
Protocol (TCP) provides reliable delivery of data across any network
path, including network paths containing satellite channels. While
TCP works over satellite channels, there are several IETF stan-
dardized mechanisms that enable TCP to more effectively utilize the
available capacity of the network path. This document outlines some
of these TCP mitigations. At this time, all mitigations discussed in
this document are IETF standards track mechanisms (or are com-
pliant with IETF standards).
I RFC-2018, TCP Selective Acknowledgment Options, October 1996.
Abstract: TCP may experience poor performance when multiple
packets are lost from one window of data. With the limited informa-
tion available from cumulative acknowledgments, a TCP sender can
only learn about a single lost packet per round-trip time. An aggres-
sive sender could choose to retransmit packets early, but such
retransmitted segments may have already been received successfully.
A selective acknowledgment (SACK) mechanism, combined with a
selective repeat retransmission policy, can help to overcome these lim-
itations. The receiving TCP sends back SACK packets to the sender
informing the sender of data that have been received. The sender can
then retransmit only the missing data segments. This memo propos-
es an implementation of SACK and discusses its performance and
related issues.
I RFC-1323, TCP Extensions for High Performance, May 1992.
Abstract: This memo presents a set of TCP extensions to improve
performance over large bandwidth*delay product paths and to pro-
vide reliable operation over very high-speed paths. It defines new
TCP options for scaled windows and timestamps, which are designed
to provide compatible interworking with TCPs that do not imple-
ment the extensions. The timestamps are used for two distinct
mechanisms: RTTM (round-trip time measurement) and PAWS (pro-
tect against wrapped sequences). Selective acknowledgments are not
included in this memo. This memo combines and supersedes RFC-
1072 and RFC-1185, adding additional clarification and more
detailed specification. Appendix C of RFC-1323 summarizes the
changes from the earlier RFCs.
I RFC-1072, TCP Extensions for Long Delay Paths, October 1988.
Status of this memo: This memo proposes a set of extensions to the
TCP to provide efficient operation over a path with a high band-
448
Chapter Fifteen
TLFeBOOK
