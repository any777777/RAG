---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0226"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 226
confidence: "first-pass"
extraction_method: "structured-local"
---

Hence
[C/No]  77.85  9.5  87.35 dBHz
The equations giving the probability of bit error are derived on the
basis that the filtering provides maximum signal-to-noise ratio. In
practice, there are a number of reasons why the optimal filtering may
not be achieved. The raised-cosine response is a theoretical model that
can only be approximated in practice. Also, for economic reasons, it is
desirable to use production filters manufactured to the same specifi-
cations for the transmit and receive filter functions, and this may
result in some deviation from the desired theoretical response. The
usual approach in practice is that one knows the BER that is accept-
able for a given application. The corresponding ratio of bit energy to
noise density can then be found from Eq. (10.18) or from a graph such
as that shown in Fig. 10.17. Once the theoretical value of Eb/No is
found, an implementation margin, amounting to a few decibels at
most, is added to allow for imperfections in the filtering. This is illus-
trated in the following example.
Example 10.3
A BPSK satellite digital link is required to operate with a
bit error rate of no more than 105, the implementation margin being 2 dB.
Calculate the required Eb/No ratio in decibels.
solution
The graph of Fig. 10.17 shows that Eb/No is around 9 dB for a
BER of 105. By plotting this region to an expanded scale, a more accurate
value of Eb/No can be obtained. For ease of presentation, the Eb/No ratio will
be denoted by x. A suitable range for x is
x:  8, 8.2.. 10
In decibels, this is
xdB (x) :  10  log (x)
Equation (10.18) gives
Pe (x) :  .5  1  erf x 
This is plotted in Fig. 10.18, from which Eb/No is seen to be close to 9.6 dB.
This is without an implementation margin. The required value, including
an implementation margin, is 9.6  2  11.6 dB.
To summarize, BER is a specified requirement, which enables Eb/No
to be determined by using Eq. (10.18) or Fig. 10.17. The rate Rb also
will be specified, and hence the [C/No] ratio can be found by using Eq.
(10.24). The [C/No] ratio is then used in the link budget calculations,
as described in Chap. 12.
Digital Signals
275
TLFeBOOK

## Page 290

9
1•10–4
1•10–5
1•10–6
9.2
Pe(x)
9.4
xdB(x)
9.6
9.8
10
Figure 10.18
Solution to Example 10.3.
Figure 10.19
(a) Use of optimum terminal filter to maximize the signal-to-
noise voltage ratio; (b) plot of Eq. (10.25).
276
TLFeBOOK

## Page 291
