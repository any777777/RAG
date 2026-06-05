---
chunk_id: "book-ca4fca8dd8-chunk-1377"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1377
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
837
In the late 1990s and early 2000s, interest in neural networks waned as other techniques
such as Bayes nets, ensemble methods, and kernel machines came to the fore. Interest in deep
models was sparked when Geoff Hinton’s research on deep Bayesian networks—generative
models with category variables at the root and evidence variables at the leaves—began to bear
fruit, outperforming kernel machines on small benchmark data sets (Hinton et al., 2006).
Interest in deep learning exploded when Krizhevsky et al. (2013) used deep convolutional
networks to win the ImageNet competition (Russakovsky et al., 2015).
Commentators often cite the availability of “big data” and the processing power of GPUs
as the main contributing factors in the emergence of deep learning. Architectural improve-
ments were also important, including the adoption of the ReLU activation function instead of
the logistic sigmoid (Jarrett et al., 2009; Nair and Hinton, 2010; Glorot et al., 2011) and later
the development of residual networks (He et al., 2016).
On the algorithmic side, the use of stochastic gradient descent (SGD) with small batches
was essential in allowing neural networks to scale to large data sets (Bottou and Bousquet,
2008). Batch normalization (Ioffe and Szegedy, 2015) also helped in making the training pro-
cess faster and more reliable and has spawned several additional normalization techniques (Ba
et al., 2016; Wu and He, 2018; Miyato et al., 2018). Several papers have studied the empirical
behavior of SGD on large networks and large data sets (Dauphin et al., 2015; Choromanska
et al., 2014; Goodfellow et al., 2015b). On the theoretical side, some progress has been made
on explaining the observation that SGD applied to overparameterized networks often reaches
a global minimum with a training error of zero, although so far the theorems to this effect
assume a network with layers far wider than would ever occur in practice (Allen-Zhu et al.,
2018; Du et al., 2018). Such networks have more than enough capacity to function as lookup
tables for the training data.
The last piece of the puzzle, at least for vision applications, was the use of convolutional
networks. These had their origins in the descriptions of the mammalian visual system by
neurophysiologists David Hubel and Torsten Wiesel (Hubel and Wiesel, 1959, 1962, 1968).
They described “simple cells” in the visual system of a cat that resemble edge detectors,
as well as “complex cells” that are invariant to some transformations such as small spatial
translations. In modern convolutional networks, the output of a convolution is analogous to a
simple cell while the output of a pooling layer is analogous to a complex cell.
The work of Hubel and Wiesel inspired many of the early connectionist models of vision
(Marr and Poggio, 1976). The neocognitron (Fukushima, 1980; Fukushima and Miyake,
1982), designed as a model of the visual cortex, was essentially a convolutional network in
terms of model architecture, although an effective training algorithm for such networks had
to wait until Yann LeCun and collaborators showed how to apply back-propagation (LeCun
et al., 1995). One of the early commercial successes of neural networks was handwritten digit
recognition using convolutional networks (LeCun et al., 1995).
Recurrent neural networks (RNNs) were commonly proposed as models of brain function
in the 1970s, but no effective learning algorithms were associated with these proposals. The
method of back-propagation through time appears in the PhD thesis of Paul Werbos (1974),
and his later review paper (Werbos, 1990) gives several additional references to rediscoveries
of the method in the 1980s. One of the most inﬂuential early works on RNNs was due to
Jeff Elman (1990), building on an RNN architecture suggested by Michael Jordan (1986).
Williams and Zipser (1989) present an algorithm for online learning in RNNs. Bengio et al.
