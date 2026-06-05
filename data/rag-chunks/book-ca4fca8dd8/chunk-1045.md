---
chunk_id: "book-ca4fca8dd8-chunk-1045"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1045
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.4
Making Collective Decisions
627
clicks on the ad. The top slots are considered more valuable because they are more likely to
be noticed and clicked on.
Imagine that three bidders, b1,b2 and b3, have valuations for a click of v1 =200,v2 =180,
and v3 =100, and that n = 2 slots are available; and it is known that the top spot is clicked on
5% of the time and the bottom spot 2%. If all bidders bid truthfully, then b1 wins the top slot
and pays 180, and has an expected return of (200−180)×0.05=1. The second slot goes to
b2. But b1 can see that if she were to bid anything in the range 101–179, she would concede
the top slot to b2, win the second slot, and yield an expected return of (200−100)×.02=2.
Thus, b1 can double her expected return by bidding less than her true value in this case.
In general, bidders in this n + 1 price auction must spend a lot of energy analyzing the
bids of others to determine their best strategy; there is no simple dominant strategy.
Aggarwal et al. (2006) show that there is a unique truthful auction mechanism for this
multislot problem, in which the winner of slot j pays the price for slot j just for those addi-
tional clicks that are available at slot j and not at slot j +1. The winner pays the price for the
lower slot for the remaining clicks. In our example, b1 would bid 200 truthfully, and would
pay 180 for the additional .05 −.02=.03 clicks in the top slot, but would pay only the cost
of the bottom slot, 100, for the remaining .02 clicks. Thus, the total return to b1 would be
(200−180)×.03+(200−100)×.02=2.6.
Another example of where auctions can come into play within AI is when a collection of
agents are deciding whether to cooperate on a joint plan. Hunsberger and Grosz (2000) show
that this can be accomplished efﬁciently with an auction in which the agents bid for roles in
the joint plan.
Common goods
Now let’s consider another type of game, in which countries set their policy for controlling
air pollution. Each country has a choice: they can reduce pollution at a cost of -10 points for
implementing the necessary changes, or they can continue to pollute, which gives them a net
utility of -5 (in added health costs, etc.) and also contributes -1 points to every other country
(because the air is shared across countries). Clearly, the dominant strategy for each country
is “continue to pollute,” but if there are 100 countries and each follows this policy, then each
country gets a total utility of -104, whereas if every country reduced pollution, they would
each have a utility of -10. This situation is called the tragedy of the commons: if nobody has
Tragedy of the
commons
to pay for using a common resource, then it may be exploited in a way that leads to a lower
total utility for all agents. It is similar to the prisoner’s dilemma: there is another solution
to the game that is better for all parties, but there appears to be no way for rational agents to
arrive at that solution under the current game.
One approach for dealing with the tragedy of the commons is to change the mechanism to
one that charges each agent for using the commons. More generally, we need to ensure that
all externalities—effects on global utility that are not recognized in the individual agents’
Externalities
transactions—are made explicit.
Setting the prices correctly is the difﬁcult part. In the limit, this approach amounts to
creating a mechanism in which each agent is effectively required to maximize global utility,
but can do so by making a local decision. For this example, a carbon tax would be an example
of a mechanism that charges for use of the commons in a way that, if implemented well,
maximizes global utility.
