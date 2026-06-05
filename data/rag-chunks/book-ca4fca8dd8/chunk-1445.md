---
chunk_id: "book-ca4fca8dd8-chunk-1445"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1445
confidence: "first-pass"
extraction_method: "structured-local"
---

872
Chapter 23
Reinforcement Learning
They called their method behavioral cloning. A few years later, the same research group
reported that the method was much more fragile than had been reported initially (Camacho
and Michie, 1995): even very small perturbations caused the learned policy to deviate from
the desired trajectory, leading to compounding errors as the agent strayed further and further
from the training set. (See also the discussion on page 973.) Work on apprenticeship learning
aims to make the approach more robust, in part by including information about the desired
outcomes rather than just the expert policy. Ng et al. (2003) and Coates et al. (2009) show
how apprenticeship learning works for learning to ﬂy an actual helicopter, as illustrated in
Figure 23.9(b) on page 868.
Inverse reinforcement learning (IRL) was introduced by Russell (1998), and the ﬁrst al-
gorithms were developed by Ng and Russell (2000). (A similar problem has been studied in
economics for much longer, under the heading of structural estimation of MDPs (Sargent,
1978).) The algorithm given in the chapter is due to Abbeel and Ng (2004). Baker et al.
(2009) describe how the understanding of another agent’s actions can be seen as inverse plan-
ning. Ho et al. (2017) show that agents can learn better from behaviors that are instructive
rather than optimal. Hadﬁeld-Menell et al. (2017a) extend IRL into a game-theoretic formu-
lation that encompasses both observer and demonstrator, showing how teaching and learning
behaviors emerge as solutions of the game.
Garc´ıa and Fern´andez (2015) give a comprehensive survey on safe reinforcement learn-
ing. Munos et al. (2017) describe an algorithm for safe off-policy (e.g., Q-learning) explo-
ration. Hans et al. (2008) break the problem of safe exploration into two parts: deﬁning a
safety function to indicate which states to avoid, and deﬁning a backup policy to lead the
agent back to safety when it might otherwise enter an unsafe state. You et al. (2017) show
how to train a deep reinforcement learning model to drive a car in simulation, and then use
transfer learning to drive safely in the real world.
Thomas et al. (2017) offer an approach to learning that is guaranteed, with high proba-
bility, to do no worse than the current policy. Akametalu et al. (2014) describe a reachability-
based approach, in which the learning process operates under the guidance of a control policy
that ensures the agent never reaches an unsafe state. Saunders et al. (2018) demonstrate that
a system can use human intervention to stop it from wandering out of the safe region, and can
learn over time to need less intervention.
Policy search methods were brought to the fore by Williams (1992), who developed the
REINFORCE family of algorithms, which stands for “REward Increment = Nonnegative Fac-
tor × Offset Reinforcement × Characteristic Eligibility.” Later work by Marbach and Tsitsik-
lis (1998), Sutton et al. (2000), and Baxter and Bartlett (2000) strengthened and generalized
the convergence results for policy search. Schulman et al. (2015b) describe trust region pol-
icy optimization, a theoretically well-founded and also practical policy search algorithm that
has spawned many variants. The method of correlated sampling to reduce variance in Monte
Carlo comparisons is due to Kahn and Marshall (1953); it is also one of a number of variance
reduction methods explored by Hammersley and Handscomb (1964).
Early approaches to hierarchical reinforcement learning (HRL) attempted to construct
hierarchies using state abstraction—that is, grouping states together into abstract states and
then doing RL in the abstract state space (Dayan and Hinton, 1993). Unfortunately, the tran-
sition model for abstract states is typically non-Markovian, leading to divergent behavior of
standard RL algorithms. The temporal abstraction approach in this chapter was developed in
