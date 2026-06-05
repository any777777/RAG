---
chunk_id: "book-ca4fca8dd8-chunk-1027"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1027
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.3
Cooperative Game Theory
617
that goes to player i. The payoff must satisfy the constraint that each coalition C splits up all
of its value ν(C) among its members:
∑
i∈C
xi = ν(C)
for all C ∈CS
For example, given the game ({1,2,3},ν) where ν({1})=4 and ν({2,3})=10, a possible
outcome is:
({{1},{2,3}},(4,5,5)).
That is, player 1 stays alone and accepts a value of 4, while players 2 and 3 team up to receive
a value of 10, which they choose to split evenly.
Some cooperative games have the feature that when two coalitions merge together, they
do no worse than if they had stayed apart. This property is called superadditivity. Formally,
Superadditivity
a game is superadditive if its characteristic function satisﬁes the following condition:
ν(C∪D) ≥ν(C)+ν(D)
for all C,D ⊆N
If a game is superadditive, then the grand coalition receives a value that is at least as high
as or higher than the total received by any other coalition structure. However, as we will see
shortly, superadditive games do not always end up with a grand coalition, for much the same
reason that the players do not always arrive at a collectively desirable Pareto-optimal outcome
in the prisoner’s dilemma.
17.3.2 Strategy in cooperative games
The basic assumption in cooperative game theory is that players will make strategic decisions
about who they will cooperate with. Intuitively, players will not desire to work with unpro-
ductive players—they will naturally seek out players that collectively yield a high coalitional
value. But these sought-after players will be doing their own strategic reasoning. Before we
can describe this reasoning, we need some further deﬁnitions.
An imputation for a cooperative game (N,ν) is a payoff vector that satisﬁes the follow-
Imputation
ing two conditions:
∑n
i=1 xi = ν(N)
xi ≥ν({i}) for all i ∈N .
The ﬁrst condition says that an imputation must distribute the total value of the grand coali-
tion; the second condition, known as individual rationality, says that each player is at least
Individual rationality
as well off as if it had worked alone.
Given an imputation x = (x1,...,xn) and a coalition C ⊆N, we deﬁne x(C) to be the sum
∑i∈C xi—the total amount disbursed to C by the imputation x.
Next, we deﬁne the core of a game (N,ν) as the set of all imputations x that satisfy the
Core
condition x(C) ≥ν(C) for every possible coalition C ⊂N. Thus, if an imputation x is not
in the core, then there exists some coalition C ⊂N such that ν(C) > x(C). The players in C
would refuse to join the grand coalition because they would be better off sticking with C.
The core of a game therefore consists of all the possible payoff vectors that no coalition
could object to on the grounds that they could do better by not joining the grand coalition.
Thus, if the core is empty, then the grand coalition cannot form, because no matter how the
grand coalition divided its payoff, some smaller coalition would refuse to join. The main
computational questions around the core relate to whether or not it is empty, and whether a
particular payoff distribution is in the core.
