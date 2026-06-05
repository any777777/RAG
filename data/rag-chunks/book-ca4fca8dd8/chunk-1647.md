---
chunk_id: "book-ca4fca8dd8-chunk-1647"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1647
confidence: "first-pass"
extraction_method: "structured-local"
---

1002
Chapter 27
Computer Vision
(a)
(b)
(c)
(d)
Figure 27.10 (a) Original image. (b) Boundary contours, where the higher the Pb value,
the darker the contour. (c) Segmentation into regions, corresponding to a ﬁne partition of
the image. Regions are rendered in their mean colors. (d) Segmentation into regions, corre-
sponding to a coarser partition of the image, resulting in fewer regions. (Images courtesy of
Pablo Arbelaez, Michael Maire, Charless Fowlkes and Jitendra Malik.)
It turns out that the approaches based on ﬁnding boundaries and on ﬁnding regions can
be coupled, but we will not explore these possibilities here. Segmentation based purely on
low-level, local attributes such as brightness and color can not be expected to deliver the ﬁnal
correct boundaries of all the objects in the scene. To reliably ﬁnd boundaries associated with
objects, it is also necessary to incorporate high-level knowledge of the kinds of objects one
may expect to encounter in a scene. At this time, a popular strategy is to produce an over-
segmentation of an image, where one is guaranteed not to have missed marking any of the true
boundaries but may have marked many extra false boundaries as well. The resulting regions,
called superpixels, provide a signiﬁcant reduction in computational complexity for various
algorithms, as the number of superpixels may be in the hundreds, compared to millions of
raw pixels. Exploiting high-level knowledge of objects is the subject of the next section, and
actually detecting the objects in images is the subject of Section 27.5.
27.4 Classifying Images
Image classiﬁcation applies to two main cases. In one, the images are of objects, taken from
a given taxonomy of classes, and there’s not much else of signiﬁcance in the picture—for
example, a catalog of clothing or furniture images, where the background doesn’t matter, and
the output of the classiﬁer is “cashmere sweater” or “desk chair.”
In the other case, each image shows a scene containing multiple objects. So in grassland
you might see a giraffe and a lion, and in the living room you might see a couch and lamp,
but you don’t expect a giraffe or a submarine in a living room. We now have methods for
large-scale image classiﬁcation that can accurately output “grassland” or “living room.”
Modern systems classify images using appearance (i.e., color and texture, as opposed
Appearance
to geometry). There are two difﬁculties. First, different instances of the same class could
look different—some cats are black and others are orange. Second, the same cat could look
