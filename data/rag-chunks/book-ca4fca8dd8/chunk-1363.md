---
chunk_id: "book-ca4fca8dd8-chunk-1363"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1363
confidence: "first-pass"
extraction_method: "structured-local"
---

830
Chapter 22
Deep Learning
As written, L does not yet seem to be any easier to maximize than logP. Fortunately, we
can rewrite Equation (22.17) to reveal improved computational tractability:
L = logP(x)−
Z
Q(z)log Q(z)
P(z|x)dz
= −
Z
Q(z)logQ(z)dz+
Z
Q(z)logP(x)P(z|x)dz
= H(Q)+Ez∼Q logP(z,x)
where H(Q) is the entropy of the Q distribution. For some variational families Q (such
as Gaussian distributions), H(Q) can be evaluated analytically. Moreover, the expectation,
Ez∼Q logP(z,x), admits an efﬁcient unbiased estimate via samples of z from Q. For each
sample, P(z,x) can usually be evaluated efﬁciently—for example, if P is a Bayes net, P(z,x)
is just a product of conditional probabilities because z and x comprise all the variables.
Variational autoencoders provide a means of performing variational learning in the deep
learning setting. Variational learning involves maximizing L with respect to the parameters
of both P and Q. For a variational autoencoder, the decoder g(z) is interpreted as deﬁning
logP(x|z). For example, the output of the decoder might deﬁne the mean of a conditional
Gaussian. Similarly, the output of the encoder f(x) is interpreted as deﬁning the parameters of
Q—for example, Q might be a Gaussian with mean f(x). Training the variational autoencoder
then consists of maximizing L with respect to the parameters of both the encoder f and the
decoder g, which can themselves be arbitrarily complicated deep networks.
Deep autoregressive models
An autoregressive model (or AR model) is one in which each element xi of the data vector x
Autoregressive
model
is predicted based on other elements of the vector. Such a model has no latent variables. If x
is of ﬁxed size, an AR model can be thought of as a fully observable and possibly fully con-
nected Bayes net. This means that calculating the likelihood of a given data vector according
to an AR model is trivial; the same holds for predicting the value of a single missing variable
given all the others, and for sampling a data vector from the model.
The most common application of autoregressive models is in the analysis of time series
data, where an AR model of order k predicts xt given xt−k,...,xt−1. In the terminology of
Chapter 14, an AR model is a non-hidden Markov model. In the terminology of Chapter 24,
an n-gram model of letter or word sequences is an AR model of order n−1.
In classical AR models, where the variables are real-valued, the conditional distribution
P(xt |xt−k,...,xt−1) is a linear–Gaussian model with ﬁxed variance whose mean is a weighted
linear combination of xt−k,...,xt−1—in other words, a standard linear regression model. The
maximum likelihood solution is given by the Yule–Walker equations, which are closely
Yule–Walker
equations
related to the normal equations on page 698.
A deep autoregressive model is one in which the linear–Gaussian model is replaced
Deep autoregressive
model
by an arbitrary deep network with a suitable output layer depending on whether xt is dis-
crete or continuous. Recent applications of this autoregressive approach include DeepMind’s
WaveNet model for speech generation (van den Oord et al., 2016a). WaveNet is trained
on raw acoustic signals, sampled 16,000 times per second, and implements a nonlinear AR
model of order 4800 with a multilayer convolutional structure. In tests it proves to be sub-
stantially more realistic than previous state-of-the-art speech generation systems.
