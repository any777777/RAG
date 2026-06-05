---
chunk_id: "book-ca4fca8dd8-chunk-1411"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1411
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.4
Generalization in Reinforcement Learning
855
behavior can be generated from a much simpler utility function approximator that is learnable
from far fewer experiences.
Function approximation makes it practical to represent utility (or Q) functions for very
large state spaces, but more importantly, it allows for inductive generalization: the agent can
generalize from states it has visited to states it has not yet visited. Tesauro (1992) used this
technique to build a backgammon-playing program that played at human champion level,
even though it explored only a trillionth of the complete state space of backgammon.
23.4.1 Approximating direct utility estimation
The method of direct utility estimation (Section 23.2) generates trajectories in the state space
and extracts, for each state, the sum of rewards received from that state onward until termina-
tion. The state and the sum of rewards received constitute a training example for a supervised
learning algorithm. For example, suppose we represent the utilities for the 4×3 world using
a simple linear function, where the features of the squares are just their x and y coordinates.
In that case, we have
ˆUθ(x,y) = θ0 +θ1x+θ2y.
(23.9)
Thus, if (θ0,θ1,θ2)=(0.5,0.2,0.1), then ˆUθ(1,1)=0.8. Given a collection of trials, we obtain
a set of sample values of ˆUθ(x,y), and we can ﬁnd the best ﬁt, in the sense of minimizing the
squared error, using standard linear regression (see Chapter 19).
For reinforcement learning, it makes more sense to use an online learning algorithm
that updates the parameters after each trial. Suppose we run a trial and the total reward
obtained starting at (1,1) is 0.4. This suggests that ˆUθ(1,1), currently 0.8, is too large and
must be reduced. How should the parameters be adjusted to achieve this? As with neural-
network learning, we write an error function and compute its gradient with respect to the
parameters. If uj(s) is the observed total reward from state s onward in the jth trial, then
the error is deﬁned as (half) the squared difference of the predicted total and the actual total:
E j(s) = ( ˆUθ(s)−uj(s))2/2. The rate of change of the error with respect to each parameter θi
is ∂E j/∂θi, so to move the parameter in the direction of decreasing the error, we want
θi ←θi −α ∂E j(s)
∂θi
= θi +α[uj(s)−ˆUθ(s)]∂ˆUθ(s)
∂θi
.
(23.10)
This is called the Widrow–Hoff rule, or the delta rule, for online least-squares. For the
Widrow–Hoﬀrule
Delta rule
linear function approximator ˆUθ(s) in Equation (23.9), we get three simple update rules:
θ0 ←θ0 +α[uj(s)−ˆUθ(s)],
θ1 ←θ1 +α[uj(s)−ˆUθ(s)]x,
θ2 ←θ2 +α[uj(s)−ˆUθ(s)]y.
We can apply these rules to the example where ˆUθ(1,1) is 0.8 and uj(1,1) is 0.4. Parame-
ters θ0, θ1, and θ2 are all decreased by 0.4α, which reduces the error for (1,1). Notice that
changing the parameters θi in response to an observed transition between two states also ◀
changes the values of ˆUθ for every other state! This is what we mean by saying that function
approximation allows a reinforcement learner to generalize from its experiences.
The agent will learn faster if it uses a function approximator, provided that the hypothesis
space is not too large and includes some functions that are a reasonably good ﬁt to the true
utility function. Exercise 23.APLM asks you to evaluate the performance of direct utility
