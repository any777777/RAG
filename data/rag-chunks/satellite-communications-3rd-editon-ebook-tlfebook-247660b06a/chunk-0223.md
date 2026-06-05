---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0223"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 223
confidence: "first-pass"
extraction_method: "structured-local"
---

10.6.3
Transmission rate and bandwidth
for PSK modulation
Equation (10.14), which shows the baseband signal p(t) multiplied onto
the carrier cos 
0t, is equivalent to double-sideband, suppressed-carri-
er modulation. The digital modulator circuit of Fig. 10.12a is similar to
the single-sideband modulator circuit shown in Fig. 9.2, the difference
being that after the multiplier, the digital modulator requires a band-
pass filter, while the analog modulator requires a single-sideband filter.
As shown in Fig. 9.1, the DSBSC spectrum extends to twice the high-
est frequency in the baseband spectrum. For BPSK modulation the lat-
ter is given by Eq. (10.11) with Rsym replaced with Rb:
BIF  2B  (1  ) Rb
(10.15)
Thus, for BPSK with a rolloff factor of unity, the IF bandwidth in hertz
is equal to twice the bit rate in bits per second.
As shown in the previous section, QPSK is equivalent to the sum of
two orthogonal BPSK carriers, each modulated at a rate Rb/2, and
therefore, the symbol rate is Rsym  Rb/2. The spectra of the two BPSK
modulated waves overlap exactly, but interference is avoided at the
receiver because of the coherent detection using quadrature carriers.
Equation (10.15) is modified for QPSK to
BIF  (1  ) Rsym
(10.16)

Rb
An important characteristic of any digital modulation scheme is
the ratio of data bit rate to transmission bandwidth. The units for
this ratio are usually quoted as bits per second per hertz (a dimen-
sionless ratio in fact because it is equivalent to bits per cycle). Note
that it is the data bit rate Rb and not the symbol rate Rsym which is
used.
For BPSK, Eq. (10.15) gives an Rb/BIF ratio of 1/(1  ), and for
QPSK, Eq. (10.16) gives an Rb/BIF ratio of 2/(1  ). Thus QPSK is twice
as efficient as BPSK in this respect. However, more complex equipment
is required to generate and detect the QSPK modulated signal.
10.6.4
Bit error rate for PSK modulation
Referring back to Fig. 10.13, the noise at the input to the receiver can
cause errors in the detected signal. The noise voltage, which adds to
the signal, fluctuates randomly between positive and negative values,
and thus the sampled value of signal plus noise may have the opposite
polarity to that of the signal alone. This would constitute an error in
(1  ) 

2
Digital Signals
271
TLFeBOOK

## Page 286
