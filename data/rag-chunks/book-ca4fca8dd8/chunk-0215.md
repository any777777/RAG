---
chunk_id: "book-ca4fca8dd8-chunk-0215"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 215
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 4.1
Local Search and Optimization Problems
131
Figure 4.4 Illustration of why ridges cause difﬁculties for hill climbing. The grid of states
(dark circles) is superimposed on a ridge rising from left to right, creating a sequence of
local maxima that are not directly connected to each other. From each local maximum, all
the available actions point downhill. Topologies like this are common in low-dimensional
state spaces, such as points in a two-dimensional plane. But in state spaces with hundreds or
thousands of dimensions, this intuitive picture does not hold, and there are usually at least a
few dimensions that make it possible to escape from ridges and plateaus.
• Plateaus: A plateau is a ﬂat area of the state-space landscape. It can be a ﬂat local
Plateau
maximum, from which no uphill exit exists, or a shoulder, from which progress is
Shoulder
possible. (See Figure 4.1.) A hill-climbing search can get lost wandering on the plateau.
In each case, the algorithm reaches a point at which no progress is being made. Starting
from a randomly generated 8-queens state, steepest-ascent hill climbing gets stuck 86% of
the time, solving only 14% of problem instances. On the other hand, it works quickly, taking
just 4 steps on average when it succeeds and 3 when it gets stuck—not bad for a state space
with 88 ≈17 million states.
How could we solve more problems? One answer is to keep going when we reach a
plateau—to allow a sideways move in the hope that the plateau is really a shoulder, as shown
Sideways move
in Figure 4.1. But if we are actually on a ﬂat local maximum, then this approach will wander
on the plateau forever. Therefore, we can limit the number of consecutive sideways moves,
stopping after, say, 100 consecutive sideways moves. This raises the percentage of problem
instances solved by hill climbing from 14% to 94%. Success comes at a cost: the algorithm
averages roughly 21 steps for each successful instance and 64 for each failure.
Many variants of hill climbing have been invented. Stochastic hill climbing chooses at
Stochastic hill
climbing
random from among the uphill moves; the probability of selection can vary with the steepness
of the uphill move. This usually converges more slowly than steepest ascent, but in some
state landscapes, it ﬁnds better solutions. First-choice hill climbing implements stochastic
First-choice hill
climbing
hill climbing by generating successors randomly until one is generated that is better than the
current state. This is a good strategy when a state has many (e.g., thousands) of successors.
Another variant is random-restart hill climbing, which adopts the adage, “If at ﬁrst you
Random-restart hill
climbing
don’t succeed, try, try again.” It conducts a series of hill-climbing searches from randomly
