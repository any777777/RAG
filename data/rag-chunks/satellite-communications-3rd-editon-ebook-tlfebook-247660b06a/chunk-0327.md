---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0327"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 327
confidence: "first-pass"
extraction_method: "structured-local"
---

implementation of the synchronization is a complicated process.
Corrections must be included for changes in propagation delay which
result from the slowly varying position of the satellite (see Sec. 7.4).
In general, the procedure for transmit timing control has two stages.
First, there is the need for a station just entering, or reentering after
a long delay, to acquire its correct slot position, this being referred to
as burst position acquisition. Once the time slot has been acquired,
the traffic station must maintain the correct position, this being
known as burst position synchronization.
Open-loop timing control.
This is the simplest method of transmit tim-
ing. A station transmits at a fixed interval following reception of the
timing markers, according to the burst time plan, and sufficient
guard time is allowed to absorb the variations in propagation delay.
The burst position error can be large with this method, and longer
guard times are necessary, which reduces frame efficiency (see Sec.
14.7.7). However, for frame times longer than about 45 ms, the loss of
efficiency is less than 10 percent. In a modified version of the open-
loop method known as adaptive open-loop timing, the range is com-
puted at the traffic station from orbital data or from measurements,
and the traffic earth station makes its own corrections in timing to
allow for the variations in the range. It should be noted that with
open-loop timing, no special acquisition procedure is required.
Loopback timing control.
Loopback refers to the fact that an earth
station receives its own transmission, from which it can determine
range. It follows that the loopback method can only be used where
the satellite transmits a global or regional beam encompassing all
392
Chapter Fourteen
Figure 14.16
Start of receive frame (SORF) marker in a time burst plan.
TLFeBOOK

## Page 403
