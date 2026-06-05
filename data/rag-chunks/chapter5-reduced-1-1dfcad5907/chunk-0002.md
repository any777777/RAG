---
chunk_id: "chapter5-reduced-1-1dfcad5907-chunk-0002"
source_id: "chapter5-reduced-1-1dfcad5907"
source_file: "Chapter5_reduced-1.pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 2
confidence: "first-pass"
extraction_method: "structured-local"
---

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

## Slide 11

Minimax: Example

11

## Slide 12

Minimax: Example

12

## Slide 13

The minimax search algorithm

13

function Minimax-Decision(state) returns an action
inputs: state, current state in game
return the a in Actions(state) maximizing Min-Value(Result(a, state))

function Max-Value(state) returns a utility value
if Terminal-Test(state) then return Utility(state)
v ← −∞
for a, s in Successors(state) do v ← Max(v, Min-Value(s))
return v

function Min-Value(state) returns a utility value
if Terminal-Test(state) then return Utility(state)
v ← ∞
for a, s in Successors(state) do v ← Min(v, Max-Value(s))
return v

## Slide 14

Properties of minimax

Complete?? Yes, if tree is finite (chess has specific rules for this)

Optimal?? Yes, against an optimal opponent. Otherwise??

Time complexity?? O(bm)

Space complexity?? O(bm) (depth-first exploration) For chess, b ≈ 35, m ≈ 100 for “reasonable” games
⇒ exact solution completely infeasible
But do we need to explore every path?

14

## Slide 15

minimax search drawback

Number of game states is exponential in the number of moves.

Solution: Do not examine every node

Alpha-beta pruning
Remove branches that do not influence final decision
General idea: you can bracket the highest/lowest  value at a node, even before all its successors have been evaluated

15

## Slide 16

Alpha-Beta Pruning

minimax(root) = max(min(3,12,8), min(2,x,y), min(14,5,2))
= max(3, min(2,x,y), 2)
= max(3,z,2)	where z = min(2,x,y)
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

4	6
x	y

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

## Slide 17

Alpha-Beta Pruning: Ex

17

Prune when Alpha>Beta

## Slide 18

18

Alpha-Beta Pruning:Ex

## Slide 19

Alpha-Beta Pruning: Ex

19

## Slide 20

Alpha-Beta Pruning: Ex

20

## Slide 21

[-∞, +∞]

Range of possible values
[-∞,+∞]

Alpha-Beta Example

21

## Slide 22

[-∞,3]

[-∞,+∞]

Alpha-Beta Example (continued)

22

## Slide 23

Alpha-Beta Example (continued)

[-∞,3]

[-∞,+∞]

23

## Slide 24

[3,+∞]

[3,3]

Alpha-Beta Example (continued)

24

## Slide 25

[-∞,2]

[3,3]

[3,+∞]
This		node	is	worse for	MAX

Alpha-Beta Example (continued)

25

## Slide 26

[-∞,2]

[3,14]

[3,3]

[-∞,14]

,

Alpha-Beta Example (continued)

26

## Slide 27

[-∞,2]

[3,5]

[3,3]

[-∞,5]

,

Alpha-Beta Example (continued)

27

## Slide 28

[2,2]

[-∞,2]

[3,3]

[3,3]

Alpha-Beta Example (continued)

28

## Slide 29

[2,2]

[-∞,2]

[3,3]

[3,3]

Alpha-Beta Example (continued)

29

## Slide 30

Alpha-Beta Pruning
