---
chunk_id: "book-ca4fca8dd8-chunk-1415"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1415
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.4
Generalization in Reinforcement Learning
857
has a ﬂat value function, so the quadratic features get zero weight; then, any nonzero weight
on the linear features causes the car to slide off the road to one side or the other.
One solution to this problem, called experience replay, ensures that the car keeps re-
Experience replay
living its youthful crashing behavior at regular intervals. The learning algorithm can retain
trajectories from the entire learning process and replay those trajectories to ensure that its
value function is still accurate for parts of the state space it no longer visits.
For model-based reinforcement learning systems, function approximation can also be
very helpful for learning a model of the environment. Remember that learning a model for
an observable environment is a supervised learning problem, because the next percept gives
the outcome state. Any of the supervised learning methods in Chapters 19, 21, and 22 can be
used, with suitable adjustments for the fact that we need to predict a complete state description
rather than just a Boolean classiﬁcation or a single real value. With a learned model, the agent
can do a look-ahead search to improve its decisions and can carry out internal simulations to
improve its approximate representations of U or Q rather than requiring slow and potentially
expensive real-world experiences.
For a partially observable environment, the learning problem is much more difﬁcult be-
cause the next percept is no longer a label for the state prediction problem. If we know what
the hidden variables are and how they are causally related to each other and to the observable
variables, then we can ﬁx the structure of a dynamic Bayesian network and use the EM algo-
rithm to learn the parameters, as was described in Chapter 21. Learning the internal structure
of dynamic Bayesian networks and creating new state variables is still considered a difﬁcult
problem. Deep recurrent neural networks (Section 22.6) have in some cases been successful
at inventing the hidden structure.
23.4.3 Deep reinforcement learning
There are two reasons why we need to go beyond linear function approximators: ﬁrst, there
may be no good linear function that comes close to approximating the utility function or
the Q-function; second, we may not be able to invent the necessary features, particularly in
new domains. If you think about it, these are really the same reason: it is always possible
to represent U or Q as linear combinations of features, especially if we have features such
as f1(s)=U(s) or f2(s,a)=Q(s,a), but unless we can come up with such features (in an
efﬁciently computable form) the linear function approximator may be insufﬁcient.
For these reasons (or reason), researchers have explored more complex, nonlinear func-
tion approximators since the earliest days of reinforcement learning. Currently, deep neural
networks (Chapter 22) are very popular in this role and have proved to be effective even when
the input is a raw image with no human-designed feature extraction at all. If all goes well,
the deep neural network in effect discovers the useful features for itself. And if the ﬁnal layer
of the network is linear, then we can see what features the network is using to build its own
linear function approximator. A reinforcement learning system that uses a deep network as a
function approximator is called a deep reinforcement learning system.
Just as in Equation (23.9), the deep network is a function parameterized by θ, except that
now the function is much more complicated. The parameters are all the weights in all the
layers of the network. Nonetheless, the gradients required for Equations (23.11) and (23.12)
are just the same as the gradients required for supervised learning, and they can be computed
by the same back-propagation process described in Section 22.4.
