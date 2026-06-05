---
chunk_id: "book-ca4fca8dd8-chunk-0993"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 993
confidence: "first-pass"
extraction_method: "structured-local"
---

598
Chapter 17
Multiagent Decision Making
It is, however, possible to get to the (refuse,refuse) solution if we change the game.
We could change it to a cooperative game where the agents are allowed to form a binding
agreement. Or we could change to a repeated game in which the players know that they will
meet again—we will see how this works below. Alternatively, the players might have moral
beliefs that encourage cooperation and fairness. But that would mean they have different
utility functions, and again, they would be playing a different game.
The presence of a dominant strategy for a particular player greatly simpliﬁes the decision
making process for that player. Once Ali has realized that testifying is a dominant strategy,
she doesn’t need to invest any effort in trying to ﬁgure out what Bo will do, because she
knows that no matter what Bo does, testifying would be her best response. However, most
Best response
games have neither dominant strategies nor dominant strategy equilibria. It is rare that a
single strategy is the best response to all possible counterpart strategies.
The next solution concept we consider is weaker than dominant strategy equilibrium, but
it is much more widely applicable. It is called Nash equilibrium, and is named for John
Nash equilibrium
Forbes Nash, Jr. (1928–2015), who studied it in his 1950 Ph.D. thesis—work for which he
was awarded a Nobel Prize in 1994.
A strategy proﬁle is a Nash equilibrium if no player could unilaterally change their strat-
egy and as a consequence receive a higher payoff, under the assumption that the other players
stayed with their strategy choices. Thus, in a Nash equilibrium, every player is simultaneously
playing a best response to the choices of their counterparts. A Nash equilibrium represents a
stable point in a game: stable in the sense that there is no rational incentive for any player to
deviate. However, Nash equilibria are local stable points: as we will see, a game may contain
multiple Nash equilibria.
Since a dominant strategy is a best response to all counterpart strategies, it follows that
any dominant strategy equilibrium must also be a Nash equilibrium (Exercise 17.EQIB). In
the prisoner’s dilemma, therefore, there is a unique dominant strategy equilibrium, which is
also the unique Nash equilibrium.
The following example game demonstrates, ﬁrst, that sometimes games have no dominant
strategies, and second, that some games have multiple Nash equilibria.
Ali:l
Ali:r
Bo:t
A = 10,B = 10
A = 0,B = 0
Bo:b
A = 0,B = 0
A = 1,B = 1
It is easy to verify that there are no dominant strategies in this game, for either player, and
hence no dominant strategy equilibrium. However, the strategy proﬁles (t,l) and (b,r) are
both Nash equilibria. Now, clearly it is in the interests of both agents to aim for the same
Nash equilibrium—either (t,l) or (b,r)—but since we are in the domain of non-cooperative
game theory, players must make their choices independently, without any knowledge of the
choices of the others, and without any way of making an agreement with them. This is an
example of a coordination problem: the players want to coordinate their actions globally,
so that they both choose actions leading to the same equilibrium, but must do so using only
local decision making.
A number of approaches to resolving coordination problems have been proposed. One
idea is that of focal points. A focal point in a game is an outcome that in some way stands
Focal point
out to players as being an “obvious” outcome upon which to coordinate their choices. This
