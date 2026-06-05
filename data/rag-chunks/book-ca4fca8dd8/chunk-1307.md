---
chunk_id: "book-ca4fca8dd8-chunk-1307"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1307
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
797
For the complete-data case, the inner loop to learn the parameters is very fast—just a
matter of extracting conditional frequencies from the data set. When there are hidden vari-
ables, the inner loop may involve many iterations of EM or a gradient-based algorithm, and
each iteration involves the calculation of posteriors in a Bayes net, which is itself an NP-hard
problem. To date, this approach has proved impractical for learning complex models.
One possible improvement is the so-called structural EM algorithm, which operates in
Structural EM
much the same way as ordinary (parametric) EM except that the algorithm can update the
structure as well as the parameters. Just as ordinary EM uses the current parameters to com-
pute the expected counts in the E-step and then applies those counts in the M-step to choose
new parameters, structural EM uses the current structure to compute expected counts and
then applies those counts in the M-step to evaluate the likelihood for potential new struc-
tures. (This contrasts with the outer-loop/inner-loop method, which computes new expected
counts for each potential structure.) In this way, structural EM may make several structural
alterations to the network without once recomputing the expected counts, and is capable of
learning nontrivial Bayes net structures. Structural EM has a search space over the space
of structures rather than the space of structures and parameters. Nonetheless, much work
remains to be done before we can say that the structure-learning problem is solved.
Summary
Statistical learning methods range from simple calculation of averages to the construction of
complex models such as Bayesian networks. They have applications throughout computer
science, engineering, computational biology, neuroscience, psychology, and physics. This
chapter has presented some of the basic ideas and given a ﬂavor of the mathematical under-
pinnings. The main points are as follows:
• Bayesian learning methods formulate learning as a form of probabilistic inference,
using the observations to update a prior distribution over hypotheses. This approach
provides a good way to implement Ockham’s razor, but quickly becomes intractable for
complex hypothesis spaces.
• Maximum a posteriori (MAP) learning selects a single most likely hypothesis given
the data. The hypothesis prior is still used and the method is often more tractable than
full Bayesian learning.
• Maximum-likelihood learning simply selects the hypothesis that maximizes the likeli-
hood of the data; it is equivalent to MAP learning with a uniform prior. In simple cases
such as linear regression and fully observable Bayesian networks, maximum-likelihood
solutions can be found easily in closed form. Naive Bayes learning is a particularly
effective technique that scales well.
• When some variables are hidden, local maximum likelihood solutions can be found
using the expectation maximization (EM) algorithm. Applications include unsuper-
vised clustering using mixtures of Gaussians, learning Bayesian networks, and learning
hidden Markov models.
• Learning the structure of Bayesian networks is an example of model selection. This
usually involves a discrete search in the space of structures. Some method is required
for trading off model complexity against degree of ﬁt.
