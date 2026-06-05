---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0358"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 358
confidence: "first-pass"
extraction_method: "structured-local"
---

the autocorrelation, and this requires careful selection of the spread-
ing functions used in the overall system (see, for example, Dixon,
1984).
14.10.4
Spectrum spreading and despread-
ing
In Sec. 10.6.3 the idea of bandwidth for PSK modulation was intro-
duced. In general, for a BPSK signal at a bit rate Rb, the main lobe of
the power-density spectrum occupies a bandwidth extending from fc 
Rb to fc  Rb. This is sketched in Fig. 14.38a. A similar result applies
when the modulation signal is c(t), the power density spectrum being
as sketched in Fig. 14.38b. It should be mentioned here that because
c(t) exhibits periodicity, the spectrum density will be a line function,
and Fig. 14.38b shows the envelope of the spectrum. The spectrum
shows the power density (watts per hertz) in the signal. For constant
carrier power, it follows that if a signal is forced to occupy a wider
bandwidth, its spectrum density will be reduced. This is a key result
in CDMA systems. In all direct-sequence spread-spectrum systems,
the chip rate is very much greater than the information bit rate, or Rch
% Rb. The bandwidth is determined mainly by Rch so that the power
density of the signal described by Eq. (14.34) is spread over the band-
width determined by Rch. The power density will be reduced approxi-
mately in the ratio of Rch to Rb.
Assuming then that acquisition and tracking have been accom-
plished, c(t) in the receiver (Fig. 14.33) performs in effect a despread-
ing function in that it restores the spectrum of the wanted signal to
what it was before the spreading operation in the transmitter. This is
Satellite Access
427
W/Hz
W/Hz
fc–Rb
fc–Rch
fc+Rb
fc+Rch
fc
fc
(a)
(b)
Figure 14.38
Spectrum for a BPSK signal: (a) without spreading, (b) with spreading.
TLFeBOOK

## Page 438
