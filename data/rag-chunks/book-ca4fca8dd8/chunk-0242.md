---
chunk_id: "book-ca4fca8dd8-chunk-0242"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 242
confidence: "first-pass"
extraction_method: "structured-local"
---

148
Chapter 4
Search in Complex Environments
belief state, consisting of the ﬁrst few states examined, is also unsolvable. In some cases, this
leads to a speedup proportional to the size of the belief states, which may themselves be as
large as the physical state space itself.
4.4.2 Searching in partially observable environments
Many problems cannot be solved without sensing. For example, the sensorless 8-puzzle is
impossible. On the other hand, a little bit of sensing can go a long way: we can solve 8-
puzzles if we can see just the upper-left corner square. The solution involves moving each
tile in turn into the observable square and keeping track of its location from then on.
For a partially observable problem, the problem speciﬁcation will specify a PERCEPT(s)
function that returns the percept received by the agent in a given state. If sensing is non-
deterministic, then we can use a PERCEPTS function that returns a set of possible percepts.
For fully observable problems, PERCEPT(s)=s for every state s, and for sensorless problems
PERCEPT(s)=null.
Consider a local-sensing vacuum world, in which the agent has a position sensor that
yields the percept L in the left square, and R in the right square, and a dirt sensor that yields
Dirty when the current square is dirty and Clean when it is clean. Thus, the PERCEPT in state
1 is [L,Dirty]. With partial observability, it will usually be the case that several states produce
the same percept; state 3 will also produce [L,Dirty]. Hence, given this initial percept, the
initial belief state will be {1,3}. We can think of the transition model between belief states
for partially observable problems as occurring in three stages, as shown in Figure 4.15:
• The prediction stage computes the belief state resulting from the action, RESULT(b,a),
exactly as we did with sensorless problems. To emphasize that this is a prediction, we
use the notation ˆb=RESULT(b,a), where the “hat” over the b means “estimated,” and
we also use PREDICT(b,a) as a synonym for RESULT(b,a).
• The possible percepts stage computes the set of percepts that could be observed in the
predicted belief state (using the letter o for observation):
POSSIBLE-PERCEPTS(ˆb) = {o : o=PERCEPT(s) and s ∈ˆb}.
• The update stage computes, for each possible percept, the belief state that would result
from the percept. The updated belief state bo is the set of states in ˆb that could have
produced the percept:
bo = UPDATE(ˆb,o) = {s : o=PERCEPT(s) and s ∈ˆb}.
The agent needs to deal with possible percepts at planning time, because it won’t know
the actual percepts until it executes the plan. Notice that nondeterminism in the phys-
ical environment can enlarge the belief state in the prediction stage, but each updated
belief state bo can be no larger than the predicted belief state ˆb; observations can only
help reduce uncertainty. Moreover, for deterministic sensing, the belief states for the
different possible percepts will be disjoint, forming a partition of the original predicted
belief state.
Putting these three stages together, we obtain the possible belief states resulting from a given
action and the subsequent possible percepts:
RESULTS(b,a) = {bo : bo = UPDATE(PREDICT(b,a),o) and
o ∈POSSIBLE-PERCEPTS(PREDICT(b,a))}.
(4.5)
