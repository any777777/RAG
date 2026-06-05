---
chunk_id: "book-ca4fca8dd8-chunk-1379"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1379
confidence: "first-pass"
extraction_method: "structured-local"
---

838
Chapter 22
Deep Learning
(1994) analyzed the problem of vanishing gradients in recurrent networks. The long short-
term memory (LSTM) architecture (Hochreiter, 1991; Hochreiter and Schmidhuber, 1997;
Gers et al., 2000) was proposed as a way of avoiding this problem. More recently, effective
RNN designs have been derived automatically (Jozefowicz et al., 2015; Zoph and Le, 2016).
Many methods have been tried for improving generalization in neural networks. Weight
decay was suggested by Hinton (1987) and analyzed mathematically by Krogh and Hertz
(1992). The dropout method is due to Srivastava et al. (2014a). Szegedy et al. (2013) intro-
duced the idea of adversarial examples, spawning a huge literature.
Poole et al. (2017) showed that deep networks (but not shallow ones) can disentangle
complex functions into ﬂat manifolds in the space of hidden units. Rolnick and Tegmark
(2018) showed that the number of units required to approximate a certain class of polynomials
of n variables grows exponentially for shallow networks but only linearly for deep networks.
White et al. (2019) showed that their BANANAS system could do neural architecture
search (NAS) by predicting the accuracy of a network to within 1% after training on just
200 random sample architectures. Zoph and Le (2016) use reinforcement learning to search
the space of neural network architectures. Real et al. (2018) use an evolutionary algorithm
to do model selection, Liu et al. (2017) use evolutionary algorithms on hierarchical repre-
sentations, and Jaderberg et al. (2017) describe population-based training. Liu et al. (2019)
relax the space of architectures to a continuous differentiable space and use gradient descent
to ﬁnd a locally optimal solution. Pham et al. (2018) describe the ENAS (Efﬁcient Neural
Architecture Search) system, which searches for optimal subgraphs of a larger graph. It is
fast because it does not need to retrain parameters. The idea of searching for a subgraph goes
back to the “optimal brain damage” algorithm of LeCun et al. (1990).
Despite this impressive array of approaches, there are critics who feel the ﬁeld has not yet
matured. Yu et al. (2019) show that in some cases these NAS algorithms are no more efﬁcient
than random architecture selection. For a survey of recent results in neural architecture search,
see Elsken et al. (2018).
Unsupervised learning constitutes a large subﬁeld within statistics, mostly under the
heading of density estimation. Silverman (1986) and Murphy (2012) are good sources for
classical and modern techniques in this area. Principal components analysis (PCA) dates
back to Pearson (1901); the name comes from independent work by Hotelling (1933). The
probabilistic PCA model (Tipping and Bishop, 1999) adds a generative model for the prin-
cipal components themselves. The variational autoencoder is due to Kingma and Welling
(2013) and Rezende et al. (2014); Jordan et al. (1999) provide an introduction to variational
methods for inference in graphical models.
For autoregressive models, the classic text is by Box et al. (2016). The Yule–Walker equa-
tions for ﬁtting AR models were developed independently by Yule (1927) and Walker (1931).
Autoregressive models with nonlinear dependencies were developed by several authors (Frey,
1998; Bengio and Bengio, 2001; Larochelle and Murray, 2011). The autoregressive WaveNet
model (van den Oord et al., 2016a) was based on earlier work on autoregressive image gen-
eration (van den Oord et al., 2016b). Generative adversarial networks, or GANs, were ﬁrst
proposed by Goodfellow et al. (2015a), and have found many applications in AI. Some the-
oretical understanding of their properties is emerging, leading to improved GAN models and
algorithms (Li and Malik, 2018b, 2018a; Zhu et al., 2019). Part of that understanding involves
protecting against adversarial attacks (Carlini et al., 2019).
