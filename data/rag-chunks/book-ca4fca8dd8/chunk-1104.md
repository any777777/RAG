---
chunk_id: "book-ca4fca8dd8-chunk-1104"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1104
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 18.4
Programs as Probability Models
661
Figure 18.12 The top panel shows twelve degraded images produced by executing the gen-
erative program from Figure 18.11. The number of letters, their identities, the amount of
additive noise, and the speciﬁc pixel-wise noise are all part of the domain of the probability
model. The bottom panel shows twelve degraded images produced by executing the genera-
tive program from Figure 18.15. The Markov model for letters typically yields sequences of
letters that are easier to pronounce.
18.4.2 Syntax and semantics
A generative program is an executable program in which every random choice deﬁnes a
Generative program
random variable in an associated probability model. Let us imagine unrolling the execution
of a program that makes random choices, step by step. Let Xi be the random variable corre-
sponding to the ith random choice made by the program; as usual, xi denotes a possible value
of Xi. Let us call ω = {xi} an execution trace of the generative program—that is, a sequence
Execution trace
of possible values for the random choices. Running the program once generates one such
trace, hence the term “generative program.”
The space of all possible execution traces Ωcan be viewed as the sample space of a
probability model deﬁned by the generative program. The probability distribution over traces
can be deﬁned as the product of the probabilities of each individual random choice: P(ω) =
∏i P(xi|x1,...xi−1). This is analogous to the distribution over worlds in an OUPM.
It is conceptually straightforward to convert any OUPM into a corresponding generative
program. This generative program makes random choices for each number statement and for
the value of each basic random variable whose existence is implied by the number statements.
The main extra work that the generative program needs to do is to create data structures that
represent the objects, functions, and relations of the possible worlds in the OUPM. These
data structures are created automatically by the OUPM inference engine because the OUPM
assumes that every possible world is a ﬁrst-order model structure, whereas a typical PPL
makes no such assumption.
The images in Figure 18.12 can be used to get an intuitive understanding of the probabil-
ity distribution P(Ω): we see varying levels of noise, and in the less noisy images, we also
see sequences of letters of varying lengths. Let ω1 be the trace corresponding to the image
in the top right corner of this ﬁgure, containing the letters ocflwe. If we unrolled this trace
ω1 into a Bayesian network, it would have 4,104 nodes: 1 node for the variable n; 6 nodes
for the variables letters[i]; 1 node for the noise variance; and 4,096 nodes for the pixels in
noisy image. We thus see that this generative program deﬁnes an open-universe probability
model: the number of random choices it makes is not bounded a priori, but instead depends
on the value of the random variable n.
