---
chunk_id: "book-ca4fca8dd8-chunk-1341"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1341
confidence: "first-pass"
extraction_method: "structured-local"
---

818
Chapter 22
Deep Learning
back to the next layer. As the ﬁgure shows, the messages are all partial derivatives of the loss
L. For example, the backward message ∂L/∂hj is the partial derivative of L with respect to
j’s ﬁrst input, which is the forward message from h to j. Now, h affects L through both j and
k, so we have
∂L/∂h = ∂L/∂hj +∂L/∂hk .
(22.11)
With this equation, the node h can compute the derivative of L with respect to h by summing
the incoming messages from j and k. Now, to compute the outgoing messages ∂L/∂fh and
∂L/∂gh, we use the following equations:
∂L
∂fh
= ∂L
∂h
∂h
∂fh
and
∂L
∂gh
= ∂L
∂h
∂h
∂gh
.
(22.12)
In Equation (22.12), ∂L/∂h was already computed by Equation (22.11), and ∂h/∂fh and
∂h/∂gh are just the derivatives of h with respect to its ﬁrst and second arguments, respec-
tively. For example, if h is a multiplication node—that is, h(f,g)= f · g—then ∂h/∂fh =g
and ∂h/∂gh = f. Software packages for deep learning typically come with a library of node
types (addition, multiplication, sigmoid, and so on), each of which knows how to compute its
own derivatives as needed for Equation (22.12).
The back-propagation process begins with the output nodes, where each initial message
∂L/∂ˆyj is calculated directly from the expression for L in terms of the predicted value ˆy
and the true value y from the training data. At each internal node, the incoming backward
messages are summed according to Equation (22.11) and the outgoing messages are generated
from Equation (22.12). The process terminates at each node in the computation graph that
represents a weight w (e.g., the light mauve ovals in Figure 22.3(b)). At that point, the
sum of the incoming messages to w is ∂L/∂w—precisely the gradient we need to update w.
Exercise 22.BPRE asks you to apply this process to the simple network in Figure 22.3 in order
to rederive the gradient expressions in Equations (22.4) and (22.5).
Weight-sharing, as used in convolutional networks (Section 22.3) and recurrent networks
(Section 22.6), is handled simply by treating each shared weight as a single node with multiple
outgoing arcs in the computation graph. During back-propagation, this results in multiple
incoming gradient messages. By Equation (22.11), this means that the gradient for the shared
weight is the sum of the gradient contributions from each place it is used in the network.
It is clear from this description of the back-propagation process that its computational
cost is linear in the number of nodes in the computation graph, just like the cost of the for-
ward computation. Furthermore, because the node types are typically ﬁxed when the network
is designed, all of the gradient computations can be prepared in symbolic form in advance
and compiled into very efﬁcient code for each node in the graph. Note also that the mes-
sages in Figure 22.6 need not be scalars: they could equally be vectors, matrices, or higher-
dimensional tensors, so that the gradient computations can be mapped onto GPUs or TPUs to
beneﬁt from parallelism.
One drawback of back-propagation is that it requires storing most of the intermediate
values that were computed during forward propagation in order to calculate gradients in the
backward pass. This means that the total memory cost of training the network is proportional
to the number of units in the entire network. Thus, even if the network itself is represented
only implicitly by propagation code with lots of loops, rather than explicitly by a data struc-
ture, all of the intermediate results of that propagation code have to be stored explicitly.
