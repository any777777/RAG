---
chunk_id: "book-ca4fca8dd8-chunk-1576"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1576
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 957

Section 26.5
Planning and Control
957
Figure 26.20 Trajectory optimization for motion planning. Two point-obstacles with circu-
lar bands of decreasing cost around them. The optimizer starts with the straight line trajectory,
and lets the obstacles bend the line away from collisions, ﬁnding the minimum path through
the cost ﬁeld.
for Jeff only. We see that F does not have a direct dependence on τ(s), so the ﬁrst term in the
formula is 0. We are left with
∇τJ(s) = 0−d
dt ˙τ(s)
since the partial of F with respect to ˙τ(s) is ˙τ(s).
Notice how we made things easier for ourselves when deﬁning Jeff —it’s a nice quadratic
of the derivative (and we even put a 1
2 in front so that the 2 nicely cancels out). In practice,
you will see this trick happen a lot for optimization—the art is not just in choosing how to
optimize the cost function, but also in choosing a cost function that will play nicely with how
you will optimize it. Simplifying our gradient, we get
∇τJ(s) = −¨τ(s).
Now, since Jeff is a quadratic, setting this gradient to 0 gives us the solution for τ if we
didn’t have to deal with obstacles. Integrating once, we get that the ﬁrst derivative needs
to be constant; integrating again we get that τ(s) = a · s + b, with a and b determined by
the endpoint constraints for τ(0) and τ(1). The optimal path with respect to Jeff is thus the
straight line from start to goal! It is indeed the most efﬁcient way to go from one to the other
if there are no obstacles to worry about.
Of course, the addition of Jobs is what makes things difﬁcult—and we will spare you
deriving its gradient here. The robot would typically initialize its path to be a straight line,
which would plow right through some obstacles. It would then calculate the gradient of the
cost about the current path, and the gradient would serve to push the path away from the
obstacles (Figure 26.20). Keep in mind that gradient descent will only ﬁnd a locally optimal
solution—just like hill climbing. Methods such as simulated annealing (Section 4.1.2) can be
used for exploration, to make it more likely that the local optimum is a good one.
26.5.3 Trajectory tracking control
We have covered how to plan motions, but not how to actually move—to apply current to
motors, to produce torque, to move the robot. This is the realm of control theory, a ﬁeld
Control theory
of increasing importance in AI. There are two main questions to deal with: how do we turn

## Page 958
