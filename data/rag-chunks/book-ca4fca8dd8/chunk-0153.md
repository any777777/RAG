---
chunk_id: "book-ca4fca8dd8-chunk-0153"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 153
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.3
Search Algorithms
91
function BEST-FIRST-SEARCH(problem,f) returns a solution node or failure
node←NODE(STATE=problem.INITIAL)
frontier←a priority queue ordered by f, with node as an element
reached←a lookup table, with one entry with key problem.INITIAL and value node
while not IS-EMPTY(frontier) do
node←POP(frontier)
if problem.IS-GOAL(node.STATE) then return node
for each child in EXPAND(problem, node) do
s←child.STATE
if s is not in reached or child.PATH-COST < reached[s].PATH-COST then
reached[s]←child
add child to frontier
return failure
function EXPAND(problem,node) yields nodes
s←node.STATE
for each action in problem.ACTIONS(s) do
s′ ←problem.RESULT(s,action)
cost←node.PATH-COST + problem.ACTION-COST(s,action,s′)
yield NODE(STATE=s′, PARENT=node, ACTION=action, PATH-COST=cost)
Figure 3.7 The best-ﬁrst search algorithm, and the function for expanding a node. The data
structures used here are described in Section 3.3.2. See Appendix B for yield.
3.3.1 Best-ﬁrst search
How do we decide which node from the frontier to expand next? A very general approach
is called best-ﬁrst search, in which we choose a node, n, with minimum value of some
Best-ﬁrst search
evaluation function, f(n). Figure 3.7 shows the algorithm. On each iteration we choose
Evaluation function
a node on the frontier with minimum f(n) value, return it if its state is a goal state, and
otherwise apply EXPAND to generate child nodes. Each child node is added to the frontier
if it has not been reached before, or is re-added if it is now being reached with a path that
has a lower path cost than any previous path. The algorithm returns either an indication of
failure, or a node that represents a path to a goal. By employing different f(n) functions, we
get different speciﬁc algorithms, which this chapter will cover.
3.3.2 Search data structures
Search algorithms require a data structure to keep track of the search tree. A node in the tree
is represented by a data structure with four components:
• node.STATE: the state to which the node corresponds;
• node.PARENT: the node in the tree that generated this node;
• node.ACTION: the action that was applied to the parent’s state to generate this node;
• node.PATH-COST: the total cost of the path from the initial state to this node. In math-
ematical formulas, we use g(node) as a synonym for PATH-COST.
Following the PARENT pointers back from a node allows us to recover the states and actions
along the path to that node. Doing this from a goal node gives us the solution.
