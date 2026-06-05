---
chunk_id: "book-ca4fca8dd8-chunk-0238"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 238
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 4.4
Search in Partially Observable Environments
145
The solution to a sensorless problem is a sequence of actions, not a conditional plan
(because there is no perceiving). But we search in the space of belief states rather than
physical states.6 In belief-state space, the problem is fully observable because the agent
always knows its own belief state. Furthermore, the solution (if any) for a sensorless problem
is always a sequence of actions. This is because, as in the ordinary problems of Chapter 3,
the percepts received after each action are completely predictable—they’re always empty! So
there are no contingencies to plan for. This is true even if the environment is nondeterministic.
We could introduce new algorithms for sensorless search problems. But instead, we can
use the existing algorithms from Chapter 3 if we transform the underlying physical problem
into a belief-state problem, in which we search over belief states rather than physical states.
The original problem, P, has components ActionsP,ResultP etc., and the belief-state problem
has the following components:
• States: The belief-state space contains every possible subset of the physical states. If P
has N states, then the belief-state problem has 2N belief states, although many of those
may be unreachable from the initial state.
• Initial state: Typically the belief state consisting of all states in P, although in some
cases the agent will have more knowledge than this.
• Actions: This is slightly tricky. Suppose the agent is in belief state b={s1,s2}, but
ACTIONSP(s1) ̸= ACTIONSP(s2); then the agent is unsure of which actions are legal. If
we assume that illegal actions have no effect on the environment, then it is safe to take
the union of all the actions in any of the physical states in the current belief state b:
ACTIONS(b) =
[
s∈b
ACTIONSP(s).
On the other hand, if an illegal action might lead to catastrophe, it is safer to allow only
the intersection, that is, the set of actions legal in all the states. For the vacuum world,
every state has the same legal actions, so both methods give the same result.
• Transition model: For deterministic actions, the new belief state has one result state
for each of the current possible states (although some result states may be the same):
b′ = RESULT(b,a) = {s′ : s′ =RESULTP(s,a) and s ∈b}.
(4.4)
With nondeterminism, the new belief state consists of all the possible results of applying
the action to any of the states in the current belief state:
b′ = RESULT(b,a) = {s′ : s′ ∈RESULTSP(s,a) and s ∈b}
=
[
s∈b
RESULTSP(s,a),
The size of b′ will be the same or smaller than b for deterministic actions, but may be
larger than b with nondeterministic actions (see Figure 4.13).
• Goal test: The agent possibly achieves the goal if any state s in the belief state satisﬁes
the goal test of the underlying problem, IS-GOALP(s). The agent necessarily achieves
the goal if every state satisﬁes IS-GOALP(s). We aim to necessarily achieve the goal.
• Action cost: This is also tricky. If the same action can have different costs in dif-
ferent states, then the cost of taking an action in a given belief state could be one of
6
In a fully observable environment, each belief state contains one physical state. Thus, we can view the algo-
rithms in Chapter 3 as searching in a belief-state space of singleton belief states.
