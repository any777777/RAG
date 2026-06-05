---
chunk_id: "book-ca4fca8dd8-chunk-1610"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1610
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.9
Alternative Robotic Frameworks
977
robot retracts the leg, lifts it up a little higher, and attempts to execute the forward swing once
again. Thus, the controller is able to react to contingencies arising from the interplay of the
robot and its environment.
The subsumption architecture offers additional primitives for synchronizing AFSMs, and
for combining output values of multiple, possibly conﬂicting AFSMs. In this way, it enables
the programmer to compose increasingly complex controllers in a bottom-up fashion. In
our example, we might begin with AFSMs for individual legs, followed by an AFSM for
coordinating multiple legs. On top of this, we might implement higher-level behaviors such
as collision avoidance, which might involve backing up and turning.
The idea of composing robot controllers from AFSMs is quite intriguing. Imagine how
difﬁcult it would be to generate the same behavior with any of the conﬁguration-space path-
planning algorithms described in the previous section. First, we would need an accurate
model of the terrain. The conﬁguration space of a robot with six legs, each of which is driven
by two independent motors, totals 18 dimensions (12 dimensions for the conﬁguration of the
legs, and six for the location and orientation of the robot relative to its environment). Even
if our computers were fast enough to ﬁnd paths in such high-dimensional spaces, we would
have to worry about nasty effects such as the robot sliding down a slope.
Because of such stochastic effects, a single path through conﬁguration space would al-
most certainly be too brittle, and even a PID controller might not be able to cope with such
contingencies. In other words, generating motion behavior deliberately is simply too complex
a problem in some cases for present-day robot motion planning algorithms.
Unfortunately, the subsumption architecture has its own problems. First, the AFSMs
are driven by raw sensor input, an arrangement that works if the sensor data is reliable and
contains all necessary information for decision making, but fails if sensor data has to be
integrated in nontrivial ways over time. Subsumption-style controllers have therefore mostly
been applied to simple tasks, such as following a wall or moving toward visible light sources.
Second, the lack of deliberation makes it difﬁcult to change the robot’s goals. A robot
with a subsumption architecture usually does just one task, and it has no notion of how to
modify its controls to accommodate different goals (just like the dung beetle on page 59).
Third, in many real-world problems, the policy we want is often too complex to encode
explicitly. Think about the example from Figure 26.28, of an autonomous car needing to
negotiate a lane change with a human driver. We might start off with a simple policy that
goes into the target lane. But when we test the car, we ﬁnd out that not every driver in the
target lane will slow down to let the car in. We might then add a bit more complexity: make
the car nudge towards the target lane, wait for a response form the driver in that lane, and
then either proceed or retreat back. But then we test the car, and realize that the nudging
needs to happen at a different speed depending on the speed of the vehicle in the target lane,
on whether there is another vehicle in front in the target lane, on whether there is a vehicle
behind the car in the initial, and so on. The number of conditions that we need to consider
to determine the right course of action can be very large, even for such a deceptively simple
maneuver. This in turn presents scalability challenges for subsumption-style architectures.
All that said, robotics is a complex problem with many approaches: deliberative, reactive,
or a mixture thereof; based on physics, cognitive models, data, or a mixture thereof. The right
approach is still a subject for debate, scientiﬁc inquiry, and engineering prowess.
