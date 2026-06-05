---
chunk_id: "book-ca4fca8dd8-chunk-0855"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 855
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 517

Bibliographical and Historical Notes
517
described in Chapter 26. Many other algorithms have been proposed to handle more general
ﬁltering problems with static or nearly-static variables, including the resample–move algo-
rithm (Gilks and Berzuini, 2001), the Liu–West algorithm (Liu and West, 2001), the Storvik
ﬁlter (Storvik, 2002), the extended parameter ﬁlter (Erol et al., 2013), and the assumed pa-
rameter ﬁlter (Erol et al., 2017). The latter is a hybrid of particle ﬁltering with a much older
idea called assumed-density ﬁlter. An assumed-density ﬁlter assumes that the posterior dis-
Assumed-density
ﬁlter
tribution over states at time t belongs to a particular ﬁnitely parameterized family; if the pro-
jection and update steps take it outside this family, the distribution is projected back to give
the best approximation within the family. For DBNs, the Boyen–Koller algorithm (Boyen
et al., 1999) and the factored frontier algorithm (Murphy and Weiss, 2001) assume that the
Factored frontier
posterior distribution can be approximated well by a product of small factors.
MCMC methods (see Section 13.4.2) can be applied to the ﬁltering problem; for example,
Gibbs sampling can be applied directly to an unrolled DBN. The particle MCMC family of
Particle MCMC
algorithms (Andrieu et al., 2010; Lindsten et al., 2014) combines MCMC on the unrolled
temporal model with particle ﬁltering to generate the MCMC proposals; although it provably
converges to the correct posterior distribution in the general case (i.e., with both static and
dynamic variables), it is an ofﬂine algorithm. To avoid the problem of increasing update
times as the unrolled network grows, the decayed MCMC ﬁlter (Marthi et al., 2002) prefers
Decayed MCMC
to sample more recent state variables, with a probability that decreases for variables further
in the past.
The book by Doucet et al. (2001) collects many important papers on sequential Monte
Carlo (SMC) algorithms, of which particle ﬁltering is the most important instance. There are
Sequential Monte
Carlo
useful tutorials by Arulampalam et al. (2002) and Doucet and Johansen (2011). There are also
several theoretical results concerning conditions under which SMC methods retain a bounded
error indeﬁnitely compared to the true posterior (Crisan and Doucet, 2002; Del Moral, 2004;
Del Moral et al., 2006).

## Page 518
