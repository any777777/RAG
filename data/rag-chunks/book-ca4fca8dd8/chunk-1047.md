---
chunk_id: "book-ca4fca8dd8-chunk-1047"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1047
confidence: "first-pass"
extraction_method: "structured-local"
---

628
Chapter 17
Multiagent Decision Making
It turns out there is a mechanism design, known as the Vickrey–Clarke–Groves or VCG
VCG
mechanism, which has two favorable properties. First, it is utility maximizing—that is, it
maximizes the global utility, which is the sum of the utilities for all parties, ∑i vi. Second,
the mechanism is truth-revealing—the dominant strategy for all agents is to reveal their true
value. There is no need for them to engage in complicated strategic bidding calculations.
We will give an example using the problem of allocating some common goods. Suppose a
city decides it wants to install some free wireless Internet transceivers. However, the number
of transceivers available is less than the number of neighborhoods that want them. The city
wants to maximize global utility, but if it says to each neighborhood council “How much do
you value a free transceiver (and by the way we will give them to the parties that value them
the most)?” then each neighborhood will have an incentive to report a very high value. The
VCG mechanism discourages this ploy and gives them an incentive to report their true value.
It works as follows:
1. The center asks each agent to report its value for an item, vi.
2. The center allocates the goods to a set of winners, W, to maximize ∑i∈W vi.
3. The center calculates for each winning agent how much of a loss their individual pres-
ence in the game has caused to the losers (who each got 0 utility, but could have got vj
if they were a winner).
4. Each winning agent then pays to the center a tax equal to this loss.
For example, suppose there are 3 transceivers available and 5 bidders, who bid 100, 50,
40, 20, and 10. Thus the set of 3 winners, W, are the ones who bid 100, 50, and 40 and the
global utility from allocating these goods is 190. For each winner, it is the case that had they
not been in the game, the bid of 20 would have been a winner. Thus, each winner pays a tax
of 20 to the center.
All winners should be happy because they pay a tax that is less than their value, and
all losers are as happy as they can be, because they value the goods less than the required
tax. That’s why the mechanism is truth-revealing. In this example, the crucial value is 20; it
would be irrational to bid above 20 if your true value was actually below 20, and vice versa.
Since the crucial value could be anything (depending on the other bidders), that means that is
always irrational to bid anything other than your true value.
The VCG mechanism is very general, and can be applied to all sorts of games, not just
auctions, with a slight generalization of the mechanism described above. For example, in a
combinatorial auction there are multiple different items available and each bidder can place
multiple bids, each on a subset of the items. For example, in bidding on plots of land, one
bidder might want either plot X or plot Y but not both; another might want any three adjacent
plots, and so on. The VCG mechanism can be used to ﬁnd the optimal outcome, although
with 2N subsets of N goods to contend with, the computation of the optimal outcome is NP-
complete. With a few caveats the VCG mechanism is unique: every other optimal mechanism
is essentially equivalent.
17.4.3 Voting
The next class of mechanisms that we look at are voting procedures, of the type that are used
for political decision making in democratic societies. The study of voting procedures derives
from the domain of social choice theory.
Social choice theory
