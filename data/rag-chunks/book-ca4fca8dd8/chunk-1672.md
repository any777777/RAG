---
chunk_id: "book-ca4fca8dd8-chunk-1672"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1672
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1020

1020
Chapter 27
Computer Vision
Figure 27.22 If you have seen many pictures of some category—say, birds (top)—you can
use them to produce a 3D reconstruction from a single new view (bottom). You need to be
sure that all objects have a fairly similar geometry (so a picture of an ostrich won’t help if
you’re looking at a sparrow), but classiﬁcation methods can sort this out. From the many
images you can estimate how texture values in the image are distributed across the object,
and thus complete the texture for parts of the bird you haven’t seen yet (bottom). Figure
courtesy of Angjoo Kanazawa, produced by a system described in Kanazawa et al. (2018b).
Top photo credit: Satori/123RF; Bottom left credit: Four Oaks/Shutterstock.
27.7.5 Making pictures
It is now common to insert computer graphics models into photographs in a convincing fash-
ion, as in Figure 27.23, where a statue has been placed into a photo of a room. First estimate
a depth map and albedo for the picture. Then estimate the lighting in the image by matching
it to other images with known lighting. Place the object in the image’s depth map, and render
the resulting world with a physical rendering program—a standard tool in computer graphics.
Finally, blend the modiﬁed image with the original image.
Neural networks can also be trained to do image transformation: mapping images from
Image
transformation
type X—for example, a blurry image; an aerial image of a town; or a drawing of a new
product—to images of type Y—for example, a deblurred version of the image; a road map;
or a product photograph. This is easiest when the training data consists of (X, Y) pairs of
images—in Figure 27.24 each example pair has an aerial image and the corresponding road
map section. The training loss compares the output of the network with the desired output,
and also has a loss component from a generative adversarial network (GAN) that ensures that
the output has the right kinds of features for images of type Y. As we see in the test portion
of Figure 27.24, systems of this kind perform very well.
Sometimes we don’t have images that are paired with each other, but we do have a big
collection of images of type X (say, pictures of horses) and a separate collection of type Y

## Page 1021
