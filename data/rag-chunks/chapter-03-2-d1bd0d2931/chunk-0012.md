---
chunk_id: "chapter-03-2-d1bd0d2931-chunk-0012"
source_id: "chapter-03-2-d1bd0d2931"
source_file: "Chapter 03 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 12
confidence: "first-pass"
extraction_method: "structured-local"
---

3.5.5 Memory-bounded search
• Memory is split between the frontier and the reached states.
• We can keep reference counts of the number of times a state has 
been reached and remove it from the reached table when there are 
no more ways to reach the state
• e.g., grid world
• Beam search limits the size of the frontier by keeping only the k
nodes with the best f -scores, discarding any other expanded nodes.
• An alternative version of beam search keeps every node whose f -score is 
within δ of the best f -score.
• In Iterative-deepening A∗search (IDA∗), the cutoff is the f -cost 
(g+h); 
• at each iteration, the cutoff value is the smallest f -cost of any node that 
exceeded the cutoff on the previous iteration.
90

## Page 87

91

## Page 88

Heuristic Functions
What is a good heuristic?
Effective branching factor b*
N+1 = 1+ b* + (b*)2 + … + (b*)d
N: Number of generated nodes
d: Solution depth
Close to 1. Why?
Allowing fairly large problems to be solved at reasonable
computational cost
Value of h
not too large - must be admissible
not too small – ineffective (expanding all nodes with f (n) < f* )

## Page 89

… Heuristic Functions
• For the 15-puzzle, there are 16!/2 states—over 10 trillion—so to 
search that space we will need the help of a good admissible 
heuristic function. 
• Here are two commonly used candidates:
• h1 = the number of misplaced tiles (blank not included). 
• For Figure 3.25, all eight tiles are out of position, so the start state has h1 = 8. 
• h1 is an admissible heuristic because any tile that is out of place will require at 
least one move to get it to the right place.
93

## Page 90

• … Here are two commonly used candidates:
• h2 = the sum of the distances of the tiles from their goal positions. 
• Because tiles cannot move along diagonals, the distance is the sum of 
the horizontal and vertical distances—sometimes called the city-block 
distance or Manhattan distance. 
• h2 is also admissible because all any move can do is move one tile one 
step closer to the goal. 
• Tiles 1 to 8 in the start state of Figure 3.25 give a Manhattan distance 
of h2 = 3+1+2+2+2+3+3+2= 18.
• As expected, neither of these overestimates the true solution 
cost, which is 26.
94
… Heuristic Functions

## Page 91
