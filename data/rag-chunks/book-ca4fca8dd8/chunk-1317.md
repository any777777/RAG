---
chunk_id: "book-ca4fca8dd8-chunk-1317"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1317
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.1
Simple Feedforward Networks
805
Figure 22.3(a) shows the traditional way a network might be depicted in a book on neu-
ral networks. A more general way to think about the network is as a computation graph
Computation graph
or dataﬂow graph—essentially a circuit in which each node represents an elementary com-
Dataﬂow graph
putation. Figure 22.3(b) shows the computation graph corresponding to the network in Fig-
ure 22.3(a); the graph makes each element of the overall computation explicit. It also dis-
tinguishes between the inputs (in blue) and the weights (in light mauve): the weights can be
adjusted to make the output ˆy agree more closely with the true value y in the training data.
Each weight is like a volume control knob that determines how much the next node in the
graph hears from that particular predecessor in the graph.
Just as Equation (22.1) described the operation of a unit in vector form, we can do some-
thing similar for the network as a whole. We will generally use W to denote a weight matrix;
for this network, W(1) denotes the weights in the ﬁrst layer (w1,3, w1,4, etc.) and W(2) denotes
the weights in the second layer (w3,5 etc.). Finally, let g(1) and g(2) denote the activation
functions in the ﬁrst and second layers. Then the entire network can be written as follows:
hw(x) = g(2)(W(2)g(1)(W(1)x)).
(22.3)
Like Equation (22.2), this expression corresponds to a computation graph, albeit a much
simpler one than the graph in Figure 22.3(b): here, the graph is simply a chain with weight
matrices feeding into each layer.
The computation graph in Figure 22.3(b) is relatively small and shallow, but the same
idea applies to all forms of deep learning: we construct computation graphs and adjust their
weights to ﬁt the data. The graph in Figure 22.3(b) is also fully connected, meaning that
Fully connected
every node in each layer is connected to every node in the next layer. This is in some sense
the default, but we will see in Section 22.3 that choosing the connectivity of the network is
also important in achieving effective learning.
22.1.2 Gradients and learning
In Section 19.6, we introduced an approach to supervised learning based on gradient de-
scent: calculate the gradient of the loss function with respect to the weights, and adjust the
weights along the gradient direction to reduce the loss. (If you have not already read Sec-
tion 19.6, we recommend strongly that you do so before continuing.) We can apply exactly
the same approach to learning the weights in computation graphs. For the weights leading
into units in the output layer—the ones that produce the output of the network, the gradient
Output layer
calculation is essentially identical to the process in Section 19.6. For weights leading into
units in the hidden layers, which are not directly connected to the outputs, the process is
Hidden layer
only slightly more complicated.
For now, we will use the squared loss function, L2, and we will calculate the gradient
for the network in Figure 22.3 with respect to a single training example (x,y). (For multiple
examples, the gradient is just the sum of the gradients for the individual examples.) The
network outputs a prediction ˆy=hw(x) and the true value is y, so we have
Loss(hw) = L2(y,hw(x)) = ∥y−hw(x)∥2 = (y−ˆy)2 .
To compute the gradient of the loss with respect to the weights, we need the same tools of cal-
culus we used in Chapter 19—principally the chain rule, ∂g(f(x))/∂x=g′(f(x))∂f(x)/∂x.
We’ll start with the easy case: a weight such as w3,5 that is connected to the output unit. We
operate directly on the network-deﬁning expressions from Equation (22.2):
