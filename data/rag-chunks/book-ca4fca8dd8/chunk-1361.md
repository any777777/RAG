---
chunk_id: "book-ca4fca8dd8-chunk-1361"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1361
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.7
Unsupervised Learning and Transfer Learning
829
Autoencoders
Many unsupervised deep learning algorithms are based on the idea of an autoencoder. An
Autoencoder
autoencoder is a model containing two parts: an encoder that maps from x to a representation
ˆz and a decoder that maps from a representation ˆz to observed data x. In general, the encoder
is just a parameterized function f and the decoder is just a parameterized function g. The
model is trained so that x ≈g(f(x)), so that the encoding process is roughly inverted by the
decoding process. The functions f and g can be simple linear models parameterized by a
single matrix or they can be represented by a deep neural network.
A very simple autoencoder is the linear autoencoder, where both f and g are linear with
a shared weight matrix W:
ˆz = f(x) = Wx
x = g(ˆz) = W⊤ˆz.
One way to train this model is to minimize the squared error ∑j ∥xj −g(f(xj))∥2 so that
x ≈g(f(x)). The idea is to train W so that a low-dimensional ˆz will retain as much in-
formation as possible to reconstruct the high-dimensional data x. This linear autoencoder
turns out to be closely connected to classical principal components analysis (PCA). When
z is m-dimensional, the matrix W should learn to span the m principal components of the
data—in other words, the set of m orthogonal directions in which the data has highest vari-
ance, or equivalently the m eigenvectors of the data covariance matrix that have the largest
eigenvalues—exactly as in PCA.
The PCA model is a simple generative model that corresponds to a simple linear autoen-
coder. The correspondence suggests that there may be a way to capture more complex kinds
of generative models using more complex kinds of autoencoders. The variational autoen-
coder (VAE) provides one way to do this.
Variational
autoencoder
Variational methods were introduced brieﬂy on page 476 as a way to approximate the
posterior distribution in complex probability models, where summing or integrating out a
large number of hidden variables is intractable. The idea is to use a variational posterior
Variational posterior
Q(z), drawn from a computationally tractable family of distributions, as an approximation to
the true posterior. For example, we might choose Q from the family of Gaussian distributions
with a diagonal covariance matrix. Within the chosen family of tractable distributions, Q is
optimized to be as close as possible to the true posterior distribution P(z|x).
For our purposes, the notion of “as close as possible” is deﬁned by the KL divergence,
which we mentioned on page 809. This is given by
DKL(Q(z)∥P(z|x)) =
Z
Q(z)log Q(z)
P(z|x)dz,
which is an average (with respect to Q) of the log ratio between Q and P. It is easy to see
that DKL(Q(z)∥P(z|x)) ≥0, with equality when Q and P coincide. We can then deﬁne the
variational lower bound L (sometimes called the evidence lower bound, or ELBO) on the
Variational lower
bound
ELBO
log likelihood of the data:
L(x,Q) = logP(x)−DKL(Q(z)∥P(z|x)).
(22.17)
We can see that L is a lower bound for logP because the KL divergence is nonnegative. Vari-
ational learning maximizes L with respect to parameters w rather than maximizing logP(x),
in the hope that the solution found, w∗, is close to maximizing logP(x) as well.
