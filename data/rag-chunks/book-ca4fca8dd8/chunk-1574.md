---
chunk_id: "book-ca4fca8dd8-chunk-1574"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1574
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.5
Planning and Control
955
qg
qs
qsample
Figure 26.18 The bidirectional RRT algorithm constructs two trees (one from the start, the
other from the goal) by incrementally connecting each sample to the closest node in each
tree, if the connection is possible. When a sample connects to both trees, that means we have
found a solution path.
(a)
(b)
(c)
Figure 26.19 Snapshots of a trajectory produced by an RRT and post-processed with short-
cutting. Courtesy of Anca Dragan.
planner). We do this repeatedly for as many steps as we have compute time for. Even then,
the trajectories might look a little unnatural due to the random positions of the milestone that
were selected, as shown in Figure 26.19.
RRT∗is a modiﬁcation to RRT that makes the algorithm asymptotically optimal: the
RRT∗
solution converges to the optimal solution as more and more milestones are sampled. The
key idea is to pick the nearest neighbor based on a notion of cost to come rather than distance
from the milestone only, and to rewire the tree, swapping parents of older vertices if it is
cheaper to reach them via the new milestone.
Trajectory optimization for kinematic planning
Randomized sampling algorithms tend to ﬁrst construct a complex but feasible path and then
optimize it. Trajectory optimization does the opposite: it starts with a simple but infeasible
path, and then works to push it out of collision. The goal is to ﬁnd a path that optimizes a cost

## Page 956
