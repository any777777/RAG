---
chunk_id: "book-ca4fca8dd8-chunk-0941"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 941
confidence: "first-pass"
extraction_method: "structured-local"
---

570
Chapter 16
Making Complex Decisions
-0.3
-0.2
-0.1
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0
 20
 40
 60
 80  100  120  140  160
Average total reward
Number of playouts
Figure 16.11 Performance of UCT as a function of the number of playouts per move for the
4×3 world using a random playout policy, averaged over 1000 runs per data point.
number of outcomes from the action. Typically, the samples will focus on the most likely
outcomes because those are most likely to be generated.
If you look closely at the tree in Figure 16.10, you will notice something: it isn’t really
a tree. For example, the root (3,2) is also a leaf, so one ought to consider this as a graph,
and one ought to constrain the value of the leaf (3,2) to be the same as the value of the root
(3,2), since they are the same state. In fact, this line of thinking quickly brings us back to
the Bellman equations that relate the values of states to the values of neighboring states. The
explored states actually constitute a sub-MDP of the original MDP, and this sub-MDP can
be solved using any of the algorithms in this chapter to yield a decision for the current state.
(Frontier states are typically given a ﬁxed estimated value.)
This general approach is called real-time dynamic programming (RTDP) and is quite
Real-time dynamic
programming
(RTDP)
analogous to LRTA∗in Chapter 4. Algorithms of this kind can be quite effective in moderate-
sized domains such as grid worlds; in larger domains such as Tetris, there are two issues.
First, the state space is such that any manageable set of explored states contains very few
repeated states, so one might as well use a simple expectimax tree. Second, a simple heuristic
for frontier nodes may not be enough to guide the agent, particularly if rewards are sparse.
One possible ﬁx is to apply reinforcement learning to generate a much more accurate
heuristic (see Chapter 23). Another approach is to look further ahead in the MDP using the
Monte Carlo approach of Section 6.4. In fact, the UCT algorithm from Figure 6.10 was
developed originally for MDPs rather than games. The changes required to solve MDPs
rather than games are minimal: they arise primarily from the fact that the opponent (nature)
is stochastic and from the need to keep track of rewards rather than just wins and losses.
When applied to the 4×3 world, the performance of UCT is not especially impres-
sive. As Figure 16.11 shows, it takes 160 playouts on average to reach a total reward of
0.4, whereas an optimal policy has an expected total reward of 0.7453 from the initial state
(see Figure 16.3). One reason UCT can have difﬁculty is that is builds a tree rather than a
graph and uses (an approximation to) expectimax rather than dynamic programming. The
4×3 world is very “loopy”: although there are only 9 nonterminal states, UCT’s playouts
often continue for more than 50 actions.
