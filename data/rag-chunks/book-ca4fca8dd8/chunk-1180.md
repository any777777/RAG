---
chunk_id: "book-ca4fca8dd8-chunk-1180"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1180
confidence: "first-pass"
extraction_method: "structured-local"
---

710
Chapter 19
Learning from Examples
Note that we need to solve a new regression problem for every query point—that’s what
it means to be local. (In ordinary linear regression, we solved the regression problem once,
globally, and then used the same hw for any query point.) Mitigating against this extra work
is the fact that each regression problem will be easier to solve, because it involves only the
examples with nonzero weight—the examples that are within the kernel width of the query.
When kernel widths are small, this may be just a few points.
Most nonparametric models have the advantage that it is easy to do leave-one-out cross-
validation without having to recompute everything. With a k-nearest-neighbors model, for
instance, when given a test example (x,y) we retrieve the k nearest neighbors once, compute
the per-example loss L(y,h(x)) from them, and record that as the leave-one-out result for
every example that is not one of the neighbors. Then we retrieve the k +1 nearest neighbors
and record distinct results for leaving out each of the k neighbors. With N examples the whole
process is O(k), not O(kN).
19.7.5 Support vector machines
In the early 2000s, the support vector machine (SVM) model class was the most popular
Support vector
machine (SVM)
approach for “off-the-shelf” supervised learning, for when you don’t have any specialized
prior knowledge about a domain. That position has now been taken over by deep learning
networks and random forests, but SVMs retain three attractive properties:
1. SVMs construct a maximum margin separator—a decision boundary with the largest
possible distance to example points. This helps them generalize well.
2. SVMs create a linear separating hyperplane, but they have the ability to embed the
data into a higher-dimensional space, using the so-called kernel trick. Often, data that
are not linearly separable in the original input space are easily separable in the higher-
dimensional space.
3. SVMs are nonparametric—the separating hyperplane is deﬁned by a set of example
points, not by a collection of parameter values. But while nearest-neighbor models
need to retain all the examples, an SVM model keeps only the examples that are closest
to the separating plane—usually only a small constant times the number of dimensions.
Thus SVMs combine the advantages of nonparametric and parametric models: they
have the ﬂexibility to represent complex functions, but they are resistant to overﬁtting.
We see in Figure 19.21(a) a binary classiﬁcation problem with three candidate decision
boundaries, each a linear separator. Each of them is consistent with all the examples, so
from the point of view of 0/1 loss, each would be equally good. Logistic regression would
ﬁnd some separating line; the exact location of the line depends on all the example points.
The key insight of SVMs is that some examples are more important than others, and that
paying attention to them can lead to better generalization.
Consider the lowest of the three separating lines in (a). It comes very close to ﬁve of the
black examples. Although it classiﬁes all the examples correctly, and thus minimizes loss, it
should make you nervous that so many examples are close to the line; it may be that other
black examples will turn out to fall on the wrong side of the line.
SVMs address this issue: Instead of minimizing expected empirical loss on the training
data, SVMs attempt to minimize expected generalization loss. We don’t know where the
as-yet-unseen points may fall, but under the probabilistic assumption that they are drawn
