---
chunk_id: "book-ca4fca8dd8-chunk-1572"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1572
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.5
Planning and Control
953
such a cell may not be a real solution, because there may be no way to safely cross the
cell. This would make the path planner unsound. On the other hand, if we insist that only
completely free cells may be used, the planner will be incomplete, because it might be the
case that the only paths to the goal go through mixed cells—it might be that a corridor is
actually wide enough for the robot to pass, but the corridor is covered only by mixed cells.
The ﬁrst approach to this problem is further subdivision of the mixed cells—perhaps
using cells of half the original size. This can be continued recursively until a path is found
that lies entirely within free cells. This method works well and is complete if there is a way to
decide if a given cell is a mixed cell, which is easy only if the conﬁguration space boundaries
have relatively simple mathematical descriptions.
It is important to note that cell decomposition does not necessarily require explicitly rep-
resenting the obstacle space Cobs. We can decide to include a cell or not by using a collision
checker. This is a crucial notion to motion planning. A collision checker is a function γ(q)
Collision checker
that maps to 1 if the conﬁguration collides with an obstacle, and 0 otherwise. It is much easier
to check whether a speciﬁc conﬁguration is in collision than to explicitly construct the entire
obstacle space Cobs.
Examining the solution path shown in Figure 26.16(a), we can see an additional difﬁculty
that will have to be resolved. The path contains arbitrarily sharp corners, but a physical robot
has momentum and cannot change direction instantaneously. This problem can be solved by
storing, for each grid cell, the exact continuous state (position and velocity) that was attained
when the cell was reached in the search. Assume further that when propagating information
to nearby grid cells, we use this continuous state as a basis, and apply the continuous robot
motion model for jumping to nearby cells. So we don’t make an instantaneous 90◦turn; we
make a rounded turn governed by the laws of motion. We can now guarantee that the resulting
trajectory is smooth and can indeed be executed by the robot. One algorithm that implements
this is hybrid A∗.
Hybrid A∗
Randomized motion planning
Randomized motion planning does graph search on a random decomposition of the conﬁgu-
ration space, rather than a regular cell decomposition. The key idea is to sample a random set
of points and to create edges between them if there is a very simple way to get from one to
the other (e.g., via a straight line) without colliding; then we can search on this graph.
A probabilistic roadmap (PRM) algorithm is one way to leverage this idea. We assume
Probabilistic
roadmap (PRM)
access to a collision checker γ (deﬁned on page 953), and to a simple planner B(q1,q2) that
Simple planner
returns a path from q1 to q2 (or failure) but does so quickly. This simple planner is not going
to be complete—it might return failure even if a solution actually exists. Its job is to quickly
try to connect q1 and q2 and let the main algorithm know if it succeeds. We will use it to
deﬁne whether an edge exists between two vertices.
The algorithm starts by sampling M milestones—points in Cfree—in addition to the
Milestone
points qs and qg. It uses rejection sampling, where conﬁgurations are sampled randomly
and collision-checked using γ until a total of M milestones are found. Next, the algorithm
uses the simple planner to try to connect pairs of milestones. If the simple planner returns
success, then an edge between the pair is added to the graph; otherwise, the graph remains as
is. We try to connect each milestone either to its k nearest neighbors (we call this k-PRM), or
to all milestones in a sphere of a radius r. Finally, the algorithm searches for a path on this
