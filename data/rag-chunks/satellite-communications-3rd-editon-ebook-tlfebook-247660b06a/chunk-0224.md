---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0224"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 224
confidence: "first-pass"
extraction_method: "structured-local"
---

the received pulse. The noise can be represented by a source at the
front of the receiver, shown in Fig. 10.13 (this is considered in more
detail in Chap. 12). It is seen that the noise is filtered by the receiver
input filter. Thus the receive filter, in addition to contributing to min-
imizing the ISI, must minimize noise while maximizing the received
signal. In short, it must maximize the received signal-to-noise ratio. In
practice for satellite links (or radio links), this usually can be achieved
by making the transmit and receive filters identical, each having a fre-
quency response which is the square root of the raised-cosine response.
Having identical filters is an advantage from the point of view of man-
ufacturing.
The most commonly encountered type of noise has a flat frequency
spectrum, meaning that the noise power spectrum density, measured
in joules (or watts per hertz), is constant. The noise spectrum density
will be denoted by No. When the filtering is designed to maximize the
received signal-to-noise ratio, the maximum signal-to-noise voltage
ratio is found to be equal to 2Eb/N
o, where Eb is the average bit ener-
gy. The average bit energy can be calculated knowing the average
received power PR and the bit period Tb:
Eb  PRTb
(10.17)
The probability of the detector making an error as a result of noise
is given by
Pe 
erfc
(10.18)
where erfc stands for complementary error function, whose value is
available in tabular or graphic form in books of mathematical tables
and as built-in functions in computational packages such as Mathcad.
In Mathcad, the error function denoted by erf (x) is provided, and
erfc (x)  1  erf (x)
(10.19)
Equation (10.18) applies for polar NRZ baseband signals and for
BPSK and QPSK modulation systems. The probability of bit error is
also referred to as the bit error rate (BER). A Pe  106 signifies a BER
of 1 bit in a million, on average. The graph of Pe versus Eb/No in deci-
bels is shown in Fig. 10.17. Note carefully that the energy ratio, not
the decibel value, of Eb/No must be used in Eq. (10.18). This is illus-
trated in the following Mathcad example.
Example 10.1
The average power received in a binary polar transmission
is 10 mW, and the bit period is 100 s. If the noise power spectral density is
0.1 J, and optimum filtering is used, determine the bit error rate.
Eb

No
12
272
Chapter Ten
TLFeBOOK

## Page 287
