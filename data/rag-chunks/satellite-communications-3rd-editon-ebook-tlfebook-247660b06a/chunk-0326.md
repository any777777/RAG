---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0326"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 326
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 401

ing markers are provided by the reference bursts, which are tied to a
highly stable clock at the reference station and transmitted through
the satellite link to the traffic stations. At any given traffic station,
detection of the unique word (or burst code word) in the reference
burst signals the start of receiving frame (SORF), the marker coincid-
ing with the last bit in the unique word.
It would be desirable to have the highly stable clock located aboard
the satellite because this would eliminate the variations in propagation
delay arising from the uplink for the reference station, but this is not
practical because of weight and space limitations. However, the refer-
ence bursts retransmitted from the satellite can be treated, for timing
purposes, as if they originated from the satellite (Spilker, 1977).
The network operates what is termed a burst time plan, a copy of
which is stored at each earth station. The burst time plan shows each
earth station where the receive bursts intended for it are relative to the
SORF marker. This is illustrated in Fig. 14.16. At earth station A the
SORF marker is received after some propagation delay tA, and the
burst time plan tells station A that a burst intended for it follows at
time TA after the SORF marker received by it. Likewise, for station B,
the propagation delay is tB, and the received bursts start at TB after the
SORF markers received at station B. The propagation delays for each
station will differ, but typically they are in the region of 120 ms each.
The burst time plan also shows a station when it must transmit its
bursts in order to reach the satellite in the correct time slots. A major
advantage of the TDMA mode of operation is that the burst time plan
is essentially under software control so that changes in traffic pat-
terns can be accommodated much more readily than is the case with
FDMA, where modifications to hardware are required. Against this,
Satellite Access
391
Figure 14.15
An example of carrier recovery circuit with a single-tuned circuit and
AFC. (From Miya, 1981.)
TLFeBOOK

## Page 402
