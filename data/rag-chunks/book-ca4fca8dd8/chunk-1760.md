---
chunk_id: "book-ca4fca8dd8-chunk-1760"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1760
confidence: "first-pass"
extraction_method: "structured-local"
---

1070
Chapter 29
The Future of AI
Agents also need ways to control their own deliberations. They must be able to use the
available time well, and cease deliberating when action is demanded. For example, a taxi-
driving agent that sees an accident ahead must decide in a split second whether to brake or
swerve. It should also spend that split second thinking about the most important questions,
such as whether the lanes to the left and right are clear and whether there is a large truck close
behind, rather than worrying about where to pick up the next passenger. These issues are
usually studied under the heading of real-time AI. As AI systems move into more complex
Real-time AI
domains, all problems will become real-time, because the agent will never have long enough
to solve the decision problem exactly.
Clearly, there is a pressing need for general methods of controlling deliberation, rather
than speciﬁc recipes for what to think about in each situation. The ﬁrst useful idea is the
anytime algorithms (Dean and Boddy, 1988; Horvitz, 1987): an algorithm whose output
Anytime algorithm
quality improves gradually over time, so that it has a reasonable decision ready whenever it is
interrupted. Examples of anytime algorithms include iterative deepening in game-tree search
and MCMC in Bayesian networks.
The second technique for controlling deliberation is decision-theoretic metareasoning
Decision-theoretic
metareasoning
(Russell and Wefald, 1989; Horvitz and Breese, 1996; Hay et al., 2012). This method, which
was mentioned brieﬂy in Sections 3.6.5 and 6.7, applies the theory of information value
(Chapter 15) to the selection of individual computations (Section 3.6.5). The value of a
computation depends on both its cost (in terms of delaying action) and its beneﬁts (in terms
of improved decision quality).
Metareasoning techniques can be used to design better search algorithms and to guarantee
that the algorithms have the anytime property. Monte Carlo tree search is one example: the
choice of leaf node at which to begin the next playout is made by an approximately rational
metalevel decision derived from bandit theory.
Metareasoning is more expensive than reﬂex action, of course, but compilation methods
can be applied so that the overhead is small compared to the costs of the computations being
controlled. Metalevel reinforcement learning may provide another way to acquire effective
policies for controlling deliberation: in essence, computations that lead to better decisions are
reinforced, while those that turn out to have no effect are penalized. This approach avoids the
myopia problems of the simple value-of-information calculation.
Metareasoning is one speciﬁc example of a reﬂective architecture—that is, an architec-
Reﬂective
architecture
ture that enables deliberation about the computational entities and actions occurring within
the architecture itself. A theoretical foundation for reﬂective architectures can be built by
deﬁning a joint state space composed from the environment state and the computational state
of the agent itself. Decision-making and learning algorithms can be designed that operate
over this joint state space and thereby serve to implement and improve the agent’s compu-
tational activities. Eventually, we expect task-speciﬁc algorithms such as alpha–beta search,
regression planning, and variable elimination to disappear from AI systems, to be replaced
by general methods that direct the agent’s computations toward the efﬁcient generation of
high-quality decisions.
Metareasoning and reﬂection (and many other efﬁciency-related architectural and algo-
rithmic devices explored in this book) are necessary because making decisions is hard. Ever
since computers were invented, their blinding speed has led people to overestimate their abil-
ity to overcome complexity, or, equivalently, to underestimate what complexity really means.
