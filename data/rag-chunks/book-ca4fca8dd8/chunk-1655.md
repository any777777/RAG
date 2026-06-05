---
chunk_id: "book-ca4fca8dd8-chunk-1655"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1655
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.5
Detecting Objects
1007
“objectness”—whether a box has an object in it, independent of what that object is. We can
ﬁnd the boxes that look like they have an object in them, and then classify the object for just
those boxes that pass the objectness test.
A network that ﬁnds regions with objects is called a regional proposal network (RPN).
Regional proposal
network (RPN)
The object detector known as Faster RCNN encodes a large collection of bounding boxes as a
map of ﬁxed size. Then it builds a network that can predict a score for each box, and trains this
network so the score is large when the box contains an object, and small otherwise. Encoding
boxes as a map is straightforward. We consider boxes centered on points throughout the
image; we don’t need to consider every possible point (because moving by one pixel is not
likely to change the classiﬁcation); a good choice is a stride (the offset between center points)
of 16 pixels. For each center point we consider several possible boxes, called anchor boxes.
Faster RCNN uses nine boxes: small, medium, and large sizes; and tall, wide, and square
aspect ratios.
In terms of the neural network architecture, construct a 3D block where each spatial
location in the block has two dimensions for the center point and one dimension for the type
of box. Now any box with a good enough objectness score is called a region of interest
(ROI), and must be checked by a classiﬁer. But CNN classiﬁers prefer images of ﬁxed size,
and the boxes that pass the objectness test will differ in size and shape. We can’t make
the boxes have the same number of pixels, but we can make them have the same number
of features by sampling the pixels to extract features, a process called ROI pooling. This
ﬁxed-size feature map is then passed to the classiﬁer.
Now for the problem of deciding which windows to report. Assume we look at windows
of size 32×32 with a stride of 1: each window is offset by just one pixel from the one before.
There will be many windows that are similar, and should have similar scores. If they all have
a score above threshold we don’t want to report all of them, because they very likely all refer
to slightly different views of the same object. On the other hand if the stride is too large, it
might be that an object is not contained within any one window, and will be missed. Instead,
we can use a greedy algorithm called non-maximum suppression. First, build a sorted list
Non-maximum
suppression
of all windows with scores over a threshold. Then, while there are windows in the list, choose
the window with the highest score and accept it as containing an object; discard from the list
all other largely overlapping windows.
Finally, we have the problem of reporting the precise location of objects. Assume we
have a window that has a high score, and has passed through non-maximum suppression. This
window is unlikely to be in exactly the right place (remember, we looked at a relatively small
number of windows with a small number of possible sizes). We use the feature representation
computed by the classiﬁer to predict improvements that will trim the window down to a
proper bounding box, a step known as bounding box regression.
Bounding box
regression
Evaluating object detectors takes care. First we need a test set: a collection of images
with each object in the image marked by a ground truth category label and bounding box.
Usually, the boxes and labels are supplied by humans. Then we feed each image to the object
detector and compare its output to the ground truth. We should be willing to accept boxes
that are off by a few pixels, because the ground truth boxes won’t be perfect. The evaluation
score should balance recall (ﬁnding all the objects that are there) and precision (not ﬁnding
objects that are not there).
