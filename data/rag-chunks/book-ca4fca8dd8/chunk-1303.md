---
chunk_id: "book-ca4fca8dd8-chunk-1303"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1303
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 21.3
Learning with Hidden Variables: The EM Algorithm
795
P(R1|R0)
R0
P(R1|R0)
P(R1|R0)
P(R1|R0)
P(R1|R0)
R0
P(R2|R1)
R1
P(R3|R2)
R2
P(R4|R3)
R3
R1 P(U1|R1)
R1 P(U1|R1)
R2 P(U2|R2)
R3 P(U3|R3)
R4 P(U4|R4)
Rain4
Rain0
Rain1
Rain0
Rain1
Rain2
Rain3
Umbrella1
Umbrella1
Umbrella2
Umbrella3
Umbrella4
Figure 21.15 An unrolled dynamic Bayesian network that represents a hidden Markov
model (repeat of Figure 14.16).
21.3.3 Learning hidden Markov models
Our ﬁnal application of EM involves learning the transition probabilities in hidden Markov
models (HMMs). Recall from Section 14.3 that a hidden Markov model can be represented
by a dynamic Bayes net with a single discrete state variable, as illustrated in Figure 21.15.
Each data point consists of an observation sequence of ﬁnite length, so the problem is to
learn the transition probabilities from a set of observation sequences (or from just one long
sequence).
We have already seen how to learn Bayes nets, but there is a complication: in Bayes
nets, each parameter is distinct; in a hidden Markov model, on the other hand, the individual
transition probabilities from state i to state j at time t, θi jt =P(Xt+1 = j|Xt =i), are repeated
across time—that is, θijt =θij for all t. To estimate the transition probability from state i to
state j, we simply calculate the expected proportion of times that the system undergoes a
transition to state j when in state i:
θi j ←∑
t
ˆN(Xt+1 = j,Xt =i)/∑
t
ˆN(Xt =i).
The expected counts are computed by an HMM inference algorithm. The forward–backward
algorithm shown in Figure 14.4 can be modiﬁed very easily to compute the necessary prob-
abilities. One important point is that the probabilities required are obtained by smoothing
rather than ﬁltering. Filtering gives the probability distribution of the current state given the
past, but smoothing gives the distribution given all evidence, including what happens after
a particular transition occurred. The evidence in a murder case is usually obtained after the
crime (i.e., the transition from state i to state j) has taken place.
21.3.4 The general form of the EM algorithm
We have seen several instances of the EM algorithm. Each involves computing expected
values of hidden variables for each example and then recomputing the parameters, using the
expected values as if they were observed values. Let x be all the observed values in all the
examples, let Z denote all the hidden variables for all the examples, and let θ be all the
parameters for the probability model. Then the EM algorithm is
θ(i+1) = argmax
θ
∑
z
P(Z=z|x,θ(i))L(x,Z=z|θ).
