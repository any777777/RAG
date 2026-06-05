---
chunk_id: "chapter5-reduced-ac4ee82777-chunk-0002"
source_id: "chapter5-reduced-ac4ee82777"
source_file: "Chapter5_reduced.pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

MAX
A
B
C
D
3
12
8
2
4
6
14
5
2
The minimax value at a min node is the minimum
of backed-up values, because your opponent will
do what’s best for them (and worst for you).
3
2
2
3
a1
a2
a3
b1
b2
b3
c1
c2
c3
d1
d2
d3
MIN
Two-ply game tree: minimax tree
9

## Page 10

MAX
A
B
C
D
3
12
8
2
4
6
14
5
2
3
2
2
3
a1
a2
a3
b1
b2
b3
c1
c2
c3
d1
d2
d3
MIN
The minimax decision
Minimax maximizes the worst-case outcome for max.
Two-ply game tree: minimax tree
10

## Page 11

Minimax: Example
11

## Page 12

Minimax: Example
12

## Page 13

The minimax search algorithm
13
function M INIMAX-DECISION(state) returns an action
inputs: state, current state in game
return the a in ACTIONS(state) maximizing MIN-VALUE(RESULT(a, state))
function M AX-VALUE(state) returns a utility value
if T E R M I N A L- TEST(state) then return UTILITY(state)
v ←−∞
for a, s in SUCCESSORS(state) do v ←MAX(v, MIN-VALUE(s))
return v
function MIN-VALUE(state) returns a utility value
if T E R M I N A L- TEST(state) then return UTILITY(state)
v ←∞
for a, s in SUCCESSORS(state) do v ←MIN(v, M AX-VALUE(s))
return v

## Page 14

Properties of minimax
Complete?? Yes, if tree is finite (chess has specific rules for this)
Optimal?? Yes, against an optimal opponent. Otherwise?? 
Time complexity?? O(bm)
Space complexity?? O(bm) (depth-first exploration) For chess, b ≈35, m
≈100 for “reasonable” games
⇒exact solution completely infeasible
But do we need to explore every path?
14

## Page 15

minimax search drawback
Number of game states is exponential in the number of moves.
Solution: Do not examine every node
Alpha-beta pruning
Remove branches that do not influence final decision
General idea: you can bracket the highest/lowest value at a node, even
before all its successors have been evaluated
15

## Page 16

Alpha-Beta Pruning
minimax(root) = max(min(3,12,8), min(2,x,y), min(14,5,2))
= max(3, min(2,x,y), 2)
= max(3,z,2)
where z = min(2,x,y)
= 3
MAX
A
B
C
D
3
12
8
2
4
6
x
y
14
5
2
3
2
2
3
a1
a2
a3
b1
b2
b3
c1
c2
c3
d1
d2
d3
MIN
16

## Page 17

Alpha-Beta Pruning: Ex
17
Prune when 
Alpha>Beta

## Page 18

18
Alpha-Beta Pruning:Ex

## Page 19

Alpha-Beta Pruning: Ex
19

## Page 20

Alpha-Beta Pruning: Ex
20

## Page 21

[-∞, +∞]
Range of possible values
[-∞,+∞]
Alpha-Beta Example
21

## Page 22

[-∞,3]
[-∞,+∞]
Alpha-Beta Example (continued)
22

## Page 23

Alpha-Beta Example (continued)
[-∞,3]
[-∞,+∞]
23

## Page 24

[3,+∞]
[3,3]
Alpha-Beta Example (continued)
24

## Page 25

[-∞,2]
[3,3]
[3,+∞]
This node is worse 
for MAX
Alpha-Beta Example (continued)
25

## Page 26
