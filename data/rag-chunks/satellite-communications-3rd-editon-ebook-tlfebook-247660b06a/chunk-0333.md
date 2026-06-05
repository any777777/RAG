---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0333"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 333
confidence: "first-pass"
extraction_method: "structured-local"
---

is true in general. In practice, once frame synchronization has been
established, a time window can be formed around the expected time
of arrival for the UW such that the correlation detector is only in oper-
ation for the window period. This greatly reduces the probability of
false detection.
14.7.6
Traffic data
The traffic data immediately follow the preamble in a burst. As shown
in Fig. 14.13, the traffic data subburst is further subdivided into time
slots addressed to the individual destination stations. Any given desti-
nation station selects only the data in the time slots intended for that
station. As with FDMA networks, TDMA networks can be operated
with both preassigned and demand assigned channels, and examples
of both types will be given shortly.
The greater the fraction of frame time that is given over to traffic,
the higher is the efficiency. The concept of frame efficiency is discussed
in the next section.
14.7.7
Frame efficiency and channel
capacity
The frame efficiency is a measure of the fraction of frame time used for
the transmission of traffic. Frame efficiency may be defined as
Frame efficiency  F 
(14.26)
Alternatively, this can be written as
F  1  
(14.27)
In these equations, bits per frame are implied. The overhead bits
consist of the sum of the preamble, the postamble, the guard intervals,
and the reference-burst bits per frame. The equations may be stated in
terms of symbols rather than bits, or the actual times may be used.
For a fixed overhead, Eq. (14.27) shows that a longer frame, or
greater number of total bits, results in higher efficiency. However,
longer frames require larger buffer memories and also add to the prop-
agation delay. Synchronization also may be made more difficult, keep-
ing in mind that the satellite position is varying with time. It is clear
that a lower overhead also leads to higher efficiency, but again, reduc-
ing synchronizing and guard times may result in more complex equip-
ment being required.
overhead bits

total bits
traffic bits

total bits
398
Chapter Fourteen
TLFeBOOK

## Page 409
