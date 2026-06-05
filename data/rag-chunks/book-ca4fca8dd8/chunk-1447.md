---
chunk_id: "book-ca4fca8dd8-chunk-1447"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1447
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
873
the late 1990s (Parr and Russell, 1998; Andre and Russell, 2002; Sutton et al., 2000) and ex-
tended to handle concurrent behaviors by Marthi et al. (2005). Dietterich (2000) introduced
the notion of an additive decomposition of Q-functions induced by the subroutine hierarchy.
Temporal abstraction is based on a much earlier result due to Forestier and Varaiya (1978),
who showed that a large MDP can be decomposed into a two-layer system in which a su-
pervisory layer chooses among low-level controllers, each of which returns control to the
supervisor on completion. The problem of learning the abstraction hierarchy itself has been
studied at least since the work of Peter Andreae (1985); for a recent exploration into learn-
ing robot motion primitives, see Frans et al. (2018). The keepaway game was introduced by
Stone et al. (2005); the HRL solution given here is due to Bai and Russell (2017).
Neuroscience has often inspired reinforcement learning and conﬁrmed the value of the
approach. Research using single-cell recording suggests that the dopamine system in primate
brains implements something resembling value-function learning (Schultz et al., 1997). The
neuroscience text by Dayan and Abbott (2001) describes possible neural implementations of
temporal-difference learning; related research describes other neuroscientiﬁc and behavioral
experiments (Dayan and Niv, 2008; Niv, 2009; Lee et al., 2012).
Work in reinforcement learning has been accelerated by the availability of open-source
simulation environments for developing and testing learning agents. The University of Al-
berta’s Arcade Learning Environment (ALE) (Bellemare et al., 2013) provided such a frame-
work for 55 classic Atari video games. The pixels on the screen are provided to the agent as
percepts, along with a hardwired score of the game so far. ALE was used by the DeepMind
team to implement DQN learning and verify the generality of their system on a wide variety
of games (Mnih et al., 2015).
DeepMind in turn open-sourced several agent platforms, including the DeepMind Lab
(Beattie et al., 2016), the AI Safety Gridworlds (Leike et al., 2017), the Unity game platform
(Juliani et al., 2018), and the DM Control Suite (Tassa et al., 2018). Blizzard released the
StarCraft II Learning Environment (SC2LE), to which DeepMind added the PySC2 compo-
nent for machine learning in Python (Vinyals et al., 2017a).
Facebook’s AI Habitat simulation (Savva et al., 2019) provides a photo-realistic virtual
environment for indoor robotic tasks, and their HORIZON platform (Gauci et al., 2018) en-
ables reinforcement learning in large-scale production systems. The SYNTHIA system (Ros
et al., 2016) is a simulation environment designed for improving the computer vision ca-
pabilities of self-driving cars. The OpenAI Gym (Brockman et al., 2016) provides several
environments for reinforcement learning agents, and is compatible with other simulations
such as the Google Football simulator.
Littman (2015) surveys reinforcement learning for a general scientiﬁc audience. The
canonical text by Sutton and Barto (2018), two of the ﬁeld’s pioneers, shows how reinforce-
ment learning weaves together the ideas of learning, planning, and acting. Kochenderfer
(2015) takes a slightly less mathematical approach, with plenty of real-world examples. A
short book by Szepesvari (2010) gives an overview of reinforcement learning algorithms.
Bertsekas and Tsitsiklis (1996) provide a rigorous grounding in the theory of dynamic pro-
gramming and stochastic convergence. Reinforcement learning papers are published fre-
quently in the journals Machine Learning and Journal of Machine Learning Research, and
in the the proceedings of the International Conference on Machine Learning (ICML) and the
Neural Information Processing Systems (NeurIPS) conferences.
