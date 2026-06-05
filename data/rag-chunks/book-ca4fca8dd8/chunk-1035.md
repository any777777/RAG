---
chunk_id: "book-ca4fca8dd8-chunk-1035"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1035
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.3
Cooperative Game Theory
621
{1}, {2}, {3}, {4}
{1}, {2}, {3, 4}
{1}, {2, 3, 4}
{1, 2}, {3, 4}
{2}, {1, 3, 4}
{1, 3}, {2, 4}
{1, 2, 3, 4}
{3},{1, 2, 4}
{1, 4},{ 2, 3}
{4},{1, 2, 3}
{1, 2}, {3}, {4}
{1}, {3}, {2, 4}
{2}, {4}, {1, 3}
{2}, {3}, {1, 4}
level 1
level 2
level 3
level 4
{1}, {4}, {2, 3}
Figure 17.7 The coalition structure graph for N = {1,2,3,4}. Level 1 has coalition struc-
tures containing a single coalition; level 2 has coalition structures containing two coalitions,
and so on.
This scheme is a complete representation—in the worst case, we need a rule for every pos-
sible coalition. Moreover, the Shapley value can be computed in polynomial time with this
scheme; the details are more involved than for the simple rules described above, although the
basic principle is the same; see the notes at the end of the chapter for references.
Coalition structures for maximum social welfare
We obtain a different perspective on cooperative games if we assume that the agents share
a common purpose. For example, if we think of the agents as being workers in a company,
then the strategic considerations relating to coalition formation that are addressed by the core,
for example, are not relevant. Instead, we might want to organize the workforce (the agents)
into teams so as to maximize their overall productivity. More generally, the task is to ﬁnd a
coalition that maximizes the social welfare of the system, deﬁned as the sum of the values of
the individual coalitions. We write the social welfare of a coalition structure CS as sw(CS),
with the following deﬁnition:
sw(CS) = ∑
C∈CS
ν(C).
Then a socially optimal coalition structure CS∗with respect to G maximizes this quantity.
Finding a socially optimal coalition structure is a very natural computational problem, which
has been studied beyond the multiagent systems community: it is sometimes called the set
partitioning problem. Unfortunately, the problem is NP-hard, because the number of possi-
Set partitioning
problem
ble coalition structures grows exponentially in the number of players.
Finding the optimal coalition structure by naive exhaustive search is therefore infeasible
in general. An inﬂuential approach to optimal coalition structure formation is based on the
idea of searching a subspace of the coalition structure graph. The idea is best explained
Coalition structure
graph
with reference to an example.
Suppose we have a game with four agents, N = {1,2,3,4}. There are ﬁfteen possible
coalition structures for this set of agents. We can organize these into a coalition structure
graph as shown in Figure 17.7, where the nodes at level ℓof the graph correspond to all
the coalition structures with exactly ℓcoalitions. An upward edge in the graph represents
the division of a coalition in the lower node into two separate coalitions in the upper node.
