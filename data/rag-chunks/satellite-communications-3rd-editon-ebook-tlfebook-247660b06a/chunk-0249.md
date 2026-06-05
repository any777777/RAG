---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0249"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 249
confidence: "first-pass"
extraction_method: "structured-local"
---

wait ARQ, the transmitter stores a copy of the block just transmitted and
waits for the acknowledgment signal. If a NAK signal is received, it
retransmits the block, and if an ACK signals is received, it transmits the
next block. In either case, the delay between transmissions is about half
a second, the round-trip time to and from a geostationary satellite. This
would be unacceptable in many applications.
What is required is continuous transmission of blocks incorporating
the retransmission of corrupted blocks when these are detected. Go
back N ARQ achieves this by having the blocks and the acknowledg-
ment signals numbered. The transmitter must now be capable of stor-
ing the number of blocks N transmitted over the round-trip time and
updating the storage as each ACK signal is received. If the receiver
detects an error in block i, say, it transmits an NAKi signal and refuses
to accept any further blocks until it has received the correct version of
block i. The transmitter goes back to block i and restarts the transmis-
sion from there. This means that block i and all subsequent blocks are
retransmitted. It is clear that a delay will only be encountered when an
NAK signal is received, but there is the additional time loss resulting
from the retransmission of the good blocks following the corrupted
block. The method can be further improved by using what is termed
selective repeat ARQ, where only a correct version of the corrupted
block is retransmitted, and not the subsequent blocks. This creates a
storage requirement at the receiver because it must be able to store the
subsequent blocks while waiting for the corrected version of the cor-
rupted block.
It should be noted that in addition to the ACK and NAK signals, the
transmitter operates a timeout clock. If the acknowledgment signal
(ACK or NAK) for a given block is not received within the timeout
period, the transmitter puts the ARQ mechanism into operation. This
requires the receiver to be able to identify the blocks so that it recog-
nizes which ones are repeats.
The throughput of an ARQ system is defined at the ratio of the aver-
age number of data bits accepted at the receiver in a given time to the
number of data bits that could have been accepted if ARQ had not been
used. Let PA be the probability that a block is accepted; then, as shown
in Taub and Schilling (1986), the throughputs are
GobackN 
(11.10)
SelectiveRepeat 
PA
(11.11)
Typically, for a BCH (1023, 973) code and N  4, the throughput for go
back N is 0.915, and for selective repeat, 0.942.
k
n
PA

PA  N (1  PA)
k
n
Error Control Coding
301
TLFeBOOK
