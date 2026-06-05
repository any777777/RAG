---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0243"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 243
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 307

the bits are labeled from b1 to b24. These are fed into shift registers as
shown in Fig. 11.5b, where, again, for definiteness seven rows and six
columns are shown. Rather than encoding the rows, the columns are
encoded so that the parity bits fill up the last three rows. It will be seen,
therefore, that the bits are not encoded in the order in which they
appear in the data bit stream. The encoded bits are read out row by row
as shown in Fig. 11.5c. Row 4 is shown in detail. If now an error burst
occurs which changes bits b5, b4, and b3, these will appear as separate
errors in the encoded words formed by columns 2, 3, and 4. The words
formed by the column bits are encoded to correct single errors (in this
example), and therefore, the burst of errors has been corrected.
11.6
Concatenated Codes
Codes designed to correct for burst errors can be combined with codes
designed to correct for random errors, a process known as concatena-
Error Control Coding
293
b1
b2
b3
b23
b24
.  .  .
.  .  .
.  .  .
Time
(a)
(b)
(c)
Column No.
Row No.
1
2
3
4
5
6
b24
b23
b22
b21
b20
b19
1
b18
b17
b16
b15
b14
b13
2
b12
b11
b10
b9
b8
b7
3
b6
b5
b4
b3
b2
b1
4
c1
c4
c7
c10
c13
c16
5
c2
c5
c8
c11
c14
c17
6
c3
c6
c9
c12
c15
b18
7
Time
Row 6
Row 7
Row 5
Row 3
Row 2
Row 1
b1
b2
b3
b4
b5
b6
Row 4
Figure 11.5
Illustrating interleaving (see Sec. 11.5).
TLFeBOOK

## Page 308
