---
chunk_id: "book-ca4fca8dd8-chunk-1327"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1327
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.3
Convolutional Networks
811
22.3 Convolutional Networks
We mentioned in Section 22.2.1 that an image cannot be thought of as a simple vector of in-
put pixel values, primarily because adjacency of pixels really matters. If we were to construct
a network with fully connected layers and an image as input, we would get the same result
whether we trained with unperturbed images or with images all of whose pixels had been ran-
domly permuted. Furthermore, suppose there are n pixels and n units in the ﬁrst hidden layer,
to which the pixels provide input. If the input and the ﬁrst hidden layer are fully connected,
that means n2 weights; for a typical megapixel RGB image, that’s 9 trillion weights. Such a
vast parameter space would require correspondingly vast numbers of training images and a
huge computational budget to run the training algorithm.
These considerations suggest that we should construct the ﬁrst hidden layer so that each ◀
hidden unit receives input from only a small, local region of the image. This kills two birds
with one stone. First, it respects adjacency, at least locally. (And we will see later that if
subsequent layers have the same locality property, then the network will respect adjacency in
a global sense.) Second, it cuts down the number of weights: if each local region has l ≪n
pixels, then there will be ln ≪n2 weights in all.
So far, so good. But we are missing another important property of images: roughly
speaking, anything that is detectable in one small, local region of the image—perhaps an eye
or a blade of grass—would look the same if it appeared in another small, local region of the
image. In other words, we expect image data to exhibit approximate spatial invariance, at
Spatial invariance
least at small to moderate scales.3 We don’t necessarily expect the top halves of photos to
look like bottom halves, so there is a scale beyond which spatial invariance no longer holds.
Local spatial invariance can be achieved by constraining the l weights connecting a local
region to a unit in the hidden layer to be the same for each hidden unit. (That is, for hidden
units i and j, the weights w1,i,...,wl,i are the same as w1,j,...,wl,j.) This makes the hidden
units into feature detectors that detect the same feature wherever it appear in the image.
Typically, we want the ﬁrst hidden layer to detect many kinds of features, not just one; so
for each local image region we might have d hidden units with d distinct sets of weights.
This means that there are dl weights in all—a number that is not only far smaller than n2,
but is actually independent of n, the image size. Thus, by injecting some prior knowledge—
namely, knowledge of adjacency and spatial invariance—we can develop models that have
far fewer parameters and can learn much more quickly.
A convolutional neural network (CNN) is one that contains spatially local connections,
Convolutional neural
network (CNN)
at least in the early layers, and has patterns of weights that are replicated across the units
in each layer. A pattern of weights that is replicated across multiple local regions is called
a kernel and the process of applying the kernel to the pixels of the image (or to spatially
Kernel
organized units in a subsequent layer) is called convolution.4
Convolution
Kernels and convolutions are easiest to illustrate in one dimension rather than two or
more, so we will assume an input vector x of size n, corresponding to n pixels in a one-
3
Similar ideas can be applied to process time-series data sources such as audio waveforms. These typically
exhibit temporal invariance—a word sounds the same no matter what time of day it is uttered. Recurrent neural
networks (Section 22.6) automatically exhibit temporal invariance.
4
In the terminology of signal processing, we would call this operation a cross-correlation, not a convolution.
But “convolution” is used within the ﬁeld of neural networks.
