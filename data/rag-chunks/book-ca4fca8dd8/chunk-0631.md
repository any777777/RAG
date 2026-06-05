---
chunk_id: "book-ca4fca8dd8-chunk-0631"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 631
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.5
Planning and Acting in Nondeterministic Domains
383
Cleaning a set of rooms by cleaning each room in turn is hardly rocket science: it is
easy for humans because of the hierarchical structure of the task. When we consider how
difﬁcult humans ﬁnd it to solve small puzzles such as the 8-puzzle, it seems likely that the
human capacity for solving complex problems derives not from considering combinatorics,
but rather from skill in abstracting and decomposing problems to eliminate combinatorics.
The angelic approach can be extended to ﬁnd least-cost solutions by generalizing the
notion of reachable set. Instead of a state being reachable or not, each state will have a cost
for the most efﬁcient way to get there. (The cost is inﬁnite for unreachable states.) The
optimistic and pessimistic descriptions bound these costs. In this way, angelic search can
ﬁnd provably optimal abstract plans without having to consider their implementations. The
same approach can be used to obtain effective hierarchical look-ahead algorithms for online
Hierarchical
look-ahead
search, in the style of LRTA∗(page 158).
In some ways, such algorithms mirror aspects of human deliberation in tasks such as
planning a vacation to Hawaii—consideration of alternatives is done initially at an abstract
level over long time scales; some parts of the plan are left quite abstract until execution time,
such as how to spend two lazy days on Moloka‘i, while others parts are planned in detail,
such as the ﬂights to be taken and lodging to be reserved—without these latter reﬁnements,
there is no guarantee that the plan would be feasible.
11.5 Planning and Acting in Nondeterministic Domains
In this section we extend planning to handle partially observable, nondeterministic, and un-
known environments. The basic concepts mirror those in Chapter 4, but there are differences
arising from the use of factored representations rather than atomic representations. This af-
fects the way we represent the agent’s capability for action and observation and the way
we represent belief states—the sets of possible physical states the agent might be in—for
partially observable environments. We can also take advantage of many of the domain-
independent methods given in Section 11.3 for calculating search heuristics.
We will cover sensorless planning (also known as conformant planning) for environ-
ments with no observations; contingency planning for partially observable and nondetermin-
istic environments; and online planning and replanning for unknown environments. This
will allow us to tackle sizable real-world problems.
Consider this problem: given a chair and a table, the goal is to have them match—have
the same color. In the initial state we have two cans of paint, but the colors of the paint and
the furniture are unknown. Only the table is initially in the agent’s ﬁeld of view:
Init(Object(Table)∧Object(Chair)∧Can(C1)∧Can(C2)∧InView(Table))
Goal(Color(Chair,c)∧Color(Table,c))
There are two actions: removing the lid from a paint can and painting an object using the
paint from an open can.
Action(RemoveLid(can),
PRECOND:Can(can)
EFFECT:Open(can))
Action(Paint(x,can),
PRECOND:Object(x)∧Can(can)∧Color(can,c)∧Open(can)
EFFECT:Color(x,c))
