---
chunk_id: "book-ca4fca8dd8-chunk-1427"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1427
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 23.6
Apprenticeship and Inverse Reinforcement Learning
863
Thus, the true gradient of the policy value is approximated by a sum of terms involving
the gradient of the action-selection probability in each trial. For the sequential case, this
generalizes to
∇θρ(θ) ≈1
N
N
∑
j=1
uj(s)∇θπθ(s,aj)
πθ(s,aj)
for each state s visited, where aj is executed in s on the jth trial and uj(s) is the total reward
received from state s onward in the jth trial. The resulting algorithm, called REINFORCE, is
due to Ron Williams (1992); it is usually much more effective than hill climbing using lots of
trials at each value of θ. However, it is still much slower than necessary.
Consider the following task: given two blackjack policies, determine which is best. The
policies might have true net returns per hand of, say, −0.21% and +0.06%, so ﬁnding out
which is better is very important. One way to do this is to have each policy play against a
standard “dealer” for a certain number of hands and then to measure their respective winnings.
The problem with this, as we have seen, is that the winnings of each policy ﬂuctuate wildly
depending on whether it receives good or bad cards. One would need several million hands to
have a reliable indication of which policy is better. The same issue arises when using random
sampling to compare two adjacent policies in a hill-climbing algorithm.
A better solution for blackjack is to generate a certain number of hands in advance and
have each program play the same set of hands. In this way, we eliminate the measurement ◀
error due to differences in the cards received. Only a few thousand hands are needed to
determine which of the two blackjack policies is better.
This idea, called correlated sampling, can be applied to policy search in general, given
Correlated sampling
an environment simulator in which the random-number sequences can be repeated. It was
implemented in a policy-search algorithm called PEGASUS (Ng and Jordan, 2000), which
was one of the ﬁrst algorithms to achieve completely stable autonomous helicopter ﬂight (see
Figure 23.9(b)). It can be shown that the number of random sequences required to ensure
that the value of every policy is well estimated depends only on the complexity of the policy
space, and not at all on the complexity of the underlying domain.
23.6 Apprenticeship and Inverse Reinforcement Learning
Some domains are so complex that it is difﬁcult to deﬁne a reward function for use in rein-
forcement learning. Exactly what do we want our self-driving car to do? Certainly it should
not take too long to get to the destination, but it should not drive so fast as to incur undue
risk or to get speeding tickets. It should conserve fuel/energy. It should avoid jostling or
accelerating the passengers too much, but it can slam on the brakes in an emergency. And
so on. Deciding how much weight to give to each of these factors is a difﬁcult task. Worse
still, there are almost certainly important factors we have forgotten, such as the obligation
to behave with consideration for other drivers. Omitting a factor usually leads to behavior
that assigns an extreme value to the omitted factor—in this case, extremely inconsiderate
driving—in order to maximize the remaining factors.
One approach is to do extensive testing in simulation, notice problematic behaviors, and
try to modify the reward function to eliminate those behaviors. Another approach is to seek
additional sources of information about the appropriate reward function. One such source
