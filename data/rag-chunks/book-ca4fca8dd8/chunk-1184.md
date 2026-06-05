---
chunk_id: "book-ca4fca8dd8-chunk-1184"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1184
confidence: "first-pass"
extraction_method: "structured-local"
---

714
Chapter 19
Learning from Examples
+
+ +
+
+
+
+
+
+
+
+ +
+
+
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
–
– –
–
–
–
–
–
–
Figure 19.23 Illustration of the increased expressive power obtained by ensemble learning.
We take three linear threshold hypotheses, each of which classiﬁes positively on the unshaded
side, and classify as positive any example classiﬁed positively by all three. The resulting
triangular region is a hypothesis not expressible in the original hypothesis space.
does not cleanly separate the classes, but reﬂects the reality of the noisy data. That is pos-
sible with the soft margin classiﬁer, which allows examples to fall on the wrong side of the
Soft margin
decision boundary, but assigns them a penalty proportional to the distance required to move
them back to the correct side.
The kernel method can be applied not only with learning algorithms that ﬁnd optimal
linear separators, but also with any other algorithm that can be reformulated to work only
with dot products of pairs of data points, as in Equations (19.10) and (19.11). Once this is
done, the dot product is replaced by a kernel function and we have a kernelized version of
Kernelization
the algorithm.
19.8 Ensemble Learning
So far we have looked at learning methods in which a single hypothesis is used to make pre-
dictions. The idea of ensemble learning is to select a collection, or ensemble, of hypotheses,
Ensemble learning
h1,h2,...,hn, and combine their predictions by averaging, voting, or by another level of ma-
chine learning. We call the individual hypotheses base models and their combination an
Base model
ensemble model.
Ensemble model
There are two reasons to do this. The ﬁrst is to reduce bias. The hypothesis space of
a base model may be too restrictive, imposing a strong bias (such as the bias of a linear
decision boundary in logistic regression). An ensemble can be more expressive, and thus
have less bias, than the base models. Figure 19.23 shows that an ensemble of three linear
classiﬁers can represent a triangular region that could not be represented by a single linear
classiﬁer. An ensemble of n linear classiﬁers allows more functions to be realizable, at a cost
of only n times more computation; this is often better than allowing a completely general
hypothesis space that might require exponentially more computation.

## Page 715
