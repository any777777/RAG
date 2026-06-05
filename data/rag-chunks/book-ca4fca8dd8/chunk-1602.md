---
chunk_id: "book-ca4fca8dd8-chunk-1602"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1602
confidence: "first-pass"
extraction_method: "structured-local"
---

972
Chapter 26
Robotics
have you grab the eggs and milk from the fridge, while the robot fetches the ﬂour from the
cabinet. The robot knows this because it can measure quite precisely where everyone is. But
suppose you start heading for the ﬂour cabinet. You are going against the optimal joint plan.
Rather than sticking to it and stubbornly also going for the ﬂour, the MPC robot recalculates
the optimal plan, and now that you are close enough to the ﬂour it is best for the robot to grab
the wafﬂe iron instead.
If we know that people might deviate from optimality, we can account for it ahead of time.
In our example, the robot can try to anticipate that you are going for the ﬂour the moment you
take your ﬁrst step (say, using the prediction technique above). Even if it is still technically
optimal for you to turn around and head for the fridge, the robot should not assume that’s
what is going to happen. Instead, the robot can compute a plan in which you keep doing what
you seem to want.
Humans as black box agents
We don’t have to treat people as objective-driven, intentional agents to get robots to coordi-
nate with us. An alternative model is that the human is merely some agent whose policy πH
“messes” with the environment dynamics. The robot does not know πH, but can model the
problem as needing to act in an MDP with unknown dynamics. We have seen this before: for
general agents in Chapter 23, and for robots in particular in Section 26.7.
The robot can ﬁt a policy model πH to human data, and use it to compute an optimal
policy for itself. Due to scarcity of data, this has been mostly used so far at the task level. For
instance, robots have learned through interaction what actions people tend to take (in response
to its own actions) for the task of placing and drilling screws in an industrial assembly task.
Then there is also the model-free reinforcement learning alternative: the robot can start
with some initial policy or value function, and keep improving it over time via trial and error.
26.8.2 Learning to do what humans want
Another way interaction with humans comes into robotics is in JR itself—the robot’s cost or
reward function. The framework of rational agents and the associated algorithms reduce the
problem of generating good behavior to specifying a good reward function. But for robots,
as for many other AI agents, getting the cost right is still difﬁcult.
Take autonomous cars: we want them to reach the destination, to be safe, to drive com-
fortably for their passengers, to obey trafﬁc laws, etc. A designer of such a system needs to
trade off these different components of the cost function. The designer’s task is hard because
robots are built to help end users, and not every end user is the same. We all have different
preferences for how aggressively we want our car to drive, etc.
Below, we explore two alternatives for trying to get robot behavior to match what we
actually want the robot to do. The ﬁrst is to learn a cost function from human input. The
second is to bypass the cost function and imitate human demonstrations of the task.
Preference learning: Learning cost functions
Imagine that an end user is showing a robot how to do a task. For instance, they are driving
the car in the way they would like it to be driven by the robot. Can you think of a way for the
robot to use these actions—we call them “demonstrations”—to ﬁgure out what cost function
it should optimize?
