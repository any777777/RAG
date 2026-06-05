---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0236"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 236
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 300

11.3.1
Hamming codes
For an integer m  2, the k and n values are related as n  2m  1 and
k  n  m. Thus some of the permissible combinations are
m
n
k
2
3
1
3
7
4
4
15
11
5
31
26
6
63
57
7
127
120
It will be seen that the code rate rc  k/n approaches unity as m
increases, which leads to more efficient coding. However, only a single
error can be corrected with Hamming codes.
11.3.2
BCH codes
BCH stands for the names of the inventors, Bose, Chaudhuri, and
Hocquenghen. These codes can correct up to t errors, and where m is
any positive integer, the permissible values are n  2m  1 and k  n
 mt. The integers m and t are arbitrary, which gives the code designer
considerable flexibility in choice. Proakis and Salehi (1994) give an
extensive listing of the parameters for BCH codes, from which the fol-
lowing values have been obtained:
n
k
t
7
4
1
15
11
1
15
7
2
15
5
3
31
26
1
31
21
2
31
16
3
31
11
5
31
6
7
As usual, the code rate is rc  k/n.
11.3.3
Reed-Solomon codes
The codes described so far work well with errors that occur randomly
rather than in bursts. However, there are situations where errors do
occur in bursts; that is, a number of bits that are close together may
experience errors as a result of impulse-type noise or impulse-type
interference. Reed-Solomon (R-S) codes are designed to correct errors
under these conditions. Instead of encoding directly in bits, the bits are
grouped into symbols, and the datawords and codewords are encoded
286
Chapter Eleven
TLFeBOOK

## Page 301
