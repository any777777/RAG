---
chunk_id: "chapter-04-2-778b49407b-chunk-0004"
source_id: "chapter-04-2-778b49407b"
source_file: "New folder/Chapter 04 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

Allow “bad” moves occasionally, depending on “temperature”
High temperature => more bad moves allowed, shake the system out of its local minimum
Gradually reduce temperature according to some schedule

## Slide 21

4.1.3 Local beam search

Keeping track of k states instead of just one 
Algorithm:
It begins with k randomly generated states
At each step, all the successors of all k states are generated
If anyone is a goal, the algorithm halts
Otherwise, it selects the k best successors from the complete list and repeats

Similar to have k random-restart of Hill-climbing search?
In a random-restart hill-climbing search, each search process runs independently of the others
In a local beam search, useful information is passed among the parallel search threads
The algorithm quickly abandons unfruitful searches and moves its resources to where the most progress is being made
Stochastic beam search chooses successors with probability proportional to the successor’s value, thus increasing diversity.

21

## Slide 22

Beam search example (K=4)

8

6

7

8

22

## Slide 23

Evolutionary algorithms can be seen as variants of stochastic beam search that are explicitly motivated by the natural selection in biology: 
there is a population of individuals (states), 
in which the fittest (highest value) individuals produce offspring (successor states) 
that populate the next generation, 
a process called recombination ( cross-over)

23

4.1.4 Evolutionary algorithms

## Slide 24

24

Evolutionary Algorithms :  Genetic Algorithm

Initial Population: GAs begin with a set of k randomly generated states (population) , Each state is represented as a string (of digits)

Fitness Function: Each state is rated by the objective/fitness function
Returns higher values for better states, 
The probability of being chosen for reproducing is directly proportional to the fitness score
Selection: Two pairs are selected at random for reproduction (in accordance with the probabilities)

Crossover: For each pair to be mated, a crossover point is chosen randomly from the positions in the string
The offspring are created by crossing over the parent strings at the crossover point

Mutation: Each location is subject to random mutation with a small independent probability

## Slide 25

25

… Evolutionary algorithms

## Slide 26

26

… Evolutionary algorithms

## Slide 27

27

… Evolutionary algorithms

Genetic algorithms are similar to stochastic beam search, but with the addition of the crossover operation.

## Slide 28
