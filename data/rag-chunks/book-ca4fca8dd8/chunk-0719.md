---
chunk_id: "book-ca4fca8dd8-chunk-0719"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 719
confidence: "first-pass"
extraction_method: "structured-local"
---

432
Chapter 13
Probabilistic Reasoning
.001
.002
.70
.95
.94
.29
.001
.01
A
t
f
E
t
f
t
f
B
t
t
f
f
Burglary
P(B=true)
P(E=true)
P(M=true|A)
.90
.05
A
t
f
P(J=true|A)
P(A=true|B,E)
Alarm
JohnCalls
MaryCalls
Earthquake
Figure 13.2 A typical Bayesian network, showing both the topology and the conditional
probability tables (CPTs). In the CPTs, the letters B, E, A, J, and M stand for Burglary,
Earthquake, Alarm, JohnCalls, and MaryCalls, respectively.
tion 13.2.) Each row in a CPT contains the conditional probability of each node value for a
conditioning case. A conditioning case is just a possible combination of values for the parent
Conditioning case
nodes—a miniature possible world, if you like. Each row must sum to 1, because the entries
represent an exhaustive set of cases for the variable. For Boolean variables, once you know
that the probability of a true value is p, the probability of false must be 1 −p, so we often
omit the second number, as in Figure 13.2. In general, a table for a Boolean variable with k
Boolean parents contains 2k independently speciﬁable probabilities. A node with no parents
has only one row, representing the prior probabilities of each possible value of the variable.
Notice that the network does not have nodes corresponding to Mary’s currently listening
to loud music or to the telephone ringing and confusing John. These factors are summarized
in the uncertainty associated with the links from Alarm to JohnCalls and MaryCalls. This
shows both laziness and ignorance in operation, as explained on page 404: it would be a lot
of work to ﬁnd out why those factors would be more or less likely in any particular case, and
we have no reasonable way to obtain the relevant information anyway.
The probabilities actually summarize a potentially inﬁnite set of circumstances in which
the alarm might fail to go off (high humidity, power failure, dead battery, cut wires, a dead
mouse stuck inside the bell, etc.) or John or Mary might fail to call and report it (out to lunch,
on vacation, temporarily deaf, passing helicopter, etc.). In this way, a small agent can cope
with a very large world, at least approximately.
13.2 The Semantics of Bayesian Networks
The syntax of a Bayes net consists of a directed acyclic graph with some local probability
information attached to each node. The semantics deﬁnes how the syntax corresponds to a
joint distribution over the variables of the network.
Assume that the Bayes net contains n variables, X1,...,Xn. A generic entry in the joint
distribution is then P(X1 =x1 ∧... ∧Xn =xn), or P(x1,...,xn) for short. The semantics of
