---
chunk_id: "book-ca4fca8dd8-chunk-1365"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1365
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.7
Unsupervised Learning and Transfer Learning
831
Generative adversarial networks
A generative adversarial network (GAN) is actually a pair of networks that combine to
Generative
adversarial network
(GAN)
form a generative system. One of the networks, the generator, maps values from z to x in
Generator
order to produce samples from the distribution Pw(x). A typical scheme samples z from a unit
Gaussian of moderate dimension and then passes it through a deep network hw to obtain x.
The other network, the discriminator, is a classiﬁer trained to classify inputs x as real (drawn
Discriminator
from the training set) or fake (created by the generator). GANs are a kind of implicit model
Implicit model
in the sense that samples can be generated but their probabilities are not readily available; in a
Bayes net, on the other hand, the probability of a sample is just the product of the conditional
probabilities along the sample generation path.
The generator is closely related to the decoder from the variational autoencoder frame-
work. The challenge in implicit modeling is to design a loss function that makes it possible
to train the model using samples from the distribution, rather than maximizing the likelihood
assigned to training examples from the data set.
Both the generator and the discriminator are trained simultaneously, with the generator
learning to fool the discriminator and the discriminator learning to accurately separate real
from fake data. The competition between generator and discriminator can be described in
the language of game theory (see Chapter 17). The idea is that in the equilibrium state of the
game, the generator should reproduce the training distribution perfectly, such that the discrim-
inator cannot perform better than random guessing. GANs have worked particularly well for
image generation tasks. For example, GANs can create photorealistic, high-resolution images
of people who have never existed (Karras et al., 2017).
Unsupervised translation
Translation tasks, broadly construed, consist of transforming an input x that has rich structure
into an output y that also has rich structure. In this context, “rich structure” means that the
data are multidimensional and have interesting statistical dependencies among the various
dimensions. Images and natural language sentences have a rich structure, but a single number,
such as a class ID, does not. Transforming a sentence from English to French or converting
a photo of a night scene into an equivalent photo taken during the daytime are both examples
of translation tasks.
Supervised translation consists of gathering many (x,y) pairs and training the model to
map each x to the corresponding y. For example, machine translation systems are often
trained on pairs of sentences that have been translated by professional human translators. For
other kinds of translation, supervised training data may not be available. For example, con-
sider a photo of a night scene containing many moving cars and pedestrians. It is presumably
not feasible to ﬁnd all of the cars and pedestrians and return them to their original positions in
the night-time photo in order to retake the same photo in the daytime. To overcome this dif-
ﬁculty, it is possible to use unsupervised translation techniques that are capable of training
Unsupervised
translation
on many examples of x and many separate examples of y but no corresponding (x,y) pairs.
These approaches are generally based on GANs; for example, one can train a GAN gen-
erator to produce a realistic example of y when conditioned on x, and another GAN generator
to perform the reverse mapping. The GAN training framework makes it possible to train a
generator to generate any one of many possible samples that the discriminator accepts as a
