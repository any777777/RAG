---
chunk_id: "book-ca4fca8dd8-chunk-1651"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1651
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.4
Classifying Images
1005
Digits
Kernels
Convolution output
Test against threshold 
Figure 27.12 On the far left, some images from the MNIST data set. Three kernels appear
on the center left. They are shown at actual size (tiny blocks) and magniﬁed to reveal their
content: mid-grey is zero, light is positive, and dark is negative. Center right shows the results
of applying these kernels to the images. Right shows pixels where the response is bigger than
a threshold (green) or smaller than a threshold (red). You should notice that this gives (from
top to bottom): a horizontal bar detector; a vertical bar detector; and (harder to note) a line
ending detector. These detectors pay attention to the contrast of the bar, so (for example) a
horizontal bar that is light on top and dark below produces a positive (green) response, and
one that is dark on top and light below gets a negative (red) response. These detectors are
moderately effective, but not perfect.
means that locations in the second layer are affected by a larger window of pixels than those
in the ﬁrst layer. You should think of these as representing “patterns of patterns.” If we place
a third layer on top of the second layer, locations in that third layer will depend on an even
larger window of pixels; a fourth layer will depend on a yet larger window, and so on. The
network is creating patterns at multiple levels, and is doing that by learning from the data
rather than having the patterns given to it by a programmer.
While training a CNN “out of the box” does sometimes work, it helps to know a few
practical techniques. One of the most important is data set augmentation, in which training
Data set
augmentation
examples are copied and modiﬁed slightly. For example, one might randomly shift, rotate,
or stretch an image by a small amount, or randomly shift the hue of the pixels by a small
amount. Introducing this simulated variation in viewpoint or lighting to the data set helps to
increase the size of the data set, though of course the new examples are highly correlated with
the originals. It is also possible to use augmentation at test time rather than training time. In
this approach, the image is replicated and modiﬁed several times (e.g., with random cropping)
and the classiﬁer is run on each of the modiﬁed images. The outputs of the classiﬁer from
each copy are then used to vote for a ﬁnal decision on the overall class.
When you are classifying images of scenes, every pixel could be helpful. But when you
are classifying images of objects, some pixels aren’t part of the object, and so might be a
