---
chunk_id: "book-ca4fca8dd8-chunk-1571"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1571
confidence: "first-pass"
extraction_method: "structured-local"
---

952
Chapter 26
Robotics
start
goal
start
goal
(a)
(b)
Figure 26.16 (a) Value function and path found for a discrete grid cell approximation of the
conﬁguration space. (b) The same path visualized in workspace coordinates. Notice how the
robot bends its elbow to avoid a collision with the vertical obstacle.
Cell decomposition
An alternative approach to motion planning is to discretize the C-space. Cell decomposition
Cell decomposition
methods decompose the free space into a ﬁnite number of contiguous regions, called cells.
These cells are designed so that the path-planning problem within a single cell can be solved
by simple means (e.g., moving along a straight line). The path-planning problem then be-
comes a discrete graph search problem (as with visibility graphs and Voronoi graphs) to ﬁnd
a path through a sequence of cells.
The simplest cell decomposition consists of a regularly spaced grid. Figure 26.16(a)
shows a square grid decomposition of the space and a solution path that is optimal for this
grid size. Grayscale shading indicates the value of each free-space grid cell—the cost of
the shortest path from that cell to the goal. (These values can be computed by a deterministic
form of the VALUE-ITERATION algorithm given in Figure 16.6 on page 563.) Figure 26.16(b)
shows the corresponding workspace trajectory for the arm. Of course, we could also use the
A∗algorithm to ﬁnd a shortest path.
This grid decomposition has the advantage that it is simple to implement, but it suffers
from three limitations. First, it is workable only for low-dimensional conﬁguration spaces,
because the number of grid cells increases exponentially with d, the number of dimensions.
(Sounds familiar? This is the curse of dimensionality.) Second, paths through discretized
state space will not always be smooth. We see in Figure 26.16(a) that the diagonal parts of
the path are jagged and hence very difﬁcult for the robot to follow accurately. The robot can
attempt to smooth out the solution path, but this is far from straightforward.
Third, there is the problem of what to do with cells that are “mixed”—that is, neither
entirely within free space nor entirely within occupied space. A solution path that includes

## Page 953
