---
chunk_id: "book-ca4fca8dd8-chunk-1122"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1122
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.2
Supervised Learning
673
imposed by the hypothesis space. For example, the hypothesis space of linear functions
induces a strong bias: it only allows functions consisting of straight lines. If there are any
patterns in the data other than the overall slope of a line, a linear function will not be able
to represent those patterns. We say that a hypothesis is underﬁtting when it fails to ﬁnd a
Underﬁtting
pattern in the data. On the other hand, the piecewise linear function has low bias; the shape
of the function is driven by the data.
By variance we mean the amount of change in the hypothesis due to ﬂuctuation in the
Variance
training data. The two rows of Figure 19.1 represent data sets that were each sampled from
the same f(x) function. The data sets turned out to be slightly different. For the ﬁrst three
columns, the small difference in the data set translates into a small difference in the hypothe-
sis. We call that low variance. But the degree-12 polynomials in the fourth column have high
variance: look how different the two functions are at both ends of the x-axis. Clearly, at least
one of these polynomials must be a poor approximation to the true f(x). We say a function
is overﬁtting the data when it pays too much attention to the particular data set it is trained
Overﬁtting
on, causing it to perform poorly on unseen data.
Often there is a bias–variance tradeoff: a choice between more complex, low-bias hy-
Bias–variance
tradeoﬀ
potheses that ﬁt the training data well and simpler, low-variance hypotheses that may gen-
eralize better. Albert Einstein said in 1933, “the supreme goal of all theory is to make the
irreducible basic elements as simple and as few as possible without having to surrender the
adequate representation of a single datum of experience.” In other words, Einstein recom-
mends choosing the simplest hypothesis that matches the data. This principle can be traced
further back to the 14th-century English philosopher William of Ockham.2 His principle that
“plurality [of entities] should not be posited without necessity” is called Ockham’s razor
because it is used to “shave off” dubious explanations.
Deﬁning simplicity is not easy. It seems clear that a polynomial with only two parameters
is simpler than one with thirteen parameters. We will make this intuition more precise in
Section 19.3.4. However, in Chapter 22 we will see that deep neural network models can
often generalize quite well, even though they are very complex—some of them have billions
of parameters. So the number of parameters by itself is not a good measure of a model’s
ﬁtness. Perhaps we should be aiming for “appropriateness,” not “simplicity” in a model
class. We will consider this issue in Section 19.4.1.
Which hypothesis is best in Figure 19.1? We can’t be certain. If we knew the data
represented, say, the number of hits to a Web site that grows from day to day, but also cycles
depending on the time of day, then we might favor the sinusoidal function. If we knew the
data was deﬁnitely not cyclic but had high noise, that would favor the linear function.
In some cases, an analyst is willing to say not just that a hypothesis is possible or im-
possible, but rather how probable it is. Supervised learning can be done by choosing the
hypothesis h∗that is most probable given the data:
h∗= argmax
h∈H
P(h|data).
By Bayes’ rule this is equivalent to
h∗= argmax
h∈H
P(data|h)P(h).
2
The name is often misspelled as “Occam.”
