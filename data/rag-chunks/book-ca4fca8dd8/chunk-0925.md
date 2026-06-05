---
chunk_id: "book-ca4fca8dd8-chunk-0925"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 925
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 558

558
Chapter 16
Making Complex Decisions
0.8516
0.9078
0.9578
0.8016
0.7003
0.7453
0.6953
0.6514
0.4279
Figure 16.3 The utilities of the states in the 4×3 world with γ =1 and r= −0.04 for tran-
sitions to nonterminal states.
The utility function U(s) allows the agent to select actions by using the principle of
maximum expected utility from Chapter 15—that is, choose the action that maximizes the
reward for the next step plus the expected discounted utility of the subsequent state:
π∗(s) = argmax
a∈A(s) ∑
s′
P(s′ |s,a)[R(s,a,s′)+γU(s′)].
(16.4)
We have deﬁned the utility of a state, U(s), as the expected sum of discounted rewards from
that point onwards. From this, it follows that there is a direct relationship between the utility
of a state and the utility of its neighbors: the utility of a state is the expected reward for the
▶
next transition plus the discounted utility of the next state, assuming that the agent chooses
the optimal action. That is, the utility of a state is given by
U(s) = max
a∈A(s)∑
s′
P(s′ |s,a)[R(s,a,s′)+γU(s′)].
(16.5)
This is called the Bellman equation, after Richard Bellman (1957). The utilities of the
Bellman equation
states—deﬁned by Equation (16.2) as the expected utility of subsequent state sequences—are
solutions of the set of Bellman equations. In fact, they are the unique solutions, as we show
in Section 16.2.1.
Let us look at one of the Bellman equations for the 4×3 world. The expression for
U(1,1) is
max{ [0.8(−0.04+γU(1,2))+0.1(−0.04+γU(2,1))+0.1(−0.04+γU(1,1))],
[0.9(−0.04+γU(1,1))+0.1(−0.04+γU(1,2))],
[0.9(−0.04+γU(1,1))+0.1(−0.04+γU(2,1))],
[0.8(−0.04+γU(2,1))+0.1(−0.04+γU(1,2))+0.1(−0.04+γU(1,1))]}
where the four expressions correspond to Up, Left, Down and Right moves. When we plug in
the numbers from Figure 16.3, with γ =1, we ﬁnd that Up is the best action.
Another important quantity is the action-utility function, or Q-function: Q(s,a) is the
Q-function
expected utility of taking a given action in a given state. The Q-function is related to utilities
in the obvious way:
U(s) = max
a Q(s,a).
(16.6)

## Page 559
