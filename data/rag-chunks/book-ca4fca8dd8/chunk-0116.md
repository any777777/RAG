---
chunk_id: "book-ca4fca8dd8-chunk-0116"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 116
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.4
The Structure of Agents
69
function SIMPLE-REFLEX-AGENT(percept) returns an action
persistent: rules, a set of condition–action rules
state←INTERPRET-INPUT(percept)
rule←RULE-MATCH(state,rules)
action←rule.ACTION
return action
Figure 2.10 A simple reﬂex agent. It acts according to a rule whose condition matches the
current state, as deﬁned by the percept.
Even a little bit of unobservability can cause serious trouble. For example, the braking
rule given earlier assumes that the condition car-in-front-is-braking can be determined from
the current percept—a single frame of video. This works if the car in front has a centrally
mounted (and hence uniquely identiﬁable) brake light. Unfortunately, older models have
different conﬁgurations of taillights, brake lights, and turn-signal lights, and it is not always
possible to tell from a single image whether the car is braking or simply has its taillights
on. A simple reﬂex agent driving behind such a car would either brake continuously and
unnecessarily, or, worse, never brake at all.
We can see a similar problem arising in the vacuum world. Suppose that a simple reﬂex
vacuum agent is deprived of its location sensor and has only a dirt sensor. Such an agent
has just two possible percepts: [Dirty] and [Clean]. It can Suck in response to [Dirty]; what
should it do in response to [Clean]? Moving Left fails (forever) if it happens to start in square
A, and moving Right fails (forever) if it happens to start in square B. Inﬁnite loops are often
unavoidable for simple reﬂex agents operating in partially observable environments.
Escape from inﬁnite loops is possible if the agent can randomize its actions. For exam-
Randomization
ple, if the vacuum agent perceives [Clean], it might ﬂip a coin to choose between Right and
Left. It is easy to show that the agent will reach the other square in an average of two steps.
Then, if that square is dirty, the agent will clean it and the task will be complete. Hence, a
randomized simple reﬂex agent might outperform a deterministic simple reﬂex agent.
We mentioned in Section 2.3 that randomized behavior of the right kind can be rational in
some multiagent environments. In single-agent environments, randomization is usually not
rational. It is a useful trick that helps a simple reﬂex agent in some situations, but in most
cases we can do much better with more sophisticated deterministic agents.
2.4.3 Model-based reﬂex agents
The most effective way to handle partial observability is for the agent to keep track of the
part of the world it can’t see now. That is, the agent should maintain some sort of internal
state that depends on the percept history and thereby reﬂects at least some of the unobserved
Internal state
aspects of the current state. For the braking problem, the internal state is not too extensive—
just the previous frame from the camera, allowing the agent to detect when two red lights at
the edge of the vehicle go on or off simultaneously. For other driving tasks such as changing
lanes, the agent needs to keep track of where the other cars are if it can’t see them all at once.
And for any driving to be possible at all, the agent needs to keep track of where its keys are.
