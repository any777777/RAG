---
chunk_id: "book-ca4fca8dd8-chunk-0328"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 328
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 6.3
Heuristic Alpha–Beta Tree Search
203
(b) White to move
(a) White to move
Figure 6.8 Two chess positions that differ only in the position of the rook at lower right.
In (a), Black has an advantage of a knight and two pawns, which should be enough to win
the game. In (b), White will capture the queen, giving it an advantage that should be strong
enough to win.
centuries, chess players have developed ways of judging the value of a position using just this
idea. For example, introductory chess books give an approximate material value for each
Material value
piece: each pawn is worth 1, a knight or bishop is worth 3, a rook 5, and the queen 9. Other
features such as “good pawn structure” and “king safety” might be worth half a pawn, say.
These feature values are then simply added up to obtain the evaluation of the position.
Mathematically, this kind of evaluation function is called a weighted linear function
Weighted linear
function
because it can be expressed as
EVAL(s) = w1 f1(s)+w2 f2(s)+···+wn fn(s) =
n
∑
i=1
wi fi(s),
where each fi is a feature of the position (such as “number of white bishops”) and each wi is
a weight (saying how important that feature is). The weights should be normalized so that the
sum is always within the range of a loss (0) to a win (+1). A secure advantage equivalent to
a pawn gives a substantial likelihood of winning, and a secure advantage equivalent to three
pawns should give almost certain victory, as illustrated in Figure 6.8(a). We said that the
evaluation function should be strongly correlated with the actual chances of winning, but it
need not be linearly correlated: if state s is twice as likely to win as state s′ we don’t require
that EVAL(S) be twice EVAL(S’); all we require is that EVAL(S) > EVAL(S’).
Adding up the values of features seems like a reasonable thing to do, but in fact it involves
a strong assumption: that the contribution of each feature is independent of the values of the
other features. For this reason, current programs for chess and other games also use nonlinear
combinations of features. For example, a pair of bishops might be worth more than twice the
value of a single bishop, and a bishop is worth more in the endgame than earlier—when the
move number feature is high or the number of remaining pieces feature is low.
Where do the features and weights come from? They’re not part of the rules of chess,
but they are part of the culture of human chess-playing experience. In games where this
