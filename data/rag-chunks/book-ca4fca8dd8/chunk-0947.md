---
chunk_id: "book-ca4fca8dd8-chunk-0947"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 947
confidence: "first-pass"
extraction_method: "structured-local"
---

574
Chapter 16
Making Complex Decisions
λ
λ
λ
λ
λ
λ
λ
λ
λ
λ
λ
λ
0
2
0
7.2
0
0
0
2
0
7.2
0
0
0
0
0
0
0
(a)
(b)
Figure 16.13 (a) The reward sequence M =0,2,0,7.2,0,0,0,... augmented with a choice to
switch permanently to a constant arm Mλ at each point. (b) An MDP whose optimal value
is exactly equivalent to the optimal value for (a), at the point where the optimal policy is
indifferent between M and Mλ.
maximum value attained by the ratio. In combination with a ﬁxed arm Mλ with 0 < λ ≤
1.0133, the optimal policy collects the ﬁrst four rewards from M and then switches to Mλ.
For λ > 1.0133, the optimal policy always chooses Mλ.
To calculate the Gittins index for a general arm M with current state s, we simply make
the following observation: at the tipping point where an optimal policy is indifferent between
choosing arm M and choosing the ﬁxed arm Mλ, the value of choosing M is the same as the
value of choosing an inﬁnite sequence of λ-rewards.
Suppose we augment M so that at each state in M, the agent has two choices: either
continue with M as before, or quit and receive an inﬁnite sequence of λ-rewards (see Fig-
ure 16.13(a)). This turns M into an MDP, whose optimal policy is just the optimal stopping
rule for M. Hence the value of an optimal policy in this new MDP is equal to the value of
an inﬁnite sequence of λ-rewards, that is, λ/(1−γ). So we can just solve this MDP ...but,
unfortunately, we don’t know the value of λ to put into the MDP, as this is precisely what
we are trying to calculate. But we do know that, at the tipping point, an optimal policy is
indifferent between M and Mλ, so we could replace the choice to get an inﬁnite sequence of
λ-rewards with the choice to go back and restart M from its initial state s. (More precisely, we
add a new action in every state that has the same rewards and outcomes as the action avail-
able in s; see Exercise 16.KATV.) This new MDP Ms, called a restart MDP, is illustrated in
Restart MDP
Figure 16.13(b).
We have the general result that the Gittins index for an arm M in state s is equal to 1−γ
times the value of an optimal policy for the restart MDP Ms. This MDP can be solved by any
of the algorithms in Section 16.2. Value iteration applied to Ms in Figure 16.13(b) gives a
value of 2.0266 for the start state, so we have λ=2.0266·(1−γ)=1.0133 as before.
16.3.2 The Bernoulli bandit
Perhaps the simplest and best-known instance of a bandit problem is the Bernoulli bandit,
Bernoulli bandit
where each arm Mi produces a reward of 0 or 1 with a ﬁxed but unknown probability µi.
The state of arm Mi is deﬁned by si and fi, the counts of successes (1s) and failures (0s) so
far for that arm; the transition probability predicts the next outcome to be 1 with probability
(si)/(si + fi) and 0 with probability (fi)/(si + fi). The counts are initialized to 1 so that
the initial probabilities are 1/2 rather than 0/0.4 The Markov reward process is shown in
Figure 16.14(a).
4
The probabilities are those of a Bayesian updating process with a Beta(1,1) prior (see Section 21.2.5).
