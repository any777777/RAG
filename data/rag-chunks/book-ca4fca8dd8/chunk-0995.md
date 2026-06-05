---
chunk_id: "book-ca4fca8dd8-chunk-0995"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 995
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.2
Non-Cooperative Game Theory
599
is of course not a precise deﬁnition—what it means will depend on the game at hand. In
the example above, though, there is one obvious focal point: the outcome (t,l) would give
both players substantially higher utility than they would obtain if they coordinated on (b,r).
From the point of view of game theory, both outcomes are Nash equilibria—but it would be
a perverse player indeed who expected to coordinate on (b,r).
Some games have no Nash equilibria in pure strategies, as the following game, called
matching pennies, illustrates. In this game, Ali and Bo simultaneously choose one side of a
Matching pennies
coin, either heads of tails: if they make the same choices, then Bo gives Ali $1, while if they
make different choices, then Ali gives Bo $1:
Ali:heads
Ali:tails
Bo:heads
A = 1,B = −1
A = −1,B = 1
Bo:tails
A = −1,B = 1
A = 1,B = −1
We invite the reader to check that the game contains no dominant strategies, and that no
outcome is a Nash equilibrium in pure strategies: in every outcome, one player regrets their
choice, and would rather have chosen differently, given the choice of the other player.
To ﬁnd a Nash equilibrium, the trick is to use mixed strategies—to allow players to ran-
domize over their choices. Nash proved that every game has at least one Nash equilibrium in ◀
mixed strategies. This explains why Nash equilibrium is such an important solution concept:
other solution concepts, such as dominant strategy equilibrium, are not guaranteed to exist for
every game, but we always get a solution if we look for Nash equilibria with mixed strategies.
In the case of matching pennies, we have a Nash equilibrium in mixed strategies if both
players choose heads and tails with equal probability. To see that this outcome is indeed a
Nash equilibrium, suppose one of the players chose an outcome with a probability other than
0.5. Then the other player would be able to exploit that, putting all their weight behind a
particular strategy. For example, suppose Bo played heads with probability 0.6 (and so tails
with probability 0.4). Then Ali would do best to play heads with certainty. It is then easy to
see that Bo playing heads with probability 0.6 could not form part of any Nash equilibrium.
17.2.2 Social welfare
The main perspective in game theory is that of players within the game, trying to obtain the
best outcomes for themselves that they can. However, it is sometimes instructive to adopt a
different perspective. Suppose you were a benevolent, omniscient entity looking down on the
game, and you were able to choose the outcome. Being benevolent, you want to choose the
best overall outcome—the outcome that would be best for society as a whole, so to speak.
How should you choose? What criteria might you apply? This is where the notion of social
welfare comes in.
Social welfare
Probably the most important and least contentious social welfare criterion is that you
should avoid outcomes that waste utility. This requirement is captured in the concept of
Pareto optimality, which is named for the Italian economist Vilfredo Pareto (1848–1923).
Pareto optimality
An outcome is Pareto optimal if there is no other outcome that would make one player better
off without making someone else worse off. If you choose an outcome that is not Pareto
optimal, then it wastes utility in the sense that you could have given more utility to at least
one agent, without taking any from other agents.
Utilitarian social welfare is a measure of how good an outcome is in the aggregate. The
Utilitarian social
welfare
utilitarian social welfare of an outcome is simply the sum of utilities given to players by that
