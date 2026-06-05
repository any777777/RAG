---
chunk_id: "book-ca4fca8dd8-chunk-0229"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 229
confidence: "first-pass"
extraction_method: "structured-local"
---

138
Chapter 4
Search in Complex Environments
in the 17th century, after the development of calculus by Newton and Leibniz.2 We ﬁnd uses
for these techniques in several places in this book, including the chapters on learning, vision,
and robotics.
We begin with an example. Suppose we want to place three new airports anywhere in
Romania, such that the sum of squared straight-line distances from each city on the map
to its nearest airport is minimized. (See Figure 3.1 for the map of Romania.) The state
space is then deﬁned by the coordinates of the three airports: (x1,y1), (x2,y2), and (x3,y3).
This is a six-dimensional space; we also say that states are deﬁned by six variables. In
Variable
general, states are deﬁned by an n-dimensional vector of variables, x. Moving around in this
space corresponds to moving one or more of the airports on the map. The objective function
f(x) = f(x1,y1,x2,y2,x3,y3) is relatively easy to compute for any particular state once we
compute the closest cities. Let Ci be the set of cities whose closest airport (in the state x) is
airport i. Then, we have
f(x) = f(x1,y1,x2,y2,x3,y3) =
3
∑
i=1 ∑
c∈Ci
(xi −xc)2 +(yi −yc)2 .
(4.1)
This equation is correct not only for the state x but also for states in the local neighborhood
of x. However, it is not correct globally; if we stray too far from x (by altering the location
of one or more of the airports by a large amount) then the set of closest cities for that airport
changes, and we need to recompute Ci.
One way to deal with a continuous state space is to discretize it. For example, instead of
Discretization
allowing the (xi,yi) locations to be any point in continuous two-dimensional space, we could
limit them to ﬁxed points on a rectangular grid with spacing of size δ (delta). Then instead of
having an inﬁnite number of successors, each state in the space would have only 12 succes-
sors, corresponding to incrementing one of the 6 variables by ±δ. We can then apply any of
our local search algorithms to this discrete space. Alternatively, we could make the branching
factor ﬁnite by sampling successor states randomly, moving in a random direction by a small
amount, δ. Methods that measure progress by the change in the value of the objective func-
tion between two nearby points are called empirical gradient methods. Empirical gradient
Empirical gradient
search is the same as steepest-ascent hill climbing in a discretized version of the state space.
Reducing the value of δ over time can give a more accurate solution, but does not necessarily
converge to a global optimum in the limit.
Often we have an objective function expressed in a mathematical form such that we can
use calculus to solve the problem analytically rather than empirically. Many methods attempt
to use the gradient of the landscape to ﬁnd a maximum. The gradient of the objective function
Gradient
is a vector ∇f that gives the magnitude and direction of the steepest slope. For our problem,
we have
∇f =
 ∂f
∂x1
, ∂f
∂y1
, ∂f
∂x2
, ∂f
∂y2
, ∂f
∂x3
, ∂f
∂y3

.
In some cases, we can ﬁnd a maximum by solving the equation ∇f =0. (This could be done,
for example, if we were placing just one airport; the solution is the arithmetic mean of all the
cities’ coordinates.) In many cases, however, this equation cannot be solved in closed form.
For example, with three airports, the expression for the gradient depends on what cities are
2
Knowledge of vectors, matrices, and derivatives is useful for this section (see Appendix A).
