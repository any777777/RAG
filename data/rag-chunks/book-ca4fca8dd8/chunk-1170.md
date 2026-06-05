---
chunk_id: "book-ca4fca8dd8-chunk-1170"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1170
confidence: "first-pass"
extraction_method: "structured-local"
---

704
Chapter 19
Learning from Examples
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
 1
 0
 1000 2000 3000 4000
Proportion correct
Number of weight updates
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
 1
 0
 25000  50000 75000
Proportion correct
Number of weight updates
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
 1
 0
 25000 50000 75000
Proportion correct
Number of weight updates
(a)
(b)
(c)
Figure 19.18 Repeat of the experiments in Figure 19.16 using logistic regression. The plot
in (a) covers 5000 iterations rather than 700, while the plots in (b) and (c) use the same scale
as before.
The derivative g′ of the logistic function satisﬁes g′(z)=g(z)(1−g(z)), so we have
g′(w·x) = g(w·x)(1−g(w·x)) = hw(x)(1−hw(x))
so the weight update for minimizing the loss takes a step in the direction of the difference
between input and prediction, (y−hw(x)), and the length of that step depends on the constant
α and g′:
wi ←wi +α(y−hw(x))×hw(x)(1−hw(x))×xi .
(19.9)
Repeating the experiments of Figure 19.16 with logistic regression instead of the linear
threshold classiﬁer, we obtain the results shown in Figure 19.18. In (a), the linearly sep-
arable case, logistic regression is somewhat slower to converge, but behaves much more
predictably. In (b) and (c), where the data are noisy and nonseparable, logistic regression
converges far more quickly and reliably. These advantages tend to carry over into real-world
applications, and logistic regression has become one of the most popular classiﬁcation tech-
niques for problems in medicine, marketing, survey analysis, credit scoring, public health,
and other applications.
19.7 Nonparametric Models
Linear regression uses the training data to estimate a ﬁxed set of parameters w. That deﬁnes
our hypothesis hw(x), and at that point we can throw away the training data, because they
are all summarized by w. A learning model that summarizes data with a set of parameters of
ﬁxed size (independent of the number of training examples) is called a parametric model.
Parametric model
When data sets are small, it makes sense to have a strong restriction on the allowable
hypotheses, to avoid overﬁtting. But when there are millions or billions of examples to learn
from, it seems like a better idea to let the data speak for themselves rather than forcing them
to speak through a tiny vector of parameters. If the data say that the correct answer is a very
wiggly function, we shouldn’t restrict ourselves to linear or slightly wiggly functions.
A nonparametric model is one that cannot be characterized by a bounded set of parame-
Nonparametric
model
ters. For example, the piecewise linear function from Figure 19.1 retains all the data points as
part of the model. Learning methods that do this have also been described as instance-based
learning or memory-based learning. The simplest instance-based learning method is table
Instance-based
learning
