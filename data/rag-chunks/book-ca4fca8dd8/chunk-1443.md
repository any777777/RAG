---
chunk_id: "book-ca4fca8dd8-chunk-1443"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1443
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
871
reinforcement learning combines inﬂuences from animal psychology, neuroscience, opera-
tions research, and optimal control theory.
The connection between reinforcement learning and Markov decision processes was ﬁrst
made by Werbos (1977). (Work by Ian Witten (1977) described a TD-like process in the
language of control theory.) The development of reinforcement learning in AI stems primarily
from work at the University of Massachusetts in the early 1980s (Barto et al., 1981). An
inﬂuential paper by Rich Sutton (1988) provided a mathematical understanding of temporal-
difference methods. The combination of temporal-difference learning with the model-based
generation of simulated experiences was proposed in Sutton’s DYNA architecture (Sutton,
1990). Q-learning was developed in Chris Watkins’s Ph.D. thesis (1989), while SARSA
appeared in a technical report by Rummery and Niranjan (1994). Prioritized sweeping was
introduced independently by Moore and Atkeson (1993) and Peng and Williams (1993).
Function approximation in reinforcement learning goes back to Arthur Samuel’s checkers
program (1959). The use of neural networks to represent value functions was common in the
1980s and came to the fore in Gerry Tesauro’s TD-Gammon program (Tesauro, 1992, 1995).
Deep neural networks are currently the most popular choice for function approximators in
reinforcement learning. Arulkumaran et al. (2017) and Francois-Lavet et al. (2018) give
overviews of deep RL. The DQN system (Mnih et al., 2015) uses a deep network to learn
a Q-function, while ALPHAZERO (Silver et al., 2018) learns both a value function for use
with a known model and a Q-function for use in metalevel decisions that guide search. Irpan
(2018) warns that deep RL systems can perform poorly if the actual environment is even
slightly different from the training environment.
Weighted linear combinations of features and neural networks are factored represen-
tations for function approximation. It is also possible to apply reinforcement learning to
structured representations; this is called relational reinforcement learning (Tadepalli et al.,
2004). The use of relational descriptions allows for generalization across complex behaviors
involving different objects.
Analysis of the convergence properties of reinforcement learning algorithms using func-
tion approximation is an extremely technical subject. Results for TD learning have been pro-
gressively strengthened for the case of linear function approximators (Sutton, 1988; Dayan,
1992; Tsitsiklis and Van Roy, 1997), but several examples of divergence have been presented
for nonlinear functions (see Tsitsiklis and Van Roy, 1997, for a discussion). Papavassiliou
and Russell (1999) describe a type of reinforcement learning that converges with any form of
function approximator, provided that the problem of ﬁtting the hypothesis to the data is solv-
able. Liu et al. (2018) describe the family of gradient TD algorithms and provide extensive
theoretical analysis of convergence and sample complexity.
A variety of exploration methods for sequential decision problems are discussed by Barto
et al. (1995). Kearns and Singh (1998) and Brafman and Tennenholtz (2000) describe algo-
rithms that explore unknown environments and are guaranteed to converge on near-optimal
policies with a sample complexity that is polynomial in the number of states. Bayesian re-
inforcement learning (Dearden et al., 1998, 1999) provides another angle on both model
uncertainty and exploration.
The basic idea underlying imitation learning is to apply supervised learning to a training
set of expert actions. This is an old idea in adaptive control, but ﬁrst came to prominence
in AI with the work of Sammut et al. (1992) on “Learning to Fly” in a ﬂight simulator.
