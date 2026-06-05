---
chunk_id: "book-ca4fca8dd8-chunk-1623"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1623
confidence: "first-pass"
extraction_method: "structured-local"
---

Bibliographical and Historical Notes
985
visibility graphs (Wesley and Lozano-Perez, 1979). Guibas et al. (1992) developed efﬁcient
Visibility graph
techniques for calculating Voronoi diagrams incrementally, and Choset (1996) generalized
Voronoi diagrams to broader motion planning problems.
John Canny (1988) established the ﬁrst singly exponential algorithm for motion planning.
The seminal text by Latombe (1991) covers a variety of approaches to motion planning, as
do the texts by Choset et al. (2005) and LaValle (2006). Kavraki et al. (1996) developed the
theory of probabilistic roadmaps. Kuffner and LaValle (2000) developed rapidly exploring
random trees (RRTs).
Involving optimization in geometric motion planning began with elastic bands (Quinlan
and Khatib, 1993), which reﬁne paths when the conﬁguration-space obstacles change. Ratliff
et al. (2009) formulated the idea as the solution to an optimal control problem, allowing
the initial trajectory to start in collision, and deforming it by mapping workspace obstacle
gradients via the Jacobian into the conﬁguration space. Schulman et al. (2013) proposed a
practical second-order alternative.
The control of robots as dynamical systems—whether for manipulation or navigation—
has generated a vast literature. While this chapter explained the basics of trajectory tracking
control and optimal control, it left out entire subﬁelds, including adaptive control, robust
control, and Lyapunov analysis. Rather than assuming everything about the system is known
a priori, adaptive control aims to adapt the dynamics parameters and/or the control law online.
Robust control, on the other hand, aims to design controllers that perform well in spite of
uncertainty and external disturbances.
Lyapunov analysis was originally developed in the 1890s for the stability analysis of
general nonlinear systems, but it was not until the early 1930s that control theorists realized
its true potential. With the development of optimization methods, Lyapunov analysis was
extended to control barrier functions, which lend themselves nicely to modern optimization
tools. These methods are widely used in modern robotics for real-time controller design and
safety analysis.
Crucial works in robotic control include a trilogy on impedance control by Hogan (1985)
and a general study of robot dynamics by Featherstone (1987). Dean and Wellman (1991)
were among the ﬁrst to try to tie together control theory and AI planning systems. Three clas-
sic textbooks on the mathematics of robot manipulation are due to Paul (1981), Craig (1989),
and Yoshikawa (1990). Control for manipulation is covered by Murray (2017).
The area of grasping is also important in robotics—the problem of determining a stable
grasp is quite difﬁcult (Mason and Salisbury, 1985). Competent grasping requires touch sens-
ing, or haptic feedback, to determine contact forces and detect slip (Fearing and Hollerbach,
Haptic feedback
1985). Understanding how to grasp the the wide variety of objects in the world is a daunting
task. (Bousmalis et al., 2017) describe a system that combines real-world experimentation
with simulations guided by sim-to-real transfer to produce robust grasping.
Potential-ﬁeld control, which attempts to solve the motion planning and control problems
simultaneously, was developed for robotics by Khatib (1986). In mobile robotics, this idea
was viewed as a practical solution to the collision avoidance problem, and was later extended
into an algorithm called vector ﬁeld histograms by Borenstein (1991).
Vector ﬁeld
histogram
ILQR is currently widely used at the intersection of motion planning and control and is
due to Li and Todorov (2004). It is a variant of the much older differential dynamic program-
ming technique (Jacobson and Mayne, 1970).
