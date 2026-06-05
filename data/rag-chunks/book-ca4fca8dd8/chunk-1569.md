---
chunk_id: "book-ca4fca8dd8-chunk-1569"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1569
confidence: "first-pass"
extraction_method: "structured-local"
---

950
Chapter 26
Robotics
qg
qs
Figure 26.14 A visibility graph. Lines connect every pair of vertices that can “see” each
other—lines that don’t go through an obstacle. The shortest path must lie upon these lines.
The motion planning problem can be made more complex in various ways: deﬁning the
goal as a set of possible conﬁgurations rather than a single conﬁguration; deﬁning the goal
in the workspace rather than the C-space; deﬁning a cost function (e.g., path length) to be
minimized; satisfying constraints (e.g., if the path involves carrying a cup of coffee, making
sure that the cup is always oriented upright so the coffee does not spill).
The spaces of motion planning: Let’s take a step back and make sure we understand the
spaces involved in motion planning. First, there is the workspace or world W. Points in W are
points in the everyday three-dimensional world. Next, we have the space of conﬁgurations,
C. Points q in C are d-dimensional, with d the robot’s number of degrees of freedom, and
map to sets of points A(q) in W. Finally, there is the space of paths. The space of paths is a
space of functions. Each point in this space maps to an entire curve through C-space. This
space is ∞-dimensional! Intuitively, we need d dimensions for each conﬁguration along the
path, and there are as many conﬁgurations on a path as there are points in the number line
interval [0,1]. Now let’s consider some ways of solving the motion planning problem.
Visibility graphs
For the simpliﬁed case of two-dimensional conﬁguration spaces and polygonal C-space ob-
stacles, visibility graphs are a convenient way to solve the motion planning problem with a
Visibility graph
guaranteed shortest-path solution. Let Vobs ⊂C be the set of vertices of the polygons making
up Cobs, and let V = Vobs ∪{qs,qg}.
We construct a graph G = (V,E) on the vertex set V with edges ei j ∈E connecting a
vertex vi to another vertex vj if the line connecting the two vertices is collision-free—that is,
if {λvi +(1−λ)v j : λ ∈[0,1]}∩Cobs = {}. When this happens, we say the two vertices “can
see each other,” which is where “visibility” graphs got their name.
To solve the motion planning problem, all we need to do is run a discrete graph search
(e.g., best-ﬁrst search) on the graph G with starting state qs and goal qg. In Figure 26.14
we see a visibility graph and an optimal three-step solution. An optimal search on visibility
graphs will always give us the optimal path (if one exists), or report failure if no path exists.
Voronoi diagrams
Visibility graphs encourage paths that run immediately adjacent to an obstacle—if you had to
walk around a table to get to the door, the shortest path would be to stick as close to the table
as possible. However, if motion or sensing is nondeterministic, that would put you at risk of
bumping into the table. One way to address this is to pretend that the robot’s body is a bit
