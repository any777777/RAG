---
chunk_id: "chapter-03-2-d1bd0d2931-chunk-0008"
source_id: "chapter-03-2-d1bd0d2931"
source_file: "Chapter 03 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 8
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 55

Iterative deepening search
Find the best l by gradually increasing it until a goal is found
This will occur when l reaches d
Combines the benefits of DFS and BFS
Space complexity is O(bm) – like DFS
It is complete – like BFS
Comparing it with BFS, which one is faster?
Time Complexity: O(bd)
In general, iterative deepening is the preferred uninformed search method when
the search space is large and the depth of the solution is not known.
…
b
Idea: get DFS’s space advantage with BFS’s time / shallow-solution 
advantages
Run a DFS with depth limit 1.  If no solution…
Run a DFS with depth limit 2.  If no solution…
Run a DFS with depth limit 3.  …..
57

## Page 56

58
Complete?? Yes
Time?? db1 + (d −1)b2 + . . . + bd = O(bd)
Space?? O(bd)
Optimal?? Yes, if step cost = 1
Can be modified to explore uniform-cost tree
Numerical comparison for b = 10 and d = 5, solution at far right leaf:
N (IDS) = 50 + 400 + 3, 000 + 20,000 + 100,000 = 123,450
N (BFS) = 10 + 100 + 1, 000 + 10,000 + 100,000 + 999,990 = 1, 111, 100
IDS does better because other nodes at depth d are not expanded
Properties of iterative deepening search

## Page 57

Video of Demo Contours UCS Pacman Small Maze
59

## Page 58

Video of Demo Empty UCS
60

## Page 59

Video of Demo Maze with Deep/Shallow Water --- DFS, BFS, or UCS? 
(part 1)
61

## Page 60

Video of Demo Maze with Deep/Shallow Water --- DFS, BFS, or UCS? (part 2)
62

## Page 61

Video of Demo Maze with Deep/Shallow Water --- DFS, BFS, or UCS? (part 3)
63

## Page 62

3.4.5 Bidirectional search
64

## Page 63

Bidirectional search
Run two simultaneous searches – one forward from the initial state and
the other backward from the goal
hoping that the two searches meet in the middle
What’s the saving?
bd/2 + bd/2 is much less than bd
Time and Space Complexity: O(bd/2)
How to implement it
replacing the goal test with a check to see whether the
frontiers of the two searches intersect
✅Advantages
⚠️Limitations
Faster than BFS/DFS
Needs reverse goal search
Efficient for large depths
Effective for unique goals
Hard if goal unknown

## Page 64

3.4.6 Comparing uninformed search 
algorithms
66

## Page 65
