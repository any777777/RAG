---
chunk_id: "book-ca4fca8dd8-chunk-1649"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1649
confidence: "first-pass"
extraction_method: "structured-local"
---

1004
Chapter 27
Computer Vision
ﬁne-grained categories. ImageNet also spurred progress with an annual competition. Systems
are evaluated by both the classiﬁcation accuracy of their single best guess and by top-5 ac-
curacy, in which systems are allowed to submit ﬁve guesses—for example, malamute, husky,
akita, samoyed, eskimo dog. ImageNet has 189 subcategories of dog, so even dog-loving
humans ﬁnd it hard to label images correctly with a single guess.
In the ﬁrst ImageNet competition in 2010, systems could do no better than 70% top-5
accuracy. The introduction of convolutional neural networks in 2012 and their subsequent
reﬁnement led to an accuracy of 98% in top-5 (surpassing human performance) and 87% in
top-1 accuracy by 2019. The primary reason for this success seems to be that the features that
are being used by CNN classiﬁers are learned from data, not hand-crafted by a researcher;
this ensures that the features are actually useful for classiﬁcation.
Progress in image classiﬁcation has been rapid because of the availability of large, chal-
lenging data sets such as ImageNet; because of competitions based on these data sets that
are fair and open; and because of the widespread dissemination of successful models. The
winners of competitions publish the code and often the pretrained parameters of their models,
making it easy for others to ﬁddle with successful architectures and try to make them better.
27.4.2 Why convolutional neural networks classify images well
Image classiﬁcation is best understood by looking at data sets, but ImageNet is much too
large to look at in detail. The MNIST data set is a collection of 70,000 images of handwritten
digits, 0–9, which is often used as a standard warmup data set. Looking at this data set (some
examples appear in Figure 27.12) exposes some important, quite general, properties. You can
take an image of a digit and make a number of small alterations without changing the identity
of the digit: you can shift it, rotate it, make it brighter or darker, smaller or larger. This means
that individual pixel values are not particularly informative—we know that an 8 should have
some dark pixels in the center and a 0 should not, but those dark pixels will be in slightly
different pixel locations in each instance of an 8.
Another important property of images is that local patterns can be quite informative:
The digits 0, 6, 8 and 9 have loops; the digits 4 and 8 have crossings; the digits 1, 2, 3, 5
and 7 have line endings, but no loops or crossings; the digits 6 and 9 have loops and line
endings. Furthermore, spatial relations between local patterns are informative. A 1 has two
line endings above one another; a 6 has a line ending above a loop. These observations
suggest a strategy that is a central tenet of modern computer vision: you construct features
that respond to patterns in small, localized neighborhoods; then other features look at patterns
of those features; then others look at patterns of those, and so on.
This is what convolutional neural networks do well. You should think of a layer—a con-
volution followed by a ReLU activation function—as a local pattern detector (Figure 27.12).
The convolution measures how much each local window of the image looks like the kernel
pattern; the ReLU sets low-scoring windows to zero, and emphasizes high-scoring windows.
So convolution with multiple kernels ﬁnds multiple patterns; furthermore, composite patterns
can be detected by applying another layer to the output of the ﬁrst layer.
Think about the output of the ﬁrst convolutional layer. Each location receives inputs from
pixels in a window about that location. The output of the ReLU, as we have seen, forms a
simple pattern detector. Now if we put a second layer on top of this, each location in the
second layer receives inputs from ﬁrst-layer values in a window about that location. This
