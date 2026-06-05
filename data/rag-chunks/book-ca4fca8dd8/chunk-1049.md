---
chunk_id: "book-ca4fca8dd8-chunk-1049"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1049
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.4
Making Collective Decisions
629
The basic setting is as follows. As usual, we have a set N = {1,...,n} of agents, who
in this section will be the voters. These voters want to make decisions with respect to a set
Ω= {ω1,ω2,...} of possible outcomes. In a political election, each element of Ωcould stand
for a different candidate winning the election.
Each voter will have preferences over Ω. These are usually expressed not as quantitative
utilities but rather as qualitative comparisons: we write ω ≻i ω′ to mean that outcome ω is
ranked above outcome ω′ by agent i. In an election with three candidates, agent i might have
ω2 ≻i ω3 ≻i ω1.
The fundamental problem of social choice theory is to combine these preferences, using
a social welfare function, to come up with a social preference order: a ranking of the
Social welfare
function
candidates, from most preferred down to least preferred. In some cases, we are only interested
in a social outcome—the most preferred outcome by the group as a whole. We will write
Social outcome
ω ≻∗ω′ to mean that ω is ranked above ω′ in the social preference order.
A simpler setting is where we are not concerned with obtaining an entire ordering of
candidates, but simply want to choose a set of winners. A social choice function takes as
Social choice
function
input a preference order for each voter, and produces as output a set of winners.
Democratic societies want a social outcome that reﬂects the preferences of the voters.
Unfortunately, this is not always straightforward. Consider Condorcet’s Paradox, a famous
Condorcet’s Paradox
example posed by the Marquis de Condorcet (1743–1794). Suppose we have three outcomes,
Ω= {ωa,ωb,ωc}, and three voters, N = {1,2,3}, with preferences as follows.
ωa ≻1 ωb ≻1 ωc
ωc ≻2 ωa ≻2 ωb
ωb ≻3 ωc ≻3 ωa
(17.2)
Now, suppose we have to choose one of the three candidates on the basis of these preferences.
The paradox is that:
• 2/3 of the voters prefer ω3 over ω1.
• 2/3 of the voters prefer ω1 over ω2.
• 2/3 of the voters prefer ω2 over ω3.
So, for each possible winner, we can point to another candidate who would be preferred by
at least 2/3 of the electorate. It is obvious that in a democracy we cannot hope to make every
voter happy. This demonstrates that there are scenarios in which no matter which outcome we ◀
choose, a majority of voters will prefer a different outcome.
A natural question is whether
there is any “good” social choice procedure that really reﬂects the preferences of voters. To
answer this, we need to be precise about what we mean when we say that a rule is “good.”
We will list some properties we would like a good social welfare function to satisfy:
• The Pareto Condition: The Pareto condition simply says that if every voter ranks ωi
above ωj, then ωi ≻∗ωj.
• The Condorcet Winner Condition: An outcome is said to be a Condorcet winner if
a majority of candidates prefer it over all other outcomes. To put it another way, a
Condorcet winner is a candidate that would beat every other candidate in a pairwise
election. The Condorcet winner condition says that if ωi is a Condorcet winner, then ωi
should be ranked ﬁrst.
• Independence of Irrelevant Alternatives (IIA): Suppose there are a number of candi-
dates, including ωi and ωj, and voter preferences are such that ωi ≻∗ωj. Now, suppose
