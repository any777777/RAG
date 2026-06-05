---
chunk_id: "book-ca4fca8dd8-chunk-1594"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1594
confidence: "first-pass"
extraction_method: "structured-local"
---

968
Chapter 26
Robotics
26.8 Humans and Robots
Thus far, we’ve focused on a robot planning and learning how to act in isolation. This is
useful for some robots, like the rovers we send out to explore distant planets on our behalf.
But, for the most part, we do not build robots to work in isolation. We build them to help us,
and to work in human environments, around and with us.
This raises two complementary challenges. First is optimizing reward when there are
people acting in the same environment as the robot. We call this the coordination problem
(see Section 17.1). When the robot’s reward depends on not just its own actions, but also the
actions that people take, the robot has to choose its actions in a way that meshes well with
theirs. When the human and the robot are on the same team, this turns into collaboration.
Second is the challenge of optimizing for what people actually want. If a robot is to
help people, its reward function needs to incentivize the actions that people want the robot to
execute. Figuring out the right reward function (or policy) for the robot is itself an interaction
problem. We will explore these two challenges in turn.
26.8.1 Coordination
Let’s assume for now, as we have been, that the robot has access to a clearly deﬁned reward
function. But, instead of needing to optimize it in isolation, now the robot needs to optimize
it around a human who is also acting. For example, as an autonomous car merges on the
highway, it needs to negotiate the maneuver with the human driver coming in the target lane—
should it accelerate and merge in front, or slow down and merge behind? Later, as it pulls to
a stop sign, preparing to take a right, it has to watch out for the cyclist in the bicycle lane, and
for the pedestrian about to step onto the crosswalk.
Or, consider a mobile robot in a hallway. Someone heading straight toward the robot
steps slightly to the right, indicating which side of the robot they want to pass on. The robot
has to respond, clarifying its intentions.
Humans as approximately rational agents
One way to formulate coordination with a human is to model it as a game between the robot
and the human (Section 17.2). With this approach, we explicitly make the assumption that
people are agents incentivized by objectives. This does not automatically mean that they are
perfectly rational agents (i.e., ﬁnd optimal solutions in the game), but it does mean that the
robot can structure the way it reasons about the human via the notion of possible objectives
that the human might have. In this game:
• the state of the environment captures the conﬁgurations of both the robot and human
agents; call it x = (xR,xH);
• each agent can take actions, uR and uH respectively;
• each agent has an objective that can be represented as a cost, JR and JH: each agent
wants to get to its goal safely and efﬁciently;
• and, as in any game, each objective depends on the state and on the actions of both
agents: JR(x,uR,uH) and JH(x,uH,uR). Think of the car-pedestrian interaction—the car
should stop if the pedestrian crosses, and should go forward if the pedestrian waits.
Three important aspects complicate this game. First is that the human and the robot don’t
necessarily know each other’s objectives. This makes it an incomplete information game.
Incomplete
information game
