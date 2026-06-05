---
chunk_id: "book-ca4fca8dd8-chunk-1617"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1617
confidence: "first-pass"
extraction_method: "structured-local"
---

982
Chapter 26
Robotics
• Motion planning can be solved via graph search using cell decomposition; using ran-
domized motion planning algorithms, which sample milestones in the continuous
conﬁguration space; or using trajectory optimization, which can iteratively push a
straight-line path out of collision by leveraging a signed distance ﬁeld.
• A path found by a search algorithm can be executed using the path as the reference
trajectory for a PID controller, which constantly corrects for errors between where the
robot is and where it is supposed to be, or via computed torque control, which adds a
feedforward term that makes use of inverse dynamics to compute roughly what torque
to send to make progress along the trajectory.
• Optimal control unites motion planning and trajectory tracking by computing an op-
timal trajectory directly over control inputs. This is especially easy when we have
quadratic costs and linear dynamics, resulting in a linear quadratic regulator (LQR).
Popular methods make use of this by linearizing the dynamics and computing second-
order approximations of the cost (ILQR).
• Planning under uncertainty unites perception and action by online replanning (such as
model predictive control) and information gathering actions that aid perception.
• Reinforcement learning is applied in robotics, with techniques striving to reduce the
required number of interactions with the real world. Such techniques tend to exploit
models, be it estimating models and using them to plan, or training policies that are
robust with respect to different possible model parameters.
• Interaction with humans requires the ability to coordinate the robot’s actions with
theirs, which can be formulated as a game. We usually decompose the solution into
prediction, in which we use the person’s ongoing actions to estimate what they will
do in the future, and action, in which we use the predictions to compute the optimal
motion for the robot.
• Helping humans also requires the ability to learn or infer what they want. Robots can
approach this by learning the desired cost function they should optimize from human
input, such as demonstrations, corrections, or instruction in natural language. Alterna-
tively, robots can imitate human behavior, and use reinforcement learning to help tackle
the challenge of generalization to new states.
Bibliographical and Historical Notes
The word robot was popularized by Czech playwright Karel ˇCapek in his 1920 play R.U.R.
(Rossum’s Universal Robots). The robots, which were grown chemically rather than con-
structed mechanically, end up resenting their masters and decide to take over. It appears that
it was ˇCapek’s brother, Josef, who ﬁrst combined the Czech words “robota” (obligatory work)
and “robotnik” (serf) to yield “robot” in his 1917 short story Opilec (Glanc, 1978). The term
robotics was invented for a science ﬁction story (Asimov, 1950).
The idea of an autonomous machine predates the word “robot” by thousands of years. In
7th century BCE Greek mythology, a robot named Talos was built by Hephaistos, the Greek
god of metallurgy, to protect the island of Crete. The legend is that the sorceress Medea
defeated Talos by promising him immortality but then draining his life ﬂuid. Thus, this is the
