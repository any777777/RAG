---
chunk_id: "book-ca4fca8dd8-chunk-0791"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 791
confidence: "first-pass"
extraction_method: "structured-local"
---

476
Chapter 13
Probabilistic Reasoning
Since the mid-1990s, MCMC has become the workhorse of Bayesian statistics and statis-
tical computation in many other disciplines including physics and biology. The Handbook of
Markov Chain Monte Carlo (Brooks et al., 2011) covers many aspects of this literature. The
BUGS package (Gilks et al., 1994) was an early and inﬂuential system for Bayes net model-
ing and inference using Gibbs sampling. STAN (named after Stanislaw Ulam, an originator
of Monte Carlo methods in physics) is a more recent system that uses Hamiltonian Monte
Carlo inference (Carpenter et al., 2017).
There are two very important families of approximation methods that we did not cover
in the chapter. The ﬁrst is the family of variational approximation methods, which can be
used to simplify complex calculations of all kinds. The basic idea is to propose a reduced
version of the original problem that is simple to work with, but that resembles the original
problem as closely as possible. The reduced problem is described by some variational pa-
rameters λ that are adjusted to minimize a distance function D between the original and
the reduced problem, often by solving the system of equations ∂D/∂λ=0. In many cases,
strict upper and lower bounds can be obtained. Variational methods have long been used in
statistics (Rustagi, 1976). In statistical physics, the mean-ﬁeld method is a particular varia-
tional approximation in which the individual variables making up the model are assumed to
be completely independent.
This idea was applied to solve large undirected Markov networks (Peterson and Ander-
son, 1987; Parisi, 1988). Saul et al. (1996) developed the mathematical foundations for
applying variational methods to Bayesian networks and obtained accurate lower-bound ap-
proximations for sigmoid networks with the use of mean-ﬁeld methods. Jaakkola and Jordan
(1996) extended the methodology to obtain both lower and upper bounds. Since these early
papers, variational methods have been applied to many speciﬁc families of models. The re-
markable paper by Wainwright and Jordan (2008) provides a unifying theoretical analysis of
the literature on variational methods.
A second important family of approximation algorithms is based on Pearl’s polytree
message-passing algorithm (1982a). This algorithm can be applied to general “loopy” net-
works, as suggested by Pearl (1988). The results might be incorrect, or the algorithm might
fail to terminate, but in many cases, the values obtained are close to the true values. Little
attention was paid to this so-called loopy belief propagation approach until McEliece et al.
Loopy belief
propagation
(1998) observed that it is exactly the computation performed by the turbo decoding algo-
Turbo decoding
rithm (Berrou et al., 1993), which provided a major breakthrough in the design of efﬁcient
error-correcting codes.
The implication of these observations is if loopy BP is both fast and accurate on the very
large and very highly connected networks used for decoding, it might therefore be useful
more generally. Theoretical support for these ﬁndings, including convergence proofs for
some special cases, was provided by Weiss (2000b), Weiss and Freeman (2001), and Yedidia
et al. (2005), drawing on connections to ideas from statistical physics.
Theories of causal inference going beyond randomized controlled trials were proposed
by Rubin (1974) and Robins (1986), but these ideas remained both obscure and controver-
sial until Judea Pearl developed and presented a fully articulated theory of causality based
on causal networks (Pearl, 2000). Peters et al. (2017) further develop the theory, with an
emphasis on learning. A more recent work, The Book of Why (Pearl and McKenzie, 2018),
provides a less mathematical but more readable and wide-ranging introduction.
