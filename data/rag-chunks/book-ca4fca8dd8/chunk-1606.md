---
chunk_id: "book-ca4fca8dd8-chunk-1606"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1606
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.9
Alternative Robotic Frameworks
975
on the nth iteration it uses πn to generate more data, to be added to D, which is then used to
create πn+1. In other words, at each iteration the system gathers new data under the current
policy and trains the next policy using all the data gathered so far.
Related recent techniques use adversarial training: they alternate between training a
classiﬁer to distinguish between the robot’s learned policy and the human’s demonstrations,
and training a new robot policy via reinforcement learning to fool the classiﬁer. These ad-
vances enable the robot to handle states that are near demonstrations, but generalization to
far-off states or to new dynamics is a work in progress.
Teaching interfaces and the correspondence problem. So far, we have imagined the
case of an autonomous car or an autonomous helicopter, for which human demonstrations use
the same actions that the robot can take itself: accelerating, braking, and steering. But what
happens if we do this for tasks like cleaning up the kitchen table? We have two choices here:
either the person demonstrates using their own body while the robot watches, or the person
physically guides the robot’s effectors.
The ﬁrst approach is appealing because it comes naturally to end users. Unfortunately,
it suffers from the correspondence problem: how to map human actions onto robot actions.
Correspondence
problem
People have different kinematics and dynamics than robots. Not only does that make it dif-
ﬁcult to translate or retarget human motion onto robot motion (e.g., retargeting a ﬁve-ﬁnger
human grasp to a two-ﬁnger robot grasp), but often the high-level strategy a person might use
is not appropriate for the robot.
The second approach, where the human teacher moves the robot’s effectors into the right
positions, is called kinesthetic teaching. It is not easy for humans to teach this way, espe-
Kinesthetic teaching
cially to teach robots with multiple joints. The teacher needs to coordinate all the degrees of
freedom as it is guiding the arm through the task. Researchers have thus investigated alter-
natives, like demonstrating keyframes as opposed to continuous trajectories, as well as the
Keyframe
use of visual programming to enable end users to program primitives for a task rather than
Visual programming
demonstrate from scratch (Figure 26.31). Sometimes both approaches are combined.
26.9 Alternative Robotic Frameworks
Thus far, we have taken a view of robotics based on the notion of deﬁning or learning a
reward function, and having the robot optimize that reward function (be it via planning or
learning), sometimes in coordination or collaboration with humans. This is a deliberative
Deliberative
view of robotics, to be contrasted with a reactive view.
Reactive
26.9.1 Reactive controllers
In some cases, it is easier to set up a good policy for a robot than to model the world and plan.
Then, instead of a rational agent, we have a reﬂex agent.
For example, picture a legged robot that attempts to lift a leg over an obstacle. We could
give this robot a rule that says lift the leg a small height h and move it forward, and if the leg
encounters an obstacle, move it back and start again at a higher height. You could say that h
is modeling an aspect of the world, but we can also think of h as an auxiliary variable of the
robot controller, devoid of direct physical meaning.
One such example is the six-legged (hexapod) robot, shown in Figure 26.32(a), designed
for walking through rough terrain. The robot’s sensors are inadequate to obtain accurate
