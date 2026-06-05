---
chunk_id: "book-ca4fca8dd8-chunk-1051"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1051
confidence: "first-pass"
extraction_method: "structured-local"
---

630
Chapter 17
Multiagent Decision Making
one voter changed their preferences in some way, but not about the relative ranking of
ωi and ωj. The IIA condition says that, ωi ≻∗ωj should not change.
• No Dictatorships: It should not be the case that the social welfare function simply
outputs one voter’s preferences and ignores all other voters.
These four conditions seem reasonable, but a fundamental theorem of social choice theory
called Arrow’s theorem (due to Kenneth Arrow) tells us that it is impossible to satisfy all
Arrow’s theorem
four conditions (for cases where there are at least three outcomes). That means that for
any social choice mechanism we might care to pick, there will be some situations (perhaps
unusual or pathological) that lead to controversial outcomes. However, it does not mean that
democratic decision making is hopeless in most cases. We have not yet seen any actual voting
procedures, so let’s now look at some.
• With just two candidates, simple majority vote (the standard method in the US and
Simple majority vote
UK) is the favored mechanism. We ask each voter which of the two candidates they
prefer, and the one with the most votes is the winner.
• With more than two outcomes, plurality voting is a common system. We ask each
Plurality voting
voter for their top choice, and select the candidate(s) (more than one in the case of ties)
who get the most votes, even if nobody gets a majority. While it is common, plurality
voting has been criticized for delivering unpopular outcomes. A key problem is that it
only takes into account the top-ranked candidate in each voter’s preferences.
• The Borda count (after Jean-Charles de Borda, a contemporary and rival of Condorcet)
Borda count
is a voting procedure that takes into account all the information in a voter’s preference
ordering. Suppose we have k candidates. Then for each voter i, we take their preference
ordering ≻i, and give a score of k to the top ranked candidate, a score of k −1 to the
second-ranked candidate, and so on down to the least-favored candidate in i’s ordering.
The total score for each candidate is their Borda count, and to obtain the social outcome
≻∗, outcomes are ordered by their Borda count—highest to lowest. One practical prob-
lem with this system is that it asks voters to express preferences on all the candidates,
and some voters may only care about a subset of candidates.
• In approval voting, voters submit a subset of the candidates that they approve of. The
Approval voting
winner(s) are those who are approved by the most voters. This system is often used
when the task is to choose multiple winners.
• In instant runoff voting, voters rank all the candidates, and if a candidate has a major-
Instant runoﬀvoting
ity of ﬁrst-place votes, they are declared the winner. If not, the candidate with the fewest
ﬁrst-place votes is eliminated. That candidate is removed from all the preference rank-
ings (so those voters who had the eliminated candidate as their ﬁrst choice now have
another candidate as their new ﬁrst choice) and the process is repeated. Eventually,
some candidate will have a majority of ﬁrst-place votes (unless there is a tie).
• In true majority rule voting, the winner is the candidate who beats every other can-
True majority rule
voting
didate in pairwise comparisons. Voters are asked for a full preference ranking of all
candidates. We say that ω beats ω′, if more voters have ω ≻ω′ than have ω′ ≻ω. This
system has the nice property that the majority always agrees on the winner, but it has
the bad property that not every election will be decided: in the Condorcet paradox, for
example, no candidate wins a majority.
