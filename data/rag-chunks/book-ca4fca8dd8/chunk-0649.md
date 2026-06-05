---
chunk_id: "book-ca4fca8dd8-chunk-0649"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 649
confidence: "first-pass"
extraction_method: "structured-local"
---

392
Chapter 11
Automated Planning
Plan monitoring achieves this by checking the preconditions for success of the entire
remaining plan—that is, the preconditions of each step in the plan, except those preconditions
that are achieved by another step in the remaining plan. Plan monitoring cuts off execution of
a doomed plan as soon as possible, rather than continuing until the failure actually occurs.5
Plan monitoring also allows for serendipity—accidental success. If someone comes along
and paints the table red at the same time that the agent is painting the chair red, then the ﬁnal
plan preconditions are satisﬁed (the goal has been achieved), and the agent can go home early.
It is straightforward to modify a planning algorithm so that each action in the plan is an-
notated with the action’s preconditions, thus enabling action monitoring. It is slightly more
complex to enable plan monitoring. Partial-order planners have the advantage that they have
already built up structures that contain the relations necessary for plan monitoring. Augment-
ing state-space planners with the necessary annotations can be done by careful bookkeeping
as the goal ﬂuents are regressed through the plan.
Now that we have described a method for monitoring and replanning, we need to ask,
“Does it work?” This is a surprisingly tricky question. If we mean, “Can we guarantee
that the agent will always achieve the goal?” then the answer is no, because the agent could
inadvertently arrive at a dead end from which there is no repair. For example, the vacuum
agent might have a faulty model of itself and not know that its batteries can run out. Once
they do, it cannot repair any plans. If we rule out dead ends—assume that there exists a plan
to reach the goal from any state in the environment—and assume that the environment is
really nondeterministic, in the sense that such a plan always has some chance of success on
any given execution attempt, then the agent will eventually reach the goal.
Trouble occurs when a seemingly-nondeterministic action is not actually random, but
rather depends on some precondition that the agent does not know about. For example,
sometimes a paint can may be empty, so painting from that can has no effect. No amount
of retrying is going to change this.6 One solution is to choose randomly from among the set
of possible repair plans, rather than to try the same one each time. In this case, the repair
plan of opening another can might work. A better approach is to learn a better model. Every
prediction failure is an opportunity for learning; an agent should be able to modify its model
of the world to accord with its percepts. From then on, the replanner will be able to come up
with a repair that gets at the root problem, rather than relying on luck to choose a good repair.
11.6 Time, Schedules, and Resources
Classical planning talks about what to do, in what order, but does not talk about time: how
long an action takes and when it occurs. For example, in the airport domain we could produce
a plan saying what planes go where, carrying what, but could not specify departure and arrival
times. This is the subject matter of scheduling.
Scheduling
The real world also imposes resource constraints: an airline has a limited number of
Resource constraint
staff, and staff who are on one ﬂight cannot be on another at the same time. This section
introduces techniques for planning and scheduling problems with resource constraints.
5
Plan monitoring means that ﬁnally, after 374 pages, we have an agent that is smarter than a dung beetle (see
page 59). A plan-monitoring agent would notice that the dung ball was missing from its grasp and would replan
to get another ball and plug its hole.
6
Futile repetition of a plan repair is exactly the behavior exhibited by the sphex wasp (page 59).
