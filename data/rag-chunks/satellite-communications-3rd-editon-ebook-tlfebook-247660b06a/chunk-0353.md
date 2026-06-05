---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0353"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 353
confidence: "first-pass"
extraction_method: "structured-local"
---

vides the input to the shift register, and the chips are clocked through
at the clock rate Rch. The generator starts with all stages holding bina-
ry 1s, and the following states are as shown in the table in Fig. 14.34.
Stage 3 also provides the binary output sequence. The code waveform
generated from this code is shown in Fig. 14.34b.
Such codes are known as maximal sequence or m-sequence codes
because they utilize the maximum length sequence that can be gener-
ated. For Fig. 14.34a the maximum length sequence is 7 chips as shown.
In general, the shift register passes through all states (all combinations
of 1s and 0s in the register) except the all-zero state when generating a
maximal sequence code. Therefore, a code generator employing an n-
stage shift register can generate a maximum sequence of N chips, where
N  2n  1
(14.38)
The binary 1s and 0s are randomly distributed such that the code
exhibits noiselike properties. However, there are certain deterministic
features described below, and the codes are more generally known as
PN codes, which stands for pseudo-noise codes.
1. The number of binary 1s is given by
No. of 1s 
(14.39)
2n

2
422
Chapter Fourteen
1
2
3
1
1
1
1
1
1
1
1
0
1
1
0
1
0
1
1
1
0
0
0
0
1
0
1
0
1
1
0
2
3
Clock
Repeat
(a)
+
+V
–V
t
(b)
Figure 14.34
Generation of a 7-chip maximal sequence code.
TLFeBOOK

## Page 433
