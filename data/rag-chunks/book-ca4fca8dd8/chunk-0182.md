---
chunk_id: "book-ca4fca8dd8-chunk-0182"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 182
confidence: "first-pass"
extraction_method: "structured-local"
---

110
Chapter 3
Solving Problems by Searching
There are a variety of suboptimal search algorithms, which can be characterized by the
criteria for what counts as “good enough.” In bounded suboptimal search, we look for a
Bounded suboptimal
search
solution that is guaranteed to be within a constant factor W of the optimal cost. Weighted A∗
provides this guarantee. In bounded-cost search, we look for a solution whose cost is less
Bounded-cost search
than some constant C. And in unbounded-cost search, we accept a solution of any cost, as
Unbounded-cost
search
long as we can ﬁnd it quickly.
An example of an unbounded-cost search algorithm is speedy search, which is a version
Speedy search
of greedy best-ﬁrst search that uses as a heuristic the estimated number of actions required
to reach a goal, regardless of the cost of those actions. Thus, for problems where all actions
have the same cost it is the same as greedy best-ﬁrst search, but when actions have different
costs, it tends to lead the search to ﬁnd a solution quickly, even if it might have a high cost.
3.5.5 Memory-bounded search
The main issue with A∗is its use of memory. In this section we’ll cover some implementation
tricks that save space, and then some entirely new algorithms that take better advantage of the
available space.
Memory is split between the frontier and the reached states. In our implementation of
best-ﬁrst search, a state that is on the frontier is stored in two places: as a node in the frontier
(so we can decide what to expand next) and as an entry in the table of reached states (so we
know if we have visited the state before). For many problems (such as exploring a grid), this
duplication is not a concern, because the size of frontier is much smaller than reached, so
duplicating the states in the frontier requires a comparatively trivial amount of memory. But
some implementations keep a state in only one of the two places, saving a bit of space at the
cost of complicating (and perhaps slowing down) the algorithm.
Another possibility is to remove states from reached when we can prove that they are
no longer needed. For some problems, we can use the separation property (Figure 3.6 on
page 90), along with the prohibition of U-turn actions, to ensure that all actions either move
outwards from the frontier or onto another frontier state. In that case, we need only check the
frontier for redundant paths, and we can eliminate the reached table.
For other problems, we can keep reference counts of the number of times a state has
Reference count
been reached, and remove it from the reached table when there are no more ways to reach
the state. For example, on a grid world where each state can be reached only from its four
neighbors, once we have reached a state four times, we can remove it from the table.
Now let’s consider new algorithms that are designed to conserve memory usage.
Beam search limits the size of the frontier. The easiest approach is to keep only the k
Beam search
nodes with the best f-scores, discarding any other expanded nodes. This of course makes
the search incomplete and suboptimal, but we can choose k to make good use of available
memory, and the algorithm executes fast because it expands fewer nodes. For many prob-
lems it can ﬁnd good near-optimal solutions. You can think of uniform-cost or A∗search as
spreading out everywhere in concentric contours, and think of beam search as exploring only
a focused portion of those contours, the portion that contains the k best candidates.
An alternative version of beam search doesn’t keep a strict limit on the size of the frontier
but instead keeps every node whose f-score is within δ of the best f-score. That way, when
there are a few strong-scoring nodes only a few will be kept, but if there are no strong nodes
then more will be kept until a strong one emerges.
