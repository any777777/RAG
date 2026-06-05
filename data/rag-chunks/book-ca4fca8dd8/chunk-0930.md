---
chunk_id: "book-ca4fca8dd8-chunk-0930"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 930
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 16.2
Algorithms for MDPs
563
function VALUE-ITERATION(mdp,ϵ) returns a utility function
inputs: mdp, an MDP with states S, actions A(s), transition model P(s′ |s,a),
rewards R(s,a,s′), discount γ
ϵ, the maximum error allowed in the utility of any state
local variables: U, U′, vectors of utilities for states in S, initially zero
δ, the maximum relative change in the utility of any state
repeat
U ←U′; δ←0
for each state s in S do
U′[s]←maxa∈A(s) Q-VALUE(mdp,s,a,U)
if |U′[s] −U[s]| > δ then δ←|U′[s] −U[s]|
until δ ≤ϵ(1−γ)/γ
return U
Figure 16.6 The value iteration algorithm for calculating utilities of states. The termination
condition is from Equation (16.12).
state. The n equations contain n unknowns—the utilities of the states. So we would like to
solve these simultaneous equations to ﬁnd the utilities. There is one problem: the equations
are nonlinear, because the “max” operator is not a linear operator. Whereas systems of linear
equations can be solved quickly using linear algebra techniques, systems of nonlinear equa-
tions are more problematic. One thing to try is an iterative approach. We start with arbitrary
initial values for the utilities, calculate the right-hand side of the equation, and plug it into the
left-hand side—thereby updating the utility of each state from the utilities of its neighbors.
We repeat this until we reach an equilibrium.
Let Ui(s) be the utility value for state s at the ith iteration. The iteration step, called a
Bellman update, looks like this:
Bellman update
Ui+1(s) ←max
a∈A(s)∑
s′
P(s′ |s,a)[R(s,a,s′)+γUi(s′)],
(16.10)
where the update is assumed to be applied simultaneously to all the states at each iteration.
If we apply the Bellman update inﬁnitely often, we are guaranteed to reach an equilibrium
(see “convergence of value iteration” below), in which case the ﬁnal utility values must be
solutions to the Bellman equations. In fact, they are also the unique solutions, and the corre-
sponding policy (obtained using Equation (16.4)) is optimal. The detailed algorithm, includ-
ing a termination condition when the utilities are “close enough,” is shown in Figure 16.6.
Notice that we make use of the Q-VALUE function deﬁned on page 559.
We can apply value iteration to the 4×3 world in Figure 16.1(a). Starting with initial
values of zero, the utilities evolve as shown in Figure 16.7(a). Notice how the states at differ-
ent distances from (4,3) accumulate negative reward until a path is found to (4,3), whereupon
the utilities start to increase. We can think of the value iteration algorithm as propagating
information through the state space by means of local updates.
