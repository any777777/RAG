---
chunk_id: "book-ca4fca8dd8-chunk-0939"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 939
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.2
Algorithms for MDPs
569
–1
–1
–1
0.1
0.1
0.8
0.1
0.1
0.8
0.1
0.1
0.8
3,2
0.1
0.1
0.8
Up
Right
Down
Left
3,2
3,3
4,2
3,3
4,2
3,1
4,2
3,1
3,2
3,1
3,2
3,3
Figure 16.10 Part of an expectimax tree for the 4×3 MDP rooted at (3,2). The triangular
nodes are max modes and the circular nodes are chance nodes.
The most straightforward approach is actually a simpliﬁcation of the EXPECTIMINIMAX
algorithm for game trees with chance nodes: the EXPECTIMAX algorithm builds a tree of
alternating max and chance nodes, as illustrated in Figure 16.10. (There is a slight difference
from standard EXPECTIMINIMAX in that there are rewards on nonterminal as well as terminal
transitions.) An evaluation function can be applied to the nonterminal leaves of the tree, or
they can be given a default value. A decision can be extracted from the search tree by backing
up the utility values from the leaves, taking an average at the chance nodes and taking the
maximum at the decision nodes.
For problems in which the discount factor γ is not too close to 1, the ϵ-horizon is a useful
concept. Let ϵ be a desired bound on the absolute error in the utilities computed from an
expectimax tree of bounded depth, compared to the exact utilities in the MDP. Then the ϵ-
horizon is the tree depth H such that the sum of rewards beyond any leaf at that depth is less
than ϵ—roughly speaking, anything that happens after H is irrelevant because it’s so far in
the future. Because the sum of rewards beyond H is bounded by γHRmax/(1 −γ), a depth
of H =⌈logγ ϵ(1 −γ)/Rmax⌉sufﬁces. So, building a tree to this depth gives near-optimal
decisions. For example, with γ =0.5, ϵ=0.1, and Rmax =1, we ﬁnd H =5, which seems
reasonable. On the other hand, if γ =0.9, H =44, which seems less reasonable!
In addition to limiting the depth, it is also possible to avoid the potentially enormous
branching factor at the chance nodes. (For example, if all the conditional probabilities in
a DBN transition model are nonzero, the transition probabilities, which are given by the
product of the conditional probabilities, are also nonzero, meaning that every state has some
probability of transitioning to every other state.)
As noted in Section 13.4, expectations with respect to a probability distribution P can be
approximated by generating N samples from P and using the sample mean. In mathematical
form, we have
∑
x
P(x)f(x) ≈1
N
N
∑
i=1
f(xi).
So, if the branching factor is very large, meaning that there are very many possible x values, a
good approximation to the value of the chance node can be obtained by sampling a bounded
