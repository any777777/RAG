---
chunk_id: "book-ca4fca8dd8-chunk-1033"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1033
confidence: "first-pass"
extraction_method: "structured-local"
---

620
Chapter 17
Multiagent Decision Making
17.3.3 Computation in cooperative games
From a theoretical point of view, we now have a satisfactory solution. But from a computa-
tional point of view, we need to know how to compactly represent cooperative games, and
how to efﬁciently compute solution concepts such as the core and the Shapley value.
The obvious representation for a characteristic function would be a table listing the value
ν(C) for all 2n coalitions. This is infeasible for large n. A number of approaches to com-
pactly representing cooperative games have been developed, which can be distinguished by
whether or not they are complete. A complete representation scheme is one that is capable of
representing any cooperative game. The drawback with complete representation schemes is
that there will always be some games that cannot be represented compactly. An alternative is
to use a representation scheme that is guaranteed to be compact, but which is not complete.
Marginal contribution nets
We now describe one representation scheme, called marginal contribution nets (MC-nets).
Marginal
contribution net
We will use a slightly simpliﬁed version to facilitate presentation, and the simpliﬁcation
makes it incomplete—the full version of MC-nets is a complete representation.
The idea behind marginal contribution nets is to represent the characteristic function of a
game (N,v) as a set of coalition-value rules, of the form: (Ci,xi), where Ci ⊆N is a coalition
and xi is a number. To compute the value of a coalition C, we simply sum the values of
all rules (Ci,xi) such that Ci ⊆C. Thus, given a set of rules R = {(C1,x1),...,(Ck,xk)}, the
corresponding characteristic function is:
ν(C) = ∑{xi | (Ci,xi) ∈R and Ci ⊆C}.
Suppose we have a rule set R containing the following three rules:
{({1,2},5),
({2},2),
({3},4)}.
Then, for example, we have:
• ν({1}) = 0 (because no rules apply),
• ν({3}) = 4 (third rule),
• ν({1,3}) = 4 (third rule),
• ν({2,3}) = 6 (second and third rules), and
• ν({1,2,3}) = 11 (ﬁrst, second, and third rules).
With this representation we can compute the Shapley value in polynomial time. The key
insight is that each rule can be understood as deﬁning a game on its own, in which the players
are symmetric. By appealing to Shapley’s axioms of additivity and symmetry, therefore, the
Shapley value φi(R) of player i in the game associated with the rule set R is then simply:
φi(R) = ∑
(C,x)∈R
(
x
|C|
if i ∈C
0
otherwise.
The version of marginal contribution nets that we have presented here is not a complete repre-
sentation scheme: there are games whose characteristic function cannot be represented using
rule sets of the form described above. A richer type of marginal contribution networks al-
lows for rules of the form (φ,x), where φ is a propositional logic formula over the players
N: a coalition C satisﬁes the condition φ if it corresponds to a satisfying assignment for φ.
