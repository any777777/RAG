---
chunk_id: "book-ca4fca8dd8-chunk-1057"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1057
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 17.4
Making Collective Decisions
633
offer that A2 may as well accept because A2 can do no better than γ2 at this point in time. (If
you are worried about what happens with ties, just make the offer be (1−(γ2 +ϵ),γ2 +ϵ) for
some small value of ϵ.)
So, the two strategies of A1 offering (1−γ2,γ2), and A2 accepting that offer are in Nash
equilibrium. Patient players (those with a larger γ2) will be able to obtain larger pieces of the
pie under this protocol: in this setting, patience truly is a virtue.
Now consider the general case, where there are no bounds on the number of rounds. As
in the 1-round case, A1 can craft a proposal that A2 should accept, because it gives A2 the
maximal achievable amount, given the discount factors. It turns out that A1 will get
1−γ2
1−γ1γ2
and A2 will get the remainder.
Negotiation in task-oriented domains
In this section, we consider negotiation for task-oriented domains. In such a domain, a set of
Task-oriented
domain
tasks must be carried out, and each task is initially assigned to a set of agents. The agents may
be able to beneﬁt by negotiating on who will carry out which tasks. For example, suppose
some tasks are done on a lathe machine and others on a milling machine, and that any agent
using a machine must incur a signiﬁcant setup cost. Then it would make sense for one agent
to offer another “I have to set up on the milling machine anyway; how about if I do all your
milling tasks, and you do all my lathe tasks?”
Unlike the bargaining scenario, we start with an initial allocation, so if the agents fail to
agree on any offers, they perform the tasks T 0
i that they were originally allocated.
To keep things simple, we will again assume just two agents. Let T be the set of all tasks
and let (T 0
1 ,T 0
2 ) denote the initial allocation of tasks to the two agents at time 0. Each task
in T must be assigned to exactly one agent. We assume we have a cost function c, which
for every set of tasks T ′ gives a positive real number c(T ′) indicating the cost to any agent
of carrying out the tasks T ′. (Assume the cost depends only on the tasks, not on the agent
carrying out the task.) The cost function is monotonic—adding more tasks never reduces the
cost—and the cost of doing nothing is zero: c({}) = 0. As an example, suppose the cost of
setting up the milling machine is 10 and each milling task costs 1, then the cost of a set of
two milling tasks would be 12, and the cost of a set of ﬁve would be 15.
An offer of the form (T1,T2) means that agent i is committed to performing the set of
tasks Ti, at cost c(Ti). The utility to agent i is the amount they have to gain from accepting
the offer—the difference between the cost of doing this new set of tasks versus the originally
assigned set of tasks:
Ui((T1,T2)) = c(Ti)−c(T 0
i ).
An offer (T1,T2) is individually rational if Ui((T1,T2)) ≥0 for both agents. If a deal is not
Individually rational
individually rational, then at least one agent can do better by simply performing the tasks it
was originally allocated.
The negotiation set for task-oriented domains (assuming rational agents) is the set of
offers that are both individually rational and Pareto optimal. There is no sense making an
individually irrational offer that will be refused, nor in making an offer when there is a better
offer that improves one agent’s utility without hurting anyone else.
