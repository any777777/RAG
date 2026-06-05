---
chunk_id: "book-ca4fca8dd8-chunk-1349"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1349
confidence: "first-pass"
extraction_method: "structured-local"
---

822
Chapter 22
Deep Learning
retains the properties of the full version. We can train one big network and then search for
subgraphs of the network that perform better; this search can be fast because the subgraphs
share parameters and don’t have to be retrained.
Another approach is to learn a heuristic evaluation function (as was done for A∗search).
That is, start by choosing a few hundred network architectures and train and evaluate them.
That gives us a data set of (network, score) pairs. Then learn a mapping from the features of a
network to a predicted score. From that point on we can generate a large number of candidate
networks and quickly estimate their value. After a search through the space of networks, the
best one(s) can be fully evaluated with a complete training procedure.
22.5.3 Weight decay
In Section 19.4.3 we saw that regularization—limiting the complexity of a model—can aid
generalization. This is true for deep learning models as well. In the context of neural networks
we usually call this approach weight decay.
Weight decay
Weight decay consists of adding a penalty λ∑i,jW 2
i,j to the loss function used to train the
neural network, where λ is a hyperparameter controlling the strength of the penalty and the
sum is usually taken over all of the weights in the network. Using λ=0 is equivalent to not
using weight decay, while using larger values of λ encourages the weights to become small.
It is common to use weight decay with λ near 10−4.
Choosing a speciﬁc network architecture can be seen as an absolute constraint on the
hypothesis space: a function is either representable within that architecture or it is not. Loss
function penalty terms such as weight decay offer a softer constraint: functions represented
with large weights are in the function family, but the training set must provide more evidence
in favor of these functions than is required to choose a function with small weights.
It is not straightforward to interpret the effect of weight decay in a neural network. In
networks with sigmoid activation functions, it is hypothesized that weight decay helps to
keep the activations near the linear part of the sigmoid, avoiding the ﬂat operating region
that leads to vanishing gradients. With ReLU activation functions, weight decay seems to be
beneﬁcial, but the explanation that makes sense for sigmoids no longer applies because the
ReLU’s output is either linear or zero. Moreover, with residual connections, weight decay
encourages the network to have small differences between consecutive layers rather than
small absolute weight values. Despite these differences in the behavior of weight decay
across many architectures, weight decay is still widely useful.
One explanation for the beneﬁcial effect of weight decay is that it implements a form of
maximum a posteriori (MAP) learning (see page 774). Letting X and y stand for the inputs
and outputs across the entire training set, the maximum a posteriori hypothesis hMAP satisﬁes
hMAP = argmax
w
P(y|X,W)P(W)
= argmin
w
[−logP(y|X,W)−logP(W)].
The ﬁrst term is the usual cross-entropy loss; the second term prefers weights that are likely
under a prior distribution. This aligns exactly with a regularized loss function if we set
logP(W) = −λ∑
i,j
W 2
i,j ,
which means that P(W) is a zero-mean Gaussian prior.
