---
chunk_id: "book-ca4fca8dd8-chunk-0437"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 437
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
267
dently by Selman et al. (1992), who called it GSAT and showed that it was capable of solving
a wide range of very hard problems very quickly. The WALKSAT algorithm described in this
chapter is due to Selman et al. (1996).
The “phase transition” in satisﬁability of random k-SAT problems was ﬁrst observed by
Simon and Dubois (1989) and has given rise to a great deal of theoretical and empirical
research—due, in part, to the connection to phase transition phenomena in statistical physics.
Crawford and Auton (1993) located the 3-SAT transition at a clause/variable ratio of around
4.26, noting that this coincides with a sharp peak in the run time of their SAT solver. Cook
and Mitchell (1997) provide an excellent summary of the early literature on the problem.
Algorithms such as survey propagation (Parisi and Zecchina, 2002; Maneva et al., 2007)
Survey propagation
take advantage of special properties of random SAT instances near the satisﬁability threshold
and greatly outperform general SAT solvers on such instances. The current state of theoretical
understanding is summarized by Achlioptas (2009).
Good sources for information on satisﬁability, both theoretical and practical, include the
Handbook of Satisﬁability (Biere et al., 2009), Donald Knuth’s (2015) fascicle on satisﬁa-
bility, and the regular International Conferences on Theory and Applications of Satisﬁability
Testing, known as SAT.
The idea of building agents with propositional logic can be traced back to the seminal pa-
per of McCulloch and Pitts (1943), which is well known for initiating the ﬁeld of neural net-
works, but actually was concerned with the implementation of a Boolean circuit-based agent
design in the brain. Stan Rosenschein (Rosenschein, 1985; Kaelbling and Rosenschein, 1990)
developed ways to compile circuit-based agents from declarative descriptions of the task en-
vironment. Rod Brooks (1986, 1989) demonstrates the effectiveness of circuit-based designs
for controlling robots (see Chapter 26). Brooks (1991) argues that circuit-based designs are
all that is needed for AI—that representation and reasoning are cumbersome, expensive, and
unnecessary. In our view, both reasoning and circuits are necessary. Williams et al. (2003)
describe a hybrid agent—not too different from our wumpus agent—that controls NASA
spacecraft, planning sequences of actions and diagnosing and recovering from faults.
The general problem of keeping track of a partially observable environment was intro-
duced for state-based representations in Chapter 4. Its instantiation for propositional repre-
sentations was studied by Amir and Russell (2003), who identiﬁed several classes of envi-
ronments that admit efﬁcient state-estimation algorithms and showed that for several other
classes the problem is intractable. The temporal-projection problem, which involves deter-
Temporal-projection
mining what propositions hold true after an action sequence is executed, can be seen as a
special case of state estimation with empty percepts. Many authors have studied this problem
because of its importance in planning; some important hardness results were established by
Liberatore (1997). The idea of representing a belief state with propositions can be traced to
Wittgenstein (1922).
The approach to logical state estimation using temporal indexes on propositional vari-
ables was proposed by Kautz and Selman (1992). Later generations of SATPLAN were able
to take advantage of the advances in SAT solvers and remain among the most effective ways
of solving difﬁcult planning problems (Kautz, 2006).
The frame problem was ﬁrst recognized by McCarthy and Hayes (1969). Many re-
searchers considered the problem unsolvable within ﬁrst-order logic, and it spurred a great
deal of research into nonmonotonic logics. Philosophers from Dreyfus (1972) to Crockett
