---
chunk_id: "book-ca4fca8dd8-chunk-0701"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 701
confidence: "first-pass"
extraction_method: "structured-local"
---

420
Chapter 12
Quantifying Uncertainty
can also be used (see Exercise 12.PXYZ). Section 12.4 showed that absolute independence
assertions allow a decomposition of the full joint distribution into much smaller pieces. It
turns out that the same is true for conditional independence assertions. For example, given
the assertion in Equation (12.19), we can derive a decomposition as follows:
P(Toothache,Catch,Cavity)
= P(Toothache,Catch|Cavity)P(Cavity)
(product rule)
= P(Toothache|Cavity)P(Catch|Cavity)P(Cavity)
(using 12.19).
(The reader can easily check that this equation does in fact hold in Figure 12.3.) In this
way, the original large table is decomposed into three smaller tables. The original table has
7 independent numbers. (The table has 23 =8 entries, but they must sum to 1, so 7 are
independent). The smaller tables contain a total of 2+2+1=5 independent numbers. (For
a conditional probability distribution such as P(Toothache|Cavity) there are two rows of two
numbers, and each row sums to 1, so that’s two independent numbers; for a prior distribution
such as P(Cavity) there is only one independent number.) Going from 7 to 5 might not seem
like a major triumph, but the gains can be much greater with larger number of symptoms.
In general, for n symptoms that are all conditionally independent given Cavity, the size
of the representation grows as O(n) instead of O(2n). That means that conditional indepen-
▶
dence assertions can allow probabilistic systems to scale up; moreover, they are much more
commonly available than absolute independence assertions. Conceptually, Cavity separates
Separation
Toothache and Catch because it is a direct cause of both of them. The decomposition of
large probabilistic domains into weakly connected subsets through conditional independence
is one of the most important developments in the recent history of AI.
12.6 Naive Bayes Models
The dentistry example illustrates a commonly occurring pattern in which a single cause di-
rectly inﬂuences a number of effects, all of which are conditionally independent, given the
cause. The full joint distribution can be written as
P(Cause,Effect1,...,Effectn) = P(Cause)∏
i
P(Effecti |Cause).
(12.20)
Such a probability distribution is called a naive Bayes model—“naive” because it is often
Naive Bayes
used (as a simplifying assumption) in cases where the “effect” variables are not strictly inde-
pendent given the cause variable. (The naive Bayes model is sometimes called a Bayesian
classiﬁer, a somewhat careless usage that has prompted true Bayesians to call it the idiot
Bayes model.) In practice, naive Bayes systems often work very well, even when the condi-
tional independence assumption is not strictly true.
To use a naive Bayes model, we can apply Equation (12.20) to obtain the probability of
the cause given some observed effects. Call the observed effects E=e, while the remaining
effect variables Y are unobserved. Then the standard method for inference from the joint
distribution (Equation (12.9)) can be applied:
P(Cause|e) = α∑
y
P(Cause,e,y).
