---
chunk_id: "book-ca4fca8dd8-chunk-0120"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 120
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.4
The Structure of Agents
71
function MODEL-BASED-REFLEX-AGENT(percept) returns an action
persistent: state, the agent’s current conception of the world state
transition model, a description of how the next state depends on
the current state and action
sensor model, a description of how the current world state is reﬂected
in the agent’s percepts
rules, a set of condition–action rules
action, the most recent action, initially none
state←UPDATE-STATE(state,action,percept,transition model,sensor model)
rule←RULE-MATCH(state,rules)
action←rule.ACTION
return action
Figure 2.12 A model-based reﬂex agent. It keeps track of the current state of the world,
using an internal model. It then chooses an action in the same way as the reﬂex agent.
may not be able to see around the large truck that has stopped in front of it and can only guess
about what may be causing the hold-up. Thus, uncertainty about the current state may be
unavoidable, but the agent still has to make a decision.
2.4.4 Goal-based agents
Knowing something about the current state of the environment is not always enough to decide
what to do. For example, at a road junction, the taxi can turn left, turn right, or go straight
on. The correct decision depends on where the taxi is trying to get to. In other words,
as well as a current state description, the agent needs some sort of goal information that
Goal
describes situations that are desirable—for example, being at a particular destination. The
agent program can combine this with the model (the same information as was used in the
model-based reﬂex agent) to choose actions that achieve the goal. Figure 2.13 shows the
goal-based agent’s structure.
Sometimes goal-based action selection is straightforward—for example, when goal sat-
isfaction results immediately from a single action. Sometimes it will be more tricky—for
example, when the agent has to consider long sequences of twists and turns in order to ﬁnd
a way to achieve the goal. Search (Chapters 3, 4, and 6) and planning (Chapter 11) are the
subﬁelds of AI devoted to ﬁnding action sequences that achieve the agent’s goals.
Notice that decision making of this kind is fundamentally different from the condition–
action rules described earlier, in that it involves consideration of the future—both “What will
happen if I do such-and-such?” and “Will that make me happy?” In the reﬂex agent designs,
this information is not explicitly represented, because the built-in rules map directly from
percepts to actions. The reﬂex agent brakes when it sees brake lights, period. It has no idea
why. A goal-based agent brakes when it sees brake lights because that’s the only action that
it predicts will achieve its goal of not hitting other cars.
Although the goal-based agent appears less efﬁcient, it is more ﬂexible because the
knowledge that supports its decisions is represented explicitly and can be modiﬁed. For
example, a goal-based agent’s behavior can easily be changed to go to a different destination,
