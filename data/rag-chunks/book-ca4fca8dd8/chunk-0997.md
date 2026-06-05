---
chunk_id: "book-ca4fca8dd8-chunk-0997"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 997
confidence: "first-pass"
extraction_method: "structured-local"
---

600
Chapter 17
Multiagent Decision Making
outcome. There are two key difﬁculties with utilitarian social welfare. The ﬁrst is that it
considers the sum but not the distribution of utilities among players, so it could lead to a
very unequal distribution if that happens to maximize the sum. The second difﬁculty is that
it assumes a common scale for utilities. Many economists argue that this is impossible to
establish because utility (unlikely money) is a subjective quantity. If we’re trying to decide
how to divide up a batch of cookies, should we give them all to the utility monster who says,
“I love cookies a thousand times more than anyone else?” That would maximize the total
self-reported utility, but doesn’t seem right.
The question of how utility is distributed among players is addressed by research in egal-
itarian social welfare. For example, one proposal suggests that we should maximize the
Egalitarian social
welfare
expected utility of the worst-off member of society—a maximin approach. Other metrics
are possible, including the Gini coefﬁcient, which summarizes how evenly utility is spread
Gini coeﬃcient
among the players. The main difﬁculties with such proposals is that they may sacriﬁce a great
deal of total welfare for small distributional gains, and, like plain utilitarianism, they are still
at the mercy of the utility monster.
Applying these concepts to the prisoner’s dilemma game, introduced above, explains
why it is called a dilemma. Recall that (testify,testify) is a dominant strategy equilibrium,
and the only Nash equilibrium. However, this is the only outcome that is not Pareto optimal.
The outcome (refuse,refuse) maximizes both utilitarian and egalitarian social welfare. The
dilemma in the prisoner’s dilemma thus arises because a very strong solution concept (domi-
nant strategy equilibrium) leads to an outcome that essentially fails every test of what counts
as a reasonable outcome from the point of view of the “society.” Yet there is no clear way for
the individual players to arrive at a better solution.
Computing equilibria
Let’s now consider the key computational questions associated with the concepts discussed
above. First we will consider pure strategies, where randomization is not permitted.
If players have only a ﬁnite number of possible choices, then exhaustive search can be
used to ﬁnd equilibria: iterate through each possible strategy proﬁle, and check whether any
player has a beneﬁcial deviation from that proﬁle; if not, then it is a Nash equilibrium in pure
strategies. Dominant strategies and dominant strategy equilibria can be computed by similar
algorithms. Unfortunately, the number of possible strategy proﬁles for n players each with m
possible actions, is mn, i.e., infeasibly large for an exhaustive search.
An alternative approach, which works well in some games, is myopic best response
Myopic best
response
(also known as iterated best response): start by choosing a strategy proﬁle at random; then,
if some player is not playing their optimal choice given the choices of others, ﬂip their choice
to an optimal one, and repeat the process. The process will converge if it leads to a strategy
proﬁle in which every player is making an optimal choice, given the choices of the others—a
Nash equilibrium, in other words. For some games, myopic best response does not converge,
but for some important classes of games, it is guaranteed to converge.
Computing mixed-strategy equilibria is algorithmically much more intricate. To keep
things simple, we will focus on methods for zero-sum games and comment brieﬂy on their
extension to other games at the end of this section.
In 1928, von Neumann developed a method for ﬁnding the optimal mixed strategy for
two-player, zero-sum games—games in which the payoffs always add up to zero (or a con-
Zero-sum game
