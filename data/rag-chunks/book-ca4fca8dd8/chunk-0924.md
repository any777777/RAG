---
chunk_id: "book-ca4fca8dd8-chunk-0924"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 924
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.1
Sequential Decision Problems
557
algorithms for solving MDPs to fail with additive rewards, and so provides a good rea-
son for using discounted rewards.
3. Inﬁnite sequences can be compared in terms of the average reward obtained per time
Average reward
step. Suppose that transitions to square (1,1) in the 4×3 world have a reward of 0.1
while transitions to other nonterminal states have a reward of 0.01. Then a policy that
does its best to stay in (1,1) will have higher average reward than one that stays else-
where. Average reward is a useful criterion for some problems, but the analysis of
average-reward algorithms is complex.
Additive discounted rewards present the fewest difﬁculties in evaluating histories, so we shall
use them henceforth.
16.1.2 Optimal policies and the utilities of states
Having decided that the utility of a given history is the sum of discounted rewards, we can
compare policies by comparing the expected utilities obtained when executing them. We
assume the agent is in some initial state s and deﬁne St (a random variable) to be the state the
agent reaches at time t when executing a particular policy π. (Obviously, S0 =s, the state the
agent is in now.) The probability distribution over state sequences S1,S2,..., is determined
by the initial state s, the policy π, and the transition model for the environment.
The expected utility obtained by executing π starting in s is given by
Uπ(s) = E
"
∞
∑
t =0
γtR(St,π(St),St+1)
#
,
(16.2)
where the expectation E is with respect to the probability distribution over state sequences
determined by s and π. Now, out of all the policies the agent could choose to execute starting
in s, one (or more) will have higher expected utilities than all the others. We’ll use π∗
s to
denote one of these policies:
π∗
s = argmax
π
Uπ(s).
(16.3)
Remember that π∗
s is a policy, so it recommends an action for every state; its connection
with s in particular is that it’s an optimal policy when s is the starting state. A remarkable
consequence of using discounted utilities with inﬁnite horizons is that the optimal policy is
independent of the starting state. (Of course, the action sequence won’t be independent;
remember that a policy is a function specifying an action for each state.) This fact seems
intuitively obvious: if policy π∗
a is optimal starting in a and policy π∗
b is optimal starting in b,
then, when they reach a third state c, there’s no good reason for them to disagree with each
other, or with π∗
c, about what to do next.3 So we can simply write π∗for an optimal policy.
Given this deﬁnition, the true utility of a state is just Uπ∗(s)—that is, the expected sum of
discounted rewards if the agent executes an optimal policy. We write this as U(s), matching
the notation used in Chapter 15 for the utility of an outcome. Figure 16.3 shows the utilities
for the 4×3 world. Notice that the utilities are higher for states closer to the +1 exit, because
fewer steps are required to reach the exit.
3
Although this seems obvious, it does not hold for ﬁnite-horizon policies or for other ways of combining rewards
over time, such as taking the max. The proof follows directly from the uniqueness of the utility function on states,
as shown in Section 16.2.1.
