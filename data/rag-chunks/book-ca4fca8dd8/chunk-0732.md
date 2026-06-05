---
chunk_id: "book-ca4fca8dd8-chunk-0732"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 732
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 441

Section 13.2
The Semantics of Bayesian Networks
441
Harvest
Subsidy
Buys
Cost
Figure 13.6 A simple network with discrete variables (Subsidy and Buys) and continuous
variables (Harvest and Cost).
 0
 3
 6
 9  12
Cost c
 0  3  6  9  12
Harvest 
 0
 0.1
 0.2
 0.3
 0.4
P(c | h, subsidy)
 0
 3
 6
 9  12
Cost c
 0  3  6  9  12
Harvest 
 0
 0.1
 0.2
 0.3
 0.4
| h, ¬subsidy)
 0
 3
 6
 9  12
Cost c
 0  3  6  9  12
Harvest 
 0
 0.1
 0.2
 0.3
 0.4
P(c | h)
(a)
(b)
(c)
Figure 13.7 The graphs in (a) and (b) show the probability distribution over Cost as a func-
tion of Harvest size, with Subsidy true and false, respectively. Graph (c) shows the distribu-
tion P(Cost|Harvest), obtained by summing over the two subsidy cases.
The linear–Gaussian conditional distribution has some special properties. A network con-
taining only continuous variables with linear–Gaussian distributions has a joint distribution
that is a multivariate Gaussian distribution (see Appendix A) over all the variables (Exer-
cise 13.LGEX). Furthermore, the posterior distribution given any evidence also has this prop-
erty.2 When discrete variables are added as parents (not as children) of continuous variables,
the network deﬁnes a conditional Gaussian, or CG, distribution: given any assignment to the
Conditional Gaussian
discrete variables, the distribution over the continuous variables is a multivariate Gaussian.
Now we turn to the distributions for discrete variables with continuous parents. Consider,
for example, the Buys node in Figure 13.6. It seems reasonable to assume that the customer
will buy if the cost is low and will not buy if it is high and that the probability of buying
varies smoothly in some intermediate region. In other words, the conditional distribution is
like a “soft” threshold function. One way to make soft thresholds is to use the integral of the
standard normal distribution:
Φ(x) =
Z x
−∞N(s;0,1)ds.
2
It follows that inference in linear–Gaussian networks takes only O(n3) time in the worst case, regardless of the
network topology. In Section 13.3, we see that inference for networks of discrete variables is NP-hard.

## Page 442
