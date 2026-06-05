---
chunk_id: "book-ca4fca8dd8-chunk-0298"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 298
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 5.5
The Structure of Problems
183
assignments, but bad weather at one airport can render the schedule infeasible. We would
like to repair the schedule with a minimum number of changes. This can be easily done with
a local search algorithm starting from the current schedule. A backtracking search with the
new set of constraints usually requires much more time and might ﬁnd a solution with many
changes from the current schedule.
5.5 The Structure of Problems
In this section, we examine ways in which the structure of the problem, as represented by
the constraint graph, can be used to ﬁnd solutions quickly. Most of the approaches here also
apply to other problems besides CSPs, such as probabilistic reasoning.
The only way we can possibly hope to deal with the vast real world is to decompose it into
subproblems. Looking again at the constraint graph for Australia (Figure 5.1(b), repeated as
Figure 5.12(a)), one fact stands out: Tasmania is not connected to the mainland.3 Intuitively,
it is obvious that coloring Tasmania and coloring the mainland are independent subprob-
lems—any solution for the mainland combined with any solution for Tasmania yields a solu-
Independent
subproblems
tion for the whole map.
Independence can be ascertained simply by ﬁnding connected components of the con-
Connected
component
straint graph. Each component corresponds to a subproblem CSPi. If assignment Si is a
solution of CSPi, then S
i Si is a solution of S
i CSPi. Why is this important? Suppose each
CSPi has c variables from the total of n variables, where c is a constant. Then there are n/c
subproblems, each of which takes at most dc work to solve, where d is the size of the domain.
Hence, the total work is O(dcn/c), which is linear in n; without the decomposition, the total
work is O(dn), which is exponential in n. Let’s make this more concrete: dividing a Boolean
CSP with 100 variables into four subproblems reduces the worst-case solution time from the
lifetime of the universe down to less than a second.
Completely independent subproblems are delicious, then, but rare. Fortunately, some
other graph structures are also easy to solve. For example, a constraint graph is a tree when
any two variables are connected by only one path. We will show that any tree-structured ◀
CSP can be solved in time linear in the number of variables.4 The key is a new notion of
consistency, called directional arc consistency or DAC. A CSP is deﬁned to be directional
Directional arc
consistency
arc-consistent under an ordering of variables X1,X2,...,Xn if and only if every Xi is arc-
consistent with each Xj for j > i.
To solve a tree-structured CSP, ﬁrst pick any variable to be the root of the tree, and choose
an ordering of the variables such that each variable appears after its parent in the tree. Such
an ordering is called a topological sort. Figure 5.10(a) shows a sample tree and (b) shows
Topological sort
one possible ordering. Any tree with n nodes has n −1 edges, so we can make this graph
directed arc-consistent in O(n) steps, each of which must compare up to d possible domain
values for two variables, for a total time of O(nd2). Once we have a directed arc-consistent
graph, we can just march down the list of variables and choose any remaining value. Since
each edge from a parent to its child is arc-consistent, we know that for any value we choose
for the parent, there will be a valid value left to choose for the child. That means we won’t
3
A careful cartographer or patriotic Tasmanian might object that Tasmania should not be colored the same as
its nearest mainland neighbor, to avoid the impression that it might be part of that state.
4
Sadly, very few regions of the world have tree-structured maps, although Sulawesi comes close.
