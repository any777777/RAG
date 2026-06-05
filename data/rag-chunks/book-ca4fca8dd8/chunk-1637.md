---
chunk_id: "book-ca4fca8dd8-chunk-1637"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1637
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 996

996
Chapter 27
Computer Vision
1
2
4
2
1
1
3
Figure 27.6 Different kinds of edges: (1) depth discontinuities; (2) surface orientation dis-
continuities; (3) reﬂectance discontinuities; (4) illumination discontinuities (shadows).
in the image. Thus, edge detection can come early in the pipeline of operations and we call it
an “early” or “low-level” operation.
The other operations require handling a larger area of the image. For example, a texture
description applies to a pool of pixels—to say “stripey,” you need to see some stripes. Optical
ﬂow represents where pixels move to from one image in a sequence to the next, and this
can cover a larger area. Segmentation cuts an image into regions of pixels that naturally
belong together, and doing so requires looking at the whole region. Operations like this are
sometimes referred to as “mid-level” operations.
27.3.1 Edges
Edges are straight lines or curves in the image plane across which there is a “signiﬁcant”
Edges
change in image brightness. The goal of edge detection is to abstract away from the messy,
multi-megabyte image and towards a more compact, abstract representation, as in Figure 27.6.
Effects in the scene very often result in large changes in image intensity, and so produce edges
in the image. Depth discontinuities (labeled 1 in the ﬁgure) can cause edges because when
you cross the discontinuity, the color typically changes. When the surface normal changes
(labeled 2 in the ﬁgure), the image intensity often changes. When the surface reﬂectance
changes (labeled 3), the image intensity often changes. Finally, a shadow (labeled 4) is a
discontinuity in illumination that causes an edge in the image, even though there is not an
edge in the object. Edge detectors can’t disentangle the cause of the discontinuity, which is
left to later processing.
Finding edges requires care. Figure 27.7 (top) shows a one-dimensional crosssection of
an image perpendicular to an edge, with an edge at x = 50.
You might differentiate the image and look for places where the magnitude of the deriva-
tive I′(x) is large. This almost works, but in Figure 27.7 (middle), we see that although there
is a peak at x=50, there are also subsidiary peaks at other locations (e.g., x=75) that could be
mistaken for true edges. These arise because of the presence of “noise” in the image. Noise
Noise
here means changes to the value of a pixel that don’t have to do with an edge. For example,

## Page 997
