---
chunk_id: "book-ca4fca8dd8-chunk-0999"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 999
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.2
Non-Cooperative Game Theory
601
stant, as explained on page 193). Clearly, Morra is such a game. For two-player, zero-sum
games, we know that the payoffs are equal and opposite, so we need consider the payoffs of
only one player, who will be the maximizer (just as in Chapter 6). For Morra, we pick the even
player E to be the maximizer, so we can deﬁne the payoff matrix by the values UE(e,o)—the
payoff to E if E does e and O does o. (For convenience we call player E “her” and O “him.”)
Von Neumann’s method is called the maximin technique, and it works as follows:
Maximin
• Suppose we change the rules as follows: ﬁrst E picks her strategy and reveals it to O.
Then O picks his strategy, with knowledge of E’s strategy. Finally, we evaluate the
expected payoff of the game based on the chosen strategies. This gives us a turn-taking
game to which we can apply the standard minimax algorithm from Chapter 6. Let’s
suppose this gives an outcome UE,O. Clearly, this game favors O, so the true utility U of
the original game (from E’s point of view) is at least UE,O. For example, if we just look
at pure strategies, the minimax game tree has a root value of −3 (see Figure 17.2(a)),
so we know that U ≥−3.
• Now suppose we change the rules to force O to reveal his strategy ﬁrst, followed by E.
Then the minimax value of this game is UO,E, and because this game favors E we know
that U is at most UO,E. With pure strategies, the value is +2 (see Figure 17.2(b)), so we
know U ≤+2.
Combining these two arguments, we see that the true utility U of the solution to the original
game must satisfy
UE,O ≤U ≤UO,E
or in this case,
−3 ≤U ≤2.
To pinpoint the value of U, we need to turn our analysis to mixed strategies. First, observe
the following: once the ﬁrst player has revealed a strategy, the second player might as well ◀
choose a pure strategy. The reason is simple: if the second player plays a mixed strategy,
[p:one;(1 −p):two], its expected utility is a linear combination (p ·Uone +(1 −p)·Utwo) of
the utilities of the pure strategies, Uone and Utwo. This linear combination can never be better
than the better of Uone and Utwo, so the second player can just choose the better one.
With this observation in mind, the minimax trees can be thought of as having inﬁnitely
many branches at the root, corresponding to the inﬁnitely many mixed strategies the ﬁrst
player can choose. Each of these leads to a node with two branches corresponding to the
pure strategies for the second player. We can depict these inﬁnite trees ﬁnitely by having one
“parameterized” choice at the root:
• If E chooses ﬁrst, the situation is as shown in Figure 17.2(c). E chooses the strat-
egy [p:one;(1 −p):two] at the root, and then O chooses a pure strategy (and hence a
move) given the value of p. If O chooses one, the expected payoff (to E) is 2p−3(1−
p)=5p−3; if O chooses two, the expected payoff is −3p+4(1−p)=4−7p. We can
draw these two payoffs as straight lines on a graph, where p ranges from 0 to 1 on the
x-axis, as shown in Figure 17.2(e). O, the minimizer, will always choose the lower of
the two lines, as shown by the heavy lines in the ﬁgure. Therefore, the best that E can
do at the root is to choose p to be at the intersection point, which is where
5p−3 = 4−7p
⇒
p = 7/12.
The utility for E at this point is UE,O = −1/12.
