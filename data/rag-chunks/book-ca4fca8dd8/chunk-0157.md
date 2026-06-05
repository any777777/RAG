---
chunk_id: "book-ca4fca8dd8-chunk-0157"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 157
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 3.3
Search Algorithms
93
Figure 3.7 is a graph search algorithm; if we remove all references to reached we get a tree-
like search that uses less memory but will examine redundant paths to the same state, and
thus will run slower.
Third, we can compromise and check for cycles, but not for redundant paths in general.
Since each node has a chain of parent pointers, we can check for cycles with no need for
additional memory by following up the chain of parents to see if the state at the end of the
path has appeared earlier in the path. Some implementations follow this chain all the way
up, and thus eliminate all cycles; other implementations follow only a few links (e.g., to the
parent, grandparent, and great-grandparent), and thus take only a constant amount of time,
while eliminating all short cycles (and relying on other mechanisms to deal with long cycles).
3.3.4 Measuring problem-solving performance
Before we get into the design of various search algorithms, we will consider the criteria used
to choose among them. We can evaluate an algorithm’s performance in four ways:
• Completeness: Is the algorithm guaranteed to ﬁnd a solution when there is one, and to
Completeness
correctly report failure when there is not?
• Cost optimality: Does it ﬁnd a solution with the lowest path cost of all solutions?7
Cost optimality
• Time complexity: How long does it take to ﬁnd a solution? This can be measured in
Time complexity
seconds, or more abstractly by the number of states and actions considered.
• Space complexity: How much memory is needed to perform the search?
Space complexity
To understand completeness, consider a search problem with a single goal. That goal could be
anywhere in the state space; therefore a complete algorithm must be capable of systematically
exploring every state that is reachable from the initial state. In ﬁnite state spaces that is
straightforward to achieve: as long as we keep track of paths and cut off ones that are cycles
(e.g. Arad to Sibiu to Arad), eventually we will reach every reachable state.
In inﬁnite state spaces, more care is necessary. For example, an algorithm that repeatedly
applied the “factorial” operator in Knuth’s “4” problem would follow an inﬁnite path from 4
to 4! to (4!)!, and so on. Similarly, on an inﬁnite grid with no obstacles, repeatedly moving
forward in a straight line also follows an inﬁnite path of new states. In both cases the algo-
rithm never returns to a state it has reached before, but is incomplete because wide expanses
of the state space are never reached.
To be complete, a search algorithm must be systematic in the way it explores an inﬁnite
Systematic
state space, making sure it can eventually reach any state that is connected to the initial state.
For example, on the inﬁnite grid, one kind of systematic search is a spiral path that covers all
the cells that are s steps from the origin before moving out to cells that are s+1 steps away.
Unfortunately, in an inﬁnite state space with no solution, a sound algorithm needs to keep
searching forever; it can’t terminate because it can’t know if the next state will be a goal.
Time and space complexity are considered with respect to some measure of the problem
difﬁculty. In theoretical computer science, the typical measure is the size of the state-space
graph, |V| + |E|, where |V| is the number of vertices (state nodes) of the graph and |E| is
6
We say “tree-like search” because the state space is still the same graph no matter how we search it; we are
just choosing to treat it as if it were a tree, with only one path from each node back to the root.
7
Some authors use the term “admissibility” for the property of ﬁnding the lowest-cost solution, and some use
just “optimality,” but that can be confused with other types of optimality.
