---
chunk_id: "book-ca4fca8dd8-chunk-0332"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 332
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 6.3
Heuristic Alpha–Beta Tree Search
205
a     b    c    d    e     f     g    h
8 
7 
6 
5 
4 
3 
2 
1
Figure 6.9 The horizon effect. With Black to move, the black bishop is surely doomed. But
Black can forestall that event by checking the white king with its pawns, encouraging the
king to capture the pawns. This pushes the inevitable loss of the bishop over the horizon, and
thus the pawn sacriﬁces are seen by the search algorithm as good moves rather than bad ones.
pawns, when actually all it has done is waste pawns and push the inevitable capture of the
bishop beyond the horizon that Black can see.
One strategy to mitigate the horizon effect is to allow singular extensions, moves that
Singular extension
are “clearly better” than all other moves in a given position, even when the search would
normally be cut off at that point. In our example, a search will have revealed that three moves
of the white rook—h2 to h1, then h1 to a1, and then a1 capturing the bishop on a2—are each
in turn clearly better moves, so even if a sequence of pawn moves pushes us to the horizon,
these clearly better moves will be given a chance to extend the search. This makes the tree
deeper, but because there are usually few singular extensions, the strategy does not add many
total nodes to the tree, and has proven to be effective in practice.
6.3.3 Forward pruning
Alpha–beta pruning prunes branches of the tree that can have no effect on the ﬁnal evaluation,
but forward pruning prunes moves that appear to be poor moves, but might possibly be good
Forward pruning
ones. Thus, the strategy saves computation time at the risk of making an error. In Shannon’s
terms, this is a Type B strategy. Clearly, most human chess players do this, considering only
a few moves from each position (at least consciously).
One approach to forward pruning is beam search (see page 133): on each ply, consider
only a “beam” of the n best moves (according to the evaluation function) rather than consid-
ering all possible moves. Unfortunately, this approach is rather dangerous because there is no
guarantee that the best move will not be pruned away.
The PROBCUT, or probabilistic cut, algorithm (Buro, 1995) is a forward-pruning version
of alpha–beta search that uses statistics gained from prior experience to lessen the chance that
the best move will be pruned. Alpha–beta search prunes any node that is provably outside
the current (α,β) window. PROBCUT also prunes nodes that are probably outside the win-
dow. It computes this probability by doing a shallow search to compute the backed-up value
