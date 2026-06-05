---
chunk_id: "book-ca4fca8dd8-chunk-1029"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1029
confidence: "first-pass"
extraction_method: "structured-local"
---

618
Chapter 17
Multiagent Decision Making
The deﬁnition of the core naturally leads to a system of linear inequalities, as follows (the
unknowns are variables x1,...,xn, and the values ν(C) are constants):
xi ≥ν({i}) for all i ∈N
∑i∈N xi = ν(N)
∑i∈C xi ≥ν(C)
for all C ⊆N
Any solution to these inequalities will deﬁne an imputation in the core. We can formulate the
inequalities as a linear program by using a dummy objective function (for example, maximiz-
ing ∑i∈N xi), which will allow us to compute imputations in time polynomial in the number
of inequalities. The difﬁculty is that this gives an exponential number of inequalities (one
for each of the 2n possible coalitions). Thus, this approach yields an algorithm for checking
non-emptiness of the core that runs in exponential time. Whether we can do better than this
depends on the game being studied: for many classes of cooperative game, the problem of
checking non-emptiness of the core is co-NP-complete. We give an example below.
Before proceeding, let’s see an example of a superadditive game with an empty core. The
game has three players N = {1,2,3}, and has a characteristic function deﬁned as follows:
ν(C) =
 1 if |C| ≥2
0 otherwise.
Now consider any imputation (x1,x2,x3) for this game. Since ν(N) = 1, it must be the case
that at least one player i has xi > 0, and the other two get a total payoff less than 1. Those
two could beneﬁt by forming a coalition without player i and sharing the value 1 among
themselves. But since this holds for all imputations, the core must be empty.
The core formalizes the idea of the grand coalition being stable, in the sense that no
coalition can proﬁtably defect from it. However, the core may contain imputations that are
unreasonable, in the sense that one or more players might feel they were unfair. Suppose
N = {1,2}, and we have a characteristic function ν deﬁned as follows:
ν({1}) = ν({2}) = 5
ν({1,2}) = 20.
Here, cooperation yields a surplus of 10 over what players could obtain working in isolation,
and so intuitively, cooperation will make sense in this scenario. Now, it is easy to see that the
imputation (6,14) is in the core of this game: neither player can deviate to obtain a higher
utility. But from the point of view of player 1, this might appear unreasonable, because it
gives 9/10 of the surplus to player 2. Thus, the notion of the core tells us when a grand
coalition can form, but it does not tell us how to distribute the payoff.
The Shapley value is an elegant proposal for how to divide the ν(N) value among the
Shapley value
players, given that the grand coalition N formed. Formulated by Nobel laureate Lloyd Shap-
ley in the early 1950s, the Shapley value is intended to be a fair distribution scheme.
What does fair mean? It would be unfair to distribute ν(N) based on the eye color of
players, or their gender, or skin color. Students often suggest that the value ν(N) should be
divided equally, which seems like it might be fair, until we consider that this would give the
same reward to players that contribute a lot and players that contribute nothing. Shapley’s
insight was to suggest that the only fair way to divide the value ν(N) was to do so according
to how much each player contributed to creating the value ν(N).
First we need to deﬁne the notion of a player’s marginal contribution. The marginal
Marginal
contribution
