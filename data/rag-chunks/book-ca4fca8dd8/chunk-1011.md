---
chunk_id: "book-ca4fca8dd8-chunk-1011"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1011
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.2
Non-Cooperative Game Theory
609
1,1
up
above
down
below
0,0
0,0
1
2
Figure 17.4 An extensive-form game with a counterintuitive Nash equilibrium.
of 0 for player 1; in this case, player 1 has no better alternative than choosing below. The
problem is that player 2’s threat (to play down) is not a credible threat, because if player 2
Credible threat
is actually called upon to make the choice, then she will choose up.
A reﬁnement of Nash equilibrium called subgame perfect Nash equilibrium deals with
Subgame perfect
Nash equilibrium
this problem. To deﬁne it, we need the idea of a subgame. Every decision state in a game tree
Subgame
(including the initial state) deﬁnes a subgame—the game in Figure 17.4 therefore contains
two subgames, one rooted at player 1’s decision state, one rooted at player 2’s decision state.
A proﬁle of strategies then forms a subgame perfect Nash equilibrium in a game G if it is a ◀
Nash equilibrium in every subgame of G. Applying this deﬁnition to the game of Figure 17.4,
we ﬁnd that (above,up) is subgame perfect, but (below,down) is not, because choosing down
is not a Nash equilibrium of the subgame rooted at player 2’s decision state.
Although we needed some new terminology to deﬁne subgame perfect Nash equilibrium,
we don’t need any new algorithms. The strategies computed through backward induction
will be subgame perfect Nash equilibria, and it follows that every extensive-form game of
perfect information has a subgame perfect Nash equilibrium, which can be computed in time
polynomial in the size of the game tree.
Chance and simultaneous moves
To represent stochastic games, such as backgammon, in extensive form, we add a player
called Chance, whose choices are determined by a probability distribution.
To represent simultaneous moves, as in the prisoner’s dilemma or two-ﬁnger Morra, we
impose an arbitrary order on the players, but we have the option of asserting that the earlier
player’s actions are not observable to the subsequent players: e.g., Ali must choose refuse or
testify ﬁrst, then Bo chooses, but Bo does not know what choice Ali made at that time (we
can also represent the fact that the move is revealed later). However, we assume the players
always remember all their own previous actions; this assumption is called perfect recall.
Capturing imperfect information
A key feature of extensive form that sets it apart from the game trees that we saw in Chapter 6
is that it can capture partial observability. Game theorists use the term imperfect informa-
tion to describe situations where players are uncertain about the actual state of the game.
Imperfect
information
