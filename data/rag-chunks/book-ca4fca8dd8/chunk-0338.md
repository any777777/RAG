---
chunk_id: "book-ca4fca8dd8-chunk-0338"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 338
confidence: "first-pass"
extraction_method: "structured-local"
---

208
Chapter 6
Adversarial Search and Games
exploration/exploitation tradeoff.) Monte Carlo tree search does that by maintaining a search
tree and growing it on each iteration of the following four steps, as shown in Figure 6.10:
• Selection: Starting at the root of the search tree, we choose a move (guided by the
selection policy), leading to a successor node, and repeat that process, moving down
the tree to a leaf. Figure 6.10(a) shows a search tree with the root representing a state
where white has just moved, and white has won 37 out of the 100 playouts done so
far. The thick arrow shows the selection of a move by black that leads to a node where
black has won 60/79 playouts. This is the best win percentage among the three moves,
so selecting it is an example of exploitation. But it would also have been reasonable
to select the 2/11 node for the sake of exploration—with only 11 playouts, the node
still has high uncertainty in its valuation, and might end up being best if we gain more
information about it. Selection continues on to the leaf node marked 27/35.
• Expansion: We grow the search tree by generating a new child of the selected node;
Figure 6.10(b) shows the new node marked with 0/0. (Some versions generate more
than one child in this step.)
• Simulation: We perform a playout from the newly generated child node, choosing
moves for both players according to the playout policy. These moves are not recorded
in the search tree. In the ﬁgure, the simulation results in a win for black.
• Back-propagation: We now use the result of the simulation to update all the search tree
nodes going up to the root. Since black won the playout, black nodes are incremented
in both the number of wins and the number of playouts, so 27/35 becomes 28/36 and
60/79 becomes 61/80. Since white lost, the white nodes are incremented in the number
of playouts only, so 16/53 becomes 16/54 and the root 37/100 becomes 37/101.
0/1
28/36
10/18
0/3
0/3
3/4
6/6
16/54
3/26
61/80
1/10
37/101
2/11
10/18
3/26
16/53
60/79
37/100
1/10
2/11
6/6
3/4
0/3
0/3
27/35
37/100
60/79
1/10
2/11
3/4
6/6
16/53
3/26
27/35
10/18
0/3
0/3
0/0
(a) Selection
(b) Expansion
and simulation
(c) Backpropagation
black wins
Figure 6.10 One iteration of the process of choosing a move with Monte Carlo tree search
(MCTS) using the upper conﬁdence bounds applied to trees (UCT) selection metric, shown
after 100 iterations have already been done. In (a) we select moves, all the way down the
tree, ending at the leaf node marked 27/35 (for 27 wins for black out of 35 playouts). In (b)
we expand the selected node and do a simulation (playout), which ends in a win for black. In
(c), the results of the simulation are back-propagated up the tree.
