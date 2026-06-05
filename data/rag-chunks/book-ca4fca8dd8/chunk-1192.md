---
chunk_id: "book-ca4fca8dd8-chunk-1192"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1192
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 719

Section 19.8
Ensemble Learning
719
h
h1 =
h2 =
h3 =
h4 =
Figure 19.24 How the boosting algorithm works. Each shaded rectangle corresponds to
an example; the height of the rectangle corresponds to the weight. The checks and crosses
indicate whether the example was classiﬁed correctly by the current hypothesis. The size of
the decision tree indicates the weight of that hypothesis in the ﬁnal ensemble.
This ﬁnding, which is quite robust across data sets and hypothesis spaces, came as quite
a surprise when it was ﬁrst noticed. Ockham’s razor tells us not to make hypotheses more
complex than necessary, but the graph tells us that the predictions improve as the ensemble
hypothesis gets more complex! Various explanations have been proposed for this. One view
is that boosting approximates Bayesian learning (see Chapter 21), which can be shown to
be an optimal learning algorithm, and the approximation improves as more hypotheses are
added. Another possible explanation is that the addition of further hypotheses enables the
ensemble to be more conﬁdent in its distinction between positive and negative examples,
which helps it when it comes to classifying new examples.
19.8.5 Gradient boosting
For regression and classiﬁcation of factored tabular data, gradient boosting, sometimes
Gradient boosting
called gradient boosting machines (GBM) or gradient boosted regression trees (GBRT), has
become a very popular method. As the name implies, gradient boosting is a form of boosting
using gradient descent. Recall that in ADABOOST, we start with one hypothesis h1, and boost
it with a sequence of hypotheses that pay special attention to the examples that the previous
ones got wrong. In gradient boosting we also add new boosting hypotheses, which pay atten-
tion not to speciﬁc examples, but to the gradient between the right answers and the answers
given by the previous hypotheses.
As in the other algorithms that used gradient descent, we start with a differentiable loss
function; we might use squared error for regression, or logarithmic loss for classiﬁcation. As
in ADABOOST, we then build a decision tree. In Section 19.6.2, we used gradient descent to
minimize the parameters of a model—we calculate the loss, and update the parameters in the
direction of less loss. With gradient boosting, we are not updating parameters of the existing

## Page 720
