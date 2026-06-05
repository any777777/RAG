---
chunk_id: "book-ca4fca8dd8-chunk-0060"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 60
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 1.3
The History of Artiﬁcial Intelligence
39
could collectively represent an individual concept, with a corresponding increase in robust-
ness and parallelism. Hebb’s learning methods were enhanced by Bernie Widrow (Widrow
and Hoff, 1960; Widrow, 1962), who called his networks adalines, and by Frank Rosen-
blatt (1962) with his perceptrons. The perceptron convergence theorem (Block et al.,
1962) says that the learning algorithm can adjust the connection strengths of a perceptron to
match any input data, provided such a match exists.
1.3.3 A dose of reality (1966–1973)
From the beginning, AI researchers were not shy about making predictions of their coming
successes. The following statement by Herbert Simon in 1957 is often quoted:
It is not my aim to surprise or shock you—but the simplest way I can summarize is to say
that there are now in the world machines that think, that learn and that create. Moreover,
their ability to do these things is going to increase rapidly until—in a visible future—the
range of problems they can handle will be coextensive with the range to which the human
mind has been applied.
The term “visible future” is vague, but Simon also made more concrete predictions: that
within 10 years a computer would be chess champion and a signiﬁcant mathematical theorem
would be proved by machine. These predictions came true (or approximately true) within 40
years rather than 10. Simon’s overconﬁdence was due to the promising performance of early
AI systems on simple examples. In almost all cases, however, these early systems failed on
more difﬁcult problems.
There were two main reasons for this failure. The ﬁrst was that many early AI systems
were based primarily on “informed introspection” as to how humans perform a task, rather
than on a careful analysis of the task, what it means to be a solution, and what an algorithm
would need to do to reliably produce such solutions.
The second reason for failure was a lack of appreciation of the intractability of many of
the problems that AI was attempting to solve. Most of the early problem-solving systems
worked by trying out different combinations of steps until the solution was found. This strat-
egy worked initially because microworlds contained very few objects and hence very few
possible actions and very short solution sequences. Before the theory of computational com-
plexity was developed, it was widely thought that “scaling up” to larger problems was simply
a matter of faster hardware and larger memories. The optimism that accompanied the devel-
opment of resolution theorem proving, for example, was soon dampened when researchers
failed to prove theorems involving more than a few dozen facts. The fact that a program can ◀
ﬁnd a solution in principle does not mean that the program contains any of the mechanisms
needed to ﬁnd it in practice.
The illusion of unlimited computational power was not conﬁned to problem-solving pro-
grams. Early experiments in machine evolution (now called genetic programming) (Fried-
Machine evolution
berg, 1958; Friedberg et al., 1959) were based on the undoubtedly correct belief that by
making an appropriate series of small mutations to a machine-code program, one can gen-
erate a program with good performance for any particular task. The idea, then, was to try
random mutations with a selection process to preserve mutations that seemed useful. Despite
thousands of hours of CPU time, almost no progress was demonstrated.
Failure to come to grips with the “combinatorial explosion” was one of the main criti-
cisms of AI contained in the Lighthill report (Lighthill, 1973), which formed the basis for the
