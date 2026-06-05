---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0221"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 221
confidence: "first-pass"
extraction_method: "structured-local"
---

The QPSK signal has many features in common with BPSK and will
be examined before describing in detail the carrier and bit timing
recovery circuits and the effects of noise.
10.6.2
Quadrature phase-shift keying
With quadrature phase-shift keying, the binary data are converted
into 2-bit symbols which are then used to phase modulate the carrier.
Since four combinations containing 2 bits are possible from a binary
alphabet (logical 1s and 0s), the carrier phase can be shifted to one of
four states.
Figure 10.14a shows one way in which QPSK modulation can be
achieved. The incoming bit stream p(t) is converted in the serial-to-
parallel converter into two binary streams. The conversion is illus-
trated by the waveforms of Fig. 10.14b. For illustration purposes, the
bits in the p(t) waveform are labeled a, b, c, d, e, and f. The serial-to-
parallel converter switches bit a to the I port and at the same time
switches bit b to the Q port. In the process, each bit duration is dou-
bled, so the bit rates at the I and Q outputs are half that of the input
bit rate.
The pi(t) bit stream is combined with a carrier cos 
0t in a BPSK
modulator, while the pq(t) bit stream is combined with a carrier sin 
0t,
also in a BPSK modulator. These two BPSK waveforms are added to
give the QPSK wave, the various combinations being shown in Table
10.1.
The phase-modulation angles are shown in the phasor diagram of
Fig. 10.15. Because the output from the I port modulates the carrier
directly, it is termed the in-phase component, and hence the designa-
tion I. The output from the Q port modulates a quadrature carrier, one
268
Chapter Ten
Figure 10.13
Block schematic of a coherent detector showing the carrier recovery section
and the bit timing recovery.
TLFeBOOK

## Page 283

Digital Signals
269
Figure 10.14
(a) QPSK modulator; (b) waveforms for (a).
TABLE 10.1
QPSK Modulator States
pi(t)
pq(t)
QPSK
1
1
cos 
0t  sin 
0t  2 cos (
0t  45°)
1
1
cos 
0t  sin 
0t  2 cos (
0t  45°)
1
1
cos 
0t  sin 
0t  2 cos (
0t  135°)
1
1
cos 
0t  sin 
0t  2 cos (
0t  135°)
TLFeBOOK

## Page 284
