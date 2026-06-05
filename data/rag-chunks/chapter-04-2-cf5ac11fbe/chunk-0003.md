---
chunk_id: "chapter-04-2-cf5ac11fbe-chunk-0003"
source_id: "chapter-04-2-cf5ac11fbe"
source_file: "Chapter 04 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

• Many variants (improvements) of hill climbing have been invented :
• Stochastic hill climbing
• First-choice hill climbing
• Random-restart hill climbing
14
… Hill-climbing search

## Page 15

Stochastic Hill climbing chooses at random from among the uphill moves; the 
probability of selection can vary with the steepness of the uphill move.
Not complete, gets stuck in local optima
First-choice Hill climbing implements stochastic hill climbing by generating 
successors randomly until one is generated that is better than the current state.
Not complete
Random-Restart Hill climbing conducts a series of hill-climbing searches 
from randomly generated initial states until a goal is found.
Complete in practice ( increase success probability) .
15
Hill Climbing Search

## Page 16

Hill-climbing on the 8-queens problem
No sideways moves:
Succeeds w/ prob. 0.14
Average number of moves per trial:
4 when succeeding, 3 when getting stuck
Expected total number of moves needed:
3(1-p)/p + 4 =~ 22 moves
Allowing 100 sideways moves:
Succeeds w/ prob. 0.94
Average number of moves per trial:
21 when succeeding, 65 when getting stuck
Expected total number of moves needed:
65(1-p)/p + 21 =~ 25 moves
16

## Page 17

4.1.2 Simulated annealing
• A hill-climbing algorithm that never makes “downhill” moves toward states 
with lower value (or higher cost) is always vulnerable to getting stuck in a 
local maximum. 
• In contrast, a purely random walk that moves to a successor state without 
concern for the value will eventually stumble upon the global maximum, 
but will be extremely inefficient. 
• Simulated annealing combines hill climbing with a random walk in a 
way that yields both efficiency and completeness.
• In metallurgy, annealing is the process used to temper or harden metals 
and glass by heating them to a high temperature and then gradually 
cooling them, thus allowing the material to reach a low-energy crystalline 
state.
17

## Page 18

18
… Simulated annealing

## Page 19
