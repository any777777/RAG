---
chunk_id: "book-ca4fca8dd8-chunk-1333"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1333
confidence: "first-pass"
extraction_method: "structured-local"
---

814
Chapter 22
Deep Learning
learned classiﬁer that would be able to recognize the object at a size of 10 pixels in the
original image would now be able to recognize that object in the pooled image, even
if it was too big to recognize in the original image. In other words, average-pooling
facilitates multiscale recognition. It also reduces the number of weights required in
subsequent layers, leading to lower computational cost and possibly faster learning.
• Max-pooling computes the maximum value of its l inputs. It can also be used purely
for downsampling, but it has a somewhat different semantics. Suppose we applied max-
pooling to the hidden layer [5,9,4] in Figure 22.4: the result would be a 9, indicating
that somewhere in the input image there is a darker dot that is detected by the kernel.
In other words, max-pooling acts as a kind of logical disjunction, saying that a feature
exists somewhere in the unit’s receptive ﬁeld.
If the goal is to classify the image into one of c categories, then the ﬁnal layer of the network
will be a softmax with c output units. The early layers of the CNN are image-sized, so
somewhere in between there must be signiﬁcant reductions in layer size. Convolution layers
and pooling layers with stride larger than 1 all serve to reduce the layer size. It’s also possible
to reduce the layer size simply by having a fully connected layer with fewer units than the
preceding layer. CNNs often have one or two such layers preceding the ﬁnal softmax layer.
22.3.2 Tensor operations in CNNs
We saw in Equations (22.1) and (22.3) that the use of vector and matrix notation can be helpful
in keeping mathematical derivations simple and elegant and providing concise descriptions of
computation graphs. Vectors and matrices are one-dimensional and two-dimensional special
cases of tensors, which (in deep learning terminology) are simply multidimensional arrays
Tensor
of any dimension.5
For CNNs, tensors are a way of keeping track of the “shape” of the data as it progresses
through the layers of the network. This is important because the whole notion of convolution
depends on the idea of adjacency: adjacent data elements are assumed to be semantically
related, so it makes sense to apply operators to local regions of the data. Moreover, with
suitable language primitives for constructing tensors and applying operators, the layers them-
selves can be described concisely as maps from tensor inputs to tensor outputs.
A ﬁnal reason for describing CNNs in terms of tensor operations is computational efﬁ-
ciency: given a description of a network as a sequence of tensor operations, a deep learning
software package can generate compiled code that is highly optimized for the underlying
computational substrate. Deep learning workloads are often run on GPUs (graphics process-
ing units) or TPUs (tensor processing units), which make available a high degree of paral-
lelism. For example, one of Google’s third-generation TPU pods has throughput equivalent
to about ten million laptops. Taking advantage of these capabilities is essential if one is train-
ing a large CNN on a large database of images. Thus, it is common to process not one image
at a time but many images in parallel; as we will see in Section 22.4, this also aligns nicely
with the way that the stochastic gradient descent algorithm calculates gradients with respect
to a minibatch of training examples.
Let us put all this together in the form of an example. Suppose we are training on
256×256 RGB images with a minibatch size of 64. The input in this case will be a four-
5
The proper mathematical deﬁnition of tensors requires that certain invariances hold under a change of basis.
