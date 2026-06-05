---
chunk_id: "book-ca4fca8dd8-chunk-1162"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1162
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.6
Linear Regression and Classiﬁcation
699
w1
w2
w*
w1
w2
w*
Figure 19.14 Why L1 regularization tends to produce a sparse model. Left: With L1 regu-
larization (box), the minimal achievable loss (concentric contours) often occurs on an axis,
meaning a weight of zero. Right: With L2 regularization (circle), the minimal loss is likely
to occur anywhere on the circle, giving no preference to zero weights.
regularization function should you pick? That depends on the speciﬁc problem, but L1 regu-
larization has an important advantage: it tends to produce a sparse model. That is, it often
Sparse model
sets many weights to zero, effectively declaring the corresponding attributes to be completely
irrelevant—just as LEARN-DECISION-TREE does (although by a different mechanism). Hy-
potheses that discard attributes can be easier for a human to understand, and may be less
likely to overﬁt.
Figure 19.14 gives an intuitive explanation of why L1 regularization leads to weights of
zero, while L2 regularization does not. Note that minimizing Loss(w) + λComplexity(w) is
equivalent to minimizing Loss(w) subject to the constraint that Complexity(w) ≤c, for some
constant c that is related to λ. Now, in Figure 19.14(a) the diamond-shaped box represents
the set of points w in two-dimensional weight space that have L1 complexity less than c; our
solution will have to be somewhere inside this box. The concentric ovals represent contours
of the loss function, with the minimum loss at the center. We want to ﬁnd the point in the box
that is closest to the minimum; you can see from the diagram that, for an arbitrary position
of the minimum and its contours, it will be common for the corner of the box to ﬁnd its way
closest to the minimum, just because the corners are pointy. And of course the corners are
the points that have a value of zero in some dimension.
In Figure 19.14(b), we’ve done the same for the L2 complexity measure, which repre-
sents a circle rather than a diamond. Here you can see that, in general, there is no reason
for the intersection to appear on one of the axes; thus L2 regularization does not tend to pro-
duce zero weights. The result is that the number of examples required to ﬁnd a good h is
linear in the number of irrelevant features for L2 regularization, but only logarithmic with L1
regularization. Empirical evidence on many problems supports this analysis.
Another way to look at it is that L1 regularization takes the dimensional axes seriously,
while L2 treats them as arbitrary. The L2 function is spherical, which makes it rotationally
9
It is perhaps confusing that the notation L1 and L2 is used for both loss functions and regularization functions.
They need not be used in pairs: you could use L2 loss with L1 regularization, or vice versa.
