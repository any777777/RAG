---
chunk_id: "book-ca4fca8dd8-chunk-1059"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1059
confidence: "first-pass"
extraction_method: "structured-local"
---

634
Chapter 17
Multiagent Decision Making
The monotonic concession protocol
The negotiation protocol we consider for task-oriented domains is known as the monotonic
concession protocol. The rules of this protocol are as follows.
Monotonic
concession protocol
• Negotiation proceeds in a series of rounds.
• On the ﬁrst round, both agents simultaneously propose a deal, Di = (T1,T2), from the
negotiation set. (This is different from the alternating offers we saw before.)
• An agreement is reached if the two agents propose deals D1 and D2, respectively, such
that either (i) U1(D2) ≥U1(D1) or (ii) U2(D1) ≥U2(D2), that is, if one of the agents
ﬁnds that the deal proposed by the other is at least as good or better than the proposal
it made. If agreement is reached, then the rule for determining the agreement deal is as
follows: If each agent’s offer matches or exceeds that of the other agent, then one of
the proposals is selected at random. If only one proposal exceeds or matches the other’s
proposal, then this is the agreement deal.
• If no agreement is reached, then negotiation proceeds to another round of simultaneous
proposals. In round t +1, each agent must either repeat the proposal from the previous
round or make a concession—a proposal that is more preferred by the other agent (i.e.,
Concession
has higher utility).
• If neither agent makes a concession, then negotiation terminates, and both agents im-
plement the conﬂict deal, carrying out the tasks they were originally assigned.
Since the set of possible deals is ﬁnite, the agents cannot negotiate indeﬁnitely: either the
agents will reach agreement, or a round will occur in which neither agent concedes. However,
the protocol does not guarantee that agreement will be reached quickly: since the number of
possible deals is O(2|T|), it is conceivable that negotiation will continue for a number of
rounds exponential in the number of tasks to be allocated.
The Zeuthen strategy
So far, we have said nothing about how negotiation participants might or should behave when
using the monotonic concession protocol for task-oriented domains. One possible strategy is
the Zeuthen strategy.
Zeuthen strategy
The idea of the Zeuthen strategy is to measure an agent’s willingness to risk conﬂict.
Intuitively, an agent will be more willing to risk conﬂict if the difference in utility between
its current proposal and the conﬂict deal is low. In this case, the agent has little to lose if
negotiation fails and the conﬂict deal is implemented, and so is more willing to risk conﬂict,
and less willing to concede. In contrast, if the difference between the agent’s current proposal
and the conﬂict deal is high, then the agent has more to lose from conﬂict and is therefore
less willing to risk conﬂict—and thus more willing to concede.
Agent i’s willingness to risk conﬂict at round t, denoted riskt
i, is measured as follows:
riskt
i = utility i loses by conceding and accepting j’s offer
utility i loses by not conceding and causing conﬂict.
Until an agreement is reached, the value of riskt
i will be a value between 0 and 1. Higher
values of riskt
i (nearer to 1) indicate that i has less to lose from conﬂict, and so is more
willing to risk conﬂict.
