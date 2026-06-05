---
chunk_id: "book-ca4fca8dd8-chunk-0985"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 985
confidence: "first-pass"
extraction_method: "structured-local"
---

594
Chapter 17
Multiagent Decision Making
speciﬁes what each player has to do: A should move over to the right baseline and hit the ball,
while B should just stay put at the net:
PLAN 1:
A : [Go(A,RightBaseline),Hit(A,Ball)]
B : [NoOp(B),NoOp(B)].
Problems arise, however, when a plan dictates that both agents hit the ball at the same time.
In the real world, this won’t work, but the action schema for Hit says that the ball will be
returned successfully. The difﬁculty is that preconditions constrain the state in which an
action by itself can be executed successfully, but do not constrain other concurrent actions
that might mess it up.
We solve this problem by augmenting action schemas with one new feature: a concurrent
action constraint stating which actions must or must not be executed concurrently. For
Concurrent action
constraint
example, the Hit action could be described as follows:
Action(Hit(actor,Ball),
CONCURRENT:∀b b ̸= actor ⇒¬Hit(b,Ball)
PRECOND:Approaching(Ball,loc)∧At(actor,loc)
EFFECT:Returned(Ball)).
In other words, the Hit action has its stated effect only if no other Hit action by another agent
occurs at the same time. (In the SATPLAN approach, this would be handled by a partial
action exclusion axiom.) For some actions, the desired effect is achieved only when another
action occurs concurrently. For example, two agents are needed to carry a cooler full of
beverages to the tennis court:
Action(Carry(actor,cooler,here,there),
CONCURRENT:∃b b ̸= actor ∧Carry(b,cooler,here,there)
PRECOND:At(actor,here)∧At(cooler,here)∧Cooler(cooler)
EFFECT:At(actor,there)∧At(cooler,there)∧¬At(actor,here)∧¬At(cooler,here)).
With these kinds of action schemas, any of the planning algorithms described in Chapter 11
can be adapted with only minor modiﬁcations to generate multiactor plans. To the extent that
the coupling among subplans is loose—meaning that concurrency constraints come into play
only rarely during plan search—one would expect the various heuristics derived for single-
agent planning to also be effective in the multiactor context.
17.1.4 Planning with multiple agents: Cooperation and coordination
Now let us consider a true multiagent setting in which each agent makes its own plan. To start
with, let us assume that the goals and knowledge base are shared. One might think that this
reduces to the multibody case—each agent simply computes the joint solution and executes
its own part of that solution. Alas, the “the” in “the joint solution” is misleading. Here is a
second plan that also achieves the goal:
PLAN 2:
A : [Go(A,LeftNet),NoOp(A)]
B : [Go(B,RightBaseline),Hit(B,Ball)].
If both agents can agree on either plan 1 or plan 2, the goal will be achieved. But if A chooses
plan 2 and B chooses plan 1, then nobody will return the ball. Conversely, if A chooses 1 and
B chooses 2, then they will both try to hit the ball and that too will fail. The agents know this,
but how can they coordinate to make sure they agree on the plan?
