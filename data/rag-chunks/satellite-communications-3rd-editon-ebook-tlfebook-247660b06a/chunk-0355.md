---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0355"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 355
confidence: "first-pass"
extraction_method: "structured-local"
---

As a somewhat simpler example, consider the case when n  3. In
this instance, N  7. There is only one prime factor, 7 itself, and
therefore
(7)  7 	
 6
Smax 
 2
In this case there are only two distinct maximal sequences.
14.10.3
The autocorrelation function for
c(t)
One of the most important properties of c(t) is its autocorrelation func-
tion. The autocorrelation function is a measure of how well a time-shift-
ed version of the waveform compares with the unshifted version. Figure
14.35a shows how the comparison may be made. The c(t) waveform is
multiplied with a shifted version of itself, c(t  ), and the output is
averaged (shown by the integrator). The average, of course, is indepen-
dent of time t (the integrator integrates out the time-t dependence), but
it will depend on the time lead or lag introduced by . When the wave-
forms are coincident,   0, and the average output is a maximum,
which for convenience will be normalized to 1. Any shift in time,
advance or delay, away from the   0 position will result in a decrease
in output voltage. A property of m-sequence code waveforms is that the
autocorrelation function decreases linearly from the maximum value
(unity in this case) to a negative level 1/N, as shown in Fig. 14.35b. The
very pronounced peak in the autocorrelation function provides the chief
means for acquiring acquisition and tracking so that the locally gener-
ated m-sequence code can be synchronized with the transmitted version.
(7)

n
67
424
Chapter Fourteen
c(t)
c(t-)


(a)
(b)
–Tch
Tch
0
–1
TN
N
N
Figure 14.35
(a) Generating the autocorrelation function; (b) the autocorrelation
waveform.
TLFeBOOK

## Page 435
