---
chunk_id: "book-ca4fca8dd8-chunk-0149"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 149
confidence: "first-pass"
extraction_method: "structured-local"
---

88
Chapter 3
Solving Problems by Searching
Commercial travel advice systems use a problem formulation of this kind, with many addi-
tional complications to handle the airlines’ byzantine fare structures. Any seasoned traveler
knows, however, that not all air travel goes according to plan. A really good system should in-
clude contingency plans—what happens if this ﬂight is delayed and the connection is missed?
Touring problems describe a set of locations that must be visited, rather than a single
Touring problem
goal destination. The traveling salesperson problem (TSP) is a touring problem in which
every city on a map must be visited. The aim is to ﬁnd a tour with cost < C (or in the
Traveling
salesperson problem
(TSP)
optimization version, to ﬁnd a tour with the lowest cost possible). An enormous amount
of effort has been expended to improve the capabilities of TSP algorithms. The algorithms
can also be extended to handle ﬂeets of vehicles. For example, a search and optimization
algorithm for routing school buses in Boston saved $5 million, cut trafﬁc and air pollution,
and saved time for drivers and students (Bertsimas et al., 2019). In addition to planning trips,
search algorithms have been used for tasks such as planning the movements of automatic
circuit-board drills and of stocking machines on shop ﬂoors.
A VLSI layout problem requires positioning millions of components and connections on
VLSI layout
a chip to minimize area, minimize circuit delays, minimize stray capacitances, and maximize
manufacturing yield. The layout problem comes after the logical design phase and is usually
split into two parts: cell layout and channel routing. In cell layout, the primitive components
of the circuit are grouped into cells, each of which performs some recognized function. Each
cell has a ﬁxed footprint (size and shape) and requires a certain number of connections to
each of the other cells. The aim is to place the cells on the chip so that they do not overlap
and so that there is room for the connecting wires to be placed between the cells. Channel
routing ﬁnds a speciﬁc route for each wire through the gaps between the cells. These search
problems are extremely complex, but deﬁnitely worth solving.
Robot navigation is a generalization of the route-ﬁnding problem described earlier.
Robot navigation
Rather than following distinct paths (such as the roads in Romania), a robot can roam around,
in effect making its own paths. For a circular robot moving on a ﬂat surface, the space is
essentially two-dimensional. When the robot has arms and legs that must also be controlled,
the search space becomes many-dimensional—one dimension for each joint angle. Advanced
techniques are required just to make the essentially continuous search space ﬁnite (see Chap-
ter 26). In addition to the complexity of the problem, real robots must also deal with errors
in their sensor readings and motor controls, with partial observability, and with other agents
that might alter the environment.
Automatic assembly sequencing of complex objects (such as electric motors) by a robot
Automatic assembly
sequencing
has been standard industry practice since the 1970s. Algorithms ﬁrst ﬁnd a feasible assembly
sequence and then work to optimize the process. Minimizing the amount of manual human
labor on the assembly line can produce signiﬁcant savings in time and cost. In assembly
problems, the aim is to ﬁnd an order in which to assemble the parts of some object. If the
wrong order is chosen, there will be no way to add some part later in the sequence without
undoing some of the work already done. Checking an action in the sequence for feasibility is a
difﬁcult geometrical search problem closely related to robot navigation. Thus, the generation
of legal actions is the expensive part of assembly sequencing. Any practical algorithm must
avoid exploring all but a tiny fraction of the state space. One important assembly problem is
protein design, in which the goal is to ﬁnd a sequence of amino acids that will fold into a
Protein design
three-dimensional protein with the right properties to cure some disease.
