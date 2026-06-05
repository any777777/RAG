---
chunk_id: "book-ca4fca8dd8-chunk-0811"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 811
confidence: "first-pass"
extraction_method: "structured-local"
---

488
Chapter 14
Probabilistic Reasoning over Time
function FORWARD-BACKWARD(ev,prior) returns a vector of probability distributions
inputs: ev, a vector of evidence values for steps 1,...,t
prior, the prior distribution on the initial state, P(X0)
local variables: fv, a vector of forward messages for steps 0,...,t
b, a representation of the backward message, initially all 1s
sv, a vector of smoothed estimates for steps 1,...,t
fv[0]←prior
for i= 1 to t do
fv[i]←FORWARD(fv[i−1],ev[i])
for i= t down to 1 do
sv[i]←NORMALIZE(fv[i]×b)
b←BACKWARD(b,ev[i])
return sv
Figure 14.4 The forward–backward algorithm for smoothing: computing posterior prob-
abilities of a sequence of states given a sequence of observations.
The FORWARD and
BACKWARD operators are deﬁned by Equations (14.5) and (14.9), respectively.
Plugging this into Equation (14.10), we ﬁnd that the smoothed estimate for rain on day 1 is
P(R1 |u1,u2) = α⟨0.818,0.182⟩×⟨0.69,0.41⟩≈⟨0.883,0.117⟩.
Thus, the smoothed estimate for rain on day 1 is higher than the ﬁltered estimate (0.818) in
this case. This is because the umbrella on day 2 makes it more likely to have rained on day
2; in turn, because rain tends to persist, that makes it more likely to have rained on day 1.
Both the forward and backward recursions take a constant amount of time per step; hence,
the time complexity of smoothing with respect to evidence e1:t is O(t). This is the complexity
for smoothing at a particular time step k. If we want to smooth the whole sequence, one
obvious method is simply to run the whole smoothing process once for each time step to be
smoothed. This results in a time complexity of O(t2).
A better approach uses a simple application of dynamic programming to reduce the com-
plexity to O(t). A clue appears in the preceding analysis of the umbrella example, where we
were able to reuse the results of the forward-ﬁltering phase. The key to the linear-time algo-
rithm is to record the results of forward ﬁltering over the whole sequence. Then we run the
backward recursion from t down to 1, computing the smoothed estimate at each step k from
the computed backward message bk+1:t and the stored forward message f1:k. The algorithm,
aptly called the forward–backward algorithm, is shown in Figure 14.4.
Forward–backward
algorithm
The alert reader will have spotted that the Bayesian network structure shown in Fig-
ure 14.3 is a polytree as deﬁned on page 451. This means that a straightforward application
of the clustering algorithm also yields a linear-time algorithm that computes smoothed es-
timates for the entire sequence. It is now understood that the forward–backward algorithm
is in fact a special case of the polytree propagation algorithm used with clustering methods
(although the two were developed independently).
The forward–backward algorithm forms the computational backbone for many applica-
tions that deal with sequences of noisy observations. As described so far, it has two practical
drawbacks. The ﬁrst is that its space complexity can be too high when the state space is large
