---
chunk_id: "chapter-03-2-d1bd0d2931-chunk-0007"
source_id: "chapter-03-2-d1bd0d2931"
source_file: "Chapter 03 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 7
confidence: "first-pass"
extraction_method: "structured-local"
---

Uniform Cost Issues
Remember: UCS explores increasing cost 
contours
The good: UCS is complete and optimal!

because the first solution it finds will have a cost that is at least as low as the 
cost of any other node in the frontier; 

Uniform cost search considers all paths systematically in order of increasing 
cost, never getting caught going down a single infinite path (assuming that all 
action costs are > ϵ > 0).
The bad:
Explores options in every “direction”
No information about goal location
We’ll fix that soon!
Start
Goal
…
c 3
c 2
c 1
42

## Page 41

Video of Demo Contours UCS Pacman Small Maze
43

## Page 42

Video of Demo Empty UCS
44

## Page 43

3.4.3 Depth-first search
45

## Page 44

Depth-First Search
46

## Page 45

Depth-First Search
S
a
b
d
p
a
c
e
p
h
f
r
q
q
c
G
a
q
e
p
h
f
r
q
q
c
G
a
S
G
d
b
p
q
c
e
h
a
f
r
q
p
h
f
d
b
a
c
e
r
Strategy: expand a 
deepest node first
Implementation: 
Fringe is a LIFO stack
47

## Page 46

Search Algorithm Properties
48

## Page 47

Search Algorithm Properties
Complete: Guaranteed to find a solution if one exists?
Optimal: Guaranteed to find the least cost path?
Time complexity?
Space complexity?
Cartoon of search tree:
b is the branching factor
m is the maximum depth
solutions at various depths
Number of nodes in entire tree?
1 + b + b2 + …. bm = O(bm)
…
b
1 node
b nodes
b2 nodes
bm nodes
m tiers
49

## Page 48

Depth-First Search (DFS) Properties
…
b
1 node
b nodes
b2 nodes
bm nodes
m tiers

What nodes DFS expand?
Some left prefix of the tree.
Could process the whole tree!
If m is finite, takes time O(bm)
but if solutions are dense, may be much faster 
than breadth-first

How much space does the fringe take?
Only has siblings on path to root, so O(bm)

Is it complete?
m could be infinite, so only if we prevent cycles 
(more later)
complete in finite spaces

Is it optimal?
No, it finds the “leftmost” solution, regardless of 
depth or cost
50

## Page 49

Video of Demo Maze Water DFS/BFS (part 1)
51

## Page 50

Video of Demo Maze Water DFS/BFS (part 2)
52

## Page 51

Depth-first search (DFS)
The main concerns
Wrong branch
Deep branch
The cures
Depth-limited search
Iterative deepening search

## Page 52

3.4.4 Depth-limited and iterative deepening 
search
54

## Page 53

55
… Depth-limited and iterative deepening search

## Page 54

Depth-limited search
Determining depth limit l
Nodes at depth l are treated as if they have no
successors
Incomplete if l < d
Time complexity: O(b l)
Space complexity: O(bl)
56
