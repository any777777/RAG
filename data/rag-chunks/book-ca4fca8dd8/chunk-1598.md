---
chunk_id: "book-ca4fca8dd8-chunk-1598"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1598
confidence: "first-pass"
extraction_method: "structured-local"
---

970
Chapter 26
Robotics
(a)
(b)
(c)
Figure 26.27 Making predictions by assuming that people are noisily rational given their
goal: the robot uses the past actions to update a belief over what goal the person is heading
to, and then uses the belief to make predictions about future actions. (a) The map of a room.
(b) Predictions after seeing a small part of the person’s trajectory (white path); (c) Predictions
after seeing more human actions: the robot now knows that the person is not heading to the
hallway on the left, because the path taken so far would be a poor path if that were the
person’s goal. Images courtesy of Brian D. Ziebart. See Ziebart et al. (2009).
The same can happen in driving. We might not know how much another driver values
efﬁciency, but if we see them accelerate as someone is trying to merge in front of them, we
now know a bit more about them. And once we know that, we can better anticipate what they
will do in the future—the same driver is likely to come closer behind us, or weave through
trafﬁc to get ahead.
Once the robot can make predictions about human future actions, it has reduced its prob-
lem to solving an MDP. The human actions complicate the transition function, but as long as
the robot can anticipate what action the person will take from any future state, the robot can
calculate P(x′ | x,uR): it can compute P(uH | x) from P(uH | x,JH) by marginalizing over JH,
and combine it with P(x′ | x,uR,uH), the transition (dynamics) function for how the world
updates based on both the robot’s and the human’s actions. In Section 26.5 we focused on
how to solve this in continuous state and action spaces for deterministic dynamics, and in
Section 26.6 we discussed doing it with stochastic dynamics and uncertainty.
Splitting prediction from action makes it easier for the robot to handle interaction, but
sacriﬁces performance much as splitting estimation from motion did, or splitting planning
from control.
A robot with this split no longer understands that its actions can inﬂuence what people
end up doing. In contrast, the robot in Figure 26.27 anticipates where people will go and then
optimizes for reaching its own goal and avoiding collisions with them. In Figure 26.28, we
have an autonomous car merging on the highway. If it just planned in reaction to other cars,
it might have to wait a long time while other cars occupy its target lane. In contrast, a car
that reasons about prediction and action jointly knows that different actions it could take will
result in different reactions from the human. If it starts to assert itself, the other cars are likely
to slow down a bit and make room. Roboticists are working towards coordinated interactions
like this so robots can work better with humans.
