---
chunk_id: "book-ca4fca8dd8-chunk-0657"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 657
confidence: "first-pass"
extraction_method: "structured-local"
---

396
Chapter 11
Automated Planning
AddEngine1
AddWheels1
Inspect1
AddWheels2
Inspect2
AddEngine2
100
110
120
EngineHoists(1)
WheelStations(1)
Inspectors(2)
90
80
70
60
50
40
30
20
10
0
Figure 11.15 A solution to the job-shop scheduling problem from Figure 11.13, taking into
account resource constraints. The left-hand margin lists the three reusable resources, and
actions are shown aligned horizontally with the resources they use. There are two possi-
ble schedules, depending on which assembly uses the engine hoist ﬁrst; we’ve shown the
shortest-duration solution, which takes 115 minutes.
isfaction. One popular approach is the minimum slack heuristic: on each iteration, schedule
Minimum slack
for the earliest possible start whichever unscheduled action has all its predecessors sched-
uled and has the least slack; then update the ES and LS times for each affected action and
repeat. This greedy heuristic resembles the minimum-remaining-values (MRV) heuristic in
constraint satisfaction. It often works well in practice, but for our assembly problem it yields
a 130-minute solution, not the 115-inute solution of Figure 11.15.
Up to this point, we have assumed that the set of actions and ordering constraints is
ﬁxed. Under these assumptions, every scheduling problem can be solved by a nonoverlapping
sequence that avoids all resource conﬂicts, provided that each action is feasible by itself.
However if a scheduling problem is proving very difﬁcult, it may not be a good idea to solve
it this way—it may be better to reconsider the actions and constraints, in case that leads to a
much easier scheduling problem. Thus, it makes sense to integrate planning and scheduling
by taking into account durations and overlaps during the construction of a plan. Several of
the planning algorithms in Section 11.2 can be augmented to handle this information.
11.7 Analysis of Planning Approaches
Planning combines the two major areas of AI we have covered so far: search and logic. A
planner can be seen either as a program that searches for a solution or as one that (construc-
tively) proves the existence of a solution. The cross-fertilization of ideas from the two areas
has allowed planners to scale up from toy problems where the number of actions and states
was limited to around a dozen, to real-world industrial applications with millions of states
and thousands of actions.
Planning is foremost an exercise in controlling combinatorial explosion. If there are n
propositions in a domain, then there are 2n states. Against such pessimism, the identiﬁcation
of independent subproblems can be a powerful weapon. In the best case—full decomposabil-
ity of the problem—we get an exponential speedup. Decomposability is destroyed, however,
by negative interactions between actions. SATPLAN can encode logical relations between
subproblems. Forward search addresses the problem heuristically by trying to ﬁnd patterns
(subsets of propositions) that cover the independent subproblems. Since this approach is
heuristic, it can work even when the subproblems are not completely independent.
