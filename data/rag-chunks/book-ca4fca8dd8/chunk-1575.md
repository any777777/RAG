---
chunk_id: "book-ca4fca8dd8-chunk-1575"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1575
confidence: "first-pass"
extraction_method: "structured-local"
---

956
Chapter 26
Robotics
function1 over paths. That is, we want to minimize the cost function J(τ), where τ(0) = qs
and τ(1) = qg.
J is called a functional because it is a function over functions. The argument to J is
τ, which is itself a function: τ(t) takes as input a point in the [0,1] interval and maps it to
a conﬁguration. A standard cost functional trades off between two important aspects of the
robot’s motion: collision avoidance and efﬁciency,
J = Jobs +λJeff
where the efﬁciency Jeff measures the length of the path and may also measure smoothness. A
convenient way to deﬁne efﬁciency is with a quadratic: it integrates the squared ﬁrst derivative
of τ (we will see in a bit why this does in fact incentivize short paths):
Jeff =
Z 1
0
1
2∥˙τ(s)∥2ds.
For the obstacle term, assume we can compute the distance d(x) from any point x ∈W to
the nearest obstacle edge. This distance is positive outside of obstacles, 0 at the edge, and
negative inside. This is called a signed distance ﬁeld. We can now deﬁne a cost ﬁeld in the
Signed distance ﬁeld
workspace, call it c, that has high cost inside of obstacles, and a small cost right outside. With
this cost, we can make points in the workspace really hate being inside obstacles, and dislike
being right next to them (avoiding the visibility graph problem of their always hanging out
by the edges of obstacles). Of course, our robot is not a point in the workspace, so we have
some more work to do—we need to consider all points b on the robot’s body:
Jobs =
Z 1
0
Z
b c(φb(τ(s))
|
{z
}
∈W
)∥d
ds φb(τ(s))
|
{z
}
∈W
∥db ds.
This is called a path integral—it does not just integrate c along the way for each body point,
Path integral
but it multiplies by the derivative to make the cost invariant to retiming of the path. Imagine a
robot sweeping through the cost ﬁeld, accumulating cost as is moves. Regardless of how fast
or slow the arm moves through the ﬁeld, it must accumulate the exact same cost.
The simplest way to solve the optimization problem above and ﬁnd a path is gradient
descent. If you are wondering how to take gradients of functionals with respect to functions,
something called the calculus of variations is here to help. It is especially easy for functionals
of the form
J[τ] =
Z 1
0 F(s,τ(s), ˙τ(s))ds
which are integrals of functions that depend just on the parameter s, the value of the function
at s, and the derivative of the function at s. In such a case, the Euler-Lagrange equation
Euler-Lagrange
equation
says that the gradient is
∇τJ(s) =
∂F
∂τ(s)(s)−d
dt
∂F
∂˙τ(s)(s).
If we look closely at Jeff and Jobs, they both follow this pattern. In particular for Jeff , we have
F(s,τ(s), ˙τ(s)) = ∥˙τ(s)∥2. To get a bit more comfortable with this, let’s compute the gradient
1
Roboticists like to minimize a cost function J, whereas in other parts of AI we try to maximize a utility function
U or a reward R.
