---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0246"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 246
confidence: "first-pass"
extraction_method: "structured-local"
---

sions for error probabilities as given by Eqs. (11.4) and (11.5) can be
used. Denoting by BERU the bit error rate after demodulation for the
uncoded message and by BERC the bit error rate for the coded message
after demodulation and decoding, then for the uncoded message
BERU  PeU
(11.6)
Certain codes known as perfect codes can correct errors up to some
number t. The bit error rate for such codes is given by (see, for exam-
ple, Roddy and Coolen, 1996)
BERC 
(PeC)t  1
(11.7)
where x!  x(x  1)(x 2)…3.2.1. The Hamming codes are perfect codes
that can correct one error. For this class of codes and with t  1, Eq.
(11.7) simplifies to
BERC  (n  1) PeC
2
(11.8)
A plot of BERC and BERU against [Eb/No] is shown in Fig. 11.8 for the
Hamming (7, 4) code. The crossover point occurs at about 4 dB, so for
the coding to be effective, [Eb/No] must be higher than this. Also, from
the graph, for a BER of 105, the [Eb/No] is 9 dB for the uncoded mes-
sage and 9.6 dB for the coded message. Therefore, at this BER value
the Hamming code is said to provide a coding gain of 0.6 dB.
Some values for coding gains given in Taub and Schilling (1986) are
block codes, 3 to 5 dB; convolutional coding with Viterbi decoding, 4 to
5.5 dB; concatenated codes using R-S block codes and convolutional
decoding with Viterbi decoding, 6.5 to 7.5 dB. These values are for a Pe
value of 105 and using hard decision decoding as described in the next
section.
11.9
Hard Decision and Soft Decision
Decoding
With hard decision decoding, the output from the optimum demodula-
tor is passed to a threshold detector that generates a “clean” signal, as
shown in Fig. 11.9a. Using triple redundancy again as an example, the
two codewords would be 111 and 000. For binary polar signals, these
might be represented by voltage levels 1 V 1 V 1 V and 1 V 1 V 1
V. The threshold level for the threshold detector would be set at 0 V. If
now the sampled signal from the optimum demodulator is 0.5 V 0.7 V
2 V, the output from the threshold detector would be 1 V 1 V 1 V,
and the decoder would decide that this was a binary 1 1 0 codeword and
(n  1)!

t! (n  1  t)!
Error Control Coding
297
TLFeBOOK

## Page 312
