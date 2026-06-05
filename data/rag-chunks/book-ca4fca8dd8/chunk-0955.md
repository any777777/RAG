---
chunk_id: "book-ca4fca8dd8-chunk-0955"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 955
confidence: "first-pass"
extraction_method: "structured-local"
---

578
Chapter 16
Making Complex Decisions
16.4 Partially Observable MDPs
The description of Markov decision processes in Section 16.1 assumed that the environment
was fully observable. With this assumption, the agent always knows which state it is in.
This, combined with the Markov assumption for the transition model, means that the optimal
policy depends only on the current state.
When the environment is only partially observable, the situation is, one might say, much
less clear. The agent does not necessarily know which state it is in, so it cannot execute the
action π(s) recommended for that state. Furthermore, the utility of a state s and the optimal
action in s depend not just on s, but also on how much the agent knows when it is in s. For
these reasons, partially observable MDPs (or POMDPs—pronounced “pom-dee-pees”) are
Partially observable
MDP
usually viewed as much more difﬁcult than ordinary MDPs. We cannot avoid POMDPs,
however, because the real world is one.
16.4.1 Deﬁnition of POMDPs
To get a handle on POMDPs, we must ﬁrst deﬁne them properly. A POMDP has the same
elements as an MDP—the transition model P(s′ |s,a), actions A(s), and reward function
R(s,a,s′)—but, like the partially observable search problems of Section 4.4, it also has a
sensor model P(e|s). Here, as in Chapter 14, the sensor model speciﬁes the probability of
perceiving evidence e in state s.5 For example, we can convert the 4×3 world of Figure 16.1
into a POMDP by adding a noisy or partial sensor instead of assuming that the agent knows
its location exactly. The noisy four-bit sensor from page 494 could be used, which reports the
presence or absence of a wall in each compass direction with accuracy 1−ϵ.
As with MDPs, we can obtain compact representations for large POMDPs by using dy-
namic decision networks (see Section 16.1.4). We add sensor variables Et, assuming that the
state variables Xt may not be directly observable. The POMDP sensor model is then given
by P(Et|Xt). For example, we might add sensor variables to the DDN in Figure 16.4 such as
BatteryMetert to estimate the actual charge Batteryt and Speedometert to estimate the mag-
nitude of the velocity vector ˙Xt. A sonar sensor Wallst might give estimated distances to the
nearest wall in each of the four cardinal directions relative to the robot’s current orientation;
these values depends on the current position and orientation Xt.
In Chapters 4 and 11, we studied nondeterministic and partially observable planning
problems and identiﬁed the belief state—the set of actual states the agent might be in—as a
key concept for describing and calculating solutions. In POMDPs, the belief state b becomes
a probability distribution over all possible states, just as in Chapter 14. For example, the initial
belief state for the 4×3 POMDP could be the uniform distribution over the nine nonterminal
states along with 0s for the terminal states, that is, ⟨1
9, 1
9, 1
9, 1
9, 1
9, 1
9, 1
9, 1
9, 1
9,0,0⟩.
We use the notation b(s) to refer to the probability assigned to the actual state s by be-
lief state b. The agent can calculate its current belief state as the conditional probability
distribution over the actual states given the sequence of percepts and actions so far. This is
essentially the ﬁltering task described in Chapter 14. The basic recursive ﬁltering equation
(14.5 on page 485) shows how to calculate the new belief state from the previous belief state
and the new evidence. For POMDPs, we also have an action to consider, but the result is
essentially the same. If b was the previous belief state, and the agent does action a and then
5
The sensor model can also depend on the action and outcome state, but this change is not fundamental.
