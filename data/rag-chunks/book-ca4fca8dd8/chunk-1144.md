---
chunk_id: "book-ca4fca8dd8-chunk-1144"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1144
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.4
Model Selection and Optimization
687
this overﬁtting, as with the decision trees in (a). But for other model classes, adding capacity
means that there are more candidate functions, and some of them are naturally well-suited to
the patterns of data that are in the true function f(x). The higher the capacity, the more of
these suitable representations there are, and the more likely that the optimization mechanism
will be able to land on one.
Deep neural networks (Chapter 22), kernel machines (Section 19.7.5), random forests
(Section 19.8.2), and boosted ensembles (Section 19.8.4) all have the property that their vali-
dation set error tends to decrease as capacity increases, as in Figure 19.9(b).
We could extend the model selection algorithm in various ways: we could compare dis-
parate model classes, by calling MODEL-SELECTION with DECISION-TREE-LEARNER as
an argument and then with POLYNOMIAL-LEARNER, and seeing which does better. We could
allow multiple hyperparameters, which means we would need a more complex optimization
algorithm, such as a grid search (see Section 19.9.3) rather than a linear search.
19.4.2 From error rates to loss
So far, we have been trying to minimize error rate. This is clearly better than maximizing error
rate, but it is not the full story. Consider the problem of classifying email messages as spam
or non-spam. It is worse to classify non-spam as spam (and thus potentially miss an important
message) than to classify spam as non-spam (and thus suffer a few seconds of annoyance).
So a classiﬁer with a 1% error rate, where almost all the errors were classifying spam as non-
spam, would be better than a classiﬁer with only a 0.5% error rate, if most of those errors were
classifying non-spam as spam. We saw in Chapter 15 that decision makers should maximize
expected utility, and utility is what learners should maximize as well. However, in machine
learning it is traditional to express this as a negative: to minimize a loss function rather than
Loss function
maximize a utility function. The loss function L(x,y, ˆy) is deﬁned as the amount of utility lost
by predicting h(x)= ˆy when the correct answer is f(x)=y:
L(x,y, ˆy) = Utility(result of using y given an input x)
−Utility(result of using ˆy given an input x)
This is the most general formulation of the loss function. Often a simpliﬁed version is used,
L(y, ˆy), that is independent of x. We will use the simpliﬁed version for the rest of this chapter,
which means we can’t say that it is worse to misclassify a letter from Mom than it is to
misclassify a letter from our annoying cousin, but we can say that it is 10 times worse to
classify non-spam as spam than vice versa:
L(spam,nospam) = 1,
L(nospam,spam) = 10.
Note that L(y,y) is always zero; by deﬁnition there is no loss when you guess exactly right.
For functions with discrete outputs, we can enumerate a loss value for each possible mis-
classiﬁcation, but we can’t enumerate all the possibilities for real-valued data. If f(x) is
137.035999, we would be fairly happy with h(x) = 137.036, but just how happy should we
be? In general, small errors are better than large ones; two functions that implement that idea
are the absolute value of the difference (called the L1 loss), and the square of the difference
(called the L2 loss; think “2” for square). For discrete-valued outputs, if we are content with
the idea of minimizing error rate, we can use the L0/1 loss function, which has a loss of 1 for
an incorrect answer:
