---
chunk_id: "book-ca4fca8dd8-chunk-1648"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1648
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1003

Section 27.4
Classifying Images
1003
Foreshortening
Aspect
Occlusion
Deformation
Figure 27.11 Important sources of appearance variation that can make different images of
the same object look different. First, elements can foreshorten, like the circular patch on the
top left. This patch is viewed at a glancing angle, and so is elliptical in the image. Second,
objects viewed from different directions can change shape quite dramatically, a phenomenon
known as aspect. On the top right are three different aspects of a doughnut. Occlusion causes
the handle of the mug on the bottom left to disappear when the mug is rotated. In this case,
because the body and handle belong to the same mug, we have self-occlusion. Finally, on the
bottom right, some objects can deform dramatically.
different at different times depending on several effects, (as illustrated in Figure 27.11):
• Lighting, which changes the brightness and color of the image.
• Foreshortening, which causes a pattern viewed at a glancing angle to be distorted.
• Aspect, which causes objects to look different when seen from different directions. A
doughnut seen from the side looks like a ﬂattened oval, but from above it is an annulus.
• Occlusion, where some parts of the object are hidden. Objects can occlude one another,
or parts of an object can occlude other parts, an effect known as self-occlusion.
• Deformation, where the object changes its shape. For example, the tennis player moves
her arms and legs.
Modern methods deal with these problems by learning representations and classiﬁers from
very large quantities of training data using a convolutional neural network. With a sufﬁciently
rich training set the classiﬁer will have seen any effect of importance many times in training,
and so can adjust for the effect.
27.4.1 Image classiﬁcation with convolutional neural networks
Convolutional neural networks (CNNs) are spectacularly successful image classiﬁers. With
enough training data and enough training ingenuity, CNNs produce very successful classiﬁ-
cation systems, much better than anyone has been able to produce with other methods.
The ImageNet data set played a historic role in the development of image classiﬁcation
systems by providing them with over 14 million training images, classiﬁed into over 30,000

## Page 1004
