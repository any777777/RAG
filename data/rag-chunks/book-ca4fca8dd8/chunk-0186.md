---
chunk_id: "book-ca4fca8dd8-chunk-0186"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 186
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.5
Informed (Heuristic) Search Strategies
113
RBFS is optimal if the heuristic function h(n) is admissible. Its space complexity is
linear in the depth of the deepest optimal solution, but its time complexity is rather difﬁcult
to characterize: it depends both on the accuracy of the heuristic function and on how often
the best path changes as nodes are expanded. It expands nodes in order of increasing f-score,
even if f is nonmonotonic.
IDA∗and RBFS suffer from using too little memory. Between iterations, IDA∗retains
only a single number: the current f-cost limit. RBFS retains more information in memory,
but it uses only linear space: even if more memory were available, RBFS has no way to make
use of it. Because they forget most of what they have done, both algorithms may end up
reexploring the same states many times over.
It seems sensible, therefore, to determine how much memory we have available, and
allow an algorithm to use all of it. Two algorithms that do this are MA∗(memory-bounded
MA*
A∗) and SMA∗(simpliﬁed MA∗). SMA∗is—well—simpler, so we will describe it. SMA∗
SMA*
proceeds just like A∗, expanding the best leaf until memory is full. At this point, it cannot add
a new node to the search tree without dropping an old one. SMA∗always drops the worst leaf
node—the one with the highest f-value. Like RBFS, SMA∗then backs up the value of the
forgotten node to its parent. In this way, the ancestor of a forgotten subtree knows the quality
of the best path in that subtree. With this information, SMA∗regenerates the subtree only
when all other paths have been shown to look worse than the path it has forgotten. Another
way of saying this is that if all the descendants of a node n are forgotten, then we will not
know which way to go from n, but we will still have an idea of how worthwhile it is to go
anywhere from n.
The complete algorithm is described in the online code repository accompanying this
book. There is one subtlety worth mentioning. We said that SMA∗expands the best leaf and
deletes the worst leaf. What if all the leaf nodes have the same f-value? To avoid selecting
the same node for deletion and expansion, SMA∗expands the newest best leaf and deletes the
oldest worst leaf. These coincide when there is only one leaf, but in that case, the current
search tree must be a single path from root to leaf that ﬁlls all of memory. If the leaf is not a
goal node, then even if it is on an optimal solution path, that solution is not reachable with the
available memory. Therefore, the node can be discarded exactly as if it had no successors.
SMA∗is complete if there is any reachable solution—that is, if d, the depth of the shal-
lowest goal node, is less than the memory size (expressed in nodes). It is optimal if any
optimal solution is reachable; otherwise, it returns the best reachable solution. In practical
terms, SMA∗is a fairly robust choice for ﬁnding optimal solutions, particularly when the state
space is a graph, action costs are not uniform, and node generation is expensive compared to
the overhead of maintaining the frontier and the reached set.
On very hard problems, however, it will often be the case that SMA∗is forced to switch
back and forth continually among many candidate solution paths, only a small subset of which
can ﬁt in memory. (This resembles the problem of thrashing in disk paging systems.) Then
Thrashing
the extra time required for repeated regeneration of the same nodes means that problems
that would be practically solvable by A∗, given unlimited memory, become intractable for
SMA∗. That is to say, memory limitations can make a problem intractable from the point ◀
of view of computation time. Although no current theory explains the tradeoff between time
and memory, it seems that this is an inescapable problem. The only way out is to drop the
optimality requirement.
