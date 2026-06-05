---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0356"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 356
confidence: "first-pass"
extraction_method: "structured-local"
---

14.10.3
Acquisition and tracking
One form of acquisition circuit that makes use of the autocorrela-
tion function is shown in Fig. 14.36. The output from the first mul-
tiplier is
e(t)  c(t  !) c(t) p(t) cos 
Dt
 c(t  !) c(t) cos [
Dt  (t) ]
(14.44)
Here, the information modulation, which is BPSK, is shown as (t) so
that the effect of the following bandpass filter (BPF) on the amplitude
can be more clearly seen. The BPF has a passband centered on 
D,
wide with respect to the information modulation but narrow with
respect to the code signal. It performs the amplitude-averaging func-
tion on the code signal product (see Maral and Bousquet, 1998). The
averaging process can be illustrated as follows. Consider the product
of two cosine terms and its expansion:
cos 
t cos (
t  ) 
{ cos [
t  (
t  ) ]  cos [
t  (
t  ) ] }

[cos (2
t  )  cos () ]
(14.45)
The BPF will reject the high-frequency component, leaving only the
average component 12 cos(). This signal may be considered analogous
to the c(t)c(t  !) term in Eq. (14.44). The envelope detector following
the BPF produces an output proportional to the envelope of the signal,
that is, to the average value of c(t)c(t  !). This is a direct measure of
the autocorrelation function. When it is less than the predetermined
threshold VT required for synchronism, the time shift ! incremented.
12
12
Satellite Access
425
c(t)p(t)cos
Dt
c(t-!)
VT
BPF
Envelope
detector
Threshold
detector
!
shift
PN
GEN
VAVG
VAVG<VT
VAVG>VT
Enable
tracking
Autocorrelator
To coherent
detector
X
X
Figure 14.36
Acquisition of a carrier in a CDMA system.
TLFeBOOK

## Page 436
