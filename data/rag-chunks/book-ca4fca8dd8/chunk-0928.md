---
chunk_id: "book-ca4fca8dd8-chunk-0928"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 928
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 561

Section 16.1
Sequential Decision Problems
561
Plug/Unplugt
LeftWheelt
RightWheelt
Chargingt
Batteryt
Chargingt+1
Batteryt+1
Chargingt+2
Batteryt+2
Rt
Xt
Xt+1
Ut+2
Xt+2
 X˙ t+2
 X˙ t+1
 X˙ t
Rt+1
RightWheelt+1
LeftWheelt+1
Plug/Unplugt+1
Figure 16.4 A dynamic decision network for a mobile robot with state variables for battery
level, charging status, location, and velocity, and action variables for the left and right wheel
motors and for charging.
Chapter 2; they typically have an exponential complexity advantage over atomic representa-
tions and can model quite substantial real-world problems.
Figure 16.4, which is based on the DBN in Figure 14.13(b) (page 504), shows some
elements of a slightly realistic model for a mobile robot that can charge itself. The state St is
decomposed into four state variables:
• Xt consists of the two-dimensional location on a grid plus the orientation;
• ˙Xt is the rate of change of Xt;
• Chargingt is true when the robot is plugged in to a power source;
• Batteryt is the battery level, which we model as an integer in the range 0,...,5.
The state space for the MDP is the Cartesian product of the ranges of these four variables. The
action is now a set At of action variables, comprised of Plug/Unplug, which has three values
(plug, unplug, and noop); LeftWheel for the power sent to the left wheel; and RightWheel for
the power sent to the right wheel. The set of actions for the MDP is the Cartesian product of
the ranges of these three variables. Notice that each action variable affects only a subset of
the state variables.
The overall transition model is the conditional distribution P(Xt+1|Xt,At), which can be
computed as a product of conditional probabilities from the DDN. The reward here is a single
variable that depends only on the location X (for, say, arriving at a destination) and Charging,
as the robot has to pay for electricity used; in this particular model, the reward doesn’t depend
on the action or the outcome state.
The network in Figure 16.4 has been projected two steps into the future. Notice that the
network includes nodes for the rewards for times t and t +1, but the utility for time t +2. This

## Page 562
