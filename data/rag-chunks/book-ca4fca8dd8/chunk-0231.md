---
chunk_id: "book-ca4fca8dd8-chunk-0231"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 231
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 4.2
Local Search in Continuous Spaces
139
closest to each airport in the current state. This means we can compute the gradient locally
(but not globally); for example,
∂f
∂x1
= 2 ∑
c∈C1
(x1 −xc).
(4.2)
Given a locally correct expression for the gradient, we can perform steepest-ascent hill climb-
ing by updating the current state according to the formula
x ←x+α∇f(x),
where α (alpha) is a small constant often called the step size. There exist a huge variety
Step size
of methods for adjusting α. The basic problem is that if α is too small, too many steps are
needed; if α is too large, the search could overshoot the maximum. The technique of line
search tries to overcome this dilemma by extending the current gradient direction—usually
Line search
by repeatedly doubling α—until f starts to decrease again. The point at which this occurs
becomes the new current state. There are several schools of thought about how the new
direction should be chosen at this point.
For many problems, the most effective algorithm is the venerable Newton–Raphson
Newton–Raphson
method. This is a general technique for ﬁnding roots of functions—that is, solving equations
of the form g(x)=0. It works by computing a new estimate for the root x according to
Newton’s formula
x ←x−g(x)/g′(x).
To ﬁnd a maximum or minimum of f, we need to ﬁnd x such that the gradient is a zero vector
(i.e., ∇f(x)=0). Thus, g(x) in Newton’s formula becomes ∇f(x), and the update equation
can be written in matrix–vector form as
x ←x−H−1
f (x)∇f(x),
where Hf (x) is the Hessian matrix of second derivatives, whose elements Hi j are given by
Hessian
∂2 f/∂xi∂xj. For our airport example, we can see from Equation (4.2) that H f (x) is particu-
larly simple: the off-diagonal elements are zero and the diagonal elements for airport i are just
twice the number of cities in Ci. A moment’s calculation shows that one step of the update
moves airport i directly to the centroid of Ci, which is the minimum of the local expression
for f from Equation (4.1).3 For high-dimensional problems, however, computing the n2 en-
tries of the Hessian and inverting it may be expensive, so many approximate versions of the
Newton–Raphson method have been developed.
Local search methods suffer from local maxima, ridges, and plateaus in continuous state
spaces just as much as in discrete spaces. Random restarts and simulated annealing are often
helpful. High-dimensional continuous spaces are, however, big places in which it is very easy
to get lost.
A ﬁnal topic is constrained optimization. An optimization problem is constrained if
Constrained
optimization
solutions must satisfy some hard constraints on the values of the variables. For example, in
our airport-siting problem, we might constrain sites to be inside Romania and on dry land
(rather than in the middle of lakes). The difﬁculty of constrained optimization problems
depends on the nature of the constraints and the objective function. The best-known category
is that of linear programming problems, in which constraints must be linear inequalities
Linear programming
3
In general, the Newton–Raphson update can be seen as ﬁtting a quadratic surface to f at x and then moving
directly to the minimum of that surface—which is also the minimum of f if f is quadratic.
