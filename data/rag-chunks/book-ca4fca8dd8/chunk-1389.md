---
chunk_id: "book-ca4fca8dd8-chunk-1389"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1389
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.2
Passive Reinforcement Learning
843
of trials in the environment using its policy π. In each trial, the agent starts in state (1,1) and
Trial
experiences a sequence of state transitions until it reaches one of the terminal states, (4,2) or
(4,3). Its percepts supply both the current state and the reward received for the transition that
just occurred to reach that state. Typical trials might look like this:
(1,1) -.04
→
Up (1,2) -.04
→
Up (1,3) -.04
→
Right (1,2) -.04
→
Up (1,3) -.04
→
Right (2,3) -.04
→
Right (3,3)
+1
→
Right (4,3)
(1,1) -.04
→
Up (1,2) -.04
→
Up (1,3) -.04
→
Right (2,3) -.04
→
Right (3,3) -.04
→
Right (3,2) -.04
→
Up (3,3)
+1
→
Right (4,3)
(1,1) -.04
→
Up (1,2) -.04
→
Up (1,3) -.04
→
Right (2,3) -.04
→
Right (3,3) -.04
→
Right (3,2) -1
→
Up (4,2)
Note that each transition is annotated with both the action taken and the reward received at
the next state. The object is to use the information about rewards to learn the expected utility
Uπ(s) associated with each nonterminal state s. The utility is deﬁned to be the expected sum
of (discounted) rewards obtained if policy π is followed. As in Equation (16.2) on page 557,
we write
Uπ(s) = E
"
∞
∑
t =0
γtR(St,π(St),St+1)
#
,
(23.1)
where R(St,π(St),St+1) is the reward received when action π(St) is taken in state St and
reaches state St+1. Note that St is a random variable denoting the state reached at time t when
executing policy π, starting from state S0 =s. We will include a discount factor γ in all of
our equations, but for the 4×3 world we will set γ =1, which means no discounting.
23.2.1 Direct utility estimation
The idea of direct utility estimation is that the utility of a state is deﬁned as the expected
Direct utility
estimation
total reward from that state onward (called the expected reward-to-go), and that each trial
Reward-to-go
provides a sample of this quantity for each state visited. For example, the ﬁrst of the three
trials shown earlier provides a sample total reward of 0.76 for state (1,1), two samples of 0.80
and 0.88 for (1,2), two samples of 0.84 and 0.92 for (1,3), and so on. Thus, at the end of each
sequence, the algorithm calculates the observed reward-to-go for each state and updates the
estimated utility for that state accordingly, just by keeping a running average for each state
in a table. In the limit of inﬁnitely many trials, the sample average will converge to the true
expectation in Equation (23.1).
This means that we have reduced reinforcement learning to a standard supervised learn-
ing problem in which each example is a (state, reward-to-go) pair. We have a lot of powerful
algorithms for supervised learning, so this approach seems promising, but it ignores an im-
portant constraint: The utility of a state is determined by the reward and the expected utility ◀
of the successor states. More speciﬁcally, the utility values obey the Bellman equations for a
ﬁxed policy (see also Equation (16.14)):
Ui(s) = ∑
s′
P(s′ |s,πi(s))[R(s,πi(s),s′)+γUi(s′)].
(23.2)
By ignoring the connections between states, direct utility estimation misses opportunities for
learning. For example, the second of the three trials given earlier reaches the state (3,2),
which has not previously been visited. The next transition reaches (3,3), which is known
from the ﬁrst trial to have a high utility. The Bellman equation suggests immediately that
(3,2) is also likely to have a high utility, because it leads to (3,3), but direct utility estimation
