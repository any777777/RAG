---
chunk_id: "book-ca4fca8dd8-chunk-0254"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 254
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 4.5
Online Search Agents and Unknown Environments
157
1
2
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
2
2
3
4
4
4
3
3
3
1
1
1
1
1
1
1
3
1
1
1
1
1
1
1
5
3
5
5
4
(a)
(b)
(c)
(d)
(e)
8
9
8
9
8
9
8
9
8
9
4
4
3
4
Figure 4.23 Five iterations of LRTA∗on a one-dimensional state space. Each state is labeled
with H(s), the current cost estimate to reach a goal, and every link has an action cost of 1.
The red state marks the location of the agent, and the updated cost estimates at each iteration
have a double circle.
Augmenting hill climbing with memory rather than randomness turns out to be a more
effective approach. The basic idea is to store a “current best estimate” H(s) of the cost to
reach the goal from each state that has been visited. H(s) starts out being just the heuristic
estimate h(s) and is updated as the agent gains experience in the state space.
Figure 4.23 shows a simple example in a one-dimensional state space. In (a), the agent
seems to be stuck in a ﬂat local minimum at the red state. Rather than staying where it is, the
agent should follow what seems to be the best path to the goal given the current cost estimates
for its neighbors. The estimated cost to reach the goal through a neighbor s′ is the cost to get
to s′ plus the estimated cost to get to a goal from there—that is, c(s,a,s′) + H(s′). In the
example, there are two actions, with estimated costs 1+9 to the left and 1+2 to the right, so
it seems best to move right.
In (b) it is clear that the cost estimate of 2 for the red state in (a) was overly optimistic.
Since the best move cost 1 and led to a state that is at least 2 steps from a goal, the red
state must be at least 3 steps from a goal, so its H should be updated accordingly, as shown
in Figure 4.23(b). Continuing this process, the agent will move back and forth twice more,
updating H each time and “ﬂattening out” the local minimum until it escapes to the right.
An agent implementing this scheme, which is called learning real-time A∗(LRTA∗), is
LRTA∗
shown in Figure 4.24. Like ONLINE-DFS-AGENT, it builds a map of the environment in
the result table. It updates the cost estimate for the state it has just left and then chooses the
“apparently best” move according to its current cost estimates. One important detail is that
actions that have not yet been tried in a state s are always assumed to lead immediately to the
goal with the least possible cost, namely h(s). This optimism under uncertainty encourages
Optimism under
uncertainty
the agent to explore new, possibly promising paths.
