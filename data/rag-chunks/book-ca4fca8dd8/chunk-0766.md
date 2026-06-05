---
chunk_id: "book-ca4fca8dd8-chunk-0766"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 766
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 462

462
Chapter 13
Probabilistic Reasoning
r
c
r
¬c
¬r
¬c
¬r
c
0.3856
0.1078
0.3922
0.8683
0.4074
0.1164
0.6296
0.0926
0.2778
0.0238
0.2222
0.4762
r
c
r
¬c
¬r
¬c
¬r
c
0.0000
0.0000
0.5000
1.0000
0.5000
0.0000
1.0000
0.0000
0.0000
0.0000
0.5000
0.5000
(a)
(b)
Figure 13.21 (a) The states and transition probabilities of the Markov chain for the query
P(Rain|Sprinkler=true,WetGrass=true).
Note the self-loops: the state stays the same
when either variable is chosen and then resamples the same value it already has. (b) The
transition probabilities when the CPT for Rain constrains it to have the same value as Cloudy.
We begin with some of the basic concepts for analyzing Markov chains in general. Any
such chain is deﬁned by its initial state and its transition kernel k(x →x′)—the probability
Transition kernel
of a transition to state x′ starting from state x. Now suppose that we run the Markov chain
for t steps, and let πt(x) be the probability that the system is in state x at time t. Similarly,
let πt+1(x′) be the probability of being in state x′ at time t +1. Given πt(x), we can calculate
πt+1(x′) by summing, for all states x the system could be in at time t, the probability of being
in x times the probability of making the transition to x′:
πt+1(x′) = ∑
x
πt(x)k(x →x′).
We say that the chain has reached its stationary distribution if πt =πt+1. Let us call this
Stationary
distribution
stationary distribution π; its deﬁning equation is therefore
π(x′) = ∑
x
π(x)k(x →x′)
for all x′ .
(13.11)
Provided the transition kernel k is ergodic—that is, every state is reachable from every other
Ergodic
and there are no strictly periodic cycles—there is exactly one distribution π satisfying this
equation for any given k.
Equation (13.11) can be read as saying that the expected “outﬂow” from each state (i.e.,
its current “population”) is equal to the expected “inﬂow” from all the states. One obvious
way to satisfy this relationship is if the expected ﬂow between any pair of states is the same
in both directions; that is,
π(x)k(x →x′) = π(x′)k(x′ →x)
for all x, x′ .
(13.12)
When these equations hold, we say that k(x →x′) is in detailed balance with π(x). One
Detailed balance
special case is the self-loop x = x′, i.e., a transition from a state to itself. In that case, the
detailed balance condition becomes π(x)k(x →x)=π(x)k(x →x) which is of course trivially
true for any stationary distribution π and any transition kernel k.

## Page 463
