---
chunk_id: "book-ca4fca8dd8-chunk-1555"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1555
confidence: "first-pass"
extraction_method: "structured-local"
---

938
Chapter 26
Robotics
In robotics we often use a three-level hierarchy. The task planning level decides a plan
Task planning
or policy for high-level actions, sometimes called action primitives or subgoals: move to the
door, open it, go to the elevator, press the button, etc. Then motion planning is in charge of
ﬁnding a path that gets the robot from one point to another, achieving each subgoal. Finally,
control is used to achieve the planned motion using the robot’s actuators. Since the task
Control
planning level is typically deﬁned over discrete states and actions, in this chapter we will
focus primarily on motion planning and control.
Separately, preference learning is in charge of estimating an end user’s objective, and
Preference learning
people prediction is used to forecast the actions of other people in the robot’s environment.
People prediction
All these combine to determine the robot’s behavior.
Whenever we split a problem into separate pieces we reduce complexity, but we give up
opportunities for the pieces to help each other. Action can help improve perception, and also
determine what kind of perception is useful. Similarly, decisions at the motion level might
not be the best when accounting for how that motion will be tracked; or decisions at the task
level might render the task plan uninstantiatable at the motion level. So, with progress in
these separate areas comes the push to reintegrate them: to do motion planning and control
together, to do task and motion planning together, and to reintegrate perception, prediction,
and action—closing the feedback loop. Robotics today is about continuing progress in each
area while also building on this progress to achieve better integration.
26.4 Robotic Perception
Perception is the process by which robots map sensor measurements into internal representa-
tions of the environment. Much of it uses the computer vision techniques from the previous
chapter. But perception for robotics must deal with additional sensors like lidar and tactile
sensors.
Perception is difﬁcult because sensors are noisy and the environment is partially observ-
able, unpredictable, and often dynamic. In other words, robots have all the problems of state
estimation (or ﬁltering) that we discussed in Section 14.2. As a rule of thumb, good internal
representations for robots have three properties:
1. They contain enough information for the robot to make good decisions.
2. They are structured so that they can be updated efﬁciently.
3. They are natural in the sense that internal variables correspond to natural state variables
in the physical world.
In Chapter 14, we saw that Kalman ﬁlters, HMMs, and dynamic Bayes nets can represent the
transition and sensor models of a partially observable environment, and we described both
exact and approximate algorithms for updating the belief state—the posterior probability
distribution over the environment state variables. Several dynamic Bayes net models for
this process were shown in Chapter 14. For robotics problems, we include the robot’s own
past actions as observed variables in the model. Figure 26.4 shows the notation used in this
chapter: Xt is the state of the environment (including the robot) at time t, Zt is the observation
received at time t, and At is the action taken after the observation is received.
We would like to compute the new belief state, P(Xt+1 | z1:t+1,a1:t), from the current
belief state, P(Xt | z1:t,a1:t−1), and the new observation zt+1. We did this in Section 14.2,
