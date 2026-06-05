---
chunk_id: "book-ca4fca8dd8-chunk-1573"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1573
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 954

954
Chapter 26
Robotics
qg
qg
qg
qg
qs
qs
qs
qs
Figure 26.17 The probabilistic roadmap (PRM) algorithm. Top left: the start and goal con-
ﬁgurations. Top right: sample M collision-free milestones (here M = 5). Bottom left: con-
nect each milestone to its k nearest neighbors (here k = 3). Bottom right: ﬁnd the shortest
path from the start to the goal on the resulting graph.
graph from qs to qg. If no path is found, then M more milestones are sampled, added to the
graph, and the process is repeated.
Figure 26.17 shows a roadmap with the path found between two conﬁgurations. PRMs
are not complete, but they are what is called probabilistically complete—they will eventu-
Probabilistically
complete
ally ﬁnd a path, if one exists. Intuitively, this is because they keep sampling more milestones.
PRMs work well even in high-dimensional conﬁguration spaces.
PRMs are also popular for multi-query planning, in which we have multiple motion
Multi-query planning
planning problems within the same C-space. Often, once the robot reaches a goal, it is called
upon to reach another goal in the same workspace. PRMs are really useful, because the robot
can dedicate time up front to constructing a roadmap, and amortize the use of that roadmap
over multiple queries.
Rapidly-exploring random trees
An extension of PRMs called rapidly exploring random trees (RRTs) is popular for single-
Rapidly exploring
random trees
(RRTs)
query planning. We incrementally build two trees, one with qs as the root and one with qg
as the root. Random milestones are chosen, and an attempt is made to connect each new
milestone to the existing trees. If a milestone connects both trees, that means a solution has
been found, as in Figure 26.18. If not, the algorithm ﬁnds the closest point in each tree and
adds to the tree a new edge that extends from the point by a distance δ towards the milestone.
This tends to grow the tree towards previously unexplored sections of the space.
Roboticists love RRTs for their ease of use. However, RRT solutions are typically nonop-
timal and lack smoothness. Therefore, RRTs are often followed by a post-processing step.
The most common one is “short-cutting,” in which we randomly select one of the vertices on
the solution path and try to remove it by connecting its neighbors to each other (via the simple

## Page 955
