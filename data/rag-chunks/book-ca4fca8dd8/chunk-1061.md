---
chunk_id: "book-ca4fca8dd8-chunk-1061"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1061
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
635
The Zeuthen strategy says that each agent’s ﬁrst proposal should be a deal in the negoti-
ation set that maximizes its own utility (there may be more than one). After that, the agent
who should concede on round t of negotiation should be the one with the smaller value of
risk—the one with the most to lose from conﬂict if neither concedes.
The next question to answer is how much should be conceded? The answer provided by
the Zeuthen strategy is, “Just enough to change the balance of risk to the other agent.” That
is, an agent should make the smallest concession that will make the other agent concede on
the next round.
There is one ﬁnal reﬁnement to the Zeuthen strategy. Suppose that at some point both
agents have equal risk. Then, according to the strategy, both should concede. But, knowing
this, one agent could potentially “defect” by not conceding, and so beneﬁt. To avoid the
possibility of both conceding at this point, we extend the strategy by having the agents “ﬂip a
coin” to decide who should concede if ever an equal risk situation is reached.
With this strategy, agreement will be Pareto optimal and individually rational. However,
since the space of possible deals is exponential in the number of tasks, following this strategy
may require O(2|T|) computations of the cost function at each negotiation step. Finally, the
Zeuthen strategy (with the coin ﬂipping rule) is in Nash equilibrium.
Summary
• Multiagent planning is necessary when there are other agents in the environment with
which to cooperate or compete. Joint plans can be constructed, but must be augmented
with some form of coordination if two agents are to agree on which joint plan to execute.
• Game theory describes rational behavior for agents in situations in which multiple
agents interact. Game theory is to multiagent decision making as decision theory is to
single-agent decision making.
• Solution concepts in game theory are intended to characterize rational outcomes of a
game—outcomes that might occur if every agent acted rationally.
• Non-cooperative game theory assumes that agents must make their decisions indepen-
dently. Nash equilibrium is the most important solution concept in non-cooperative
game theory. A Nash equilibrium is a strategy proﬁle in which no agent has an incen-
tive to deviate from its speciﬁed strategy. We have techniques for dealing with repeated
games and sequential games.
• Cooperative game theory considers settings in which agents can make binding agree-
ments to form coalitions in order to cooperate. Solution concepts in cooperative game
attempt to formulate which coalitions are stable (the core) and how to fairly divide the
value that a coalition obtains (the Shapley value).
• Specialized techniques are available for certain important classes of multiagent deci-
sion: the contract net for task sharing; auctions are used to efﬁciently allocate scarce
resources; bargaining for reaching agreements on matters of common interest; and vot-
ing procedures for aggregating preferences.
