---
chunk_id: "book-ca4fca8dd8-chunk-0143"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 143
confidence: "first-pass"
extraction_method: "structured-local"
---

84
Chapter 3
Solving Problems by Searching
3.1.2 Formulating problems
Our formulation of the problem of getting to Bucharest is a model—an abstract mathematical
description—and not the real thing. Compare the simple atomic state description Arad to an
actual cross-country trip, where the state of the world includes so many things: the traveling
companions, the current radio program, the scenery out of the window, the proximity of law
enforcement ofﬁcers, the distance to the next rest stop, the condition of the road, the weather,
the trafﬁc, and so on. All these considerations are left out of our model because they are
irrelevant to the problem of ﬁnding a route to Bucharest.
The process of removing detail from a representation is called abstraction. A good
Abstraction
problem formulation has the right level of detail. If the actions were at the level of “move the
right foot forward a centimeter” or “turn the steering wheel one degree left,” the agent would
probably never ﬁnd its way out of the parking lot, let alone to Bucharest.
Can we be more precise about the appropriate level of abstraction? Think of the abstract
Level of abstraction
states and actions we have chosen as corresponding to large sets of detailed world states and
detailed action sequences. Now consider a solution to the abstract problem: for example,
the path from Arad to Sibiu to Rimnicu Vilcea to Pitesti to Bucharest. This abstract solution
corresponds to a large number of more detailed paths. For example, we could drive with the
radio on between Sibiu and Rimnicu Vilcea, and then switch it off for the rest of the trip.
The abstraction is valid if we can elaborate any abstract solution into a solution in the
more detailed world; a sufﬁcient condition is that for every detailed state that is “in Arad,”
there is a detailed path to some state that is “in Sibiu,” and so on.4 The abstraction is useful if
carrying out each of the actions in the solution is easier than the original problem; in our case,
the action “drive from Arad to Sibiu” can be carried out without further search or planning by
a driver with average skill. The choice of a good abstraction thus involves removing as much
detail as possible while retaining validity and ensuring that the abstract actions are easy to
carry out. Were it not for the ability to construct useful abstractions, intelligent agents would
be completely swamped by the real world.
3.2 Example Problems
The problem-solving approach has been applied to a vast array of task environments. We list
some of the best known here, distinguishing between standardized and real-world problems.
A standardized problem is intended to illustrate or exercise various problem-solving meth-
Standardized
problem
ods. It can be given a concise, exact description and hence is suitable as a benchmark for
researchers to compare the performance of algorithms. A real-world problem, such as robot
Real-world problem
navigation, is one whose solutions people actually use, and whose formulation is idiosyn-
cratic, not standardized, because, for example, each robot has different sensors that produce
different data.
3.2.1 Standardized problems
A grid world problem is a two-dimensional rectangular array of square cells in which agents
Grid world
can move from cell to cell. Typically the agent can move to any obstacle-free adjacent cell—
horizontally or vertically and in some problems diagonally. Cells can contain objects, which
4
See Section 11.4.
