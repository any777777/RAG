---
chunk_id: "book-ca4fca8dd8-chunk-1301"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1301
confidence: "first-pass"
extraction_method: "structured-local"
---

794
Chapter 21
Learning Probabilistic Models
Continuing with the other seven kinds of candy in the table of counts, we obtain θ(1) =0.6124.
Now let us consider the other parameters, such as θF1. In the fully observable case, we
would estimate this directly from the observed counts of cherry and lime candies from bag 1.
The expected count of cherry candies from bag 1 is given by
∑
j:Flavor j =cherry
P(Bag=1|Flavor j =cherry,wrapper j,holesj).
Again, these probabilities can be calculated by any Bayes net algorithm. Completing this
process, we obtain the new values of all the parameters:
θ(1) =0.6124, θ(1)
F1 =0.6684,
θ(1)
W1 =0.6483, θ(1)
H1 =0.6558,
θ(1)
F2 =0.3887, θ(1)
W2 =0.3817, θ(1)
H2 =0.3827.
(21.11)
The log likelihood of the data increases from about −2044 initially to about −2021 after
the ﬁrst iteration, as shown in Figure 21.13(b). That is, the update improves the likelihood
itself by a factor of about e23 ≈1010. By the tenth iteration, the learned model is a better
ﬁt than the original model (L= −1982.214). Thereafter, progress becomes very slow. This
is not uncommon with EM, and many practical systems combine EM with a gradient-based
algorithm such as Newton–Raphson (see Chapter 4) for the last phase of learning.
The general lesson from this example is that the parameter updates for Bayesian net-
▶
work learning with hidden variables are directly available from the results of inference on
each example. Moreover, only local posterior probabilities are needed for each parameter.
Here, “local” means that the conditional probability table (CPT) for each variable Xi can be
learned from posterior probabilities involving just Xi and its parents Ui. Deﬁning θi jk to be the
CPT parameter P(Xi =xij |Ui =uik), the update is given by the normalized expected counts
as follows:
θijk ←ˆN(Xi =xij,Ui =uik)/ ˆN(Ui =uik).
The expected counts are obtained by summing over the examples, computing the probabili-
ties P(Xi =xij,Ui =uik) for each by using any Bayes net inference algorithm. For the exact
algorithms—including variable elimination—all these probabilities are obtainable directly as
a by-product of standard inference, with no need for extra computations speciﬁc to learning.
Moreover, the information needed for learning is available locally for each parameter.
Standing back a little, we can think about what the EM algorithm is doing in this exam-
ple as recovering seven parameters (θ, θF1, θW1, θH1, θF2, θW2, θH2) from seven (23 −1)
observed counts in the data. (The eighth count is ﬁxed by the fact that the counts sum to
1000.) If each candy were described by two attributes rather than three (say, omitting the
holes), we would have had ﬁve parameters (θ, θF1, θW1, θF2, θW2) but only three (22 −1)
observed counts. In such a case it is not possible to recover the mixture weight θ or the char-
acteristics of the two bags that were mixed together. We say that the two-attribute model is
not identiﬁable.
Identiﬁability
Identiﬁability in Bayesian networks is a tricky issue. Note that even with three attributes
and seven counts, we cannot uniquely recover the model, because there are two observation-
ally equivalent models with the Bag variable ﬂipped. Depending on how the parameters are
initialized, EM will converge either to a model where bag 1 has mostly cherry and bag 2
mostly lime, or vice versa. This kind if non-identiﬁability is unavoidable with variables that
are never observed.
