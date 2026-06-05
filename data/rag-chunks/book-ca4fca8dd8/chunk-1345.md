---
chunk_id: "book-ca4fca8dd8-chunk-1345"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1345
confidence: "first-pass"
extraction_method: "structured-local"
---

820
Chapter 22
Deep Learning
 0
 0.02
 0.04
 0.06
 0.08
 0.1
 0
 1
 2
 3
 4
 5
 6
 7
Test-set error
Number of weights (× 107)
3-layer
11-layer
Figure 22.7 Test-set error as a function of layer width (as measured by total number of
weights) for three-layer and eleven-layer convolutional networks. The data come from early
versions of Google’s system for transcribing addresses in photos taken by Street View cars
(Goodfellow et al., 2014).
One of the most important empirical ﬁndings in the ﬁeld of deep learning is that when
comparing two networks with similar numbers of weights, the deeper network usually gives
better generalization performance. Figure 22.7 shows this effect for at least one real-world
application—recognizing house numbers. The results show that for any ﬁxed number of pa-
rameters, an eleven-layer network gives much lower test-set error than a three-layer network.
Deep learning systems perform well on some but not all tasks. For tasks with high-
dimensional inputs—images, video, speech signals, etc.—they perform better than any other
pure machine learning approaches. Most of the algorithms described in Chapter 19 can handle
high-dimensional input only if it is preprocessed using manually designed features to reduce
the dimensionality. This preprocessing approach, which prevailed prior to 2010, has not
yielded performance comparable to that achieved by deep learning systems.
Clearly, deep learning models are capturing some important aspects of these tasks. In par-
ticular, their success implies that the tasks can be solved by parallel programs with a relatively
small number of steps (10 to 103 rather than, say, 107). This is perhaps not surprising, be-
cause these tasks are typically solved by the brain in less than a second, which is time enough
for only a few tens of sequential neuron ﬁrings. Moreover, by examining the internal-layer
representations learned by deep convolutional networks for vision tasks, we ﬁnd evidence
that the processing steps seem to involve extracting a sequence of increasingly abstract repre-
sentations of the scene, beginning with tiny edges, dots, and corner features and ending with
entire objects and arrangements of multiple objects.
On the other hand, because they are simple circuits, deep learning models lack the com-
positional and quantiﬁcational expressive power that we see in ﬁrst-order logic (Chapter 8)
and context-free grammars (Chapter 24).
Although deep learning models generalize well in many cases, they may also produce
unintuitive errors. They tend to produce input–output mappings that are discontinuous, so
that a small change to an input can cause a large change in the output. For example, it may
