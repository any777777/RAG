---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0374"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 374
confidence: "first-pass"
extraction_method: "structured-local"
---

transmission. It also holds copies of data already sent until it receives
an acknowledgment that the original has been received correctly. The
receive window is the amount of receive buffer space available at any
given time. This changes as the received data are processed and
removed from the buffer. The receive TCP layer sends an acknowledg-
ment (ACK) signal to the send TCP layer when it has cleared data
from its buffer, and the ACK signal also provides an update on the cur-
rent size of the receive window.
The send TCP layer keeps track of the amount of data in transit and
therefore unacknowledged. It can calculate the amount of receive
buffer space remaining, allowing for the data in transit. This remain-
ing buffer space represents the amount of data that can still be sent
and is termed the send window. The send TCP layer also sets a timeout
period, and failure to receive an ACK signal within this period results
in a duplicate packet being sent. On terrestrial networks, the probabil-
ity of bit error (see Chap. 10) is extremely low, and congestion is the
most likely reason for loss of ACK signals. Because a network carries
traffic from many sources, traffic congestion can occur. The IP layer of
the TCP/IP discards packets when congestion occurs, and hence the
corresponding ACK signals from the TCP layer do not get sent. Rather
than continually resending packets, the send station reduces its rate of
transmission, this being known as congestion control. A congestion win-
dow is applied, which starts at a size of one segment for a new connec-
tion. The window is doubled in size for each ACK received until it
reaches a maximum value determined by the number of failed ACKs
experienced. For normal operation, the congestion window grows in
size to equal the receive window. The congestion window increases
slowly at first, but as each doubling takes effect, the size increases
exponentially. This controlling mechanism is known as slow start. If
congestion sets in, this will be evidenced by an increase in the failure
to receive ACKs, and the send TCP will revert to the slow start.
15.4
Satellite Links and TCP
Although satellite links have formed part of the Internet from its begin-
ning, the rapid expansion of the Internet and the need to introduce con-
gestion control have highlighted certain performance limitations
imposed by the satellite links. Before discussing these, it should be
pointed out that the increasing demand for Internet services may well
be met best with satellite direct-to-home links, and many companies
are actively engaged in setting up just such systems (see Sec. 15.6).
In the ideal case, the virtual link between TCP layers should not be
affected by the physical link, and certainly the Transmission Control
Protocol (TCP) is so well established that it would be undesirable
Satellite Services and the Internet
443
TLFeBOOK
