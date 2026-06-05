---
chunk_id: "book-ca4fca8dd8-chunk-0200"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 200
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.6
Heuristic Functions
121
from then on will be on an optimal path. Think of the contour lines as following along this
optimal path. The search will trace along the optimal path, on each iteration adding an action
with cost c to get to a result state whose h-value will be c less, meaning that the total f =g+h
score will remain constant at C∗all along the path.
Some route-ﬁnding algorithms save even more time by adding shortcuts—artiﬁcial edges
Shortcuts
in the graph that deﬁne an optimal multi-action path. For example, if there were shortcuts
predeﬁned between all the 100 biggest cities in the U.S., and we were trying to navigate from
the Berkeley campus in California to NYU in New York, we could take the shortcut between
Sacramento and Manhattan and cover 90% of the path in one action.
hL(n) is efﬁcient but not admissible. But with a bit more care, we can come up with a
heuristic that is both efﬁcient and admissible:
hDH(n) =
max
L∈Landmarks|C∗(n,L)−C∗(goal,L)|
This is called a differential heuristic (because of the subtraction). Think of this with a
Diﬀerential heuristic
landmark that is somewhere out beyond the goal. If the goal happens to be on the optimal
path from n to the landmark, then this is saying “consider the entire path from n to L, then
subtract off the last part of that path, from goal to L, giving us the exact cost of the path from
n to goal.” To the extent that the goal is a bit off of the optimal path to the landmark, the
heuristic will be inexact, but still admissible. Landmarks that are not out beyond the goal
will not be useful; a landmark that is exactly halfway between n and goal will give hDH = 0,
which is not helpful.
There are several ways to pick landmark points. Selecting points at random is fast, but
we get better results if we take care to spread the landmarks out so they are not too close
to each other. A greedy approach is to pick a ﬁrst landmark at random, then ﬁnd the point
that is furthest from that, and add it to the set of landmarks, and continue, at each iteration
adding the point that maximizes the distance to the nearest landmark. If you have logs of
past search requests by your users, then you can pick landmarks that are frequently requested
in searches. For the differential heuristic it is good if the landmarks are spread around the
perimeter of the graph. Thus, a good technique is to ﬁnd the centroid of the graph, arrange
k pie-shaped wedges around the centroid, and in each wedge select the vertex that is farthest
from the center.
Landmarks work especially well in route-ﬁnding problems because of the way roads are
laid out in the world: a lot of trafﬁc actually wants to travel between landmarks, so civil
engineers build the widest and fastest roads along these routes; landmark search makes it
easier to recover these routes.
3.6.5 Learning to search better
We have presented several ﬁxed search strategies—breadth-ﬁrst, A∗, and so on—that have
been carefully designed and programmed by computer scientists. Could an agent learn how
to search better? The answer is yes, and the method rests on an important concept called the
metalevel state space. Each state in a metalevel state space captures the internal (compu-
Metalevel state
space
tational) state of a program that is searching in an ordinary state space such as the map of
Romania. (To keep the two concepts separate, we call the map of Romania an object-level
state space.) For example, the internal state of the A∗algorithm consists of the current search
Object-level state
space
tree. Each action in the metalevel state space is a computation step that alters the internal
