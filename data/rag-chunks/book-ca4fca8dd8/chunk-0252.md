---
chunk_id: "book-ca4fca8dd8-chunk-0252"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 252
confidence: "first-pass"
extraction_method: "structured-local"
---

156
Chapter 4
Search in Complex Environments
S
G
Figure 4.22 An environment in which a random walk will take exponentially many steps to
ﬁnd the goal.
of states under results[s,a].) Whenever the current state has unexplored actions, the agent tries
one of those actions. The difﬁculty comes when the agent has tried all the actions in a state.
In ofﬂine depth-ﬁrst search, the state is simply dropped from the queue; in an online search,
the agent has to backtrack in the physical world. In depth-ﬁrst search, this means going back
to the state from which the agent most recently entered the current state. To achieve that,
the algorithm keeps another table that lists, for each state, the predecessor states to which the
agent has not yet backtracked. If the agent has run out of states to which it can backtrack,
then its search is complete.
We recommend that the reader trace through the progress of ONLINE-DFS-AGENT when
applied to the maze given in Figure 4.19. It is fairly easy to see that the agent will, in the
worst case, end up traversing every link in the state space exactly twice. For exploration,
this is optimal; for ﬁnding a goal, on the other hand, the agent’s competitive ratio could be
arbitrarily bad if it goes off on a long excursion when there is a goal right next to the initial
state. An online variant of iterative deepening solves this problem; for an environment that is
a uniform tree, the competitive ratio of such an agent is a small constant.
Because of its method of backtracking, ONLINE-DFS-AGENT works only in state spaces
where the actions are reversible. There are slightly more complex algorithms that work in
general state spaces, but no such algorithm has a bounded competitive ratio.
4.5.3 Online local search
Like depth-ﬁrst search, hill-climbing search has the property of locality in its node expan-
sions. In fact, because it keeps just one current state in memory, hill-climbing search is
already an online search algorithm! Unfortunately, the basic algorithm is not very good for
exploration because it leaves the agent sitting at local maxima with nowhere to go. Moreover,
random restarts cannot be used, because the agent cannot teleport itself to a new start state.
Instead of random restarts, one might consider using a random walk to explore the en-
Random walk
vironment. A random walk simply selects at random one of the available actions from the
current state; preference can be given to actions that have not yet been tried. It is easy to prove
that a random walk will eventually ﬁnd a goal or complete its exploration, provided that the
space is ﬁnite and safely explorable.9 On the other hand, the process can be very slow. Fig-
ure 4.22 shows an environment in which a random walk will take exponentially many steps
to ﬁnd the goal, because, for each state in the top row except S, backward progress is twice as
likely as forward progress. The example is contrived, of course, but there are many real-world
state spaces whose topology causes these kinds of “traps” for random walks.
9
Random walks are complete on inﬁnite one-dimensional and two-dimensional grids. On a three-dimensional
grid, the probability that the walk ever returns to the starting point is only about 0.3405 (Hughes, 1995).
