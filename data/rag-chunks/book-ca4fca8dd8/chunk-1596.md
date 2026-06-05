---
chunk_id: "book-ca4fca8dd8-chunk-1596"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1596
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.8
Humans and Robots
969
Second is that the state and action spaces are continuous, as they’ve been throughout this
chapter. We learned in Chapter 6 how to do tree search to tackle discrete games, but how do
we tackle continuous spaces?
Third, even though at the high level the game model makes sense—humans do move,
and they do have objectives—a human’s behavior might not always be well-characterized as
a solution to the game. The game comes with a computational challenge not only for the
robot, but for us humans too. It requires thinking about what the robot will do in response to
what the person does, which depends on what the robot thinks the person will do, and pretty
soon we get to “what do you think I think you think I think”— it’s turtles all the way down!
Humans can’t deal with all of that, and exhibit certain suboptimalities. This means that the
robot should account for these suboptimalities.
So, then, what is an autonomous car to do when the coordination problem is this hard?
We will do something similar to what we’ve done before in this chapter. For motion planning
and control, we took an MDP and broke it up into planning a trajectory and then tracking it
with a controller. Here too, we will take the game, and break it up into making predictions
about human actions, and deciding what the robot should do given these predictions.
Predicting human action
Predicting human actions is hard because they depend on the robot’s actions and vice versa.
One trick that robots use is to pretend the person is ignoring the robot. The robot assumes
people are noisily optimal with respect to their objective, which is unknown to the robot and
is modeled as no longer dependent on the robot’s actions: JH(x,uH). In particular, the higher
the value of an action for the objective (the lower the cost to go), the more likely the human
is to take it. The robot can create a model for P(uH | x,JH), for instance using the softmax
function from page 862:
P(uH | x,JH) ∝e−Q(x,uH;JH)
(26.8)
with Q(x,uH;JH) the Q-value function corresponding to JH (the negative sign is there because
in robotics we like to minimize cost, not maximize reward). Note that the robot does not
assume perfectly optimal actions, nor does it assume that the actions are chosen based on
reasoning about the robot at all.
Armed with this model, the robot uses the human’s ongoing actions as evidence about JH.
If we have an observation model for how human actions depend on the human’s objective,
each human action can be incorporated to update the robot’s belief over what objective the
person has:
b′(JH) ∝b(JH)P(uH | x,JH).
(26.9)
An example is in Figure 26.27: the robot is tracking a human’s location and as the hu-
man moves, the robot updates its belief over human goals. As the human heads toward the
windows, the robot increases the probability that the goal is to look out the window, and
decreases the probability that the goal is going to the kitchen, which is in the other direction.
This is how the human’s past actions end up informing the robot about what the human
will do in the future. Having a belief about the human’s goal helps the robot anticipate
what next actions the human will take. The heatmap in the ﬁgure shows the robot’s future
predictions: red is most probable; blue least probable.
