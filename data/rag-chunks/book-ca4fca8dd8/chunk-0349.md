---
chunk_id: "book-ca4fca8dd8-chunk-0349"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 349
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 6.6
Partially Observable Games
215
opening move. Keeping track of the belief state as the game progresses is exactly the prob-
lem of state estimation, for which the update step is given in Equation (4.6) on page 150. We
can map Kriegspiel state estimation directly onto the partially observable, nondeterministic
framework of Section 4.4 if we consider the opponent as the source of nondeterminism; that
is, the RESULTS of White’s move are composed from the (predictable) outcome of White’s
own move and the unpredictable outcome given by Black’s reply.4
Given a current belief state, White may ask, “Can I win the game?” For a partially
observable game, the notion of a strategy is altered; instead of specifying a move to make
for each possible move the opponent might make, we need a move for every possible percept
sequence that might be received.
For Kriegspiel, a winning strategy, or guaranteed checkmate, is one that, for each possi-
Guaranteed
checkmate
ble percept sequence, leads to an actual checkmate for every possible board state in the current
belief state, regardless of how the opponent moves. With this deﬁnition, the opponent’s belief
state is irrelevant—the strategy has to work even if the opponent can see all the pieces. This
greatly simpliﬁes the computation. Figure 6.15 shows part of a guaranteed checkmate for the
KRK (king and rook versus king) endgame. In this case, Black has just one piece (the king),
so a belief state for White can be shown in a single board by marking each possible position
of the Black king.
The general AND-OR search algorithm can be applied to the belief-state space to ﬁnd
guaranteed checkmates, just as in Section 4.4. The incremental belief-state algorithm men-
tioned in Section 4.4.2 often ﬁnds midgame checkmates up to depth 9—well beyond the
abilities of most human players.
In addition to guaranteed checkmates, Kriegspiel admits an entirely new concept that
makes no sense in fully observable games: probabilistic checkmate. Such checkmates are
Probabilistic
checkmate
still required to work in every board state in the belief state; they are probabilistic with respect
to randomization of the winning player’s moves. To get the basic idea, consider the problem
of ﬁnding a lone black king using just the white king. Simply by moving randomly, the
white king will eventually bump into the black king even if the latter tries to avoid this fate,
since Black cannot keep guessing the right evasive moves indeﬁnitely. In the terminology of
probability theory, detection occurs with probability 1.
The KBNK endgame—king, bishop and knight versus king—is won in this sense; White
presents Black with an inﬁnite random sequence of choices, for one of which Black will guess
incorrectly and reveal his position, leading to checkmate. On the other hand, the KBBK
endgame is won with probability 1 −ϵ. White can force a win only by leaving one of his
bishops unprotected for one move. If Black happens to be in the right place and captures the
bishop (a move that would be illegal if the bishops are protected), the game is drawn. White
can choose to make the risky move at some randomly chosen point in the middle of a very
long sequence, thus reducing ϵ to an arbitrarily small constant, but cannot reduce ϵ to zero.
Sometimes a checkmate strategy works for some of the board states in the current belief
state but not others. Trying such a strategy may succeed, leading to an accidental check-
mate—accidental in the sense that White could not know that it would be checkmate—if
Accidental
checkmate
Black’s pieces happen to be in the right places. (Most checkmates in games between humans
4
Sometimes, the belief state will become too large to represent just as a list of board states, but we will ignore
this issue for now; Chapters 7 and 8 suggest methods for compactly representing very large belief states.
