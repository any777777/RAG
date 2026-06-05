---
chunk_id: "book-ca4fca8dd8-chunk-0894"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 894
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 15.6
The Value of Information
541
function INFORMATION-GATHERING-AGENT(percept) returns an action
persistent: D, a decision network
integrate percept into D
j←the value that maximizes VPI(E j) / C(E j)
if VPI(E j) > C(E j)
then return Request(E j)
else return the best action from D
Figure 15.9 Design of a simple, myopic information-gathering agent. The agent works by
repeatedly selecting the observation with the highest information value, until the cost of the
next observation is greater than its expected beneﬁt.
15.6.5 Nonmyopic information gathering
The fact that the value of a sequence of observations is invariant under permutations of the
sequence is intriguing but doesn’t, by itself, lead to efﬁcient algorithms for optimal infor-
mation gathering. Even if we restrict ourselves to choosing in advance a ﬁxed subset of
observations to collect, there are 2n possible such subsets from n potential observations. In
the general case, we face an even more complex problem of ﬁnding an optimal conditional
plan (as described in Section 11.5.2) that chooses an observation and then acts or chooses
more observations, depending on the outcome. Such plans form trees, and the number of
such trees is superexponential in n.9
For observations of variables in a decision network, it turns out that this problem is in-
tractable even when the network is a polytree. There are, however, special cases in which the
problem can be solved efﬁciently. Here we present one such case: the treasure hunt problem
Treasure hunt
(or the least-cost testing sequence problem, for the less romantically inclined). There are n
locations 1,...,n; each location i contains treasure with independent probability P(i); and it
costs C(i) to check location i. This corresponds to a decision network where all the potential
evidence variables Treasurei are absolutely independent. The agent examines locations in
some order until treasure is found; the question is, what is the optimal order?
To answer this question, we will need to consider the expected costs and success prob-
abilities of various sequences of observations, assuming the agent stops when treasure is
found. Let x be such a sequence; xy be the concatenation of sequences x and y; C(x) be the
expected cost of x; P(x) be the probability that sequence x succeeds in ﬁnding treasure; and
F(x)=1−P(x) be the probability that it fails. Given these deﬁnitions, we have
C(xy) = C(x)+F(x)C(y),
(15.3)
that is, the sequence xy will deﬁnitely incur the cost of x and, if x fails, it will also incur the
cost of y.
The basic idea in any sequence optimization problem is to look at the change in cost,
deﬁned by ∆=C(wxyz) −C(wyxz), when two adjacent subsequences x and y in a general
sequence wxyz are ﬂipped. When the sequence is optimal, all such changes make the se-
quence worse. The ﬁrst step is to show that the sign of the effect (increasing or decreasing
9
The general problem of generating sequential behavior in a partially observable environment falls under the
heading of partially observable Markov decision processes, which are described in Chapter 16.
