---
chunk_id: "book-ca4fca8dd8-chunk-0789"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 789
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
475
for CSPs in Chapter 5.) For exact inference in large models, where the space requirements
of clustering and variable elimination become enormous, these recursive algorithms are often
the most practical approach.
There are other important inference tasks in Bayes nets besides computing marginal prob-
abilities. The most probable explanation or MPE is the most likely assignment to the
Most probable
explanation
nonevidence variables given the evidence. (MPE is a special case of MAP—maximum a
posteriori—inference, which asks for the most likely assignment to a subset of nonevidence
variables given the evidence.) For such problems, many different algorithms have been de-
veloped, some related to shortest-path or AND–OR search algorithms; for a summary, see
Marinescu and Dechter (2009).
The ﬁrst result on the complexity of inference in Bayes nets is due to Cooper (1990),
who showed that the general problem of computing marginals in Bayesian networks is NP-
hard; as noted in the chapter, this can be strengthened to #P-hardness through a reduction
from counting satisfying assignments (Roth, 1996). This also implies the NP-hardness of
approximate inference (Dagum and Luby, 1993); however, for the case where probabilities
can be bounded away from 0 and 1, a form of likelihood weighting converges in (random-
ized) polynomial time (Dagum and Luby, 1997). Shimony (1994) showed that ﬁnding the
most probable explanation is NP-complete—intractable, but somewhat easier than comput-
ing marginals—while Park and Darwiche (2004) provide a thorough complexity analysis of
MAP computation, showing that it falls into the class of NPPP-complete problems—that is,
somewhat harder than computing marginals.
The development of fast approximation algorithms for Bayesian network inference is a
very active area, with contributions from statistics, computer science, and physics. The rejec-
tion sampling method is a general technique dating back at least to Buffon’s needle (1777);
it was ﬁrst applied to Bayesian networks by Max Henrion (1988), who called it logic sam-
pling. Importance sampling was invented originally for applications in physics (Kahn, 1950a,
1950b) and applied to Bayes net inference by Fung and Chang (1989) (who called the algo-
rithm “evidence weighting”) and by Shachter and Peot (1989).
In statistics, adaptive sampling has been applied to all sorts of Monte Carlo algorithms
to speed up convergence. The basic idea is to adapt the distribution from which samples are
generated, based on the outcome from previous samples. Gilks and Wild (1992) developed
adaptive rejection sampling, while adaptive importance sampling appears to have originated
independently in physics (Lepage, 1978), civil engineering (Karamchandani et al., 1989),
statistics (Oh and Berger, 1992), and computer graphics (Veach and Guibas, 1995). Cheng
and Druzdzel (2000) describe an adaptive version of importance sampling applied to Bayes
net inference. More recently, Le et al. (2017) have demonstrated the use of deep learning
systems to produce proposal distributions that speed up importance sampling by many orders
of magnitude.
Markov chain Monte Carlo (MCMC) algorithms began with the Metropolis algorithm,
due to Metropolis et al. (1953), which was also the source of the simulated annealing algo-
rithm described in Chapter 4. Hastings (1970) introduced the accept/reject step that is an
integral part of what we now call the Metropolis–Hastings algorithm. The Gibbs sampler was
devised by Geman and Geman (1984) for inference in undirected Markov networks. The ap-
plication of Gibbs sampling to Bayesian networks is due to Pearl (1987). The papers collected
by Gilks et al. (1996) cover both theory and applications of MCMC.
