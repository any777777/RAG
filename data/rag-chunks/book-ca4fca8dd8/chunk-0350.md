---
chunk_id: "book-ca4fca8dd8-chunk-0350"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 350
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 216

216
Chapter 6
Adversarial Search and Games
a
1
2
3
4
d
b
c
Kc3 ?
“Illegal”
“OK”
Rc3 ?
“OK”
“Check”
Figure 6.15 Part of a guaranteed checkmate in the KRK endgame, shown on a reduced
board. In the initial belief state, Black’s king is in one of three possible locations. By a
combination of probing moves, the strategy narrows this down to one. Completion of the
checkmate is left as an exercise.
are of this accidental nature.) This idea leads naturally to the question of how likely it is that a
given strategy will win, which leads in turn to the question of how likely it is that each board
state in the current belief state is the true board state.
One’s ﬁrst inclination might be to propose that all board states in the current belief state
are equally likely—but this can’t be right. Consider, for example, White’s belief state after
Black’s ﬁrst move of the game. By deﬁnition (assuming that Black plays optimally), Black
must have played an optimal move, so all board states resulting from suboptimal moves ought
to be assigned zero probability.
This argument is not quite right either, because each player’s goal is not just to move
▶
pieces to the right squares but also to minimize the information that the opponent has about
their location. Playing any predictable “optimal” strategy provides the opponent with in-
formation. Hence, optimal play in partially observable games requires a willingness to play
somewhat randomly. (This is why restaurant hygiene inspectors do random inspection visits.)
This means occasionally selecting moves that may seem “intrinsically” weak—but they gain
strength from their very unpredictability, because the opponent is unlikely to have prepared
any defense against them.

## Page 217
