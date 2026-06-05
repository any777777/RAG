---
chunk_id: "book-ca4fca8dd8-chunk-1150"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1150
confidence: "first-pass"
extraction_method: "structured-local"
---

690
Chapter 19
Learning from Examples
not be slow, although in some cases model selection has been known to suck up resources on
thousand-computer clusters for days at a time.
The search strategies from Chapters 3 and 4 can also come into play. For example, if two
hyperparameters are independent of each other, they can be optimized separately.
If there are too many combinations of possible values, then random search samples
Random search
uniformly from the set of all possible hyperparameter settings, repeating for as long as you
are willing to spend the time and computational resources. Random sampling is also a good
way to handle continuous values.
When each training run takes a long time, it can be helpful to get useful information out of
each one. Bayesian optimization treats the task of choosing good hyperparameter values as a
Bayesian
optimization
machine learning problem in itself. That is, think of the vector of hyperparameter values x as
an input, and the total loss on the validation set for the model built with those hyperparameters
as an output, y; then we are trying to ﬁnd the function y = f(x) that minimizes the loss y. Each
time we do a training run we get a new (y, f(x)) pair, which we can use to update our belief
about the shape of the function f.
The idea is to trade off exploitation (choosing parameter values that are near to a previous
good result) with exploration (trying novel parameter values). This is the same tradeoff we
saw in Monte Carlo tree search (Section 6.4), and in fact the idea of upper conﬁdence bounds
is used here as well to minimize regret. If we make the assumption that f can be approximated
by a Gaussian process, then the math of updating our belief about f works out nicely. Snoek
et al. (2013) explain the math and give a practical guide to the approach, showing that it can
outperform hand-tuning of parameters, even by experts.
An alternative to Bayesian optimization is population-based training (PBT). PBT starts
Population-based
training (PBT)
by using random search to train (in parallel) a population of models, each with different
hyperparameter values. Then a second generation of models are trained, but they can choose
hyperparameter values based on the successful values from the previous generation, as well
as by random mutation, as in genetic algorithms (Section 4.1.4). Thus, population-based
training shares the advantage of random search that many runs can be done in parallel, and it
shares the advantage of Bayesian optimization (or of hand-tuning by a clever human) that we
can gain information from earlier runs to inform later ones.
19.5 The Theory of Learning
How can we be sure that our learned hypothesis will predict well for previously unseen in-
puts? That is, how do we know that the hypothesis h is close to the target function f if
we don’t know what f is? These questions have been pondered for centuries, by Ockham,
Hume, and others. In recent decades, other questions have emerged: how many examples do
we need to get a good h? What hypothesis space should we use? If the hypothesis space is
very complex, can we even ﬁnd the best h, or do we have to settle for a local maximum? How
complex should h be? How do we avoid overﬁtting? This section examines these questions.
We’ll start with the question of how many examples are needed for learning. We saw
from the learning curve for decision tree learning on the restaurant problem (Figure 19.7 on
page 679) that accuracy improves with more training data. Learning curves are useful, but
they are speciﬁc to a particular learning algorithm on a particular problem. Are there some
more general principles governing the number of examples needed?
