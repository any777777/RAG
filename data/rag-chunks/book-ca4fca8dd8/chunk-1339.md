---
chunk_id: "book-ca4fca8dd8-chunk-1339"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1339
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.4
Learning Algorithms
817
f
g
k
j
h
∂L/∂hj
∂L/∂hk
∂L/∂fh
∂L/∂gh
Figure 22.6 Illustration of the back-propagation of gradient information in an arbitrary com-
putation graph. The forward computation of the output of the network proceeds from left to
right, while the back-propagation of gradients proceeds from right to left.
may point in entirely the wrong direction, making convergence difﬁcult. One solution
is to increase the minibatch size as training proceeds; another is to incorporate the idea
of momentum, which keeps a running average of the gradients of past minibatches in
Momentum
order to compensate for small minibatch sizes.
• Care must be taken to mitigate numerical instabilities that may arise due to overﬂow,
underﬂow, and rounding error. These are particularly problematic with the use of ex-
ponentials in softmax, sigmoid, and tanh activation functions, and with the iterated
computations in very deep networks and recurrent networks (Section 22.6) that lead to
vanishing and exploding activations and gradients.
Overall, the process of learning the weights of the network is usually one that exhibits di-
minishing returns. We run until it is no longer practical to decrease the test error by running
longer. Usually this does not mean we have reached a global or even a local minimum of
the loss function. Instead, it means we would have to make an impractically large number
of very small steps to continue reducing the cost, or that additional steps would only cause
overﬁtting, or that estimates of the gradient are too inaccurate to make further progress.
22.4.1 Computing gradients in computation graphs
On page 806, we derived the gradient of the loss function with respect to the weights in a
speciﬁc (and very simple) network. We observed that the gradient could be computed by
back-propagating error information from the output layer of the network to the hidden layers.
We also said that this result holds in general for any feedforward computation graph. Here,
we explain how this works.
Figure 22.6 shows a generic node in a computation graph. (The node h has in-degree and
out-degree 2, but nothing in the analysis depends on this.) During the forward pass, the node
computes some arbitrary function h from its inputs, which come from nodes f and g. In turn,
h feeds its value to nodes j and k.
The back-propagation process passes messages back along each link in the network. At
each node, the incoming messages are collected and new messages are calculated to pass
