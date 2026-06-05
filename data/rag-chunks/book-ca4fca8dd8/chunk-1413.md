---
chunk_id: "book-ca4fca8dd8-chunk-1413"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1413
confidence: "first-pass"
extraction_method: "structured-local"
---

856
Chapter 23
Reinforcement Learning
estimation, both with and without function approximation. The improvement in the 4×3
world is noticeable but not dramatic, because this is a very small state space to begin with.
The improvement is much greater in a 10×10 world with a +1 reward at (10,10).
The 10×10 world is well suited for a linear utility function because the true utility func-
tion is smooth and nearly linear: it is basically a diagonal slope with its lower corner at (1,1)
and its upper corner at (10,10). (See Exercise 23.TENX.) On the other hand, if we put the
+1 reward at (5,5), the true utility is more like a pyramid and the function approximator in
Equation (23.9) will fail miserably.
All is not lost, however! Remember that what matters for linear function approximation
is that the function be linear in the features. But we can choose the features to be arbitrary
nonlinear functions of the state variables. Hence, we can include a feature such as f3(x,y) =
p
(x−xg)2 +(y−yg)2 that measures the distance to the goal. With this new feature, the
linear function approximator does well.
23.4.2 Approximating temporal-diﬀerence learning
We can apply these ideas equally well to temporal-difference learners. All we need do is
adjust the parameters to try to reduce the temporal difference between successive states. The
new versions of the TD and Q-learning equations (23.3 on page 846 and 23.7 on page 853)
are given by
θi ←θi +α[R(s,a,s′)+γ ˆUθ(s′)−ˆUθ(s)]∂ˆUθ(s)
∂θi
(23.11)
for utilities and
θi ←θi +α[R(s,a,s′)+γ max
a′
ˆQθ(s′,a′)−ˆQθ(s,a)]∂ˆQθ(s,a)
∂θi
(23.12)
for Q-values. For passive TD learning, the update rule can be shown to converge to the closest
possible approximation to the true function when the function approximator is linear in the
features.4 With active learning and nonlinear functions such as neural networks, nearly all
bets are off: there are some very simple cases in which the parameters can go off to inﬁnity
with these update rules, even though there are good solutions in the hypothesis space. There
are more sophisticated algorithms that can avoid these problems, but at present reinforcement
learning with general function approximators remains a delicate art.
In addition to parameters diverging to inﬁnity, there is a more surprising problem called
catastrophic forgetting. Suppose you are training an autonomous vehicle to drive along
Catastrophic
forgetting
(simulated) roads safely without crashing. You assign a high negative reward for crossing
the edge of the road, and you use quadratic features of the road position so that the car can
learn that the utility of being in the middle of the road is higher than being close to the edge.
All goes well, and the car learns to drive perfectly down the middle of the road. After a few
minutes of this, you are starting to get bored and are about to halt the simulation and write
up the excellent results. All of a sudden, the vehicle swerves off the road and crashes. Why?
What has happened is that the car has learned too well: because it has learned to steer away
from the edge, it has learned that the entire central region of the road is a safe place to be, and
it has forgotten that the region closer to the edge is dangerous. The central region therefore
4
The deﬁnition of distance between utility functions is rather technical; see Tsitsiklis and Van Roy (1997).
