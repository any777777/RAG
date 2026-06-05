---
chunk_id: "book-ca4fca8dd8-chunk-0161"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 161
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.4
Uninformed Search Strategies
95
function BREADTH-FIRST-SEARCH(problem) returns a solution node or failure
node←NODE(problem.INITIAL)
if problem.IS-GOAL(node.STATE) then return node
frontier←a FIFO queue, with node as an element
reached←{problem.INITIAL}
while not IS-EMPTY(frontier) do
node←POP(frontier)
for each child in EXPAND(problem, node) do
s←child.STATE
if problem.IS-GOAL(s) then return child
if s is not in reached then
add s to reached
add child to frontier
return failure
function UNIFORM-COST-SEARCH(problem) returns a solution node, or failure
return BEST-FIRST-SEARCH(problem, PATH-COST)
Figure 3.9 Breadth-ﬁrst search and uniform-cost search algorithms.
for problems where all actions have the same cost, but not for problems that don’t have that
property. It is complete in either case. In terms of time and space, imagine searching a
uniform tree where every state has b successors. The root of the search tree generates b
nodes, each of which generates b more nodes, for a total of b2 at the second level. Each of
these generates b more nodes, yielding b3 nodes at the third level, and so on. Now suppose
that the solution is at depth d. Then the total number of nodes generated is
1+b+b2 +b3 +···+bd = O(bd)
All the nodes remain in memory, so both time and space complexity are O(bd). Exponential
bounds like that are scary. As a typical real-world example, consider a problem with branch-
ing factor b = 10, processing speed 1 million nodes/second, and memory requirements of 1
Kbyte/node. A search to depth d = 10 would take less than 3 hours, but would require 10
terabytes of memory. The memory requirements are a bigger problem for breadth-ﬁrst search ◀
than the execution time. But time is still an important factor. At depth d = 14, even with
inﬁnite memory, the search would take 3.5 years. In general, exponential-complexity search ◀
problems cannot be solved by uninformed search for any but the smallest instances.
3.4.2 Dijkstra’s algorithm or uniform-cost search
When actions have different costs, an obvious choice is to use best-ﬁrst search where the
evaluation function is the cost of the path from the root to the current node. This is called Di-
jkstra’s algorithm by the theoretical computer science community, and uniform-cost search
Uniform-cost search
by the AI community. The idea is that while breadth-ﬁrst search spreads out in waves of uni-
form depth—ﬁrst depth 1, then depth 2, and so on—uniform-cost search spreads out in waves
of uniform path-cost. The algorithm can be implemented as a call to BEST-FIRST-SEARCH
with PATH-COST as the evaluation function, as shown in Figure 3.9.
