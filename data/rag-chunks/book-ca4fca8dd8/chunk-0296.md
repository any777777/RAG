---
chunk_id: "book-ca4fca8dd8-chunk-0296"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 296
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 5.4
Local Search for CSPs
181
For example, consider the state {WA = red,NT = green,Q = blue} in the bottom row of
Figure 5.6. Forward checking can tell us this state is a no-good because there is no valid
assignment to SA. In this particular case, recording the no-good would not help, because
once we prune this branch from the search tree, we will never encounter this combination
again. But suppose that the search tree in Figure 5.6 were actually part of a larger search
tree that started by ﬁrst assigning values for V and T. Then it would be worthwhile to record
{WA = red,NT = green,Q = blue} as a no-good because we are going to run into the same
problem again for each possible set of assignments to V and T.
No-goods can be effectively used by forward checking or by backjumping. Constraint
learning is one of the most important techniques used by modern CSP solvers to achieve
efﬁciency on complex problems.
5.4 Local Search for CSPs
Local search algorithms (see Section 4.1) turn out to be very effective in solving many CSPs.
They use a complete-state formulation (as introduced in Section 4.1.1) where each state as-
signs a value to every variable, and the search changes the value of one variable at a time. As
an example, we’ll use the 8-queens problem, as deﬁned as a CSP on page 167. In Figure 5.8
we start on the left with a complete assignment to the 8 variables; typically this will violate
several constraints. We then randomly choose a conﬂicted variable, which turns out to be Q8,
the rightmost column. We’d like to change the value to something that brings us closer to a
solution; the most obvious approach is to select the value that results in the minimum number
of conﬂicts with other variables—the min-conﬂicts heuristic.
Min-conﬂicts
In the ﬁgure we see there are two rows that only violate one constraint; we pick Q8 =3
(that is, we move the queen to the 8th column, 3rd row). On the next iteration, in the middle
board of the ﬁgure, we select Q6 as the variable to change, and note that moving the queen to
the 8th row results in no conﬂicts. At this point there are no more conﬂicted variables, so we
have a solution. The algorithm is shown in Figure 5.9.2
Min-conﬂicts is surprisingly effective for many CSPs. Amazingly, on the n-queens prob-
lem, if you don’t count the initial placement of queens, the run time of min-conﬂicts is roughly
independent of problem size. It solves even the million-queens problem in an average of 50
steps (after the initial assignment). This remarkable observation was the stimulus leading to a
great deal of research in the 1990s on local search and the distinction between easy and hard
problems, which we take up in Section 7.6.3. Roughly speaking, n-queens is easy for local
search because solutions are densely distributed throughout the state space. Min-conﬂicts
also works well for hard problems. For example, it has been used to schedule observations
for the Hubble Space Telescope, reducing the time taken to schedule a week of observations
from three weeks (!) to around 10 minutes.
All the local search techniques from Section 4.1 are candidates for application to CSPs,
and some of those have proved especially effective. The landscape of a CSP under the min-
conﬂicts heuristic usually has a series of plateaus. There may be millions of variable as-
signments that are only one conﬂict away from a solution. Plateau search—allowing side-
ways moves to another state with the same score—can help local search ﬁnd its way off this
2
Local search can easily be extended to constrained optimization problems (COPs). In that case, all the tech-
niques for hill climbing and simulated annealing can be applied to optimize the objective function.
