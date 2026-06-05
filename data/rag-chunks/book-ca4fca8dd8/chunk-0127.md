---
chunk_id: "book-ca4fca8dd8-chunk-0127"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 127
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 2.4
The Structure of Agents
75
to be the entire agent: it takes in percepts and decides on actions. The learning element uses
feedback from the critic on how the agent is doing and determines how the performance
Critic
element should be modiﬁed to do better in the future.
The design of the learning element depends very much on the design of the performance
element. When trying to design an agent that learns a certain capability, the ﬁrst question is
not “How am I going to get it to learn this?” but “What kind of performance element will my
agent use to do this once it has learned how?” Given a design for the performance element,
learning mechanisms can be constructed to improve every part of the agent.
The critic tells the learning element how well the agent is doing with respect to a ﬁxed
performance standard. The critic is necessary because the percepts themselves provide no
indication of the agent’s success. For example, a chess program could receive a percept
indicating that it has checkmated its opponent, but it needs a performance standard to know
that this is a good thing; the percept itself does not say so. It is important that the performance
standard be ﬁxed. Conceptually, one should think of it as being outside the agent altogether
because the agent must not modify it to ﬁt its own behavior.
The last component of the learning agent is the problem generator. It is responsible
Problem generator
for suggesting actions that will lead to new and informative experiences. If the performance
element had its way, it would keep doing the actions that are best, given what it knows, but
if the agent is willing to explore a little and do some perhaps suboptimal actions in the short
run, it might discover much better actions for the long run. The problem generator’s job is to
suggest these exploratory actions. This is what scientists do when they carry out experiments.
Galileo did not think that dropping rocks from the top of a tower in Pisa was valuable in itself.
He was not trying to break the rocks or to modify the brains of unfortunate pedestrians. His
aim was to modify his own brain by identifying a better theory of the motion of objects.
The learning element can make changes to any of the “knowledge” components shown
in the agent diagrams (Figures 2.9, 2.11, 2.13, and 2.14). The simplest cases involve learning
directly from the percept sequence. Observation of pairs of successive states of the environ-
ment can allow the agent to learn “What my actions do” and “How the world evolves” in
response to its actions. For example, if the automated taxi exerts a certain braking pressure
when driving on a wet road, then it will soon ﬁnd out how much deceleration is actually
achieved, and whether it skids off the road. The problem generator might identify certain
parts of the model that are in need of improvement and suggest experiments, such as trying
out the brakes on different road surfaces under different conditions.
Improving the model components of a model-based agent so that they conform better
with reality is almost always a good idea, regardless of the external performance standard.
(In some cases, it is better from a computational point of view to have a simple but slightly
inaccurate model rather than a perfect but ﬁendishly complex model.) Information from the
external standard is needed when trying to learn a reﬂex component or a utility function.
For example, suppose the taxi-driving agent receives no tips from passengers who have
been thoroughly shaken up during the trip. The external performance standard must inform
the agent that the loss of tips is a negative contribution to its overall performance; then the
agent might be able to learn that violent maneuvers do not contribute to its own utility. In
a sense, the performance standard distinguishes part of the incoming percept as a reward
Reward
(or penalty) that provides direct feedback on the quality of the agent’s behavior. Hard-wired
Penalty
performance standards such as pain and hunger in animals can be understood in this way.
