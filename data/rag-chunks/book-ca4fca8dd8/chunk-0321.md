---
chunk_id: "book-ca4fca8dd8-chunk-0321"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 321
confidence: "first-pass"
extraction_method: "structured-local"
---

198
Chapter 6
Adversarial Search and Games
the immediate advantage of breaking an alliance against the long-term disadvantage of being
perceived as untrustworthy. See Section 17.2 for more on these complications.
If the game is not zero-sum, then collaboration can also occur with just two players.
Suppose, for example, that there is a terminal state with utilities ⟨vA =1000,vB =1000⟩and
that 1000 is the highest possible utility for each player. Then the optimal strategy is for both
players to do everything possible to reach this state—that is, the players will automatically
cooperate to achieve a mutually desirable goal.
6.2.3 Alpha–Beta Pruning
The number of game states is exponential in the depth of the tree. No algorithm can com-
pletely eliminate the exponent, but we can sometimes cut it in half, computing the correct
minimax decision without examining every state by pruning (see page 108) large parts of the
tree that make no difference to the outcome. The particular technique we examine is called
alpha–beta pruning.
Alpha–beta pruning
Consider again the two-ply game tree from Figure 6.2. Let’s go through the calculation
of the optimal decision once more, this time paying careful attention to what we know at
each point in the process. The steps are explained in Figure 6.5. The outcome is that we can
identify the minimax decision without ever evaluating two of the leaf nodes.
Another way to look at this is as a simpliﬁcation of the formula for MINIMAX. Let the
two unevaluated successors of node C in Figure 6.5 have values x and y. Then the value of
the root node is given by
MINIMAX(root) = max(min(3,12,8),min(2,x,y),min(14,5,2))
= max(3,min(2,x,y),2)
= max(3,z,2)
where z = min(2,x,y) ≤2
= 3.
In other words, the value of the root and hence the minimax decision are independent of the
values of the leaves x and y, and therefore they can be pruned.
Alpha–beta pruning can be applied to trees of any depth, and it is often possible to prune
entire subtrees rather than just leaves. The general principle is this: consider a node n some-
where in the tree (see Figure 6.6), such that Player has a choice of moving to n. If Player
has a better choice either at the same level (e.g. m′ in Figure 6.6) or at any point higher up
in the tree (e.g. m in Figure 6.6), then Player will never move to n. So once we have found
out enough about n (by examining some of its descendants) to reach this conclusion, we can
prune it.
Remember that minimax search is depth-ﬁrst, so at any one time we just have to consider
the nodes along a single path in the tree. Alpha–beta pruning gets its name from the two
extra parameters in MAX-VALUE(state,α,β) (see Figure 6.7) that describe bounds on the
backed-up values that appear anywhere along the path:
α = the value of the best (i.e., highest-value) choice we have found so far at any choice point
along the path for MAX. Think: α = “at least.”
β = the value of the best (i.e., lowest-value) choice we have found so far at any choice point
along the path for MIN. Think: β = “at most.”
