---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0237"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 237
confidence: "first-pass"
extraction_method: "structured-local"
---

in these symbols. Errors affecting a group of bits are most likely to
affect only one symbol that can be corrected by the R-S code.
Let the number of bits per symbol be k; then the number of possible
symbols is q  2k (referred to as a q-ary alphabet). Let K be the number
of symbols in a dataword and N be the number of symbols in a code-
word. Just as in the block code where k-bit datawords were mapped
into n-bit codewords, with the R-S code, datawords of K symbols are
mapped into codewords of N symbols. The additional N  K redundant
symbols are derived from the message symbols but are not part of the
message. The number of possible codewords is 2N, but only 2K of these
will contain datawords, and these are the ones that are transmitted. It
follows that the rest of the codewords are redundant, but only in the
sense that they do not contribute to the message. If now errors occur in
transmission, there is high probability that they will convert the per-
missible codewords into one or another of the redundant words that the
decoder at the receiver is designed to recognize as an error. It will be
noted that the term high probability is used. There is always the pos-
sibility, however remote, that enough errors occur to transform a trans-
mitted codeword into another legitimate codeword even though this
was not the one transmitted.
It will be observed that the wording of the preceding paragraph par-
allels that given in Sec. 11.2 on block codes, except that here the coding
is carried out on symbols. Some of the design rules for the R-S codes are
q  2k
N  q  1
2t  N  K
Here, t is the number of symbol errors that can be corrected. A simple
example will be given to illustrate these. Let k  2; then q  4, and
these four symbols may be labeled A, B, C, and D. In terms of the binary
symbols (bits) for this simple case, we could have A  00, B  01, C 
10, and D  11. One could imagine the binary numbers 00, 01, 10, and
11 being stored in memory locations labeled A, B, C, and D.
The number of symbols per codeword is N  q  1  3. Suppose that
t  1; then the rule 2t  N  K gives K  1; that is, there will be one
symbol per dataword. Hence the number of datawords is qK  4 (i.e., A,
B, C, or D), and the number of codewords is qN  43  64. These will
include permissible words of the form AP1P2, BP3P4, CP5P6, and DP7P8,
where P1P2, etc. are the parity symbols selected by the encoding rules
from the symbol alphabet A, B, C, and D. This process is illustrated in
Fig. 11.1.
At the decoder, these are the only words that are recognized as being
legitimate and can be decoded. The other possible codewords not
Error Control Coding
287
TLFeBOOK
