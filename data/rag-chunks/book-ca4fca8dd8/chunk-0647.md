---
chunk_id: "book-ca4fca8dd8-chunk-0647"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 647
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.5
Planning and Acting in Nondeterministic Domains
391
whole plan
plan
repair
S
P
O
E
G
continuation
Figure 11.12 At ﬁrst, the sequence “whole plan” is expected to get the agent from S to G.
The agent executes steps of the plan until it expects to be in state E, but observes that it is
actually in O. The agent then replans for the minimal repair plus continuation to reach G.
Now let’s return to the example problem of achieving a chair and table of matching color.
Suppose the agent comes up with this plan:
[LookAt(Table),LookAt(Chair),
if Color(Table,c)∧Color(Chair,c) then NoOp
else [RemoveLid(Can1),LookAt(Can1),
if Color(Table,c)∧Color(Can1,c) then Paint(Chair,Can1)
else REPLAN]].
Now the agent is ready to execute the plan. The agent observes that the table and can of
paint are white and the chair is black. It then executes Paint(Chair,Can1). At this point a
classical planner would declare victory; the plan has been executed. But an online execution
monitoring agent needs to check that the action succeeded.
Suppose the agent perceives that the chair is a mottled gray because the black paint is
showing through. The agent then needs to ﬁgure out a recovery position in the plan to aim for
and a repair action sequence to get there. The agent notices that the current state is identical
to the precondition before the Paint(Chair,Can1) action, so the agent chooses the empty
sequence for repair and makes its plan be the same [Paint] sequence that it just attempted.
With this new plan in place, execution monitoring resumes, and the Paint action is retried.
This behavior will loop until the chair is perceived to be completely painted. But notice that
the loop is created by a process of plan–execute–replan, rather than by an explicit loop in a
plan. Note also that the original plan need not cover every contingency. If the agent reaches
the step marked REPLAN, it can then generate a new plan (perhaps involving Can2).
Action monitoring is a simple method of execution monitoring, but it can sometimes lead
to less than intelligent behavior. For example, suppose there is no black or white paint, and
the agent constructs a plan to solve the painting problem by painting both the chair and table
red. Suppose that there is only enough red paint for the chair. With action monitoring, the
agent would go ahead and paint the chair red, then notice that it is out of paint and cannot
paint the table, at which point it would replan a repair—perhaps painting both chair and table
green. A plan-monitoring agent can detect failure whenever the current state is such that the
remaining plan no longer works. Thus, it would not waste time painting the chair red.
