---
chunk_id: "chapter-04-2-778b49407b-chunk-0003"
source_id: "chapter-04-2-778b49407b"
source_file: "New folder/Chapter 04 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

Stochastic Hill climbing chooses at random from among the uphill moves; the probability of selection can vary with the steepness of the uphill move. 
Not complete, gets stuck in local optima
First-choice Hill climbing implements stochastic hill climbing by generating successors randomly until one is generated that is better than the current state.
 Not complete
Random-Restart Hill climbing conducts a series of hill-climbing searches from randomly generated initial states until a goal is found. 
Complete in practice ( increase success probability) .

15

Hill Climbing Search

## Slide 16

Hill-climbing on the 8-queens problem

No sideways moves:
Succeeds w/ prob. 0.14
Average number of moves per trial:
4 when succeeding, 3 when getting stuck
Expected total number of moves needed:
3(1-p)/p + 4 =~ 22 moves
Allowing 100 sideways moves:
Succeeds w/ prob. 0.94
Average number of moves per trial:
21 when succeeding, 65 when getting stuck
Expected total number of moves needed:
65(1-p)/p + 21 =~ 25 moves

16

## Slide 17

4.1.2 Simulated annealing

A hill-climbing algorithm that never makes “downhill” moves toward states with lower value (or higher cost) is always vulnerable to getting stuck in a local maximum. 
In contrast, a purely random walk that moves to a successor state without concern for the value will eventually stumble upon the global maximum, but will be extremely inefficient. 
Simulated annealing combines hill climbing with a random walk in a way that yields both efficiency and completeness.
In metallurgy, annealing is the process used to temper or harden metals and glass by heating them to a high temperature and then gradually cooling them, thus allowing the material to reach a low-energy crystalline state.

17

## Slide 18

18

… Simulated annealing

## Slide 19

Simulated annealing

Algorithm:
Instead of picking the best move, it picks a random move
If the move improves the situation, it is always accepted
Otherwise, the algorithm accepts the move with some probability less than 1
The probability decreases exponentially with the “badness” of the move ∆E
The probability also decreases as the “temperature” T goes down
“bad” moves are more likely to be allowed at the start when T is high, and they become more unlikely as T decreases
schedule should lower T slowly

19

## Slide 20

Simulated annealing was used to solve VLSI layout problems beginning in the 1980s. 
It has been applied widely to factory scheduling and other large-scale optimization tasks.

20

… Simulated annealing
