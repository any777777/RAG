---
chunk_id: "book-ca4fca8dd8-chunk-1041"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1041
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.4
Making Collective Decisions
625
happen in secret backroom deals or tacitly, within the rules of the mechanism. For example,
in 1999, Germany auctioned ten blocks of cellphone spectrum with a simultaneous auction
(bids were taken on all ten blocks at the same time), using the rule that any bid must be a min-
imum of a 10% raise over the previous bid on a block. There were only two credible bidders,
and the ﬁrst, Mannesman, entered the bid of 20 million deutschmark on blocks 1-5 and 18.18
million on blocks 6-10. Why 18.18M? One of T-Mobile’s managers said they “interpreted
Mannesman’s ﬁrst bid as an offer.” Both parties could compute that a 10% raise on 18.18M
is 19.99M; thus Mannesman’s bid was interpreted as saying “we can each get half the blocks
for 20M; let’s not spoil it by bidding the prices up higher.” And in fact T-Mobile bid 20M on
blocks 6-10 and that was the end of the bidding.
The German government got less than they expected, because the two competitors were
able to use the bidding mechanism to come to a tacit agreement on how not to compete.
From the government’s point of view, a better result could have been obtained by any of these
changes to the mechanism: a higher reserve price; a sealed-bid ﬁrst-price auction, so that
the competitors could not communicate through their bids; or incentives to bring in a third
bidder. Perhaps the 10% rule was an error in mechanism design, because it facilitated the
precise signaling from Mannesman to T-Mobile.
In general, both the seller and the global utility function beneﬁt if there are more bidders,
although global utility can suffer if you count the cost of wasted time of bidders that have no
chance of winning. One way to encourage more bidders is to make the mechanism easier for
them. After all, if it requires too much research or computation on the part of the bidders,
they may decide to take their money elsewhere.
So it is desirable that the bidders have a dominant strategy. Recall that “dominant”
means that the strategy works against all other strategies, which in turn means that an agent
can adopt it without regard for the other strategies. An agent with a dominant strategy can just
bid, without wasting time contemplating other agents’ possible strategies. A mechanism by
which agents have a dominant strategy is called a strategy-proof mechanism. If, as is usually
Strategy-proof
the case, that strategy involves the bidders revealing their true value, vi, then it is called
a truth-revealing, or truthful, auction; the term incentive compatible is also used. The
Truth-revealing
revelation principle states that any mechanism can be transformed into an equivalent truth-
Revelation principle
revealing mechanism, so part of mechanism design is ﬁnding these equivalent mechanisms.
It turns out that the ascending-bid auction has most of the desirable properties. The bidder
with the highest value vi gets the goods at a price of bo +d, where bo is the highest bid among
all the other agents and d is the auctioneer’s increment.4 Bidders have a simple dominant
strategy: keep bidding as long as the current cost is below your vi. The mechanism is not
quite truth-revealing, because the winning bidder reveals only that his vi ≥bo +d; we have a
lower bound on vi but not an exact amount.
A disadvantage (from the point of view of the seller) of the ascending-bid auction is that
it can discourage competition. Suppose that in a bid for cellphone spectrum there is one
advantaged company that everyone agrees would be able to leverage existing customers and
infrastructure, and thus can make a larger proﬁt than anyone else. Potential competitors can
see that they have no chance in an ascending-bid auction, because the advantaged company
4
There is actually a small chance that the agent with highest vi fails to get the goods, in the case in which
bo < vi < bo +d. The chance of this can be made arbitrarily small by decreasing the increment d.
