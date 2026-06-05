---
chunk_id: "chapter-03-2-dbbbe61755-chunk-0006"
source_id: "chapter-03-2-dbbbe61755"
source_file: "New folder/Chapter 03 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 6
confidence: "first-pass"
extraction_method: "structured-local"
---

An uninformed search algorithm is given no clue about how close a state is to the goal(s).
For example, consider our agent in Arad with the goal of reaching Bucharest:
An uninformed agent with no knowledge of Romanian geography has no clue whether going to Zerind or Sibiu is a better first step. 
In contrast, an informed agent (Section 3.5) who knows the location of each city knows that Sibiu is much closer to Bucharest and thus more likely to be on the shortest path.

29

## Slide 30

30

Uninformed Search Strategies

Uninformed strategies use only the information available in the problem definition
Breadth-first search  (BFS)
Uniform-cost search  (UCS)
Depth-first search    (DFS)
Depth-limited search (DLS)
Iterative deepening search

## Slide 31

3.4.1 Breadth-first search

31

## Slide 32

32

… Breadth-first search

## Slide 33

Breadth-First Search

Strategy: expand a shallowest node first
Implementation: Fringe is a FIFO queue

33

## Slide 34

Breadth-First Search (BFS) Properties

What nodes does BFS expand?
Processes all nodes above shallowest solution
Let depth of shallowest solution be s
Search takes time O(bs)

How much space does the fringe take?
Has roughly the last tier, so O(bs)

Is it complete? Yes if b is finite
s must be finite if a solution exists, so yes!

Is it optimal?
Only if costs are all 1 (more on costs later)

…

b

1 node

b nodes

b2 nodes

bm nodes

s tiers

bs nodes

34

## Slide 35

36

Uninformed Search Strategies

Breadth-first search (BFS)
branching factor – a killing cost

The main concerns
Memory requirements – A bigger problem than time

Exponential complexity

35

## Slide 36

3.4.2 Dijkstra’s algorithm or uniform-cost search

36

## Slide 37

Uniform Cost Search

Strategy: expand a cheapest node first:
Fringe is a priority queue (priority: cumulative cost)

3

9

1

16

4

11

5

7

13

8

10

11

17

11

0

6

3

9

1

1

2

8

8

2

15

1

2

Cost contours

2

37

## Slide 38

4-38

Dijkstra’s algorithm: example

Step
0
1
2
3
4
5

N'
u
ux
uxy
uxyv
uxyvw
uxyvwz

D(v),p(v)
2,u
2,u
2,u

D(w),p(w)
5,u
4,x
3,y
3,y

D(x),p(x)
1,u

D(y),p(y)
∞
2,x

D(z),p(z)
∞ 
∞ 
4,y
4,y
4,y

## Slide 39

4-39

Dijkstra’s algorithm: example (2)

Resulting shortest-path tree from u:

Resulting forwarding table in u:

## Slide 40

40

## Slide 41

…

Uniform Cost Search (UCS) Properties

What nodes does UCS expand?
Processes all nodes with cost less than cheapest solution! (priority) (Expand least-cost unexpanded node)
Equivalent to breadth-first if step costs all equal 
If that solution costs C* and arcs cost at least  , then the “effective depth” is roughly C*/
Takes time O(bC*/) (exponential in effective depth)
