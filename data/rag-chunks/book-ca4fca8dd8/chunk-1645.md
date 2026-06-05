---
chunk_id: "book-ca4fca8dd8-chunk-1645"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1645
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.3
Simple Image Features
1001
Here, (x,y) ranges over pixels in the block centered at (x0,y0). We ﬁnd the (Dx,Dy) that
minimizes the SSD. The optical ﬂow at (x0,y0) is then (vx,vy) = (Dx/Dt,Dy/Dt). Note that
for this to work, there should be some texture in the scene, resulting in windows containing a
signiﬁcant variation in brightness among the pixels. If one is looking at a uniform white wall,
then the SSD is going to be nearly the same for the different candidate matches q, and the
algorithm is reduced to making a blind guess. The best-performing algorithms for measuring
optical ﬂow rely on a variety of additional constraints to deal with situations in which the
scene is only partially textured.
27.3.4 Segmentation of natural images
Segmentation is the process of breaking an image into groups of similar pixels. The basic
Segmentation
idea is that each image pixel can be associated with certain visual properties, such as bright-
ness, color, and texture. Within an object, or a single part of an object, these attributes vary
relatively little, whereas across an inter-object boundary there is typically a large change in
one or more of these attributes. We need to ﬁnd a partition of the image into sets of pixels
such that these constraints are satisﬁed as well as possible. Notice that it isn’t enough just to
ﬁnd edges, because many edges are not object boundaries. So, for example, a tiger in grass
may generate an edge on each side of each stripe and each blade of grass. In all the confusing
edge data, we may miss the tiger for the stripes.
There are two ways of studying the problem, one focusing on detecting the boundaries of
these groups, and the other on detecting the groups themselves, called regions. We illustrate
Regions
this in Figure 27.10, showing boundary detection in (b) and region extraction in (c) and (d).
One way to formalize the problem of detecting boundary curves is as a classiﬁcation
problem, amenable to the techniques of machine learning. A boundary curve at pixel location
(x,y) will have an orientation θ. An image neighborhood centered at (x,y) looks roughly
like a disk, cut into two halves by a diameter oriented at θ. We can compute the probability
Pb(x,y,θ) that there is a boundary curve at that pixel along that orientation by comparing
features in the two halves. The natural way to predict this probability is to train a machine
learning classiﬁer using a data set of natural images in which humans have marked the ground
truth boundaries—the goal of the classiﬁer is to mark exactly those boundaries marked by
humans and no others.
Boundaries detected by this technique are better than those found using the simple edge
detection technique described previously. But there are still two limitations: (1) the boundary
pixels formed by thresholding Pb(x,y,θ) are not guaranteed to form closed curves, so this
approach doesn’t deliver regions, and (2) the decision making exploits only local context,
and does not use global consistency constraints.
The alternative approach is based on trying to “cluster” the pixels into regions based on
their brightness, color and texture properties. There are a number of different ways in which
this intuition can be formalized mathematically. For instance, Shi and Malik (2000) set this
up as a graph partitioning problem. The nodes of the graph correspond to pixels, and edges
to connections between pixels. The weight Wij on the edge connecting a pair of pixels i and
j is based on how similar the two pixels are in brightness, color, texture, etc. They then
ﬁnd partitions that minimize a normalized cut criterion. Roughly speaking, the criterion for
partitioning the graph is to minimize the sum of weights of connections across the groups and
maximize the sum of weights of connections within the groups.
