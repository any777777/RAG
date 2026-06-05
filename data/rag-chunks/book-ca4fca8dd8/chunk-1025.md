---
chunk_id: "book-ca4fca8dd8-chunk-1025"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1025
confidence: "first-pass"
extraction_method: "structured-local"
---

616
Chapter 17
Multiagent Decision Making
17.3 Cooperative Game Theory
Recall that cooperative games capture decision making scenarios in which agents can form
binding agreements with one another to cooperate. They can then beneﬁt from receiving extra
value compared to what they would get by acting alone.
We start by introducing a model for a class of cooperative games. Formally, these games
are called “cooperative games with transferable utility in characteristic function form.” The
idea of the model is that when a group of agents cooperate, the group as a whole obtains
some utility value, which can then be split among the group members. The model does not
say what actions the agents will take, nor does the game structure itself specify how the value
obtained will be split up (that will come later).
Formally, we use the formula G = (N,ν) to say that a cooperative game, G, is deﬁned by
a set of players N = {1,...,n} and a characteristic function, ν, which for every subset of
Characteristic
function
players C ⊆N gives the value that the group of players could obtain, should they choose to
work together.
Typically, we assume that the empty set of players achieves nothing (ν({}) = 0), and
that the function is nonnegative (ν(C) ≥0 for all C). In some games we make the further
assumption that players achieve nothing by working alone: ν({i}) = 0 for all i ∈N.
17.3.1 Coalition structures and outcomes
It is conventional to refer to a subset of players C as a coalition. In everyday use the term
Coalition
“coalition” implies a collection of people with some common cause (such as the Coalition to
Stop Gun Violence), but we will refer to any subset of players as a coalition. The set of all
players N is known as the grand coalition.
Grand coalition
In our model, every player must choose to join exactly one coalition (which could be a
coalition of just the single player alone). Thus, the coalitions form a partition of the set of
players. We call the partition a coalition structure. Formally, a coalition structure over a set
Coalition structure
of players N is a set of coalitions {C1,...,Ck} such that:
Ci ̸= {}
Ci ⊆N
Ci ∩Cj = {} for all i ̸= j ∈N
C1 ∪···∪Ck = N .
For example, if we have N = {1,2,3}, then there are seven possible coalitions:
{1}, {2}, {3}, {1,2}, {2,3}, {3,1}, and {1,2,3}
and ﬁve possible coalition structures:
{{1},{2},{3}}, {{1},{2,3}}, {{2},{1,3}}, {{3},{1,2}}, and {{1,2,3}}.
We use the notation CS(N) to denote the set of all coalition structures over player set N, and
CS(i) to denote the coalition that player i belongs to.
The outcome of a game is deﬁned by the choices the players make, in deciding which
coalitions to form, and in choosing how to divide up the ν(C) value that each coalition re-
ceives. Formally, given a cooperative game deﬁned by (N,ν), the outcome is a pair (CS,x)
consisting of a coalition structure and a payoff vector x = (x1,...,xn) where xi is the value
Payoﬀvector
