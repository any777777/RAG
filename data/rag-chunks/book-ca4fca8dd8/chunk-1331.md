---
chunk_id: "book-ca4fca8dd8-chunk-1331"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1331
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.3
Convolutional Networks
813
Figure 22.5 The ﬁrst two layers of a CNN for a 1D image with a kernel size l =3 and a
stride s=1. Padding is added at the left and right ends in order to keep the hidden layers the
same size as the input. Shown in red is the receptive ﬁeld of a unit in the second hidden layer.
Generally speaking, the deeper the unit, the larger the receptive ﬁeld.
mostly zeroes, after all—but the fact that convolution is a linear matrix operation serves as a
reminder that gradient descent can be applied easily and effectively to CNNs, just as it can to
plain vanilla neural networks.
As mentioned earlier, there will be d kernels, not just one; so, with a stride of 1, the
output will be d times larger. This means that a two-dimensional input array becomes a
three-dimensional array of hidden units, where the third dimension is of size d. It is im-
portant to organize the hidden layer this way, so that all the kernel outputs from a particular
image location stay associated with that location. Unlike the spatial dimensions of the image,
however, this additional “kernel dimension” does not have any adjacency properties, so it
does not make sense to run convolutions along it.
CNNs were inspired originally by models of the visual cortex proposed in neuroscience.
In those models, the receptive ﬁeld of a neuron is the portion of the sensory input that can
Receptive ﬁeld
affect that neuron’s activation. In a CNN, the receptive ﬁeld of a unit in the ﬁrst hidden layer
is small—just the size of the kernel, i.e., l pixels. In the deeper layers of the network, it
can be much larger. Figure 22.5 illustrates this for a unit in the second hidden layer, whose
receptive ﬁeld contains ﬁve pixels. When the stride is 1, as in the ﬁgure, a node in the mth
hidden layer will have a receptive ﬁeld of size (l −1)m+1; so the growth is linear in m. (In
a 2D image, each dimension of the receptive ﬁeld grows linearly with m, so the area grows
quadratically.) When the stride is larger than 1, each pixel in layer m represents s pixels in
layer m−1; therefore, the receptive ﬁeld grows as O(lsm)—that is, exponentially with depth.
The same effect occurs with pooling layers, which we discuss next.
22.3.1 Pooling and downsampling
A pooling layer in a neural network summarizes a set of adjacent units from the preceding
Pooling
layer with a single value. Pooling works just like a convolution layer, with a kernel size l and
stride s, but the operation that is applied is ﬁxed rather than learned. Typically, no activation
function is associated with the pooling layer. There are two common forms of pooling:
• Average-pooling computes the average value of its l inputs. This is identical to con-
volution with a uniform kernel vector k=[1/l,...,1/l]. If we set l =s, the effect is to
coarsen the resolution of the image—to downsample it—by a factor of s. An object
Downsampling
that occupied, say, 10s pixels would now occupy only 10 pixels after pooling. The same
