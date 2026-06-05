---
chunk_id: "book-ca4fca8dd8-chunk-0221"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 221
confidence: "first-pass"
extraction_method: "structured-local"
---

134
Chapter 4
Search in Complex Environments
(a)
Initial Population
(b)
Fitness Function
(c)
Selection
(d)
Crossover
(e)
Mutation
24
23
20
11
29%
31%
26%
14%
32752411
24748552
32752411
24415124
32748552
24752411
32752124
24415411
24748552
32752411
24415124
32543213
32252124
24752411
32748152
24415417
Figure 4.6 A genetic algorithm, illustrated for digit strings representing 8-queens states. The
initial population in (a) is ranked by a ﬁtness function in (b) resulting in pairs for mating in
(c). They produce offspring in (d), which are subject to mutation in (e).
• The size of the population.
• The representation of each individual. In genetic algorithms, each individual is a string
Genetic algorithm
over a ﬁnite alphabet (often a Boolean string), just as DNA is a string over the alphabet
ACGT. In evolution strategies, an individual is a sequence of real numbers, and in
Evolution strategies
genetic programming an individual is a computer program.
Genetic
programming
• The mixing number, ρ, which is the number of parents that come together to form
offspring. The most common case is ρ = 2: two parents combine their “genes” (parts
of their representation) to form offspring. When ρ = 1 we have stochastic beam search
(which can be seen as asexual reproduction). It is possible to have ρ > 2, which occurs
only rarely in nature but is easy enough to simulate on computers.
• The selection process for selecting the individuals who will become the parents of the
Selection
next generation: one possibility is to select from all individuals with probability pro-
portional to their ﬁtness score. Another possibility is to randomly select n individuals
(n > ρ), and then select the ρ most ﬁt ones as parents.
• The recombination procedure. One common approach (assuming ρ = 2), is to randomly
select a crossover point to split each of the parent strings, and recombine the parts to
Crossover point
form two children, one with the ﬁrst part of parent 1 and the second part of parent 2;
the other with the second part of parent 1 and the ﬁrst part of parent 2.
• The mutation rate, which determines how often offspring have random mutations to
Mutation rate
their representation. Once an offspring has been generated, every bit in its composition
is ﬂipped with probability equal to the mutation rate.
• The makeup of the next generation. This can be just the newly formed offspring, or it
can include a few top-scoring parents from the previous generation (a practice called
elitism, which guarantees that overall ﬁtness will never decrease over time). The prac-
Elitism
tice of culling, in which all individuals below a given threshold are discarded, can lead
to a speedup (Baum et al., 1995).
Figure 4.6(a) shows a population of four 8-digit strings, each representing a state of the 8-
queens puzzle: the c-th digit represents the row number of the queen in column c. In (b),
each state is rated by the ﬁtness function. Higher ﬁtness values are better, so for the 8-queens
