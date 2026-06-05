---
chunk_id: "book-ca4fca8dd8-chunk-0817"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 817
confidence: "first-pass"
extraction_method: "structured-local"
---

492
Chapter 14
Probabilistic Reasoning over Time
14.3.1 Simpliﬁed matrix algorithms
With a single, discrete state variable Xt, we can give concrete form to the representations of
the transition model, the sensor model, and the forward and backward messages. Let the state
variable Xt have values denoted by integers 1,...,S, where S is the number of possible states.
The transition model P(Xt |Xt−1) becomes an S×S matrix T, where
Tij = P(Xt = j|Xt−1 =i).
That is, Tij is the probability of a transition from state i to state j. For example, if we number
the states Rain=true and Rain=false as 1 and 2, respectively, then the transition matrix for
the umbrella world deﬁned in Figure 14.2 is
T = P(Xt |Xt−1) =
 0.7 0.3
0.3 0.7

.
We also put the sensor model in matrix form. In this case, because the value of the evidence
variable Et is known at time t (call it et), we need only specify, for each state, how likely it
is that the state causes et to appear: we need P(et |Xt =i) for each state i. For mathematical
convenience we place these values into an S × S diagonal observation matrix, Ot, one for
Observation matrix
each time step. The ith diagonal entry of Ot is P(et |Xt =i) and the other entries are 0. For
example, on day 1 in the umbrella world of Figure 14.5, U1 =true, and on day 3, U3 =false,
so we have
O1 =
 0.9
0
0
0.2

;
O3 =
 0.1
0
0
0.8

.
Now, if we use column vectors to represent the forward and backward messages, all the com-
putations become simple matrix–vector operations. The forward equation (14.5) becomes
f1:t+1 = αOt+1T⊤f1:t
(14.12)
and the backward equation (14.9) becomes
bk+1:t = TOk+1bk+2:t .
(14.13)
From these equations, we can see that the time complexity of the forward–backward algo-
rithm (Figure 14.4) applied to a sequence of length t is O(S2t), because each step requires
multiplying an S-element vector by an S×S matrix. The space requirement is O(St), because
the forward pass stores t vectors of size S.
Besides providing an elegant description of the ﬁltering and smoothing algorithms for
HMMs, the matrix formulation reveals opportunities for improved algorithms. The ﬁrst is a
simple variation on the forward–backward algorithm that allows smoothing to be carried out
in constant space, independently of the length of the sequence. The idea is that smoothing
for any particular time slice k requires the simultaneous presence of both the forward and
backward messages, f1:k and bk+1:t, according to Equation (14.8). The forward–backward al-
gorithm achieves this by storing the fs computed on the forward pass so that they are available
during the backward pass. Another way to achieve this is with a single pass that propagates
both f and b in the same direction. For example, the “forward” message f can be propagated
backward if we manipulate Equation (14.12) to work in the other direction:
f1:t = α′(T⊤)−1O−1
t+1f1:t+1 .
The modiﬁed smoothing algorithm works by ﬁrst running the standard forward pass to com-
pute ft:t (forgetting all the intermediate results) and then running the backward pass for both
