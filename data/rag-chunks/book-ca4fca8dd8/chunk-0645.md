---
chunk_id: "book-ca4fca8dd8-chunk-0645"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 645
confidence: "first-pass"
extraction_method: "structured-local"
---

390
Chapter 11
Automated Planning
the robot’s behavior seems purposive rather than rote; we assume it results not from a vast,
precomputed contingent plan but from an online replanning process—which means that the
robot does need to know what it’s trying to do.
Replanning presupposes some form of execution monitoring to determine the need for
Execution
monitoring
a new plan. One such need arises when a contingent planning agent gets tired of planning
for every little contingency, such as whether the sky might fall on its head.4 This means
that the contingent plan is left in an incomplete form. For example, some branches of a
partially constructed contingent plan can simply say Replan; if such a branch is reached
during execution, the agent reverts to planning mode. As we mentioned earlier, the decision
as to how much of the problem to solve in advance and how much to leave to replanning
is one that involves tradeoffs among possible events with different costs and probabilities of
occurring. Nobody wants to have a car break down in the middle of the Sahara desert and
only then think about having enough water.
Replanning may be needed if the agent’s model of the world is incorrect. The model
for an action may have a missing precondition—for example, the agent may not know that
Missing precondition
removing the lid of a paint can often requires a screwdriver. The model may have a missing
effect—painting an object may get paint on the ﬂoor as well. Or the model may have a
Missing eﬀect
missing ﬂuent that is simply absent from the representation altogether—for example, the
Missing ﬂuent
model given earlier has no notion of the amount of paint in a can, of how its actions affect
this amount, or of the need for the amount to be nonzero. The model may also lack provision
for exogenous events such as someone knocking over the paint can. Exogenous events can
Exogenous event
also include changes in the goal, such as the addition of the requirement that the table and
chair not be painted black. Without the ability to monitor and replan, an agent’s behavior is
likely to be fragile if it relies on absolute correctness of its model.
The online agent has a choice of (at least) three different approaches for monitoring the
environment during plan execution:
• Action monitoring: before executing an action, the agent veriﬁes that all the precondi-
Action monitoring
tions still hold.
• Plan monitoring: before executing an action, the agent veriﬁes that the remaining plan
Plan monitoring
will still succeed.
• Goal monitoring: before executing an action, the agent checks to see if there is a better
Goal monitoring
set of goals it could be trying to achieve.
In Figure 11.12 we see a schematic of action monitoring. The agent keeps track of both its
original plan, whole plan, and the part of the plan that has not been executed yet, which is
denoted by plan. After executing the ﬁrst few steps of the plan, the agent expects to be in
state E. But the agent observes that it is actually in state O. It then needs to repair the plan by
ﬁnding some point P on the original plan that it can get back to. (It may be that P is the goal
state, G.) The agent tries to minimize the total cost of the plan: the repair part (from O to P)
plus the continuation (from P to G).
4
In 1954, a Mrs. Hodges of Alabama was hit by meteorite that crashed through her roof. In 1992, a piece of
the Mbale meteorite hit a small boy on the head; fortunately, its descent was slowed by banana leaves (Jenniskens
et al., 1994). And in 2009, a German boy claimed to have been hit in the hand by a pea-sized meteorite. No serious
injuries resulted from any of these incidents, suggesting that the need for preplanning against such contingencies
is sometimes overstated.
