---
chunk_id: "book-ca4fca8dd8-chunk-1570"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1570
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 951

Section 26.5
Planning and Control
951
Figure 26.15 A Voronoi diagram showing the set of points (black lines) equidistant to two
or more obstacles in conﬁguration space.
larger than it actually is, providing a buffer zone. Another way is to accept that path length
is not the only metric we want to optimize. Section 26.8.2 shows how to learn a good metric
from human examples of behavior.
A third way is to use a different technique, one that puts paths as far away from obstacles
as possible rather than hugging close to them. A Voronoi diagram is a representation that
Voronoi diagram
allows us to do just that. To get an idea for what a Voronoi diagram does, consider a space
where the obstacles are, say, a dozen small points scattered about a plane. Now surround each
of the obstacle points with a region consisting of all the points in the plane that are closer to
Region
that obstacle point than to any other obstacle point. Thus, the regions partition the plane. The
Voronoi diagram consists of the set of regions, and the Voronoi graph consists of the edges
Voronoi graph
and vertices of the regions.
When obstacles are areas, not points, everything stays pretty much the same. Each region
still contains all the points that are closer to one obstacle than to any other, where distance is
measured to the closest point on an obstacle. The boundaries between regions still correspond
to points that are equidistant between two obstacles, but now the boundary may be a curve
rather than a straight line. Computing these boundaries can be prohibitively expensive in
high-dimensional spaces.
To solve the motion planning problem, we connect the start point qs to the closest point
on the Voronoi graph via a straight line, and the same for the goal point qg. We then use
discrete graph search to ﬁnd the shortest path on the graph. For problems like navigating
through corridors indoors, this gives a nice path that goes down the middle of the corridor.
However, in outdoor settings it can come up with inefﬁcient paths, for example suggesting an
unnecessary 100 meter detour to stick to the middle of a wide-open 200-meter space.

## Page 952
