---
chunk_id: "book-ca4fca8dd8-chunk-1232"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1232
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 20.1
A Logical Formulation of Learning
743
Patrons(x,Some), then one possible generalization is given by C1(x) ≡Patrons(x,Some).
This is called dropping conditions. Intuitively, it generates a weaker deﬁnition and there-
Dropping conditions
fore allows a larger set of positive examples. There are a number of other generalization
operations, depending on the language being operated on. Similarly, we can specialize a hy-
pothesis by adding extra conditions to its candidate deﬁnition or by removing disjuncts from
a disjunctive deﬁnition. Let us see how this works on the restaurant example, using the data
in Figure 19.3.
• The ﬁrst example, X1, is positive. The attribute Alternate(X1) is true, so let the initial
hypothesis be
h1 : ∀x WillWait(x) ⇔Alternate(x) .
• The second example, X2, is negative. h1 predicts it to be positive, so it is a false positive.
Therefore, we need to specialize h1. This can be done by adding an extra condition that
will rule out X2, while continuing to classify X1 as positive. One possibility is
h2 : ∀x WillWait(x) ⇔Alternate(x)∧Patrons(x,Some) .
• The third example, X3, is positive. h2 predicts it to be negative, so it is a false negative.
Therefore, we need to generalize h2. We drop the Alternate condition, yielding
h3 : ∀x WillWait(x) ⇔Patrons(x,Some) .
• The fourth example, X4, is positive. h3 predicts it to be negative, so it is a false negative.
We therefore need to generalize h3. We cannot drop the Patrons condition, because
that would yield an all-inclusive hypothesis that would be inconsistent with X2. One
possibility is to add a disjunct:
h4 : ∀x WillWait(x) ⇔Patrons(x,Some)
∨(Patrons(x,Full)∧Fri/Sat(x)) .
Already, the hypothesis is starting to look reasonable. Obviously, there are other possibilities
consistent with the ﬁrst four examples; here are two of them:
h′
4 : ∀x WillWait(x) ⇔¬WaitEstimate(x,30-60) .
h′′
4 : ∀x WillWait(x) ⇔Patrons(x,Some)
∨(Patrons(x,Full)∧WaitEstimate(x,10-30)) .
The CURRENT-BEST-LEARNING algorithm is described nondeterministically, because at any
point, there may be several possible specializations or generalizations that can be applied. The
choices that are made will not necessarily lead to the simplest hypothesis, and may lead to an
unrecoverable situation where no simple modiﬁcation of the hypothesis is consistent with all
of the data. In such cases, the program must backtrack to a previous choice point.
The CURRENT-BEST-LEARNING algorithm and its variants have been used in many ma-
chine learning systems, starting with Patrick Winston’s (1970) “arch-learning” program. With
a large number of examples and a large space, however, some difﬁculties arise:
1. Checking all the previous examples over again for each modiﬁcation is very expensive.
2. The search process may involve a great deal of backtracking. As we saw in Chapter 19,
hypothesis space can be a doubly exponentially large place.
