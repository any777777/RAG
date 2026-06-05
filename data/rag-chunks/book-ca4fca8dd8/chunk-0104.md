---
chunk_id: "book-ca4fca8dd8-chunk-0104"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 104
confidence: "first-pass"
extraction_method: "structured-local"
---

62
Chapter 2
Intelligent Agents
Agent Type
Performance
Measure
Environment
Actuators
Sensors
Medical
diagnosis system
Healthy patient,
reduced costs
Patient, hospital,
staff
Display of
questions, tests,
diagnoses,
treatments
Touchscreen/voice
entry of
symptoms and
ﬁndings
Satellite image
analysis system
Correct
categorization of
objects, terrain
Orbiting satellite,
downlink,
weather
Display of scene
categorization
High-resolution
digital camera
Part-picking
robot
Percentage of
parts in correct
bins
Conveyor belt
with parts; bins
Jointed arm and
hand
Camera, tactile
and joint angle
sensors
Reﬁnery
controller
Purity, yield,
safety
Reﬁnery, raw
materials,
operators
Valves, pumps,
heaters, stirrers,
displays
Temperature,
pressure, ﬂow,
chemical sensors
Interactive
English tutor
Student’s score
on test
Set of students,
testing agency
Display of
exercises,
feedback, speech
Keyboard entry,
voice
Figure 2.5 Examples of agent types and their PEAS descriptions.
performance measure. Fully observable environments are convenient because the agent need
not maintain any internal state to keep track of the world. An environment might be partially
observable because of noisy and inaccurate sensors or because parts of the state are simply
missing from the sensor data—for example, a vacuum agent with only a local dirt sensor
cannot tell whether there is dirt in other squares, and an automated taxi cannot see what other
drivers are thinking. If the agent has no sensors at all then the environment is unobserv-
able. One might think that in such cases the agent’s plight is hopeless, but, as we discuss in
Unobservable
Chapter 4, the agent’s goals may still be achievable, sometimes with certainty.
Single-agent vs. multiagent: The distinction between single-agent and multiagent en-
Single-agent
Multiagent
vironments may seem simple enough. For example, an agent solving a crossword puzzle by
itself is clearly in a single-agent environment, whereas an agent playing chess is in a two-
agent environment. However, there are some subtle issues. First, we have described how an
entity may be viewed as an agent, but we have not explained which entities must be viewed
as agents. Does an agent A (the taxi driver for example) have to treat an object B (another
vehicle) as an agent, or can it be treated merely as an object behaving according to the laws of
physics, analogous to waves at the beach or leaves blowing in the wind? The key distinction
is whether B’s behavior is best described as maximizing a performance measure whose value
depends on agent A’s behavior.
