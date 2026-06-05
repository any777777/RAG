---
chunk_id: "book-ca4fca8dd8-chunk-0937"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 937
confidence: "first-pass"
extraction_method: "structured-local"
---

568
Chapter 16
Making Complex Decisions
and this is repeated several times to efﬁciently produce the next utility estimate. The resulting
algorithm is called modiﬁed policy iteration.
Modiﬁed policy
iteration
The algorithms we have described so far require updating the utility or policy for all states
at once. It turns out that this is not strictly necessary. In fact, on each iteration, we can pick
any subset of states and apply either kind of updating (policy improvement or simpliﬁed value
iteration) to that subset. This very general algorithm is called asynchronous policy iteration.
Asynchronous policy
iteration
Given certain conditions on the initial policy and initial utility function, asynchronous policy
iteration is guaranteed to converge to an optimal policy. The freedom to choose any states to
work on means that we can design much more efﬁcient heuristic algorithms—for example,
algorithms that concentrate on updating the values of states that are likely to be reached by a
good policy. There’s no sense planning for the results of an action you will never do.
16.2.3 Linear programming
Linear programming or LP, which was mentioned brieﬂy in Chapter 4 (page 139), is a
general approach for formulating constrained optimization problems, and there are many
industrial-strength LP solvers available. Given that the Bellman equations involve a lot of
sums and maxes, it is perhaps not surprising that solving an MDP can be reduced to solving
a suitably formulated linear program.
The basic idea of the formulation is to consider as variables in the LP the utilities U(s) of
each state s, noting that the utilities for an optimal policy are the highest utilities attainable that
are consistent with the Bellman equations. In LP language, that means we seek to minimize
U(s) for all s subject to the inequalities
U(s) ≥∑
s′
P(s′ |s,a)[R(s,a,s′)+γU(s′)]
for every state s and every action a.
This creates a connection from dynamic programming to linear programming, for which
algorithms and complexity issues have been studied in great depth. For example, from the
fact that linear programming is solvable in polynomial time, one can show that MDPs can
be solved in time polynomial in the number of states and actions and the number of bits
required to specify the model. In practice, it turns out that LP solvers are seldom as efﬁcient
as dynamic programming for solving MDPs. Moreover, polynomial time may sound good,
but the number of states is often very large. Finally, it’s worth remembering that even the
simplest and most uninformed of the search algorithms in Chapter 3 runs in linear time in the
number of states and actions.
16.2.4 Online algorithms for MDPs
Value iteration and policy iteration are ofﬂine algorithms: like the A∗algorithm in Chapter 3,
they generate an optimal solution for the problem, which can then be executed by a simple
agent. For sufﬁciently large MDPs, such as the Tetris MDP with 1062 states, exact ofﬂine
solution, even by a polynomial-time algorithm, is not possible. Several techniques have been
developed for approximate ofﬂine solution of MDPs; these are covered in the notes at the end
of the chapter and in Chapter 23 (Reinforcement Learning).
Here we will consider online algorithms, analogous to those used for game playing in
Chapter 6, where the agent does a signiﬁcant amount of computation at each decision point
rather than operating primarily with precomputed information.
