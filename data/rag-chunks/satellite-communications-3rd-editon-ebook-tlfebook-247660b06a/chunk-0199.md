---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0199"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 199
confidence: "first-pass"
extraction_method: "structured-local"
---

9.6.6
Noise weighting
Another factor that generally improves the postdetection signal-to-
noise ratio is referred to as noise weighting. This is the way in which
the flat noise spectrum has to be modified to take into account the fre-
quency response of the output device and the subjective effect of noise
as perceived by the observer. For example, human hearing is less sen-
sitive to a given noise power density at low and high audio frequencies
than at the middle frequency range.
Weighting curves have been established for various telephone hand-
sets in use by different telephone administrations. One of these, the
CCIR curve, is referred to as the psophometric weighting curve. When
this is applied to the flat noise density spectrum, the noise power is
reduced by 2.5 dB for a 3.1-kHz bandwidth (300–3400 Hz) compared
with flat noise over the same bandwidth. The weighting improvement
factor is denoted by [W], and hence for the CCIR curve [W]  2.5 dB.
(Do not confuse the symbol W here with that used for bandwidth ear-
lier.) For a bandwidth of b kHz, a simple adjustment gives
[W]  2.5  10 log 
 2.41  [b]
(9.14)
Here, b is in kilohertz. A noise weighting factor also can be applied
to TV viewing. The CCIR weighting factors are 11.7 dB for 525-line TV
and 11.2 dB for 625-line TV. Taking weighting into account, Eq. (9.13)
becomes
      [GP]  [P]  [W]
(9.15)
9.6.7
S/N and bandwidth for FDM/FM
telephony
In the case of FDM/FM, the receiver processing gain, excluding
emphasis and noise weighting, is given by (see, e.g., Miya, 1980, and
Halliwell, 1974)
GP 


2
(9.16)
Here, fm is a specified baseband frequency in the channel of interest,
at which GP is to be evaluated. For example, fm may be the center fre-
quency of a given channel, or it may be the top frequency of the base-
band signal. The channel bandwidth is b (usually 3.1 kHz), and Frms
is the root-mean-square deviation per channel of the signal. The rms
Frms

fm
BIF

b
C

N
S

N
b

3.1
Analog Signals
243
TLFeBOOK

## Page 258
