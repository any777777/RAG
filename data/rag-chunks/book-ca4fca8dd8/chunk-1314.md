---
chunk_id: "book-ca4fca8dd8-chunk-1314"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1314
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 802

802
Chapter 22
Deep Learning
(a)
(b)
(c)
Figure 22.1 (a) A shallow model, such as linear regression, has short computation paths
between inputs and output. (b) A decision list network (page 692) has some long paths for
some possible input values, but most paths are short. (c) A deep learning network has longer
computation paths, allowing each variable to interact with all the others.
generalization. Section 22.6 covers networks with recurrent structure, which are well suited
for sequential data. Section 22.7 describes ways to use deep learning for tasks other than
supervised learning. Finally, Section 22.8 surveys the range of applications of deep learning.
22.1 Simple Feedforward Networks
A feedforward network, as the name suggests, has connections only in one direction—that
Feedforward network
is, it forms a directed acyclic graph with designated input and output nodes. Each node com-
putes a function of its inputs and passes the result to its successors in the network. Information
ﬂows through the network from the input nodes to the output nodes, and there are no loops.
A recurrent network, on the other hand, feeds its intermediate or ﬁnal outputs back into its
Recurrent network
own inputs. This means that the signal values within the network form a dynamical system
that has internal state or memory. We will consider recurrent networks in Section 22.6.
Boolean circuits, which implement Boolean functions, are an example of feedforward
networks. In a Boolean circuit, the inputs are limited to 0 and 1, and each node implements a
simple Boolean function of its inputs, producing a 0 or a 1. In neural networks, input values
are typically continuous, and nodes take continuous inputs and produce continuous outputs.
Some of the inputs to nodes are parameters of the network; the network learns by adjusting
the values of these parameters so that the network as a whole ﬁts the training data.
22.1.1 Networks as complex functions
Each node within a network is called a unit. Traditionally, following the design proposed by
Unit
McCulloch and Pitts, a unit calculates the weighted sum of the inputs from predecessor nodes

## Page 803
