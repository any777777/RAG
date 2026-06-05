---
chunk_id: "book-ca4fca8dd8-chunk-0833"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 833
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 14.5
Dynamic Bayesian Networks
503
Figure 14.12 A bird ﬂying toward a tree (top views). (a) A Kalman ﬁlter will predict the
location of the bird using a single Gaussian centered on the obstacle. (b) A more realistic
model allows for the bird’s evasive action, predicting that it will ﬂy to one side or the other.
14.5 Dynamic Bayesian Networks
Dynamic Bayesian networks, or DBNs, extend the semantics of standard Bayesian networks
Dynamic Bayesian
network
to handle temporal probability models of the kind described in Section 14.1. We have already
seen examples of DBNs: the umbrella network in Figure 14.2 and the Kalman ﬁlter network
in Figure 14.9. In general, each slice of a DBN can have any number of state variables Xt
and evidence variables Et. For simplicity, we assume that the variables, their links, and their
conditional distributions are exactly replicated from slice to slice and that the DBN represents
a ﬁrst-order Markov process, so that each variable can have parents only in its own slice or
the immediately preceding slice. In this way, the DBN corresponds to a Bayesian network
with inﬁnitely many variables.
It should be clear that every hidden Markov model can be represented as a DBN with
a single state variable and a single evidence variable. It is also the case that every discrete-
variable DBN can be represented as an HMM; as explained in Section 14.3, we can combine
all the state variables in the DBN into a single state variable whose values are all possible
tuples of values of the individual state variables. Now, if every HMM is a DBN and every
DBN can be translated into an HMM, what’s the difference? The difference is that, by de- ◀
composing the state of a complex system into its constituent variables, we can take advantage
of sparseness in the temporal probability model.
To see what this means in practice, remember that in Section 14.3 we said that an HMM
representation for a temporal process with n discrete variables, each with up to d values,
needs a transition matrix of size O(d2n). The DBN representation, on the other hand, has size
O(ndk) if the number of parents of each variable is bounded by k. In other words, the DBN
representation is linear rather than exponential in the number of variables. For the vacuum
robot with 42 possibly dirty locations, the number of probabilities required is reduced from
5×1029 to a few thousand.
We have already explained that every Kalman ﬁlter model can be represented in a DBN
with continuous variables and linear–Gaussian conditional distributions (Figure 14.9). It
should be clear from the discussion at the end of the preceding section that not every DBN
can be represented by a Kalman ﬁlter model. In a Kalman ﬁlter, the current state distribution
