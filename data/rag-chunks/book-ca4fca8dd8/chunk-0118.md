---
chunk_id: "book-ca4fca8dd8-chunk-0118"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 118
confidence: "first-pass"
extraction_method: "structured-local"
---

70
Chapter 2
Intelligent Agents
Agent
Environment
Sensors
How the world evolves
What my actions do
Condition-action rules
Actuators
What the world
is like now
I
What action 
should do now
State
Figure 2.11 A model-based reﬂex agent.
Updating this internal state information as time goes by requires two kinds of knowledge
to be encoded in the agent program in some form. First, we need some information about how
the world changes over time, which can be divided roughly into two parts: the effects of the
agent’s actions and how the world evolves independently of the agent. For example, when the
agent turns the steering wheel clockwise, the car turns to the right, and when it’s raining the
car’s cameras can get wet. This knowledge about “how the world works”—whether imple-
mented in simple Boolean circuits or in complete scientiﬁc theories—is called a transition
model of the world.
Transition model
Second, we need some information about how the state of the world is reﬂected in the
agent’s percepts. For example, when the car in front initiates braking, one or more illumi-
nated red regions appear in the forward-facing camera image, and, when the camera gets
wet, droplet-shaped objects appear in the image partially obscuring the road. This kind of
knowledge is called a sensor model.
Sensor model
Together, the transition model and sensor model allow an agent to keep track of the state
of the world—to the extent possible given the limitations of the agent’s sensors. An agent
that uses such models is called a model-based agent.
Model-based agent
Figure 2.11 gives the structure of the model-based reﬂex agent with internal state, show-
ing how the current percept is combined with the old internal state to generate the updated
description of the current state, based on the agent’s model of how the world works. The agent
program is shown in Figure 2.12. The interesting part is the function UPDATE-STATE, which
is responsible for creating the new internal state description. The details of how models and
states are represented vary widely depending on the type of environment and the particular
technology used in the agent design.
Regardless of the kind of representation used, it is seldom possible for the agent to deter-
mine the current state of a partially observable environment exactly. Instead, the box labeled
“what the world is like now” (Figure 2.11) represents the agent’s “best guess” (or sometimes
best guesses, if the agent entertains multiple possibilities). For example, an automated taxi
