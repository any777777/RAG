---
chunk_id: "book-ca4fca8dd8-chunk-0297"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 297
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 182

182
Chapter 5
Constraint Satisfaction Problems
2
2
1
2
3
1
2
3
3
2
3
2
3
0
Figure 5.8 A two-step solution using min-conﬂicts for an 8-queens problem. At each stage,
a queen is chosen for reassignment in its column. The number of conﬂicts (in this case, the
number of attacking queens) is shown in each square. The algorithm moves the queen to the
min-conﬂicts square, breaking ties randomly.
function MIN-CONFLICTS(csp,max steps) returns a solution or failure
inputs: csp, a constraint satisfaction problem
max steps, the number of steps allowed before giving up
current←an initial complete assignment for csp
for i = 1 to max steps do
if current is a solution for csp then return current
var←a randomly chosen conﬂicted variable from csp.VARIABLES
value←the value v for var that minimizes CONFLICTS(csp,var,v,current)
set var=value in current
return failure
Figure 5.9 The MIN-CONFLICTS local search algorithm for CSPs. The initial state may be
chosen randomly or by a greedy assignment process that chooses a minimal-conﬂict value
for each variable in turn. The CONFLICTS function counts the number of constraints violated
by a particular value, given the rest of the current assignment.
plateau. This wandering on the plateau can be directed with a technique called tabu search:
keeping a small list of recently visited states and forbidding the algorithm to return to those
states. Simulated annealing can also be used to escape from plateaus.
Another technique called constraint weighting aims to concentrate the search on the
Constraint weighting
important constraints. Each constraint is given a numeric weight, initially all 1. At each step
of the search, the algorithm chooses a variable/value pair to change that will result in the
lowest total weight of all violated constraints. The weights are then adjusted by incrementing
the weight of each constraint that is violated by the current assignment. This has two beneﬁts:
it adds topography to plateaus, making sure that it is possible to improve from the current
state, and it also adds learning: over time the difﬁcult constraints are assigned higher weights.
Another advantage of local search is that it can be used in an online setting (see Sec-
tion 4.5) when the problem changes. Consider a scheduling problem for an airline’s weekly
ﬂights. The schedule may involve thousands of ﬂights and tens of thousands of personnel

## Page 183
