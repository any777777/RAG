---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0239"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 239
confidence: "first-pass"
extraction_method: "structured-local"
---

formed by the rules but which may be formed by transmission errors
will be detected as errors and corrected. It will be observed that a code-
word consists of 6 bits, and one or more of these in error will result in
a symbol error. The R-S code is capable of correcting this symbol error,
which in this simple illustration means that a burst of up to 6 bit errors
can be corrected.
R-S codes do not provide efficient error correction where the errors
are randomly distributed as distinct from occurring in bursts (Taub
and Schilling, 1986). To deal with this situation, codes may be joined
together or concatenated, one providing for random error correction
and one for burst error correction. Concatenated codes are described in
Sec. 11.6.
It should be noted that although the encoder and decoder in R-S codes
operate at the symbol level, the signal may be transmitted as a bit
stream, but it is also suitable for transmission with multilevel modula-
tion, the levels being determined by the symbols. The code rate is rc 
K/N, and the code is denoted by (N, K). In practice, it is often the case
that the symbols are bytes consisting of 8 bits; then q  28  256, and N
 q  1  255. With t  8, a NASA-standard (255, 239) R-S code results.
Shortened R-S codes employ values N′  N  l and K′  K  l and
are denoted as (N′, K′). For example, DirecTV (see Chap. 16) utilizes a
shortened R-S code for which l  109, and digital video broadcast
(DVB) utilizes one for which l  51 (Mead, 2000). These codes are
designed to correct up to t  8 symbol errors.
11.4
Convolution Codes
Convolution codes are also linear codes. A convolution encoder consists
of a shift register which provides temporary storage and a shifting
operation for the input bits and exclusive-OR logic circuits which gen-
erate the coded output from the bits currently held in the shift register.
In general, k data bits may be shifted into the register at once, and n
code bits generated. In practice, it is often the case that k  1 and n 
2, giving rise to a rate 12 code. A rate 12 encoder is illustrated in Fig.
11.2, and this will be used to explain the encoding operation.
Initially, the shift register holds all binary 0s. The input data bits are
fed in continuously at a bit rate Rb, and the shift register is clocked at
this rate. As the input moves through the register, the rightmost bit is
shifted out so that there are always 3 bits held in the register. At the
end of the message, three binary 0s are attached, to return the shift
register to its initial condition. The commutator at the output is
switched at twice the input bit rate so that two output bits are gener-
ated for each input bit shifted in. At any one time the register holds 3
bits which form the inputs to the exclusive-OR circuits.
Error Control Coding
289
TLFeBOOK
