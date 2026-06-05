---
chunk_id: "book-ca4fca8dd8-chunk-1009"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1009
confidence: "first-pass"
extraction_method: "structured-local"
---

608
Chapter 17
Multiagent Decision Making
For the moment, we will make one simplifying assumption: we assume players have
perfect information. Roughly, perfect information means that, when the game calls upon
Perfect information
them to make a decision, they know precisely where they are in the game tree: they have no
uncertainty about what has happened previously in the game. This is, of course, the situation
in games like chess or Go, but not in games like poker or Kriegspiel. In the following section,
we will show how the extensive form can be used to capture imperfect information in games,
but for the moment, we will assume perfect information.
A strategy in an extensive-form game of perfect information is a function for a player that
for every one of its decision states s dictates which action in ACTIONS(s) the player should
choose to execute. When each player has selected a strategy, then the resulting strategy proﬁle
will trace a path in the game tree from the initial state S0 to a terminal state, and the UTILITY
function deﬁnes the utilities that each player will then receive.
Given this setup, we can directly apply the apparatus of Nash equilibria that we intro-
duced above to analyze extensive-form games. To compute Nash equilibria, we can use a
straightforward generalization of the minimax search technique that we saw in Chapter 6.
In the literature on extensive-form games, the technique is called backward induction—we
already saw backward induction informally used to analyze the ﬁnitely repeated prisoner’s
dilemma. Backward induction uses dynamic programming, working backwards from termi-
nal states back to the initial state, progressively labeling each state with a payoff proﬁle (an
assignment of payoffs to players) that would be obtained if the game was played optimally
from that point on.
In more detail, for each nonterminal state s, if all the children of s have been labeled with
a payoff proﬁle, then label s with a payoff proﬁle from the child state that maximizes the
payoff of the player making the decision at state s. (If there is a tie, then choose arbitrarily; if
we have chance nodes, then compute expected utility.) The backward induction algorithm is
guaranteed to terminate, and moreover runs in time polynomial in the size of the game tree.
As the algorithm does its work, it traces out strategies for each player. As it turns out,
these strategies are Nash equilibrium strategies, and the payoff proﬁle labeling the initial state
is a payoff proﬁle that would be obtained by playing Nash equilibrium strategies. Thus, Nash
equilibrium strategies for extensive-form games can be computed in polynomial time using
backward induction; and since the algorithm is guaranteed to label the initial state with a
payoff proﬁle, it follows that every extensive-form game has at least one Nash equilibrium in
pure strategies.
These are attractive results, but there are several caveats. Game trees very quickly get
very large, so polynomial running time should be understood in that context. But more prob-
lematically, Nash equilibrium itself has some limitations when it is applied to extensive-form
games. Consider the game in Figure 17.4. Player 1 has two moves available: above or below.
If she moves below, then both players receive a payoff of 0 (regardless of the move selected
by player 2). If she moves above, then player 2 is presented with a choice of moving up or
down: if she moves down, then both players receive a payoff of 0, while if she moves up, then
they both receive 1.
Backward induction immediately tells us that (above,up) is a Nash equilibrium, resulting
in both players receiving a payoff of 1. However, (below,down) is also a Nash equilibrium,
which would result in both players receiving a payoff of 0. Player 2 is threatening player 1, by
indicating that if called upon to make a decision she will choose down, resulting in a payoff
