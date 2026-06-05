---
chunk_id: "book-ca4fca8dd8-chunk-1674"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1674
confidence: "first-pass"
extraction_method: "structured-local"
---

1022
Chapter 27
Computer Vision
i
cycle-consistency error
X
Y
yi
ˆxi
xi
Objective
Result
xi
…
Y
…
Training data
Input
Training
Test
,
yˆ
ˆ
X
Figure 27.25 Unpaired image translation: given two populations of images (here type X is
horses and type Y is zebras), but no corresponding pairs, learn to translate a horse into a
zebra. The method trains two predictors: one that maps type X to type Y, and another that
maps type Y to type X. If the ﬁrst network maps a horse xi to a zebra ˆyi, the second network
should map ˆyi back to the original xi. The difference between xi and ˆxi is what trains the two
networks. The cycle from Y to X and back must be closed. Such networks can successfully
impose rich transformations on images. Figure courtesy of Alexei A. Efros; see Zhu et al.
(2017). Running horse photo by Justyna Furmanczyk Gibaszek/Shutterstock.
X (or Y to X to Y), you get what you started with. Again, GAN losses ensure that the horse
(or zebra) pictures that the networks output are “like” real horse (or zebra) pictures.
Another artistic effect is called style transfer: the input consists of two images—the
Style transfer
content (for example, a photograph of a cat); and the style (for example, an abstract painting).
The output is a version of the cat rendered in the abstract style (see Figure 27.26). The key
insight to solving this problem is that if we examine a deep convolutional neural network
(CNN) that has been trained to do object recognition (say, on ImageNet), we ﬁnd that the
early layers tend to represent the style of a picture, and the late layers represent the content.
Let p be the content image and s be the style image, and let E(x) be the vector of activations
of an early layer on image x and L(x) be the vector of activations of a late layer on image
x. Then we want to generate some image x that has similar content to the house photo,
that is, minimizes |L(x)−L(p)|, and also has similar style to the impressionist painting, that
is, minimizes |E(x) −E(s)|. We use gradient descent with a loss function that is a linear
combination of these two factors to ﬁnd an image x that minimizes the loss.
Generative adversarial networks (GANs) can create novel photorealistic images, fooling
most people most of the time. One kind of image is the deepfake—an image or video that
Deepfake
looks like a particular person, but is generated from a model. For example, when Carrie Fisher
was 60, a generated replica of her 19-year-old face was superimposed on another actor’s body
for the making of Rogue One. The movie industry creates ever-better deepfakes for artistic
purposes, and researchers work on countermeasures for detecting deepfakes, to mitigate the
destructive effects of fake news.
Generated images can also be used to maintain privacy. For example, there are image
data sets in radiological practices that would be useful for researchers, but can’t be published
because of patient conﬁdentiality. Generative image models can take a private data set of
images and produce a synthetic data set that can be shared with researchers. This data set
should be (a) like the training data set; (b) different; and (c) controllable. Consider chest
X-rays. The synthetic data set should be like the training data set in the sense that each image
individually would fool a radiologist and the frequencies of each effect should be right, so
