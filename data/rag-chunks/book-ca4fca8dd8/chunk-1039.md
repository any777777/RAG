---
chunk_id: "book-ca4fca8dd8-chunk-1039"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1039
confidence: "first-pass"
extraction_method: "structured-local"
---

624
Chapter 17
Multiagent Decision Making
• Task announcement processing. On receipt of a task announcement, an agent decides if
it wishes to bid for the advertised task.
• Bid processing. On receiving multiple bids, the manager must decide which agent to
award the task to, and then award the task.
• Award processing. Successful bidders (contractors) must attempt to carry out the task,
which may mean generating new subtasks, which are advertised via further task an-
nouncements.
Despite (or perhaps because of) its simplicity, the contract net is probably the most widely
implemented and best-studied framework for cooperative problem solving. It is naturally
applicable in many settings—a variation of it is enacted every time you request a car with
Uber, for example.
17.4.2 Allocating scarce resources with auctions
One of the most important problems in multiagent systems is that of allocating scarce re-
sources; but we may as well simply say “allocating resources,” since in practice most useful
resources are scarce in some sense. The auction is the most important mechanism for allo-
Auction
cating resources. The simplest setting for an auction is where there is a single resource and
there are multiple possible bidders. Each bidder i has a utility value vi for the item.
Bidder
In some cases, each bidder has a private value for the item. For example, a tacky sweater
might be attractive to one bidder and valueless to another.
In other cases, such as auctioning drilling rights for an oil tract, the item has a com-
mon value—the tract will produce some amount of money, X, and all bidders value a dollar
equally—but there is uncertainty as to what the actual value of X is. Different bidders have
different information, and hence different estimates of the item’s true value. In either case,
bidders end up with their own vi. Given vi, each bidder gets a chance, at the appropriate time
or times in the auction, to make a bid bi. The highest bid, bmax, wins the item, but the price
paid need not be bmax; that’s part of the mechanism design.
The best-known auction mechanism is the ascending-bid auction,3 or English auction,
Ascending-bid
auction
English auction
in which the center starts by asking for a minimum (or reserve) bid bmin. If some bidder
is willing to pay that amount, the center then asks for bmin + d, for some increment d, and
continues up from there. The auction ends when nobody is willing to bid anymore; then the
last bidder wins the item, paying the price bid.
How do we know if this is a good mechanism? One goal is to maximize expected revenue
for the seller. Another goal is to maximize a notion of global utility. These goals overlap to
some extent, because one aspect of maximizing global utility is to ensure that the winner of
the auction is the agent who values the item the most (and thus is willing to pay the most). We
say an auction is efﬁcient if the goods go to the agent who values them most. The ascending-
Eﬃcient
bid auction is usually both efﬁcient and revenue maximizing, but if the reserve price is set too
high, the bidder who values it most may not bid, and if the reserve is set too low, the seller
may get less revenue.
Probably the most important things that an auction mechanism can do is encourage a suf-
ﬁcient number of bidders to enter the game and discourage them from engaging in collusion.
Collusion
Collusion is an unfair or illegal agreement by two or more bidders to manipulate prices. It can
3
The word “auction” comes from the Latin augeo, to increase.
