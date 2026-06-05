---
chunk_id: "book-ca4fca8dd8-chunk-0869"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 869
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 527

Section 15.3
Utility Functions
527
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
-5
-4
-3
-2
-1
 0
 1
 2
 3
 4
 5
k=3
k=10
k=30
Error in utility estimate
Figure 15.3 Unjustiﬁed optimism caused by choosing the best of k options: we assume that
each option has a true utility of 0 but a utility estimate that is distributed according to a
unit normal (brown curve). The other curves show the distributions of the maximum of k
estimates for k=3, 10, and 30.
The probability density function is the derivative of the cumulative distribution function, so
the density for X∗, the maximum of k estimates, is
P(x) = d
dx

F(x)k
= k f(x)(F(x))k−1 .
These densities are shown for different values of k in Figure 15.3 for the case where f(x) is the
unit normal. For k=3, the density for X∗has a mean around 0.85, so the average disappoint-
ment will be about 85% of the standard deviation in the utility estimates. With more choices,
extremely optimistic estimates are more likely to arise: for k=30, the disappointment will be
around twice the standard deviation in the estimates.
This tendency for the estimated expected utility of the best choice to be too high is called
the optimizer’s curse (Smith and Winkler, 2006). It afﬂicts even the most seasoned decision
Optimizer’s curse
analysts and statisticians. Serious manifestations include believing that an exciting new drug
that has cured 80% of patients in a trial will cure 80% of patients (it’s been chosen from
k= thousands of candidate drugs) or that a mutual fund advertised as having above-average
returns will continue to have them (it’s been chosen to appear in the advertisement out of k=
dozens of funds in the company’s overall portfolio). It can even be the case that what appears
to be the best choice may not be, if the variance in the utility estimate is high: a drug that has
cured 9 of 10 patients and has been selected from thousands tried is probably worse than one
that has cured 800 of 1000.
The optimizer’s curse crops up everywhere because of the ubiquity of utility-maximizing
selection processes, so taking the utility estimates at face value is a bad idea. We can avoid
the curse with a Bayesian approach that uses an explicit probability model P( c
EU |EU) of
the error in the utility estimates. Given this model and a prior on what we might reasonably
expect the utilities to be, we treat the utility estimate as evidence and compute the posterior
distribution for the true utility using Bayes’ rule.

## Page 528
