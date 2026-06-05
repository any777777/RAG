---
chunk_id: "chapter-04-2-cf5ac11fbe-chunk-0005"
source_id: "chapter-04-2-cf5ac11fbe"
source_file: "Chapter 04 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 5
confidence: "first-pass"
extraction_method: "structured-local"
---

24
Evolutionary Algorithms :  Genetic Algorithm
Initial Population: GAs begin with a set of k randomly generated states 
(population) , Each state is represented as a string (of digits)
Fitness Function: Each state is rated by the objective/fitness function
Returns higher values for better states, 
The probability of being chosen for reproducing is directly proportional to the fitness score
Selection: Two pairs are selected at random for reproduction (in 
accordance with the probabilities)
Crossover: For each pair to be mated, a crossover point is chosen 
randomly from the positions in the string
The offspring are created by crossing over the parent strings at the crossover point
Mutation: Each location is subject to random mutation with a small 
independent probability

## Page 25

25
… Evolutionary algorithms

## Page 26

26
… Evolutionary algorithms

## Page 27

27
… Evolutionary algorithms
Genetic algorithms are similar to stochastic beam search, but with the addition of 
the crossover operation.

## Page 28

Offline search – computing a complete solution before acting 
and then execute it.
Online search – interleaving computation and action 
Take an action, observe the environment, then compute the next action
Solving an exploration problem where the states and actions are 
unknown to the agent
Good for domains where there is a penalty for computing too long, or 
for stochastic domains
An example: A robot is placed in a new building and must explore it to 
build a map that it can use for getting from A to B
28

## Page 29

4.5.1 Online search problems
29

## Page 30

• The cost is the total path cost that the agent incurs as it travels. 
• It is common to compare this cost with the path cost the agent would incur if it knew 
the search space in advance—
• that is, the optimal path in the known environment.
• In the language of online algorithms, this comparison is called the competitive ratio; 
Competitive ratio: the true path cost over the path cost if it knew the search 
space in advance.

The best achievable competitive ratio can be 1
we would like it to be as small as possible.
• Online explorers are vulnerable to dead ends: 
• states from which no goal state is reachable.
• Dead ends are a real difficulty for robot exploration—
• some actions are irreversible—there is no way to return to the previous state.
30
… Online search problems

## Page 31

31
… Online search problems

## Page 32
