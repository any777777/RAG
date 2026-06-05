---
chunk_id: "book-ca4fca8dd8-chunk-0749"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 749
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 13.4
Approximate Inference for Bayesian Networks
453
P(C=.5)
P(S|c)
.10
.50
C
t
f
P(W|s,r)
.99
.90
R
t
f
t
f
.90
.00
S
t
t
f
f
P(R|c)
.80
.20
C
t
f
Cloudy
WetGrass
Rain
Sprinkler
P(C=.5)
P(W|s+r)
.99
.90
.90
.00
S+R
t t
t f
f t
f f
P(S+R|c)
.08
.10
C
t
f
.02 .72 .18
.40 .10 .40
t t
t f
f t
f f
Sprinkler+Rain
Cloudy
WetGrass
(a)
(b)
Figure 13.15 (a) A multiply connected network describing Mary’s daily lawn routine: each
morning, she checks the weather; if it’s cloudy, she usually doesn’t turn on the sprinkler;
if the sprinkler is on, or if it rains during the day, the grass will be wet. Thus, Cloudy
affects WetGrass via two different causal pathways. (b) A clustered equivalent of the multiply
connected network.
ure 13.15(b). The two Boolean nodes are replaced by a meganode that takes on four possible
Meganode
values: tt, t f, ft, and f f. The meganode has only one parent, the Boolean variable Cloudy,
so there are two conditioning cases. Although this example doesn’t show it, the process of
clustering often produces meganodes that share some variables.
Once the network is in polytree form, a special-purpose inference algorithm is required,
because ordinary inference methods cannot handle meganodes that share variables with each
other. Essentially, the algorithm is a form of constraint propagation (see Chapter 5) where the
constraints ensure that neighboring meganodes agree on the posterior probability of any vari-
ables that they have in common. With careful bookkeeping, this algorithm is able to compute
posterior probabilities for all the nonevidence nodes in the network in time linear in the size
of the clustered network. However, the NP-hardness of the problem has not disappeared: if a
network requires exponential time and space with variable elimination, then the CPTs in the
clustered network will necessarily be exponentially large.
13.4 Approximate Inference for Bayesian Networks
Given the intractability of exact inference in large networks, we will now consider approxi-
mate inference methods. This section describes randomized sampling algorithms, also called
Monte Carlo algorithms, that provide approximate answers whose accuracy depends on
Monte Carlo
the number of samples generated. They work by generating random events based on the
probabilities in the Bayes net and counting up the different answers found in those random
events. With enough samples, we can get arbitrarily close to recovering the true probability
distribution—provided the Bayes net has no deterministic conditional distributions.
