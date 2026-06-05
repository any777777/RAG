---
chunk_id: "book-ca4fca8dd8-chunk-0223"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 223
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 4.1
Local Search and Optimization Problems
135
+
=
Figure 4.7 The 8-queens states corresponding to the ﬁrst two parents in Figure 4.6(c) and
the ﬁrst offspring in Figure 4.6(d). The green columns are lost in the crossover step and the
red columns are retained. (To interpret the numbers in Figure 4.6: row 1 is the bottom row,
and 8 is the top row.)
problem we use the number of nonattacking pairs of queens, which has a value of 8×7/2 =
28 for a solution. The values of the four states in (b) are 24, 23, 20, and 11. The ﬁtness scores
are then normalized to probabilities, and the resulting values are shown next to the ﬁtness
values in (b).
In (c), two pairs of parents are selected, in accordance with the probabilities in (b). Notice
that one individual is selected twice and one not at all. For each selected pair, a crossover
point (dotted line) is chosen randomly. In (d), we cross over the parent strings at the crossover
points, yielding new offspring. For example, the ﬁrst child of the ﬁrst pair gets the ﬁrst three
digits (327) from the ﬁrst parent and the remaining digits (48552) from the second parent.
The 8-queens states involved in this recombination step are shown in Figure 4.7.
Finally, in (e), each location in each string is subject to random mutation with a small
independent probability. One digit was mutated in the ﬁrst, third, and fourth offspring. In the
8-queens problem, this corresponds to choosing a queen at random and moving it to a random
square in its column. It is often the case that the population is diverse early on in the process,
so crossover frequently takes large steps in the state space early in the search process (as in
simulated annealing). After many generations of selection towards higher ﬁtness, the popu-
lation becomes less diverse, and smaller steps are typical. Figure 4.8 describes an algorithm
that implements all these steps.
Genetic algorithms are similar to stochastic beam search, but with the addition of the
crossover operation. This is advantageous if there are blocks that perform useful functions.
For example, it could be that putting the ﬁrst three queens in positions 2, 4, and 6 (where they
do not attack each other) constitutes a useful block that can be combined with other useful
blocks that appear in other individuals to construct a solution. It can be shown mathematically
that, if the blocks do not serve a purpose—for example if the positions of the genetic code
are randomly permuted—then crossover conveys no advantage.
The theory of genetic algorithms explains how this works using the idea of a schema,
Schema
which is a substring in which some of the positions can be left unspeciﬁed. For example,
the schema 246***** describes all 8-queens states in which the ﬁrst three queens are in
positions 2, 4, and 6, respectively. Strings that match the schema (such as 24613578) are
called instances of the schema. It can be shown that if the average ﬁtness of the instances of
Instance
a schema is above the mean, then the number of instances of the schema will grow over time.
