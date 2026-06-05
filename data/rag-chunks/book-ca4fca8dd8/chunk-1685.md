---
chunk_id: "book-ca4fca8dd8-chunk-1685"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1685
confidence: "first-pass"
extraction_method: "structured-local"
---

1030
Chapter 27
Computer Vision
such as ImageNet, which provided the training data for these large, deep networks with mil-
lions of parameters. Previous data sets like Caltech-101 or PASCAL VOC didn’t have enough
training data, and MNIST and CIFAR were regarded as “toy data sets” by the computer vi-
sion community. This strand of labeling data sets for benchmarking and for extracting image
statistics itself was enabled by the desire of people to upload their photo collections to the
Internet on sites such as Flickr. The way big computation proved most helpful was through
GPUs, a hardware development initially driven by the needs of the video game industry.
Within a year or two, the evidence was quite clear. For example, the region-based con-
volutional neural network (RCNN) work of Girshick et al. (2016) showed that the AlexNet
architecture could be modiﬁed, by making use of computer vision ideas such as region pro-
posals, to make possible state-of-the-art object detection on PASCAL VOC. We have realized
that generally deeper networks work better and that overﬁtting fears are overblown. We have
new techniques such as batch normalization to deal with regularization.
The reconstruction of three-dimensional structure from multiple views has its roots in
the photogrammetry literature. In the computer vision era, Ullman (1979), and Longuet-
Higgins (1981) are inﬂuential early works. Concerns about the stability of structure from
motion were signiﬁcantly allayed by the work of Tomasi and Kanade (1992) who showed that
with the use of multiple frames, and the resulting wide baseline, shape could be recovered
quite accurately.
A conceptual innovation introduced in the 1990s was the study of projective structure
from motion. Here camera calibration is not necessary, as was shown by Faugeras (1992).
This discovery is related to the introduction of the use of geometrical invariants in object
recognition, as surveyed by Mundy and Zisserman (1992), and the development of afﬁne
structure from motion by Koenderink and Van Doorn (1991).
In the 1990s, with great increase in computer speed and storage and the widespread avail-
ability of digital video, motion analysis found many new applications. Building geometrical
models of real-world scenes for rendering by computer graphics techniques proved particu-
larly popular, led by reconstruction algorithms such as the one developed by Debevec et al.
(1996). The books by Hartley and Zisserman (2000) and Faugeras et al. (2001) provide a
comprehensive treatment of the geometry of multiple views.
Humans can perceive shape and spatial layout from a single image, and modeling this
has proved to be quite a challenge for computer vision researchers. Inferring shape from
shading was ﬁrst studied by Berthold Horn (1970), and Horn and Brooks (1989) present an
extensive survey of the main papers from a period when this was a much studied problem.
Gibson (1950) was the ﬁrst to propose texture gradients as a cue to shape. The mathematics
of occluding contours, and more generally understanding the visual events in the projection
of smooth curved objects, owes much to the work of Koenderink and van Doorn, which ﬁnds
an extensive treatment in Koenderink’s (1990) Solid Shape.
More recently, attention has turned to treating the problem of shape and surface recovery
from a single image as a probabilistic inference problem, where geometrical cues are not
modeled explicitly, but used implicitly in a learning framework. A good example is the work
of Hoiem et al. (2007); recently this has been reworked using deep neural networks.
Turning now to the applications of computer vision for guiding action, Dickmanns and
Zapp (1987) ﬁrst demonstrated a self-driving car driving on freeways at high speeds; Pomer-
leau (1993) achieved similar performance using a neural network approach. Today building
