---
chunk_id: "book-ca4fca8dd8-chunk-0611"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 611
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.3
Heuristics for Planning
371
11.3 Heuristics for Planning
Neither forward nor backward search is efﬁcient without a good heuristic function. Recall
from Chapter 3 that a heuristic function h(s) estimates the distance from a state s to the
goal, and that if we can derive an admissible heuristic for this distance—one that does not
overestimate—then we can use A∗search to ﬁnd optimal solutions.
By deﬁnition, there is no way to analyze an atomic state, and thus it requires some in-
genuity by an analyst (usually human) to deﬁne good domain-speciﬁc heuristics for search
problems with atomic states. But planning uses a factored representation for states and ac-
tions, which makes it possible to deﬁne good domain-independent heuristics.
Recall that an admissible heuristic can be derived by deﬁning a relaxed problem that is
easier to solve. The exact cost of a solution to this easier problem then becomes the heuristic
for the original problem. A search problem is a graph where the nodes are states and the
edges are actions. The problem is to ﬁnd a path connecting the initial state to a goal state.
There are two main ways we can relax this problem to make it easier: by adding more edges
to the graph, making it strictly easier to ﬁnd a path, or by grouping multiple nodes together,
forming an abstraction of the state space that has fewer states, and thus is easier to search.
We look ﬁrst at heuristics that add edges to the graph. Perhaps the simplest is the ignore-
preconditions heuristic, which drops all preconditions from actions. Every action becomes
Ignore-preconditions
heuristic
applicable in every state, and any single goal ﬂuent can be achieved in one step (if there
are any applicable actions—if not, the problem is impossible). This almost implies that the
number of steps required to solve the relaxed problem is the number of unsatisﬁed goals—
almost but not quite, because (1) some action may achieve multiple goals and (2) some actions
may undo the effects of others.
For many problems an accurate heuristic is obtained by considering (1) and ignoring (2).
First, we relax the actions by removing all preconditions and all effects except those that are
literals in the goal. Then, we count the minimum number of actions required such that the
union of those actions’ effects satisﬁes the goal. This is an instance of the set-cover problem.
Set-cover problem
There is one minor irritation: the set-cover problem is NP-hard. Fortunately a simple greedy
algorithm is guaranteed to return a set covering whose size is within a factor of logn of the
true minimum covering, where n is the number of literals in the goal. Unfortunately, the
greedy algorithm loses the guarantee of admissibility.
It is also possible to ignore only selected preconditions of actions. Consider the sliding-
tile puzzle (8-puzzle or 15-puzzle) from Section 3.2. We could encode this as a planning
problem involving tiles with a single schema Slide:
Action(Slide(t,s1,s2),
PRECOND:On(t,s1)∧Tile(t)∧Blank(s2)∧Adjacent(s1,s2)
EFFECT:On(t,s2)∧Blank(s1)∧¬On(t,s1)∧¬Blank(s2))
As we saw in Section 3.6, if we remove the preconditions Blank(s2) ∧Adjacent(s1,s2) then
any tile can move in one action to any space and we get the number-of-misplaced-tiles heuris-
tic. If we remove only the Blank(s2) precondition then we get the Manhattan-distance heuris-
tic. It is easy to see how these heuristics could be derived automatically from the action
schema description. The ease of manipulating the action schemas is the great advantage of
the factored representation of planning problems, as compared with the atomic representation
of search problems.
