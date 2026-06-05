---
chunk_id: "book-ca4fca8dd8-chunk-1653"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1653
confidence: "first-pass"
extraction_method: "structured-local"
---

1006
Chapter 27
Computer Vision
distraction. For example, if a cat is lying on a dog bed, we want a classiﬁer to concentrate
on the pixels of the cat, not the bed. Modern image classiﬁers handle this well, classifying
an image as “cat” accurately even if few pixels actually lie on the cat. There are two reasons
for this. First, CNN-based classiﬁers are good at ignoring patterns that aren’t discriminative.
Second, patterns that lie off the object might be discriminative (e.g., a cat toy, a collar with
a little bell, or a dish of cat food might actually help tell that we are looking at a cat). This
effect is known as context. Context can help or can hurt, depending quite strongly on the
Context
particular data set and application.
27.5 Detecting Objects
Image classiﬁers predict what is in the image—they classify the whole image as belonging to
one class. Object detectors ﬁnd multiple objects in an image, report what class each object is,
and also report where each object is by giving a bounding box around the object.1 The set of
Bounding box
classes is ﬁxed in advance. So we might try to detect all faces, all cars, or all cats.
We can build an object detector by looking at a small sliding window onto the larger
Sliding window
image—a rectangle. At each spot, we classify what we see in the window, using a CNN
classiﬁer. We then take the high-scoring classiﬁcations—a cat over here and a dog over
there—and ignore the other windows. After some work resolving conﬂicts, we have a ﬁnal
set of objects with their locations. There are still some details to work out:
• Decide on a window shape: The easiest choice by far is to use axis-aligned rectangles.
(The alternative—some form of mask that cuts the object out of the image—is hardly
ever used, because it is hard to represent and to compute with.) We still need to choose
the width and height of the rectangles.
• Build a classiﬁer for windows: We already know how to do this with a CNN.
• Decide which windows to look at: Out of all possible windows, we want to select ones
that are likely to have interesting objects in them.
• Choose which windows to report: Windows will overlap, and we don’t want to report
the same object multiple times in slightly different windows. Some objects are not
worth mentioning; think about the number of chairs and people in a picture of a large
packed lecture hall. Should they all be reported as individual objects? Perhaps only the
objects that appear large in the image—the front row—should be reported. The choice
depends on the intended use of the object detector.
• Report precise locations of objects using these windows: Once we know that the
object is somewhere in the window, we can afford to do more computation to ﬁgure out
a more precise location within the window.
Let’s look more carefully at the problem of deciding which windows to look at. Search-
ing all possible windows isn’t efﬁcient—in an n × n pixel image there are O(n4) possible
rectangular windows. But we know that windows that contain objects tend to have quite co-
herent color and texture. On the other hand, windows that cut an object in half have regions
or edges that cross the side of the window. So it makes sense to have a mechanism that scores
1
We will use the term “box” to mean any axis-aligned rectangular region of the image, and the term “window”
mostly as a synonym for “box,” but with the connotation that we have a window onto the input where we are
hoping to see something, and a bounding box in the output when we have found it.
