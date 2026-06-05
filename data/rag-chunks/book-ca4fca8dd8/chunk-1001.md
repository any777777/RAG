---
chunk_id: "book-ca4fca8dd8-chunk-1001"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1001
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.2
Non-Cooperative Game Theory
603
Now we know that the true utility of the original game lies between −1/12 and −1/12; that
is, it is exactly −1/12! (The conclusion is that it is better to be O than E if you are playing this
game.) Furthermore, the true utility is attained by the mixed strategy [7/12:one;5/12:two],
which should be played by both players. This strategy is called the maximin equilibrium of
Maximin equilibrium
the game, and is a Nash equilibrium. Note that each component strategy in an equilibrium
mixed strategy has the same expected utility. In this case, both one and two have the same
expected utility, −1/12, as the mixed strategy itself.
Our result for two-ﬁnger Morra is an example of the general result by von Neumann:
every two-player zero-sum game has a maximin equilibrium when you allow mixed strategies. ◀
Furthermore, every Nash equilibrium in a zero-sum game is a maximin for both players. A
player who adopts the maximin strategy has two guarantees: First, no other strategy can do
better against an opponent who plays well (although some other strategies might be better at
exploiting an opponent who makes irrational mistakes). Second, the player continues to do
just as well even if the strategy is revealed to the opponent.
The general algorithm for ﬁnding maximin equilibria in zero-sum games is somewhat
more involved than Figures 17.2(e) and (f) might suggest. When there are n possible actions,
a mixed strategy is a point in n-dimensional space and the lines become hyperplanes. It’s also
possible for some pure strategies for the second player to be dominated by others, so that they
are not optimal against any strategy for the ﬁrst player. After removing all such strategies
(which might have to be done repeatedly), the optimal choice at the root is the highest (or
lowest) intersection point of the remaining hyperplanes.
Finding this choice is an example of a linear programming problem: maximizing an
objective function subject to linear constraints. Such problems can be solved by standard
techniques in time polynomial in the number of actions (and in the number of bits used to
specify the reward function, if you want to get technical).
The question remains, what should a rational agent actually do in playing a single game
of Morra? The rational agent will have derived the fact that [7/12:one;5/12:two] is the
maximin equilibrium strategy, and will assume that this is mutual knowledge with a rational
opponent. The agent could use a 12-sided die or a random number generator to pick randomly
according to this mixed strategy, in which case the expected payoff would be -1/12 for E. Or
the agent could just decide to play one, or two. In either case, the expected payoff remains
-1/12 for E. Curiously, unilaterally choosing a particular action does not harm one’s expected
payoff, but allowing the other agent to know that one has made such a unilateral decision
does affect the expected payoff, because then the opponent can adjust strategy accordingly.
Finding equilibria in non-zero-sum games is somewhat more complicated. The general
approach has two steps: (1) Enumerate all possible subsets of actions that might form mixed
strategies. For example, ﬁrst try all strategy proﬁles where each player uses a single action,
then those where each player uses either one or two actions, and so on. This is exponential
in the number of actions, and so only applies to relatively small games. (2) For each strategy
proﬁle enumerated in (1), check to see if it is an equilibrium. This is done by solving a set of
equations and inequalities that are similar to the ones used in the zero-sum case. For two play-
ers these equations are linear and can be solved with basic linear programming techniques,
but for three or more players they are nonlinear and may be very difﬁcult to solve.
