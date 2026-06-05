---
chunk_id: "book-ca4fca8dd8-chunk-1568"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1568
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 26.5
Planning and Control
949
conf-3
conf-1
conf-2
conf-3
conf-2
conf-1
e
s
w
w
table
table
vertical
obstacle
left wall
(a)
(b)
Figure 26.13 Three robot conﬁgurations, shown in workspace and conﬁguration space.
26.5.2 Motion planning
The motion planning problem is that of ﬁnding a plan that takes a robot from one conﬁgura-
Motion planning
tion to another without colliding with an obstacle. It is a basic building block for movement
and manipulation. In Section 26.5.4 we will discuss how to do this under complicated dy-
namics, like steering a car that may drift off the path if you take a curve too fast. For now, we
will focus on the simple motion planning problem of ﬁnding a geometric path that is collision
free. Motion planning is a quintessentially continuous-state search problem, but it is often
possible to discretize the space and apply the search algorithms from Chapter 3.
The motion planning problem is sometimes referred to as the piano mover’s problem. It
Piano mover’s
problem
gets its name from a mover’s struggles with getting a large, irregular-shaped piano from one
room to another without hitting anything. We are given:
• a workspace world W in either R2 for the plane or R3 for three dimensions,
• an obstacle region O ⊂W,
• a robot with a conﬁguration space C and set of points A(q) for q ∈C,
• a starting conﬁguration qs ∈C, and
• a goal conﬁguration qg ∈C.
The obstacle region induces a C-space obstacle Cobs and its corresponding free space Cfree
deﬁned as in the previous section. We need to ﬁnd a continuous path through free space. We
will use a parameterized curve, τ(t), to represent the path, where τ(0) = qs and τ(1) = qg
and τ(t) for every t between 0 and 1 is some point in Cfree. That is, t parameterizes how
far we are along the path, from start to goal. Note that t acts somewhat like time in that as
t increases the distance along the path increases, but t is always a point on the interval [0,1]
and is not measured in seconds.

## Page 950
