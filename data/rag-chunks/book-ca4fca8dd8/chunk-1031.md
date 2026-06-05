---
chunk_id: "book-ca4fca8dd8-chunk-1031"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1031
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.3
Cooperative Game Theory
619
contribution that a player i makes to a coalition C is the value that i would add (or remove),
should i join the coalition C. Formally, the marginal contribution that player i makes to C is
denoted by mci(C):
mci(C) = ν(C∪{i})−ν(C).
Now, a ﬁrst attempt to deﬁne a payoff division scheme in line with Shapley’s suggestion
that players should be rewarded according to their contribution would be to pay each player i
the value that they would add to the coalition containing all other players:
mci(N −{i}).
The problem is that this implicitly assumes that player i is the last player to enter the coalition.
So, Shapley suggested, we need to consider all possible ways that the grand coalition could
form, that is, all possible orderings of the players N, and consider the value that i adds to
the preceding players in the ordering. Then, a player should be rewarded by being paid the
average marginal contribution that player i makes, over all possible orderings of the players,
to the set of players preceding i in the ordering.
We let P denote all possible permutations (e.g., orderings) of the players N, and denote
members of P by p, p′,... etc. Where p ∈P and i ∈N, we denote by pi the set of players
that precede i in the ordering p. Then the Shapley value for a game G is the imputation
φ(G) = (φ1(G),...,φn(G)) deﬁned as follows:
φi(G) = 1
n! ∑
p∈P
mci(pi).
(17.1)
This should convince you that the Shapley value is a reasonable proposal. But the remark-
able fact is that it is the unique solution to a set of axioms that characterizes a “fair” payoff
distribution scheme. We’ll need some more deﬁnitions before deﬁning the axioms.
We deﬁne a dummy player as a player i that never adds any value to a coalition—that is,
Dummy player
mci(C) = 0 for all C ⊆N −{i}. We will say that two players i and j are symmetric players
Symmetric players
if they always make identical contributions to coalitions—that is, mci(C) = mc j(C) for all
C ⊆N −{i, j}. Finally, where G = (N,ν) and G′ = (N,ν′) are games with the same set of
players, the game G +G′ is the game with the same player set, and a characteristic function
ν′′ deﬁned by ν′′(C) = ν(C)+ν′(C).
Given these deﬁnitions, we can deﬁne the fairness axioms satisﬁed by the Shapley value:
• Efﬁciency: ∑i∈N φi(G) = ν(N). (All the value should be distributed.)
• Dummy Player: If i is a dummy player in G then φi(G) = 0. (Players who never
contribute anything should never receive anything.)
• Symmetry: If i and j are symmetric in G then φi(G) = φj(G). (Players who make
identical contributions should receive identical payoffs.)
• Additivity: The value is additive over games: For all games G = (N,ν) and G′ = (N,ν′),
and for all players i ∈N, we have φi(G+G′) = φi(G)+φi(G′).
The additivity axiom is admittedly rather technical. If we accept it as a requirement, however,
we can establish the following key property: the Shapley value is the only way to distribute ◀
coalitional value so as to satisfy these fairness axioms.
