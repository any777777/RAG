---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0235"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 235
confidence: "first-pass"
extraction_method: "structured-local"
---

bits, identical to the input bit. As an example, consider the situation
when n  3. A binary 1 at the input to the encoder results in a 111 code-
word at the output, and a binary 0 at the input results in a 000 code-
word at the output. At the receiver, the logic circuits in the decoder
produce a 1 when 111 is present at the input and a 0 when 000 is pre-
sent. It is assumed that synchronization is maintained between
encoder and decoder. If a codeword other than 111 or 000 is received,
the decoder detects an error and can request a retransmission (ARQ).
Forward error correction (FEC) can take place on the basis of a
“majority vote.” In this case, the logic circuits in the decoder are
designed to produce a 1 at the output whenever two or three 1s occur
in the received codeword (codewords 111, 101, 011, and 110) and a 0
whenever two or three 0s appear in the codeword (codewords 000, 001,
010, and 100). An odd number of “repeats” is used to avoid a tied vote.
Errors can still get through if the noise results in two or three suc-
cessive errors in a codeword. For example, if the noise changes a 111
into a 000 or a 000 into a 111, the output will be in error whether error
detection or forward error correction (FEC) is used. If two errors occur
in a codeword, then the “majority vote” method for FEC will result in
an error. However, the probability of two or three consecutive errors
occurring is very much less than the probability of a single error. This
assumes that the bit energy stays the same, an aspect that is discussed
in Sec. 11.7.
The code rate rc is defined as the ratio of dataword bits to codeword bits
(note that although it is called a rate, it is not a rate in bits per second):
rc 
(11.1)
For a given level of performance (i.e., number of errors detected or cor-
rected), the greater the code rate, the more efficient is the code. Codes
that are more efficient than repetitive encoding are used in practice.
11.3
Cyclic Codes
Cyclic codes are a subclass of linear block codes. They possess the prop-
erty that a cyclic shift of a codeword is also a codeword. For example, if
a codeword consists of the elements {c1 c2 c3 c4 c5 c6 c7}, then {c2 c3 c4 c5 c6
c7 c1} is also a codeword. The advantage of cyclic codes is that they are
easily implemented in practice through the use of shift registers and
modulo-2 adders. Cyclic codes are widely used in satellite transmis-
sion, and the properties of the most important of these are summarized
in the following sections. Only certain combinations of k and n are per-
mitted in these codes. As pointed out in Taub and Schilling (1986), a
code is an invention, and these codes are named after their inventors.
k
n
Error Control Coding
285
TLFeBOOK
