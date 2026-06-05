---
chunk_id: "book-ca4fca8dd8-chunk-1615"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1615
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
981
Center, where they entered structures deemed too dangerous for human search and rescue
crews. Here too, these robots are initially deployed via teleoperation, and as technology
advances they are becoming more and more autonomous, with a human operator in charge
but not having to specify every single command.
Industry: The majority of robots today are deployed in factories, automating tasks that
are difﬁcult, dangerous, or dull for humans. (The majority of factory robots are in automobile
factories.) Automating these tasks is a positive in terms of efﬁciently producing what society
needs. At the same time, it also means displacing some human workers from their jobs. This
has important policy and economics implications—the need for retraining and education, the
need for a fair division of resources, etc. These topics are discussed further in Section 28.3.5.
Summary
Robotics is about physically embodied agents, which can change the state of the physical
world. In this chapter, we have learned the following:
• The most common types of robots are manipulators (robot arms) and mobile robots.
They have sensors for perceiving the world and actuators that produce motion, which
then affects the world via effectors.
• The general robotics problem involves stochasticity (which can be handled by MDPs),
partial observability (which can be handled by POMDPs), and acting with and around
other agents (which can be handled with game theory). The problem is made even
harder by the fact that most robots work in continuous and high-dimensional state and
action spaces. They also operate in the real world, which refuses to run faster than real
time and in which failures lead to real things being damaged, with no “undo” capability.
• Ideally, the robot would solve the entire problem in one go: observations in the form
of raw sensor feeds go in, and actions in the form of torques or currents to the motors
come out. In practice though, this is too daunting, and roboticists typically decouple
different aspects of the problem and treat them independently.
• We typically separate perception (estimation) from action (motion generation). Percep-
tion in robotics involves computer vision to recognize the surroundings through cam-
eras, but also localization and mapping.
• Robotic perception concerns itself with estimating decision-relevant quantities from
sensor data. To do so, we need an internal representation and a method for updating
this internal representation over time.
• Probabilistic ﬁltering algorithms such as particle ﬁlters and Kalman ﬁlters are useful
for robot perception. These techniques maintain the belief state, a posterior distribution
over state variables.
• For generating motion, we use conﬁguration spaces, where a point speciﬁes everything
we need to know to locate every body point on the robot. For instance, for a robot arm
with two joints, a conﬁguration consists of the two joint angles.
• We typically decouple the motion generation problem into motion planning, concerned
with producing a plan, and trajectory tracking control, concerned with producing a
policy for control inputs (actuator commands) that results in executing the plan.
