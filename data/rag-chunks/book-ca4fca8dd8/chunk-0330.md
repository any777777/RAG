---
chunk_id: "book-ca4fca8dd8-chunk-0330"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 330
confidence: "first-pass"
extraction_method: "structured-local"
---

204
Chapter 6
Adversarial Search and Games
kind of experience is not available, the weights of the evaluation function can be estimated
by the machine learning techniques of Chapter 23. Applying these techniques to chess has
conﬁrmed that a bishop is indeed worth about three pawns, and it appears that centuries of
human experience can be replicated in just a few hours of machine learning.
6.3.2 Cutting oﬀsearch
The next step is to modify ALPHA-BETA-SEARCH so that it will call the heuristic EVAL
function when it is appropriate to cut off the search. We replace the two lines in Figure 6.7
that mention IS-TERMINAL with the following line:
if game.IS-CUTOFF(state, depth) then return game.EVAL(state, player), null
We also must arrange for some bookkeeping so that the current depth is incremented on each
recursive call. The most straightforward approach to controlling the amount of search is to
set a ﬁxed depth limit so that IS-CUTOFF(state, depth) returns true for all depth greater than
some ﬁxed depth d (as well as for all terminal states). The depth d is chosen so that a move
is selected within the allocated time. A more robust approach is to apply iterative deepening.
(See Chapter 3.) When time runs out, the program returns the move selected by the deepest
completed search. As a bonus, if in each round of iterative deepening we keep entries in
the transposition table, subsequent rounds will be faster, and we can use the evaluations to
improve move ordering.
These simple approaches can lead to errors due to the approximate nature of the eval-
uation function. Consider again the simple evaluation function for chess based on material
advantage. Suppose the program searches to the depth limit, reaching the position in Fig-
ure 6.8(b), where Black is ahead by a knight and two pawns. It would report this as the
heuristic value of the state, thereby declaring that the state is a probable win by Black. But
White’s next move captures Black’s queen with no compensation. Hence, the position is
actually favorable for White, but this can be seen only by looking ahead.
The evaluation function should be applied only to positions that are quiescent—that is,
Quiescence
positions in which there is no pending move (such as a capturing the queen) that would wildly
swing the evaluation. For nonquiescent positions the IS-CUTOFF returns false, and the search
continues until quiescent positions are reached. This extra quiescence search is sometimes
Quiescence search
restricted to consider only certain types of moves, such as capture moves, that will quickly
resolve the uncertainties in the position.
The horizon effect is more difﬁcult to eliminate. It arises when the program is facing
Horizon eﬀect
an opponent’s move that causes serious damage and is ultimately unavoidable, but can be
temporarily avoided by the use of delaying tactics. Consider the chess position in Figure 6.9.
It is clear that there is no way for the black bishop to escape. For example, the white rook can
capture it by moving to h1, then a1, then a2; a capture at depth 6 ply.
But Black does have a sequence of moves that pushes the capture of the bishop “over
the horizon.” Suppose Black searches to depth 8 ply. Most moves by Black will lead to the
eventual capture of the bishop, and thus will be marked as “bad” moves. But Black will also
consider the sequence of moves that starts by checking the king with a pawn, and enticing the
king to capture the pawn. Black can then do the same thing with a second pawn. That takes
up enough moves that the capture of the bishop would not be discovered during the remainder
of Black’s search. Black thinks that the line of play has saved the bishop at the price of two
