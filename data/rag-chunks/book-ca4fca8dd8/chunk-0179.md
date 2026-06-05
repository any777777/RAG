---
chunk_id: "book-ca4fca8dd8-chunk-0179"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 179
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 107

Section 3.5
Informed (Heuristic) Search Strategies
107
O
Z
A
T
L
M
D
C
R
F
P
G
B
U
H
E
V
I
N
380
400
420
S
Figure 3.20 Map of Romania showing contours at f = 380, f = 400, and f = 420, with
Arad as the start state. Nodes inside a given contour have f = g+h costs less than or equal
to the contour value.
With an inadmissible heuristic, A∗may or may not be cost-optimal. Here are two cases
where it is: First, if there is even one cost-optimal path on which h(n) is admissible for all
nodes n on the path, then that path will be found, no matter what the heuristic says for states
off the path. Second, if the optimal solution has cost C∗, and the second-best has cost C2, and
if h(n) overestimates some costs, but never by more than C2 −C∗, then A∗is guaranteed to
return cost-optimal solutions.
3.5.3 Search contours
A useful way to visualize a search is to draw contours in the state space, just like the contours
Contour
in a topographic map. Figure 3.20 shows an example. Inside the contour labeled 400, all
nodes have f(n) = g(n)+h(n) ≤400, and so on. Then, because A∗expands the frontier node
of lowest f-cost, we can see that an A∗search fans out from the start node, adding nodes in
concentric bands of increasing f-cost.
With uniform-cost search, we also have contours, but of g-cost, not g+h. The contours
with uniform-cost search will be “circular” around the start state, spreading out equally in all
directions with no preference towards the goal. With A∗search using a good heuristic, the
g + h bands will stretch toward a goal state (as in Figure 3.20) and become more narrowly
focused around an optimal path.
It should be clear that as you extend a path, the g costs are monotonic: the path cost
Monotonic
always increases as you go along a path, because action costs are always positive.12 Therefore
you get concentric contour lines that don’t cross each other, and if you choose to draw the
lines ﬁne enough, you can put a line between any two nodes on any path.
12 Technically, we say “strictly monotonic” for costs that always increase, and “monotonic” for costs that never
decrease, but might remain the same.

## Page 108
