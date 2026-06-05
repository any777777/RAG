---
chunk_id: "book-ca4fca8dd8-chunk-0340"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 340
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 6.4
Monte Carlo Tree Search
209
function MONTE-CARLO-TREE-SEARCH(state) returns an action
tree←NODE(state)
while IS-TIME-REMAINING() do
leaf ←SELECT(tree)
child←EXPAND(leaf)
result←SIMULATE(child)
BACK-PROPAGATE(result, child)
return the move in ACTIONS(state) whose node has highest number of playouts
Figure 6.11 The Monte Carlo tree search algorithm. A game tree, tree, is initialized, and
then we repeat a cycle of SELECT / EXPAND / SIMULATE / BACK-PROPAGATE until we run
out of time, and return the move that led to the node with the highest number of playouts.
We repeat these four steps either for a set number of iterations, or until the allotted time has
expired, and then return the move with the highest number of playouts.
One very effective selection policy is called “upper conﬁdence bounds applied to trees”
or UCT. The policy ranks each possible move based on an upper conﬁdence bound formula
UCT
called UCB1. (See Section 16.3.3 for more details.) For a node n, the formula is:
UCB1
UCB1(n)= U(n)
N(n) +C ×
s
logN(PARENT(n))
N(n)
where U(n) is the total utility of all playouts that went through node n, N(n) is the number of
playouts through node n, and PARENT(n) is the parent node of n in the tree. Thus U(n)
N(n) is the
exploitation term: the average utility of n. The term with the square root is the exploration
term: it has the count N(n) in the denominator, which means the term will be high for nodes
that have only been explored a few times. In the numerator it has the log of the number of
times we have explored the parent of n. This means that if we are selecting n some non-
zero percentage of the time, the exploration term goes to zero as the counts increase, and
eventually the playouts are given to the node with highest average utility.
C is a constant that balances exploitation and exploration. There is a theoretical argument
that C should be
√
2, but in practice, game programmers try multiple values for C and choose
the one that performs best. (Some programs use slightly different formulas; for example,
ALPHAZERO adds in a term for move probability, which is calculated by a neural network
trained from past self-play.) With C=1.4, the 60/79 node in Figure 6.10 has the highest
UCB1 score, but with C=1.5, it would be the 2/11 node.
Figure 6.11 shows the complete UCT MCTS algorithm. When the iterations terminate,
the move with the highest number of playouts is returned. You might think that it would
be better to return the node with the highest average utility, but the idea is that a node with
65/100 wins is better than one with 2/3 wins, because the latter has a lot of uncertainty. In any
event, the UCB1 formula ensures that the node with the most playouts is almost always the
node with the highest win percentage, because the selection process favors win percentage
more and more as the number of playouts goes up.
The time to compute a playout is linear, not exponential, in the depth of the game tree,
because only one move is taken at each choice point. That gives us plenty of time for multiple
