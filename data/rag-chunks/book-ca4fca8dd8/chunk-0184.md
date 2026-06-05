---
chunk_id: "book-ca4fca8dd8-chunk-0184"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 184
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.5
Informed (Heuristic) Search Strategies
111
Iterative-deepening A∗search (IDA∗) is to A∗what iterative-deepening search is to
Iterative-deepening
A∗search
depth-ﬁrst: IDA∗gives us the beneﬁts of A∗without the requirement to keep all reached
states in memory, at a cost of visiting some states multiple times. It is a very important and
commonly used algorithm for problems that do not ﬁt in memory.
In standard iterative deepening the cutoff is the depth, which is increased by one each
iteration. In IDA∗the cutoff is the f-cost (g + h); at each iteration, the cutoff value is the
smallest f-cost of any node that exceeded the cutoff on the previous iteration. In other words,
each iteration exhaustively searches an f-contour, ﬁnds a node just beyond that contour, and
uses that node’s f-cost as the next contour. For problems like the 8-puzzle where each path’s
f-cost is an integer, this works very well, resulting in steady progress towards the goal each
iteration. If the optimal solution has cost C∗, then there can be no more than C∗iterations (for
example, no more than 31 iterations on the hardest 8-puzzle problems). But for a problem
where every node has a different f-cost, each new contour might contain only one new node,
and the number of iterations could be equal to the number of states.
Recursive best-ﬁrst search (RBFS) (Figure 3.22) attempts to mimic the operation of
Recursive best-ﬁrst
search
standard best-ﬁrst search, but using only linear space. RBFS resembles a recursive depth-
ﬁrst search, but rather than continuing indeﬁnitely down the current path, it uses the f limit
variable to keep track of the f-value of the best alternative path available from any ancestor
of the current node. If the current node exceeds this limit, the recursion unwinds back to the
alternative path. As the recursion unwinds, RBFS replaces the f-value of each node along the
path with a backed-up value—the best f-value of its children. In this way, RBFS remembers
Backed-up value
the f-value of the best leaf in the forgotten subtree and can therefore decide whether it’s worth
reexpanding the subtree at some later time. Figure 3.23 shows how RBFS reaches Bucharest.
RBFS is somewhat more efﬁcient than IDA∗, but still suffers from excessive node re-
generation. In the example in Figure 3.23, RBFS follows the path via Rimnicu Vilcea, then
function RECURSIVE-BEST-FIRST-SEARCH(problem) returns a solution or failure
solution, fvalue←RBFS(problem, NODE(problem.INITIAL), ∞)
return solution
function RBFS(problem,node,f limit) returns a solution or failure, and a new f-cost limit
if problem.IS-GOAL(node.STATE) then return node
successors←LIST(EXPAND(node))
if successors is empty then return failure, ∞
for each s in successors do
// update f with value from previous search
s.f ←max(s.PATH-COST + h(s), node.f))
while true do
best←the node in successors with lowest f-value
if best.f > f limit then return failure, best.f
alternative←the second-lowest f-value among successors
result,best. f ←RBFS(problem,best,min(f limit,alternative))
if result ̸= failure then return result, best.f
Figure 3.22 The algorithm for recursive best-ﬁrst search.
