---
chunk_id: "book-ca4fca8dd8-chunk-0655"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 655
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.6
Time, Schedules, and Resources
395
Start
[0,0]
AddEngine1
30
 [0,15]
AddWheels1
30
 [30,45]
10
Inspect1
[60,75]
Finish
[85,85]
10
Inspect2
[75,75]
15
AddWheels2
[60,60]
60
AddEngine2
[0,0]
AddEngine1
AddWheels1
Inspect1
AddWheels2
Inspect2
AddEngine2
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
Figure 11.14 Top: a representation of the temporal constraints for the job-shop scheduling
problem of Figure 11.13. The duration of each action is given at the bottom of each rectangle.
In solving the problem, we compute the earliest and latest start times as the pair [ES,LS],
displayed in the upper left. The difference between these two numbers is the slack of an
action; actions with zero slack are on the critical path, shown with bold arrows. Bottom: the
same solution shown as a timeline. Blue rectangles represent time intervals during which an
action may be executed, provided that the ordering constraints are respected. The unoccupied
portion of a blue rectangle indicates the slack.
that the LS and ES computations are done once for each action, and each computation iterates
over at most b other actions.) Therefore, ﬁnding a minimum-duration schedule, given a partial
ordering on the actions and no resource constraints, is quite easy.
Mathematically speaking, critical-path problems are easy to solve because they are de-
ﬁned as a conjunction of linear inequalities on the start and end times. When we introduce
resource constraints, the resulting constraints on start and end times become more compli-
cated. For example, the AddEngine actions, which begin at the same time in Figure 11.14,
require the same EngineHoist and so cannot overlap. The “cannot overlap” constraint is a
disjunction of two linear inequalities, one for each possible ordering. The introduction of
disjunctions turns out to make scheduling with resource constraints NP-hard.
Figure 11.15 shows the solution with the fastest completion time, 115 minutes. This is
30 minutes longer than the 85 minutes required for a schedule without resource constraints.
Notice that there is no time at which both inspectors are required, so we can immediately
move one of our two inspectors to a more productive position.
There is a long history of work on optimal scheduling. A challenge problem posed in
1963—to ﬁnd the optimal schedule for a problem involving just 10 machines and 10 jobs of
100 actions each—went unsolved for 23 years (Lawler et al., 1993). Many approaches have
been tried, including branch-and-bound, simulated annealing, tabu search, and constraint sat-
