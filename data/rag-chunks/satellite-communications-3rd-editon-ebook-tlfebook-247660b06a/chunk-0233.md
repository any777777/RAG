---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0233"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 233
confidence: "first-pass"
extraction_method: "structured-local"
---

coding is employed, the distinction between Pe and BER becomes impor-
tant. Pe is still determined by conditions at the input, but the error con-
trol will, if properly implemented, make the probability of bit error at the
output (the BER) less than that at the input. Error control coding applies
only to digital signals, and in most cases the signal is in binary form,
where the message symbols are bits, or logic 1s and 0s.
Encoding refers to the process of adding coding bits to the uncoded
bit stream, and decoding refers to the process of recovering the original
(uncoded) bit stream from the coded bit stream. Both processes are usu-
ally combined in one unit termed a codec.
11.2
Linear Block Codes
A block code requires that the message stream be partitioned into
blocks of bits (considering only binary messages at this stage). Let each
block contain k bits, and let these k bits define a dataword. The num-
ber of datawords is 2k. There is no redundancy in the system, meaning
that even a single bit error in transmission would convert one dataword
into another, which of course would constitute an error.
The datawords can be encoded into codewords which consist of n bits,
where n  k  r. The additional r bits are derived from the message bits
but are not part of the message. The number of possible codewords is
2n, but only 2k of these will contain datawords, and these are the ones
that are transmitted. It follows that the rest of the codewords are
redundant, but only in the sense that they do not contribute to the mes-
sage. (The r additional bits are referred to as redundant bits and are
also known as parity check bits.) If now errors occur in transmission,
there is high probability that they will convert the permissible code-
words into one or another of the redundant words that the decoder at
the receiver is designed to recognize as an error. It will be noted that
the term high probability is used. There is always the possibility, how-
ever remote, that enough errors occur to transform a transmitted code-
word into another legitimate codeword in error.
As a matter of definition, a code is termed linear when any linear
combination of two codewords is also a codeword. For binary codewords
in particular, the linear operation encountered is modulo-2 addition.
All codes encountered in practice are linear, which has a bearing on the
theoretical development (see, for example Proakis and Salehi, 1994).
The definition is given here for completeness. The theoretical work is
not required because only the practical properties of interest in satel-
lite communications are described.
A repetition code illustrates some of the general properties of block
codes. In a repetition code, each bit is considered to be a dataword, in
effect, k  1. For n-redundancy encoding, the output of the encoder is n
284
Chapter Eleven
TLFeBOOK
