---
chunk_id: "chapter-03-2-d1bd0d2931-chunk-0006"
source_id: "chapter-03-2-d1bd0d2931"
source_file: "Chapter 03 (2).pdf"
source_type: "pdf"
topics:
  - "Unclassified"
chunk_index: 6
confidence: "first-pass"
extraction_method: "structured-local"
---

Breadth-First Search (BFS) Properties
What nodes does BFS expand?
Processes all nodes above shallowest solution
Let depth of shallowest solution be s
Search takes time O(bs)
How much space does the fringe take?
Has roughly the last tier, so O(bs)
Is it complete? Yes if b is finite
s must be finite if a solution exists, so yes!
Is it optimal?
Only if costs are all 1 (more on costs later)
…
b
1 node
b nodes
b2 nodes
bm nodes
s tiers
bs nodes
34

## Page 33

36
Uninformed Search Strategies
Breadth-first search (BFS)
branching factor – a killing cost
The main concerns
Memory requirements – A bigger problem than time
Exponential complexity
35

## Page 34

3.4.2 Dijkstra’s algorithm or uniform-cost 
search
36

## Page 35

Uniform Cost Search
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
Strategy: expand a 
cheapest node first:
Fringe is a priority queue 
(priority: cumulative cost)
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
Cost 
contours
2
37

## Page 36

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
u
y
x
w
v
z
2
2
1
3
1
1
2
5
3
5

## Page 37

4-39
Dijkstra’s algorithm: example (2) 
u
y
x
w
v
z
Resulting shortest-path tree from u:
v
x
y
w
z
(u,v)
(u,x)
(u,x)
(u,x)
(u,x)
destination
link
Resulting forwarding table in u:

## Page 38

40

## Page 39

…
Uniform Cost Search (UCS) Properties
What nodes does UCS expand?
Processes all nodes with cost less than cheapest solution! 
(priority) (Expand least-cost unexpanded node)
Equivalent to breadth-first if step costs all equal 
If that solution costs C* and arcs cost at least , then the 
“effective depth” is roughly C*/
Takes time O(bC*/) (exponential in effective depth)
How much space does the fringe take?
Has roughly the last tier, so O(bC*/)
Is it complete?
Assuming best solution has a finite cost and minimum arc cost 
is positive, yes!
Is it optimal?
Yes!  (Proof next lecture via A*)
b
C*/“tiers”
c 3
c 2
c 1
41

## Page 40
