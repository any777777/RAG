---
chunk_id: "book-ca4fca8dd8-chunk-1007"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1007
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.2
Non-Cooperative Game Theory
607
The outcomes and payoffs are the same as if both players had chosen DOVE, but unlike that
case, GRIM playing against GRIM forms a Nash equilibrium, and Ali and Bo are able to
rationally achieve an outcome that is impossible in the one-shot version of the game.
To see that these strategies form a Nash equilibrium, suppose for the sake of contradiction
that they do not. Then one player—assume without loss of generality that it is Ali—has a
beneﬁcial deviation, in the form of an FSM strategy that would yield a higher payoff than
GRIM. Now, at some point this strategy would have to do something different from GRIM—
otherwise it would obtain the same utility. So, at some point it must play testify. But then
Bo’s GRIM strategy would ﬂip to punishment mode, by permanently testifying in response.
At that point, Ali would be doomed to receive a payoff of no more than −5: worse than the
−1 she would have received by choosing GRIM. Thus, both players choosing GRIM forms a
Nash equilibrium in the inﬁnitely repeated prisoner’s dilemma, giving a rationally sustained
outcome that is impossible in the one-shot version of the game.
This is an instance of a general class of results called the Nash folk theorems, which
Nash folk theorems
characterize the outcomes that can be sustained by Nash equilibria in inﬁnitely repeated
games. Let’s say a player’s security value is the best payoff that the player could guaran-
tee to obtain. Then the general form of the Nash folk theorems is roughly that every outcome ◀
in which every player receives at least their security value can be sustained as a Nash equi-
librium in an inﬁnitely repeated game. GRIM strategies are the key to the folk theorems: the
mutual threat of punishment if any agent fails to play their part in the desired outcome keeps
players in line. But it works as a deterrent only if the other player believes you have adopted
this strategy—or at least that you might have adopted it.
We can also get different solutions by changing the agents, rather than changing the
rules of engagement. Suppose the agents are ﬁnite state machines with n states and they are
playing a game with m > n total steps. The agents are thus incapable of representing the
number of remaining steps, and must treat it as an unknown. Therefore, they cannot do the
backward induction, and are free to arrive at the more favorable (refuse, refuse) equilibrium
in the iterated Prisoner’s Dilemma. In this case, ignorance is bliss—or rather, having your
opponent believe that you are ignorant is bliss. Your success in these repeated games depends
to a signiﬁcant extent on the other player’s perception of you as a bully or a simpleton, and
not on your actual characteristics.
17.2.4 Sequential games: The extensive form
In the general case, a game consists of a sequence of turns that need not be all the same. Such
games are best represented by a game tree, which game theorists call the extensive form. The
Extensive form
tree includes all the same information we saw in Section 6.1: an initial state S0, a function
PLAYER(s) that tells which player has the move, a function ACTIONS(s) enumerating the
possible actions, a function RESULT(s,a) that deﬁnes the transition to a new state, and a
partial function UTILITY(s, p), which is deﬁned only on terminal states, to give the payoff
for each player. Stochastic games can be captured by introducing a distinguished player,
Chance, that can take random actions. Chance’s “strategy” is part of the deﬁnition of the
game, speciﬁed as a probability distribution over actions (the other players get to choose
their own strategy). To represent games with nondeterministic actions, such as billiards, we
break the action into two pieces: the player’s action itself has a deterministic result, and then
Chance has a turn to react to the action in its own capricious way.
