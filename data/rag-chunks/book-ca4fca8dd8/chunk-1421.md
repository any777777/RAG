---
chunk_id: "book-ca4fca8dd8-chunk-1421"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1421
confidence: "first-pass"
extraction_method: "structured-local"
---

860
Chapter 23
Reinforcement Learning
The theoretical foundations of HRL are based on the concept of the joint state space, in
Joint state space
which each state (s,m) is composed of a physical state s and a machine state m. The machine
state is deﬁned by the current internal state of the agent program: the program counter for
each subroutine on the current call stack, the values of the arguments, and the values of all
local and global variables. For example, if the agent program has chosen to pass to teammate
Ali and is in the middle of calculating the speed of the pass, then the fact that Ali is the
argument of PASS-TO is part of the current machine state. A choice state σ=(s,m) is one
Choice state
in which the program counter for m is at a choice point in the agent program. Between two
choice states, any number of computational transitions and physical actions may occur, but
they are all preordained, so to speak: by deﬁnition, the agent isn’t making any choices in
between choice states. Essentially, the hierarchical RL agent is solving a Markovian decision
problem with the following elements:
• The states are the choice states σ of the joint state space.
• The actions at σ are the choices c available in σ according to the partial program.
• The reward function ρ(σ,c,σ′) is the expected sum of rewards for all physical transi-
tions occurring between the choice states σ and σ′.
• The transition model τ(σ,c,σ′) is deﬁned in the obvious way: if c invokes a physical ac-
tion a, then τ borrows from the physical model P(s′ |s,a); if c invokes a computational
transition, such as calling a subroutine, then the transition deterministically modiﬁes
the computational state m according to the rules of the programming language.6
By solving this decision problem, the agent ﬁnds the optimal policy that is consistent with
original partial program.
Hierarchical RL can be a very effective method for learning complex behaviors. In keep-
away, an HRL agent based on the partial program sketched above learns a policy that keeps
possession forever against the standard taker policy—a signiﬁcant improvement on the pre-
vious record of about 10 seconds. One important characteristic is that the lower-level skills
are not ﬁxed subroutines in the usual sense; their choices are sensitive to the entire internal
state of the agent program, so they behave differently depending on where they are invoked
within that program and what is going on at the time. If necessary, the Q-functions for the
lower-level choices can be initialized by a separate training process with its own reward func-
tion, and then integrated into the overall system so they can be adapted to function well in the
context of the whole agent.
In the preceding section we saw that shaping rewards can be helpful for learning com-
plex behaviors. In HRL, the fact that learning takes place in the joint state space provides
additional opportunities for shaping. For example, to help with learning the Q-function for
accurate passing within the PASS-TO routine, we can provide a shaping reward that depends
on the location of the intended recipient and the proximity of opponents to that player: the
ball should be close to the recipient and far from the opponents. That seems entirely obvious;
but the identity of the intended recipient for a pass is not part of the physical state of the
▶
6
Because more than one physical action may be executed before the next choice state is reached, the problem is
technically a semi-Markov decision process, which allows actions to have different durations, including stochastic
durations. If the discount factor γ < 1, then the action duration affects the discounting applied to the reward
obtained during the action, which means that some extra discount bookkeeping has to be done and the transition
model includes the duration distribution.
