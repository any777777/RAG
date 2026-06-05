---
chunk_id: "chapter-03-2-dbbbe61755-chunk-0007"
source_id: "chapter-03-2-dbbbe61755"
source_file: "New folder/Chapter 03 (2).pptx"
source_type: "pptx"
topics:
  - "Unclassified"
chunk_index: 7
confidence: "first-pass"
extraction_method: "structured-local"
---

How much space does the fringe take?
Has roughly the last tier, so O(bC*/)

Is it complete?
Assuming best solution has a finite cost and minimum arc cost is positive, yes!
Is it optimal?
Yes!  (Proof next lecture via A*)

b

C*/  “tiers”

c  3

c  2

c  1

41

## Slide 42

Uniform Cost Issues

Remember: UCS explores increasing cost contours

The good: UCS is complete and optimal!
 because the first solution it finds will have a cost that is at least as low as the cost of any other node in the frontier; 
Uniform cost search considers all paths systematically in order of increasing cost, never getting caught going down a single infinite path (assuming that all action costs are > ϵ  > 0).
The bad:
Explores options in every “direction”
No information about goal location

We’ll fix that soon!

Start

Goal

42

## Slide 43

Video of Demo Contours UCS Pacman Small Maze

43

## Slide 44

Video of Demo Empty UCS

44

## Slide 45

3.4.3 Depth-first search

45

## Slide 46

Depth-First Search

46

## Slide 47

Depth-First Search

r

Strategy: expand a deepest node first
Implementation: Fringe is a LIFO stack

47

## Slide 48

Search Algorithm Properties

48

## Slide 49

Search Algorithm Properties

Complete: Guaranteed to find a solution if one exists?
Optimal: Guaranteed to find the least cost path?
Time complexity?
Space complexity?

Cartoon of search tree:
b is the branching factor
m is the maximum depth
solutions at various depths

Number of nodes in entire tree?
1 + b + b2 + …. bm = O(bm)

…

b

1 node

b nodes

b2 nodes

bm nodes

m tiers

49

## Slide 50

Depth-First Search (DFS) Properties

What nodes DFS expand?
Some left prefix of the tree.
Could process the whole tree!
If m is finite, takes time O(bm)
but if solutions are dense, may be much faster than breadth-first

How much space does the fringe take?
Only has siblings on path to root, so O(bm)

Is it complete?
m could be infinite, so only if we prevent cycles (more later)
complete in finite spaces

Is it optimal?
No, it finds the “leftmost” solution, regardless of depth or cost

50

## Slide 51

Video of Demo Maze Water DFS/BFS (part 1)

51

## Slide 52

Video of Demo Maze Water DFS/BFS (part 2)

52

## Slide 53

Depth-first search (DFS)

The main concerns
Wrong branch
Deep branch
The cures
Depth-limited search
Iterative deepening search

53

## Slide 54

3.4.4 Depth-limited and iterative deepening search

54

## Slide 55

55

… Depth-limited and iterative deepening search

## Slide 56

Depth-limited search
