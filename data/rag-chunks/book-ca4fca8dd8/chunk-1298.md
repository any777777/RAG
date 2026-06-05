---
chunk_id: "book-ca4fca8dd8-chunk-1298"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1298
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 792

792
Chapter 21
Learning Probabilistic Models
-200
-100
 0
 100
 200
 300
 400
 500
 600
 700
 0
 5
 10
 15
 20
Log-likelihood L
Iteration number
-2020
-2010
-2000
-1990
-1980
 0
 20
 40
 60
 80
 100
 120
Log-likelihood L
Iteration number
(a)
(b)
Figure 21.13 Graphs showing the log likelihood of the data, L, as a function of the EM
iteration. The horizontal line shows the log likelihood according to the true model. (a) Graph
for the Gaussian mixture model in Figure 21.12. (b) Graph for the Bayesian network in
Figure 21.14(a).
(a)
(b)
C
X
Hole
Bag
P(Bag=1)
Wrapper
Flavor
Bag
1
2
P(F=cherry | B)
θF1
θ
θF1
Figure 21.14 (a) A mixture model for candy. The proportions of different ﬂavors, wrappers,
and presence of holes depend on the bag, which is not observed. (b) Bayesian network for
a Gaussian mixture. The mean and covariance of the observable variables X depend on the
component C.
21.3.2 Learning Bayes net parameter values for hidden variables
To learn a Bayesian network with hidden variables, we apply the same insights that worked
for mixtures of Gaussians. Figure 21.14(a) represents a situation in which there are two bags
of candy that have been mixed together. Candies are described by three features: in addition
to the Flavor and the Wrapper, some candies have a Hole in the middle and some do not.
The distribution of candies in each bag is described by a naive Bayes model: the features

## Page 793
