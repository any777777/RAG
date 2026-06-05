---
chunk_id: "book-ca4fca8dd8-chunk-1043"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1043
confidence: "first-pass"
extraction_method: "structured-local"
---

626
Chapter 17
Multiagent Decision Making
can always bid higher. Thus, the competitors may not enter at all, and the advantaged com-
pany ends up winning at the reserve price.
Another negative property of the English auction is its high communication costs. Either
the auction takes place in one room or all bidders have to have high-speed, secure communi-
cation lines; in either case they have to have time to go through several rounds of bidding.
An alternative mechanism, which requires much less communication, is the sealed-bid
auction. Each bidder makes a single bid and communicates it to the auctioneer, without the
Sealed-bid auction
other bidders seeing it. With this mechanism, there is no longer a simple dominant strategy.
If your value is vi and you believe that the maximum of all the other agents’ bids will be bo,
then you should bid bo +ϵ, for some small ϵ, if that is less than vi. Thus, your bid depends on
your estimation of the other agents’ bids, requiring you to do more work. Also, note that the
agent with the highest vi might not win the auction. This is offset by the fact that the auction
is more competitive, reducing the bias toward an advantaged bidder.
A small change in the mechanism for sealed-bid auctions leads to the sealed-bid second-
price auction, also known as a Vickrey auction.5 In such auctions, the winner pays the
Sealed-bid
second-price auction
Vickrey auction
price of the second-highest bid, bo, rather than paying his own bid. This simple modiﬁcation
completely eliminates the complex deliberations required for standard (or ﬁrst-price) sealed-
bid auctions, because the dominant strategy is now simply to bid vi; the mechanism is truth-
revealing. Note that the utility of agent i in terms of his bid bi, his value vi, and the best bid
among the other agents, bo, is
Ui =
 (vi −bo)
if bi > bo
0
otherwise.
To see that bi = vi is a dominant strategy, note that when (vi−bo) is positive, any bid that wins
the auction is optimal, and bidding vi in particular wins the auction. On the other hand, when
(vi−bo) is negative, any bid that loses the auction is optimal, and bidding vi in particular loses
the auction. So bidding vi is optimal for all possible values of bo, and in fact, vi is the only bid
that has this property. Because of its simplicity and the minimal computation requirements
for both seller and bidders, the Vickrey auction is widely used in distributed AI systems.
Internet search engines conduct several trillion auctions each year to sell advertisements
along with their search results, and online auction sites handle $100 billion a year in goods,
all using variants of the Vickrey auction. Note that the expected value to the seller is bo,
which is the same expected return as the limit of the English auction as the increment d goes
to zero. This is actually a very general result: the revenue equivalence theorem states that,
Revenue equivalence
theorem
with a few minor caveats, any auction mechanism in which bidders have values vi known only
to themselves (but know the probability distribution from which those values are sampled),
will yield the same expected revenue. This principle means that the various mechanisms are
not competing on the basis of revenue generation, but rather on other qualities.
Although the second-price auction is truth-revealing, it turns out that auctioning n goods
with an n+1 price auction is not truth-revealing. Many Internet search engines use a mech-
anism where they auction n slots for ads on a page. The highest bidder wins the top spot,
the second highest gets the second spot, and so on. Each winner pays the price bid by the
next-lower bidder, with the understanding that payment is made only if the searcher actually
5
Named after William Vickrey (1914–1996), who won the 1996 Nobel Prize in economics for this work and
died of a heart attack three days later.
