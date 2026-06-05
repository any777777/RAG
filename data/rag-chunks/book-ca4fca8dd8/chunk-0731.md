---
chunk_id: "book-ca4fca8dd8-chunk-0731"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 731
confidence: "first-pass"
extraction_method: "structured-local"
---

440
Chapter 13
Probabilistic Reasoning
13.2.3 Bayesian nets with continuous variables
Many real-world problems involve continuous quantities, such as height, mass, temperature,
and money. By deﬁnition, continuous variables have an inﬁnite number of possible values,
so it is impossible to specify conditional probabilities explicitly for each value. One way to
handle continuous variables is with discretization—that is, dividing up the possible values
Discretization
into a ﬁxed set of intervals. For example, temperatures could be divided into three categories:
(<0oC), (0oC−100oC), and (>100oC). In choosing the number of categories, there is a
tradeoff between loss of accuracy and large CPTs which can lead to slow run times.
Another approach is to deﬁne a continuous variable using one of the standard families
of probability density functions (see Appendix A). For example, a Gaussian (or normal)
distribution N(x;µ,σ2) is speciﬁed by just two parameters, the mean µ and the variance
σ2. Yet another solution—sometimes called a nonparametric representation—is to deﬁne
Nonparametric
the conditional distribution implicitly with a collection of instances, each containing speciﬁc
values of the parent and child variables. We explore this approach further in Chapter 19.
A network with both discrete and continuous variables is called a hybrid Bayesian net-
work. To specify a hybrid network, we have to specify two new kinds of distributions: the
Hybrid Bayesian
network
conditional distribution for a continuous variable given discrete or continuous parents; and the
conditional distribution for a discrete variable given continuous parents. Consider the simple
example in Figure 13.6, in which a customer buys some fruit depending on its cost, which
depends in turn on the size of the harvest and whether the government’s subsidy scheme is op-
erating. The variable Cost is continuous and has continuous and discrete parents; the variable
Buys is discrete and has a continuous parent.
For the Cost variable, we need to specify P(Cost|Harvest,Subsidy). The discrete par-
ent is handled by enumeration—that is, by specifying both P(Cost|Harvest,subsidy) and
P(Cost|Harvest,¬subsidy). To handle Harvest, we specify how the distribution over the cost
c depends on the continuous value h of Harvest. In other words, we specify the parameters
of the cost distribution as a function of h. The most common choice is the linear–Gaussian
Linear–Gaussian
conditional distribution, in which the child has a Gaussian distribution whose mean µ varies
linearly with the value of the parent and whose standard deviation σ is ﬁxed. We need two
distributions, one for subsidy and one for ¬subsidy, with different parameters:
P(c|h,subsidy) = N(c;ath+bt,σ2
t ) =
1
σt
√
2π
e−1
2

c−(at h+bt )
σt
2
P(c|h,¬subsidy) = N(c;af h+b f ,σ2
f ) =
1
σ f
√
2π
e
−1
2

c−(af h+b f )
σf
2
.
For this example, then, the conditional distribution for Cost is speciﬁed by naming the linear–
Gaussian distribution and providing the parameters at, bt, σt, af , bf , and σ f . Figures 13.7(a)
and (b) show these two relationships. Notice that in each case the slope of c versus h is
negative, because cost decreases as the harvest size increases. (Of course, the assumption of
linearity implies that the cost becomes negative at some point; the linear model is reasonable
only if the harvest size is limited to a narrow range.) Figure 13.7(c) shows the distribution
P(c|h), averaging over the two possible values of Subsidy and assuming that each has prior
probability 0.5. This shows that even with very simple models, quite interesting distributions
can be represented.
