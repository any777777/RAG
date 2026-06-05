---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0385"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 385
confidence: "first-pass"
extraction_method: "structured-local"
---

infer from this that there was an error. While this is not as good as a
regular TCP/IP connection, which would have reported a failure to
connect on the first SYN, the system does adjust to the error and
removes the spoofing on the setup on a second try.
15.8
Asymmetric Channels
The term asymmetry applies in two senses to an Internet connection.
It can refer to the data flow, which is often asymmetric in nature. A
short request being sent for a Web page and the returned Web page
may be a much larger document. Also, the acknowledgment packets
sent on the return or reverse link are generally shorter than the
TCP segments sent on the forward link. Values of 1500 bytes for
Satellite Services and the Internet
451
SYN
SYN ACK
<DATA>
FIN
ACK
FIN ACK
RESET from
Host B is too
late
Connection refused
by host
RESET
SYN
Actual (end-to-end)
message
Spoofed message
Host A
Host B
Enhancer Pair
Figure 15.7
Connection establishment and closing. (From West and McCann, 2000.)
SYN
SYN ACK
<DATA>
FIN
FIN
ACK
RESET from
Host B 
Connection refused
by host
RESET
SYN
Actual (end-to-end)
message
Spoofed message
(ignored)
Host A
Host B
Enhancer Pair
Figure 15.8
Improved connection close. (From West and McCann, 2000.)
TLFeBOOK

## Page 462
