---
chunk_id: "book-ca4fca8dd8-chunk-1359"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1359
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.7
Unsupervised Learning and Transfer Learning
827
case that our current approach to supervised deep learning renders some tasks completely
unattainable because the requirements for labeled data would exceed what the human race
(or the universe) can supply. Moreover, even in cases where the task is feasible, labeling
large data sets usually requires scarce and expensive human labor.
For these reasons, there is intense interest in several learning paradigms that reduce the
dependence on labeled data. As we saw in Chapter 19, these paradigms include unsuper-
vised learning, transfer learning, and semisupervised learning. Unsupervised learning
algorithms learn solely from unlabeled inputs x, which are often more abundantly available
than labeled examples. Unsupervised learning algorithms typically produce generative mod-
els, which can produce realistic text, images, audio, and video, rather than simply predicting
labels for such data. Transfer learning algorithms require some labeled examples but are able
to improve their performance further by studying labeled examples for different tasks, thus
making it possible to draw on more existing sources of data. Semisupervised learning algo-
rithms require some labeled examples but are able to improve their performance further by
also studying unlabeled examples. This section covers deep learning approaches to unsuper-
vised and transfer learning; while semisupervised learning is also an active area of research
in the deep learning community, the techniques developed so far have not proven broadly
effective in practice, so we do not cover them.
22.7.1 Unsupervised learning
Supervised learning algorithms all have essentially the same goal: given a training set of
inputs x and corresponding outputs y= f(x), learn a function h that approximates f well.
Unsupervised learning algorithms, on the other hand, take a training set of unlabeled exam-
ples x. Here we describe two things that such an algorithm might try to do. The ﬁrst is to
learn new representations—for example, new features of images that make it easier to iden-
tify the objects in an image. The second is to learn a generative model—typically in the form
of a probability distribution from which new samples can be generated. (The algorithms for
learning Bayes nets in Chapter 21 fall in this category.) Many algorithms are capable of both
representation learning and generative modeling.
Suppose we learn a joint model PW(x,z), where z is a set of latent, unobserved variables
that represent the content of the data x in some way. In keeping with the spirit of the chapter,
we do not predeﬁne the meanings of the z variables; the model is free to learn to associate
z with x however it chooses. For example, a model trained on images of handwritten digits
might choose to use one direction in z space to represent the thickness of pen strokes, another
to represent ink color, another to represent background color, and so on. With images of
faces, the learning algorithm might choose one direction to represent gender and another to
capture the presence or absence of glasses, as illustrated in Figure 22.9.
A learned probability model PW(x,z) achieves both representation learning (it has con-
structed meaningful z vectors from the raw x vectors) and generative modeling: if we inte-
grate z out of PW(x,z) we obtain PW(x).
Probabilistic PCA: A simple generative model
There have been many proposals for the form that PW(x,z) might take. One of the simplest
is the probabilistic principal components analysis (PPCA) model.7 In a PPCA model, z
PPCA
