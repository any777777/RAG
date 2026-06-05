---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0320"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 320
confidence: "first-pass"
extraction_method: "structured-local"
---

ly for the purpose of transmitting reference bursts to which the others
can be synchronized. The time interval from the start of one reference
burst to the next is termed a frame. A frame contains the reference
burst R and the bursts from the other earth stations, these being
shown as A, B, and C in Fig. 14.10.
Figure 14.11 illustrates the basic principles of burst transmission for
a single channel. Overall, the transmission appears continuous
because the input and output bit rates are continuous and equal.
However, within the transmission channel, input bits are temporarily
stored and transmitted in bursts. Since the time interval between
bursts is the frame time TF, the required buffer capacity is
M  RbTF
(14.15)
The buffer memory fills up at the input bit rate Rb during the frame
time interval. These M bits are transmitted as a burst in the next
frame without any break in continuity of the input. The M bits are
transmitted in the burst time TB, and the transmission rate, which is
equal to the burst bit rate, is
R TDMA 
 Rb
(14.16)
This is also referred to as the burst rate, but note that this means
the instantaneous bit rate within a burst (not the number of bursts per
second, which is simply equal to the frame rate). It will be seen that
the average bit rate for the burst mode is simply M/TF, which is equal
to the input and output rates.
The frame time TF will be seen to add to the overall propagation
delay. For example, in the simple system illustrated in Fig. 14.11, even
if the actual propagation delay between transmit and receive buffers
is assumed to be zero, the receiving side would still have to wait a time
TF

TB
M

TB
384
Chapter Fourteen
Figure 14.11
Burst-mode transmission linking two continuous-mode streams.
TLFeBOOK

## Page 395
