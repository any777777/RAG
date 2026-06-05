---
chunk_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a-chunk-0242"
source_id: "satellite-communications-3rd-editon-ebook-tlfebook-247660b06a"
source_file: "New folder (3)/Satellite.Communications.3rd.Editon.eBook-TLFeBOOK.pdf"
source_type: "pdf"
topics:
  - "Satellite Communications"
  - "References and Textbooks"
chunk_index: 242
confidence: "first-pass"
extraction_method: "structured-local"
---

Decoding is a more difficult problem than encoding, and as the exam-
ple suggests, the search process could quickly become impracticable for
long messages. The Viterbi algorithm is used widely in practice for
decoding. An example of a commercially available codec is the CDV-
10MIC single-chip codec made by Signal Processors Limited (Signal
Processors, Ltd., 1990). The data sheet for this codec is shown in Fig.
11.4. The CDV-10MIC utilizes Viterbi decoding. It has a constraint
length of 7 and can be adjusted for code rates of 12, 23, and 34 by means
of what is termed punctured coding. With punctured coding, the basic
code is generated at code rate 12, but by selectively discarding some of
the output bits, other rates can be achieved (Mead, 2000). The advan-
tage is that a single encoder can be used for different rates.
11.5
Interleaving
The idea behind interleaving is to change the order in which the bits are
encoded so that a burst of errors gets dispersed across a number of code-
words rather than being concentrated in one codeword. Interleaving as
applied in block codes will be used here to illustrate the technique, but
it also can be used with convolutional coding (Taub and Schilling, 1986).
Figure 11.5a shows part of the data bit stream where for definiteness
292
Chapter Eleven
The CDV-10MIC is a single integrated circuit which implements all the functions
required for a constraint length 7, rate 1/2, and punctured 2/3 or 3/4 rate, convolu-
tional encoder, and Viterbi algorithm decoder. Important features of this chip are:
I Full decoder and encoder implementation for rates 1/2, 2/3, and 3/4
I Complies with INTELSAT IESS-308 and IESS-309 specifications
I Extremely low implementation margin
I No external components required for punctured code implementation
I Operates at all information rates up to 10 Mbits/s. Higher speed versions are
under development
I All synchronization circuits are included on chip. External connection of ambi-
guity state counter and ambiguity resolution inputs allows maximum application
flexibility
I Advanced synchronization detectors enable very rapid synchronization. Rate, 3/4
block and phase synchronization in less than 8200 information bits (5500 trans-
mitted symbols).
I Soft decision decoder inputs (3 bits, 8 levels)
I
Erasure inputs for implementing punctured codes at other rates
I
Path memory length options to optimize performance when implementing high-
rate punctured codes
I Error-monitoring facilities included on chip
I Synchronization detector outputs and control inputs to enable efficient synchro-
nization in higher-speed multiplexed structures.
Figure 11.4
Specifications for a single-chip Viterbi codec. (Courtesy of Signal Processors,
Ltd., Cambridge U.K.)
TLFeBOOK
