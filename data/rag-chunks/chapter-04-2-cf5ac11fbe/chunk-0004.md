---
chunk_id: "chapter-04-2-cf5ac11fbe-chunk-0004"
source_id: "chapter-04-2-cf5ac11fbe"
source_file: "Chapter 04 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 4
confidence: "first-pass"
extraction_method: "structured-local"
---

Simulated annealing
Algorithm:
Instead of picking the best move, it picks a random move
If the move improves the situation, it is always accepted
Otherwise, the algorithm accepts the move with some
probability less than 1
The probability decreases exponentially with the “badness” of
the move ∆E
The probability also decreases as the “temperature” T goes
down
“bad” moves are more likely to be allowed at the start when T
is high, and they become more unlikely as T decreases
schedule should lower T slowly

## Page 20

• Simulated annealing was used to solve VLSI layout problems 
beginning in the 1980s. 
• It has been applied widely to factory scheduling and other large-
scale optimization tasks.
20
… Simulated annealing
Allow “bad” moves occasionally, depending on “temperature”
High temperature => more bad moves allowed, shake the system out 
of its local minimum
Gradually reduce temperature according to some schedule

## Page 21

4.1.3 Local beam search
Keeping track of k states instead of just one 
Algorithm:
It begins with k randomly generated states
At each step, all the successors of all k states are generated
If anyone is a goal, the algorithm halts
Otherwise, it selects the k best successors from the complete list and repeats
Similar to have k random-restart of Hill-climbing search?
In a random-restart hill-climbing search, each search process runs independently of the 
others
In a local beam search, useful information is passed among the parallel search threads
The algorithm quickly abandons unfruitful searches and moves its resources to where the most progress is being 
made
• Stochastic beam search chooses successors with probability 
proportional to the successor’s value, thus increasing diversity.
21

## Page 22

Beam search example (K=4)
8
6
7
8
9
7
7
7
6
8
9
9
8
7
9
3
5
10
10
9
X
X
X
X
9
8
9
9
10
9
9
10
X
X
X
X
22

## Page 23

• Evolutionary algorithms can be seen as variants of 
stochastic beam search that are explicitly motivated by the 
natural selection in biology: 
• there is a population of individuals (states), 
• in which the fittest (highest value) individuals produce offspring 
(successor states) 
• that populate the next generation, 
• a process called recombination ( cross-over) 
23
4.1.4 Evolutionary algorithms

## Page 24
