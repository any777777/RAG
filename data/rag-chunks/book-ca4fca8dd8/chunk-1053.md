---
chunk_id: "book-ca4fca8dd8-chunk-1053"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1053
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.4
Making Collective Decisions
631
Strategic manipulation
Besides Arrow’s Theorem, another important negative results in the area of social choice
theory is the Gibbard–Satterthwaite Theorem. This result relates to the circumstances
Gibbard–
Satterthwaite
Theorem
under which a voter can beneﬁt from misrepresenting their preferences.
Recall that a social choice function takes as input a preference order for each voter, and
gives as output a set of winning candidates. Each voter has, of course, their own true prefer-
ences, but there is nothing in the deﬁnition of a social choice function that requires voters to
report their preferences truthfully; they can declare whatever preferences they like.
In some cases, it can make sense for a voter to misrepresent their preferences. For exam-
ple, in plurality voting, voters who think their preferred candidate has no chance of winning
may vote for their second choice instead. That means plurality voting is a game in which
voters have to think strategically (about the other voters) to maximize their expected utility.
This raises an interesting question: can we design a voting mechanism that is immune to
such manipulation—a mechanism that is truth-revealing? The Gibbard–Satterthwaite Theo-
rem tells us that we can not: Any social choice function that satisﬁes the Pareto condition for ◀
a domain with more than two outcomes is either manipulable or a dictatorship. That is, for
any “reasonable” social choice procedure, there will be some circumstances under which a
voter can in principle beneﬁt by misrepresenting their preferences. However, it does not tell
us how such manipulation might be done; and it does not tell us that such manipulation is
likely in practice.
17.4.4 Bargaining
Bargaining, or negotiation, is another mechanism that is used frequently in everyday life. It
has been studied in game theory since the 1950s and more recently has become a task for
automated agents. Bargaining is used when agents need to reach agreement on a matter of
common interest. The agents make offers (also called proposals or deals) to each other under
speciﬁc protocols, and either accept or reject each offer.
Bargaining with the alternating oﬀers protocol
One inﬂuential bargaining protocol is the alternating offers bargaining model. For simplic-
Alternating oﬀers
bargaining model
ity we’ll again assume just two agents. Bargaining takes place in a sequence of rounds. A1
begins, at round 0, by making an offer. If A2 accepts the offer, then the offer is implemented.
If A2 rejects the offer, then negotiation moves to the next round. This time A2 makes an offer
and A1 chooses to accept or reject it, and so on. If the negotiation never terminates (because
agents reject every offer) then we deﬁne the outcome to be the conﬂict deal. A convenient
Conﬂict deal
simplifying assumption is that both agents prefer to reach an outcome—any outcome—in
ﬁnite time rather than being stuck in the inﬁnitely time-consuming conﬂict deal.
We will use the scenario of dividing a pie to illustrate alternating offers. The idea is that
there is some resource (the “pie”) whose value is 1, which can be divided into two parts, one
part for each agent. Thus an offer in this scenario is a pair (x,1 −x), where x is the amount
of the pie that A1 gets, and 1−x is the amount that A2 gets. The space of possible deals (the
negotiation set) is thus:
Negotiation set
{(x,1−x) : 0 ≤x ≤1}.
