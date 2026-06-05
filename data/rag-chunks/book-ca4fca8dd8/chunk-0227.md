---
chunk_id: "book-ca4fca8dd8-chunk-0227"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 227
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 4.2
Local Search in Continuous Spaces
137
function GENETIC-ALGORITHM(population,ﬁtness) returns an individual
repeat
weights←WEIGHTED-BY(population, ﬁtness)
population2←empty list
for i = 1 to SIZE(population) do
parent1, parent2←WEIGHTED-RANDOM-CHOICES(population,weights,2)
child←REPRODUCE(parent1,parent2)
if (small random probability) then child←MUTATE(child)
add child to population2
population←population2
until some individual is ﬁt enough, or enough time has elapsed
return the best individual in population, according to ﬁtness
function REPRODUCE(parent1,parent2) returns an individual
n←LENGTH(parent1)
c←random number from 1 to n
return APPEND(SUBSTRING(parent1,1,c), SUBSTRING(parent2,c+1, n))
Figure 4.8 A genetic algorithm. Within the function, population is an ordered list of indi-
viduals, weights is a list of corresponding ﬁtness values for each individual, and ﬁtness is a
function to compute these values.
Clearly, this effect is unlikely to be signiﬁcant if adjacent bits are totally unrelated to
each other, because then there will be few contiguous blocks that provide a consistent bene-
ﬁt. Genetic algorithms work best when schemas correspond to meaningful components of a
solution. For example, if the string is a representation of an antenna, then the schemas may
represent components of the antenna, such as reﬂectors and deﬂectors. A good component is
likely to be good in a variety of different designs. This suggests that successful use of genetic
algorithms requires careful engineering of the representation.
In practice, genetic algorithms have their place within the broad landscape of optimiza-
tion methods (Marler and Arora, 2004), particularly for complex structured problems such as
circuit layout or job-shop scheduling, and more recently for evolving the architecture of deep
neural networks (Miikkulainen et al., 2019). It is not clear how much of the appeal of genetic
algorithms arises from their superiority on speciﬁc tasks, and how much from the appealing
metaphor of evolution.
4.2 Local Search in Continuous Spaces
In Chapter 2, we explained the distinction between discrete and continuous environments,
pointing out that most real-world environments are continuous. A continuous action space
has an inﬁnite branching factor, and thus can’t be handled by most of the algorithms we have
covered so far (with the exception of ﬁrst-choice hill climbing and simulated annealing).
This section provides a very brief introduction to some local search techniques for con-
tinuous spaces. The literature on this topic is vast; many of the basic techniques originated
