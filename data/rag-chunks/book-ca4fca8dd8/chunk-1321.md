---
chunk_id: "book-ca4fca8dd8-chunk-1321"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1321
confidence: "first-pass"
extraction_method: "structured-local"
---

808
Chapter 22
Deep Learning
attributes. If the attributes are Boolean, we have n input nodes; usually false is mapped to
an input of 0 and true is mapped to 1, although sometimes −1 and +1 are used. Numeric
attributes, whether integer or real-valued, are typically used as is, although they may be scaled
to ﬁt within a ﬁxed range; if the magnitudes for different examples vary enormously, the
values can be mapped onto a log scale.
Images do not quite ﬁt into the category of factored data; although an RGB image of size
X ×Y pixels can be thought of as 3XY integer-valued attributes (typically with values in the
range {0,...,255}), this would ignore the fact that the RGB triplets belong to the same pixel
in the image and the fact that pixel adjacency really matters. Of course, we can map adjacent
pixels onto adjacent input nodes in the network, but the meaning of adjacency is completely
lost if the internal layers of the network are fully connected. In practice, networks used with
image data have array-like internal structures that aim to reﬂect the semantics of adjacency.
We will see this in more detail in Section 22.3.
Categorical attributes with more than two values—like the Type attribute in the restaurant
problem from Chapter 19, which has values French, Italian, Thai, or burger)—are usually
encoded using the so-called one-hot encoding. An attribute with d possible values is repre-
sented by d separate input bits. For any given value, the corresponding input bit is set to 1 and
all the others are set to 0. This generally works better than mapping the values to integers.
If we used integers for the Type attribute, Thai would be 3 and burger would be 4. Because
the network is a composition of continuous functions, it would have no choice but to pay
attention to numerical adjacency, but in this case the numerical adjacency between Thai and
burger is semantically meaningless.
22.2.2 Output layers and loss functions
On the output side of the network, the problem of encoding the raw data values into actual
values y for the output nodes of the graph is much the same as the input encoding problem.
For example, if the network is trying to predict the Weather variable from Chapter 12, which
has values {sun,rain,cloud,snow}, we would use a one-hot encoding with four bits.
So much for the data values y. What about the prediction ˆy? Ideally, it would exactly
match the desired value y, and the loss would be zero, and we’d be done. In practice, this
seldom happens—especially before we have started the process of adjusting the weights!
Thus, we need to think about what an incorrect output value means, and how to measure the
loss. In deriving the gradients in Equations (22.4) and (22.5), we began with the squared-
error loss function. This keeps the algebra simple, but it is not the only possibility. In fact,
for most deep learning applications, it is more common to interpret the output values ˆy as
probabilities and to use the negative log likelihood as the loss function—exactly as we did
with maximum likelihood learning in Chapter 21.
Maximum likelihood learning ﬁnds the value of w that maximizes the probability of the
observed data. And because the log function is monotonic, this is equivalent to maximizing
the log likelihood of the data, which is equivalent in turn to minimizing a loss function deﬁned
as the negative log likelihood. (Recall from page 776 that taking logs turns products of
probabilities into sums, which are more amenable for taking derivatives.) In other words, we
are looking for w∗that minimizes the sum of negative log probabilities of the N examples:
w∗= argmin
w
−
N
∑
j=1
logPw(yj |xj).
(22.6)
