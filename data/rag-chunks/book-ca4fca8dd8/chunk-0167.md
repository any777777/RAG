---
chunk_id: "book-ca4fca8dd8-chunk-0167"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 167
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.4
Uninformed Search Strategies
99
function ITERATIVE-DEEPENING-SEARCH(problem) returns a solution node or failure
for depth = 0 to ∞do
result←DEPTH-LIMITED-SEARCH(problem,depth)
if result ̸= cutoff then return result
function DEPTH-LIMITED-SEARCH(problem, ℓ) returns a node or failure or cutoff
frontier←a LIFO queue (stack) with NODE(problem.INITIAL) as an element
result←failure
while not IS-EMPTY(frontier) do
node←POP(frontier)
if problem.IS-GOAL(node.STATE) then return node
if DEPTH(node) > ℓthen
result←cutoff
else if not IS-CYCLE(node) do
for each child in EXPAND(problem, node) do
add child to frontier
return result
Figure 3.12 Iterative deepening and depth-limited tree-like search. Iterative deepening re-
peatedly applies depth-limited search with increasing limits. It returns one of three different
types of values: either a solution node; or failure, when it has exhausted all nodes and proved
there is no solution at any depth; or cutoff, to mean there might be a solution at a deeper depth
than ℓ. This is a tree-like search algorithm that does not keep track of reached states, and thus
uses much less memory than best-ﬁrst search, but runs the risk of visiting the same state mul-
tiple times on different paths. Also, if the IS-CYCLE check does not check all cycles, then
the algorithm may get caught in a loop.
The time complexity is O(bd) when there is a solution, or O(bm) when there is none. Each
iteration of iterative deepening search generates a new level, in the same way that breadth-
ﬁrst search does, but breadth-ﬁrst does this by storing all nodes in memory, while iterative-
deepening does it by repeating the previous levels, thereby saving memory at the cost of more
time. Figure 3.13 shows four iterations of iterative-deepening search on a binary search tree,
where the solution is found on the fourth iteration.
Iterative deepening search may seem wasteful because states near the top of the search
tree are re-generated multiple times. But for many state spaces, most of the nodes are in the
bottom level, so it does not matter much that the upper levels are repeated. In an iterative
deepening search, the nodes on the bottom level (depth d) are generated once, those on the
next-to-bottom level are generated twice, and so on, up to the children of the root, which are
generated d times. So the total number of nodes generated in the worst case is
N(IDS) = (d)b1 +(d −1)b2 +(d −2)b3 ···+bd ,
which gives a time complexity of O(bd)—asymptotically the same as breadth-ﬁrst search.
For example, if b = 10 and d = 5, the numbers are
N(IDS) = 50+400+3,000+20,000+100,000 = 123,450
N(BFS) = 10+100+1,000+10,000+100,000 = 111,110.
If you are really concerned about the repetition, you can use a hybrid approach that runs
