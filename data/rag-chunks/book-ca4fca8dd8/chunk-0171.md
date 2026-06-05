---
chunk_id: "book-ca4fca8dd8-chunk-0171"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 171
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.4
Uninformed Search Strategies
101
function BIBF-SEARCH(problemF, fF, problemB, fB) returns a solution node, or failure
nodeF ←NODE(problemF.INITIAL)
// Node for a start state
nodeB ←NODE(problemB.INITIAL)
// Node for a goal state
frontierF ←a priority queue ordered by fF, with nodeF as an element
frontierB ←a priority queue ordered by fB, with nodeB as an element
reachedF ←a lookup table, with one key nodeF.STATE and value nodeF
reachedB ←a lookup table, with one key nodeB.STATE and value nodeB
solution←failure
while not TERMINATED(solution, frontierF, frontierB) do
if fF(TOP(frontierF)) < fB(TOP(frontierB)) then
solution←PROCEED(F, problemF, frontierF, reachedF, reachedB, solution)
else solution←PROCEED(B, problemB, frontierB, reachedB, reachedF, solution)
return solution
function PROCEED(dir, problem, frontier, reached, reached2, solution) returns a solution
// Expand node on frontier; check against the other frontier in reached2.
// The variable “dir” is the direction: either F for forward or B for backward.
node←POP(frontier)
for each child in EXPAND(problem, node) do
s←child.STATE
if s not in reached or PATH-COST(child) < PATH-COST(reached[s]) then
reached[s]←child
add child to frontier
if s is in reached2 then
solution2 ←JOIN-NODES(dir, child, reached2[s]))
if PATH-COST(solution2) < PATH-COST(solution) then
solution←solution2
return solution
Figure 3.14 Bidirectional best-ﬁrst search keeps two frontiers and two tables of reached
states. When a path in one frontier reaches a state that was also reached in the other half of
the search, the two paths are joined (by the function JOIN-NODES) to form a solution. The
ﬁrst solution we get is not guaranteed to be the best; the function TERMINATED determines
when to stop looking for new solutions.
For this to work, we need to keep track of two frontiers and two tables of reached states,
and we need to be able to reason backwards: if state s′ is a successor of s in the forward
direction, then we need to know that s is a successor of s′ in the backward direction. We have
a solution when the two frontiers collide.9
There are many different versions of bidirectional search, just as there are many different
unidirectional search algorithms. In this section, we describe bidirectional best-ﬁrst search.
Although there are two separate frontiers, the node to be expanded next is always one with
a minimum value of the evaluation function, across either frontier. When the evaluation
9
In our implementation, the reached data structure supports a query asking whether a given state is a member,
and the frontier data structure (a priority queue) does not, so we check for a collision using reached; but concep-
tually we are asking if the two frontiers have met up. The implementation can be extended to handle multiple
goal states by loading the node for each goal state into the backwards frontier and backwards reached table.
