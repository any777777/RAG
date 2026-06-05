---
chunk_id: "book-ca4fca8dd8-chunk-0347"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 347
confidence: "first-pass"
extraction_method: "structured-local"
---

214
Chapter 6
Adversarial Search and Games
arrive at bounds for the average without looking at every number. For example, say that all
utility values are between −2 and +2; then the value of leaf nodes is bounded, and in turn we
can place an upper bound on the value of a chance node without looking at all its children.
In games where the branching factor for chance nodes is high—consider a game like
Yahtzee where you roll 5 dice on every turn—you may want to consider forward pruning that
samples a smaller number of the possible chance branches. Or you may want to avoid using
an evaluation function altogether, and opt for Monte Carlo tree search instead, where each
playout includes random dice rolls.
6.6 Partially Observable Games
Bobby Fischer declared that “chess is war,” but chess lacks at least one major characteristic
of real wars, namely, partial observability. In the “fog of war,” the whereabouts of enemy
units is often unknown until revealed by direct contact. As a result, warfare includes the use
of scouts and spies to gather information and the use of concealment and bluff to confuse the
enemy.
Partially observable games share these characteristics and are thus qualitatively different
from the games in the preceding sections. Video games such as StarCraft are particularly chal-
lenging, being partially observable, multi-agent, nondeterministic, dynamic, and unknown.
In deterministic partially observable games, uncertainty about the state of the board arises
entirely from lack of access to the choices made by the opponent. This class includes chil-
dren’s games such as Battleship (where each player’s ships are placed in locations hidden
from the opponent) and Stratego (where piece locations are known but piece types are hid-
den). We will examine the game of Kriegspiel, a partially observable variant of chess in
Kriegspiel
which pieces are completely invisible to the opponent. Other games also have partially ob-
servable versions: Phantom Go, Phantom tic-tac-toe, and Screen Shogi.
6.6.1 Kriegspiel: Partially observable chess
The rules of Kriegspiel are as follows: White and Black each see a board containing only
their own pieces. A referee, who can see all the pieces, adjudicates the game and periodically
makes announcements that are heard by both players. First, White proposes to the referee
a move that would be legal if there were no black pieces. If the black pieces prevent the
move, the referee announces “illegal,” and White keeps proposing moves until a legal one is
found—learning more about the location of Black’s pieces in the process.
Once a legal move is proposed, the referee announces one or more of the following:
“Capture on square X” if there is a capture, and “Check by D” if the black king is in check,
where D is the direction of the check, and can be one of “Knight,” “Rank,” “File,” “Long
diagonal,” or “Short diagonal.” If Black is checkmated or stalemated, the referee says so;
otherwise, it is Black’s turn to move.
Kriegspiel may seem terrifyingly impossible, but humans manage it quite well and com-
puter programs are beginning to catch up. It helps to recall the notion of a belief state as
deﬁned in Section 4.4 and illustrated in Figure 4.14—the set of all logically possible board
states given the complete history of percepts to date. Initially, White’s belief state is a sin-
gleton because Black’s pieces haven’t moved yet. After White makes a move and Black
responds, White’s belief state contains 20 positions, because Black has 20 replies to any
