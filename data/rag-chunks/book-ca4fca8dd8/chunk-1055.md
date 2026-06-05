---
chunk_id: "book-ca4fca8dd8-chunk-1055"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1055
confidence: "first-pass"
extraction_method: "structured-local"
---

632
Chapter 17
Multiagent Decision Making
Now, how should agents negotiate in this setting? To understand the answer to this question,
we will ﬁrst look at a few simpler cases.
First, suppose that we allow just one round to take place. Thus, A1 makes a proposal;
A2 can either accept it (in which case the deal is implemented), or reject it (in which case
the conﬂict deal is implemented). This is an ultimatum game. In this case, it turns out that
Ultimatum game
A1—the ﬁrst mover—has all the power. Suppose that A1 proposes to get all the pie, that is,
proposes the deal (1,0). If A2 rejects, then the conﬂict deal is implemented; since by deﬁni-
tion A2 would prefer to get 0 rather than the conﬂict deal, A2 would be better off accepting.
Of course, A1 cannot do better than getting the whole pie. Thus, these two strategies—A1
proposes to get the whole pie, and A2 accepts—form a Nash equilibrium.
Now consider the case where we permit exactly two rounds of negotiation. Now the
power has shifted: A2 can simply reject the ﬁrst offer, thereby turning the game into a one-
round game in which A2 is the ﬁrst mover and thus will get the whole pie. In general, if the
number of rounds is a ﬁxed number, then whoever moves last will get all the pie.
Now let’s move on to the general case, where there is no bound on the number of rounds.
Suppose that A1 uses the following strategy:
Always propose (1,0), and always reject any counteroffer.
What is A2’s best response to this? If A2 continually rejects the proposal, then the agents will
negotiate forever, which by deﬁnition is the worst outcome for A2 (as well as for A1). So
A2 can do no better than accepting the ﬁrst proposal that A1 makes. Again, this is a Nash
equilibrium. But what if A1 uses the strategy:
Always propose (0.8,0.2), and always reject any offer.
By a similar argument we can see that for this offer or for any possible deal (x,1 −x) in
▶
the negotiation set, there is a Nash equilibrium pair of negotiation strategies such that the
outcome will be agreement on the deal in the ﬁrst time period.
Impatient agents
This analysis tells us that if no constraints are placed on the number of rounds then there will
be an inﬁnite number of Nash equilibria. So let’s add an assumption:
For any outcome x and times t1 and t2, where t1 < t2, both agents would prefer
outcome x at time t1 over outcome x at time t2.
In other words, agents are impatient. A standard approach to impatience is to use a discount
factor γi (see page 555) for each agent (0 ≤γi < 1). Suppose that at some point in the
negotiation agent i is offered a slice of the pie of size x. The value of the slice x at time t is
γt
ix. Thus on the ﬁrst negotiation step (time 0), the value is γ0
i x = x, and at any subsequent
point in time the value of the same offer will be less. A larger value for γi (closer to 1) thus
implies more patience; a smaller value means less patience.
To analyze the general case, let’s ﬁrst consider bargaining over ﬁxed periods of time, as
above. The 1-round case has the same analysis as given above: we simply have an ultimatum
game. With two rounds the situation changes, because the value of the pie reduces in accor-
dance with discount factors γi. Suppose A2 rejects A1’s initial proposal. Then A2 will get the
whole pie with an ultimatum in the second round. But the value of that whole pie has reduced:
it is only worth γ2 to A2. Agent A1 can take this fact into account by offering (1−γ2,γ2), an
