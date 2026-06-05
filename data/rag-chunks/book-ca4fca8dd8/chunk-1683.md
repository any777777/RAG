---
chunk_id: "book-ca4fca8dd8-chunk-1683"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1683
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
1029
Through much of the 1960s, 1970s, and 1980s, there were two distinct paradigms in
which visual recognition was pursued, dictated by different perspectives on what was per-
ceived to be the primary problem. Computer vision research on object recognition largely fo-
cused on issues arising from the projection of three-dimensional objects onto two-dimensional
images. The idea of alignment, also ﬁrst introduced by Roberts, resurfaced in the 1980s in
the work of Lowe (1987) and Huttenlocher and Ullman (1990).
The pattern recognition community took a different approach, viewing the 3D–to–2D
aspects of the problem as insigniﬁcant. Their motivating examples were in domains such
as optical character recognition and handwritten zip code recognition, in which the primary
concern is that of learning the typical variations characteristic of a class of objects and sep-
arating them from other classes. We can trace neural net architectures for image analysis
back to Hubel and Wiesel’s (1962, 1968) studies of the visual cortex in cats and monkeys.
They developed a hierarchical model of the visual pathway with neurons in lower areas of the
brain (especially the area called V1) responding to features such as oriented edges and bars,
and neurons in higher areas responding to more speciﬁc stimuli (“grandmother cells” in the
cartoon version).
Fukushima (1980) proposed a neural network architecture for pattern recognition explic-
itly motivated by Hubel and Wiesel’s hierarchy. His model had alternating layers of simple
cells and complex cells, thus incorporating downsampling, and also had shift invariance, thus
incorporating convolutional structure. LeCun et al. (1989) took the additional step of using
back-propagation to train the weights of this network, and what we today call convolutional
neural networks were born. See LeCun et al. (1995) for a comparison of approaches.
Starting in the late 1990s, accompanying a much greater role of probabilistic modeling
and statistical machine learning in the ﬁeld of artiﬁcial intelligence in general, there was a
rapprochement between these two traditions. Two lines of work contributed signiﬁcantly.
One was research on face detection (Rowley et al., 1998; Viola and Jones, 2004) that demon-
strated the power of pattern recognition techniques on clearly important and useful tasks.
The other was the development of point descriptors, which enable the construction of
feature vectors from parts of objects (Schmid and Mohr, 1996). There are three key strategies
to build a good local point descriptor: one uses orientations to get illumination invariance; one
needs to describe image structure close to a point in detail, and further away only roughly; and
one needs to use spatial histograms to suppress variations caused by small errors in locating
the point. Lowe’s (2004) SIFT descriptor exploited these ideas very effectively; another
popular variant was the HOG descriptor due to Dalal and Triggs (2005).
The 1990s and 2000s saw a continuing debate between the devotees of clever feature
design such as SIFT and HOG and the aﬁcionados of neural networks who believed that good
features should emerge automatically from end-to-end training. The way to settle such a
debate is through benchmarks on standard data sets, and in the 2000s results on a standard
object detection data set, PASCAL VOC, argued in favor of hand-designed features. This
changed when Krizhevsky et al. (2013) showed that on the task of image classiﬁcation on the
ImageNet data set, their neural network (called AlexNet) gave signiﬁcantly lower error rates
than the mainstream computer vision techniques.
What was the secret sauce behind the success of AlexNet? Besides the technical innova-
tions (such as the use of ReLU activation units) we must give a lot of credit to big data and
big computation. By big data we mean the availability of large data sets with category labels,
