---
chunk_id: "book-ca4fca8dd8-chunk-1553"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1553
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.3
What kind of problem is robotics solving?
937
Three-ﬁngered grippers offer slightly more ﬂexibility while maintaining simplicity. At the
other end of the spectrum are humanoid (anthropomorphic) hands. For instance, the Shadow
Dexterous Hand has a total of 20 actuators. This offers a lot more ﬂexibility for complex
manipulation, including in-hand manipulator maneuvers (think of picking up your cell phone
and rotating it in-hand to orient it right-side up), but this ﬂexibility comes at a price—learning
to control these complex grippers is more challenging.
26.3 What kind of problem is robotics solving?
Now that we know what the robot hardware might be, we’re ready to consider the agent
software that drives the hardware to achieve our goals. We ﬁrst need to decide the computa-
tional framework for this agent. We have talked about search in deterministic environments,
MDPs for stochastic but fully observable environments, POMDPs for partial observability,
and games for situations in which the agent is not acting in isolation. Given a computational
framework, we need to instantiate its ingredients: reward or utility functions, states, actions,
observation spaces, etc.
We have already noted that robotics problems are nondeterministic, partially observable,
and multiagent. Using the game-theoretic notions from Chapter 17, we can see that some-
times the agents are cooperative and sometimes they are competitive. In a narrow corridor
where only one agent can go ﬁrst, a robot and a person collaborate because they both want
to make sure they don’t bump into each other. But in some cases they might compete a bit to
reach their destination quickly. If the robot is too polite and always makes room, it might get
stuck in crowded situations and never reach its goal.
Therefore, when robots act in isolation and know their environment, the problem they
are solving can be formulated as an MDP; when they are missing information it becomes a
POMDP; and when they act around people it can often be formulated as a game.
What is the robot’s reward function in this formulation? Usually the robot is acting in
service of a human—for example delivering a meal to a hospital patient for the patient’s
reward, not its own. For most robotics settings, even though robot designers might try to
specify a good enough proxy reward function, the true reward function lies with the user
whom the robot is supposed to help. The robot will either need to decipher the user’s desires,
or rely on an engineer to specify an approximation of the user’s desires.
As for the robot’s action, state, and observation spaces, the most general form is that
observations are raw sensor feeds (e.g., the images coming in from cameras, or the laser hits
coming in from lidar); actions are raw electric currents being sent to the motors; and state is
what the robot needs to know for its decision making. This means there is a huge gap between
the low-level percepts and motor controls, and the high-level plans the robot needs to make.
To bridge the gap, roboticists decouple aspects of the problem to simplify it.
For instance, we know that when we solve POMDPs properly, perception and action
interact: perception informs which actions make sense, but action also informs perception,
with agents taking actions to gather information when that information has value in later
time steps. However, robots often separate perception from action, consuming the outputs
of perception and pretending they will not get any more information in the future. Further,
hierarchical planning is called for, because a high-level goal like “get to the cafeteria” is far
removed from a motor command like “rotate the main axle 1 ◦,”
