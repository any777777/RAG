---
chunk_id: "book-ca4fca8dd8-chunk-1392"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1392
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 845

Section 23.2
Passive Reinforcement Learning
845
function PASSIVE-ADP-LEARNER(percept) returns an action
inputs: percept, a percept indicating the current state s′ and reward signal r
persistent: π, a ﬁxed policy
mdp, an MDP with model P, rewards R, actions A, discount γ
U, a table of utilities for states, initially empty
Ns′|s,a, a table of outcome count vectors indexed by state and action, initially zero
s, a, the previous state and action, initially null
if s′ is new then U[s′]←0
if s is not null then
increment Ns′|s,a[s,a][s’]
R[s, a, s′]←r
add a to A[s]
P(· | s,a)←NORMALIZE(Ns′|s,a[s, a])
U ←POLICYEVALUATION(π, U, mdp)
s,a←s′,π[s′]
return a
Figure 23.2 A passive reinforcement learning agent based on adaptive dynamic program-
ming. The agent chooses a value for γ and then incrementally computes the P and R values
of the MDP. The POLICY-EVALUATION function solves the ﬁxed-policy Bellman equations,
as described on page 567.
 0.5
 0.6
 0.7
 0.8
 0.9
 1
 0
 20
 40
 60
 80
 100
(1,1)
(1,3)
(2,1)
(3,2)
(3,3)
Utility estimates
Number of trials
 0
 0.05
 0.1
 0.15
 0.2
 0
 20
 40
 60
 80
 100
RMS error in utility
Number of trials
(a)
(b)
Figure 23.3 The passive ADP learning curves for the 4×3 world, given the optimal policy
shown in Figure 23.1. (a) The utility estimates for a selected subset of states, as a function
of the number of trials. Notice that it takes 14 and 23 trials respectively before the rarely
visited states (2,1) and (3,2) “discover” that they connect to the +1 exit state at (4,3). (b) The
root-mean-square error (see Appendix A) in the estimate for U(1,1), averaged over 50 runs
of 100 trials each.

## Page 846
