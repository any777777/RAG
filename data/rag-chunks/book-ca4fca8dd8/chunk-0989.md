---
chunk_id: "book-ca4fca8dd8-chunk-0989"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 989
confidence: "first-pass"
extraction_method: "structured-local"
---

596
Chapter 17
Multiagent Decision Making
of ﬁngers displayed be f. If f is odd, O collects f dollars from E; and if f is even, E collects
f dollars from O.1 The payoff matrix for two-ﬁnger Morra is as follows:
O: one
O: two
E: one
E = +2,O = −2
E = −3,O = +3
E: two
E = −3,O = +3
E = +4,O = −4
We say that E is the row player and O is the column player. So, for example, the lower-right
Row player
Column player
corner shows that when player O chooses action two and E also chooses two, the payoff is
+4 for E and −4 for O.
Before analyzing two-ﬁnger Morra, it is worth considering why game-theoretic ideas are
needed at all: why can’t we tackle the challenge facing (say) player E using the apparatus of
decision theory and utility maximization that we’ve been using elsewhere in the book? To
see why something else is needed, let’s suppose E is trying to ﬁnd the best action to perform.
The alternatives are one or two. If E chooses one, then the payoff will be either +2 or −3.
Which payoff E will actually receive, however, will depend on the choice made by O: the
most that E can do, as the row player, is to force the outcome of the game to be in a particular
row. Similarly, O chooses only the column.
To choose optimally between these possibilities, E must take into account how O will
act as a rational decision maker. But O, in turn, should take into account the fact that E is
a rational decision maker. Thus, decision making in multiagent settings is quite different in
character to decision making in single-agent settings, because the players need to take each
other’s reasoning into account. The role of solution concepts in game theory is to try to make
Solution concept
this kind of reasoning precise.
The term strategy is used in game theory to denote what we have previously called a
Strategy
policy. A pure strategy is a deterministic policy; for a single-move game, a pure strategy
Pure strategy
is just a single action. As we will see below, for many games an agent can do better with a
mixed strategy, which is a randomized policy that selects actions according to a probability
Mixed strategy
distribution. The mixed strategy that chooses action a with probability p and action b other-
wise is written [p:a;(1 −p):b]. For example, a mixed strategy for two-ﬁnger Morra might
be [0.5:one;0.5:two]. A strategy proﬁle is an assignment of a strategy to each player; given
Strategy proﬁle
the strategy proﬁle, the game’s outcome is a numeric value for each player—if players use
mixed strategies, then we must use expected utility.
So, how should agents decide act in games like Morra? Game theory provides a range
of solution concepts that attempt to deﬁne rational action with respect to an agent’s beliefs
about the other agent’s beliefs. Unfortunately, there is no one perfect solution concept: it
is problematic to deﬁne what “rational” means when each agent chooses only part of the
strategy proﬁle that determines the outcome.
We introduce our ﬁrst solution concept through what is probably the most famous game
in the game theory canon—the prisoner’s dilemma. This game is motivated by the following
Prisoner’s dilemma
story: Two alleged burglars, Ali and Bo, are caught red-handed near the scene of a burglary
and are interrogated separately. A prosecutor offers each a deal: if you testify against your
partner as the leader of a burglary ring, you’ll go free for being the cooperative one, while
1
Morra is a recreational version of an inspection game. In such games, an inspector chooses a day to inspect a
facility (such as a restaurant or a biological weapons plant), and the facility operator chooses a day to hide all the
nasty stuff. The inspector wins if the days are different, and the facility operator wins if they are the same.
