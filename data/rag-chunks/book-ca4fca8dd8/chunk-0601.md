---
chunk_id: "book-ca4fca8dd8-chunk-0601"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 601
confidence: "first-pass"
extraction_method: "structured-local"
---

364
Chapter 11
Automated Planning
Init(At(C1, SFO) ∧At(C2, JFK) ∧At(P1, SFO) ∧At(P2, JFK)
∧Cargo(C1) ∧Cargo(C2) ∧Plane(P1) ∧Plane(P2)
∧Airport(JFK) ∧Airport(SFO))
Goal(At(C1, JFK) ∧At(C2, SFO))
Action(Load(c, p, a),
PRECOND: At(c, a) ∧At(p, a) ∧Cargo(c) ∧Plane(p) ∧Airport(a)
EFFECT: ¬ At(c, a) ∧In(c, p))
Action(Unload(c, p, a),
PRECOND: In(c, p) ∧At(p, a) ∧Cargo(c) ∧Plane(p) ∧Airport(a)
EFFECT: At(c, a) ∧¬ In(c, p))
Action(Fly(p, from, to),
PRECOND: At(p, from) ∧Plane(p) ∧Airport(from) ∧Airport(to)
EFFECT: ¬ At(p, from) ∧At(p, to))
Figure 11.1 A PDDL description of an air cargo transportation planning problem.
must be taken to make sure the At predicates are maintained properly. When a plane ﬂies
from one airport to another, all the cargo inside the plane goes with it. In ﬁrst-order logic it
would be easy to quantify over all objects that are inside the plane. But PDDL does not have
a universal quantiﬁer, so we need a different solution. The approach we use is to say that a
piece of cargo ceases to be At anywhere when it is In a plane; the cargo only becomes At the
new airport when it is unloaded. So At really means “available for use at a given location.”
The following plan is a solution to the problem:
[Load(C1,P1,SFO),Fly(P1,SFO,JFK),Unload(C1,P1,JFK),
Load(C2,P2,JFK),Fly(P2,JFK,SFO),Unload(C2,P2,SFO)].
11.1.2 Example domain: The spare tire problem
Consider the problem of changing a ﬂat tire (Figure 11.2). The goal is to have a good spare
tire properly mounted onto the car’s axle, where the initial state has a ﬂat tire on the axle and
a good spare tire in the trunk. To keep it simple, our version of the problem is an abstract
one, with no sticky lug nuts or other complications. There are just four actions: removing
the spare from the trunk, removing the ﬂat tire from the axle, putting the spare on the axle,
and leaving the car unattended overnight. We assume that the car is parked in a particu-
larly bad neighborhood, so that the effect of leaving it overnight is that the tires disappear.
[Remove(Flat,Axle),Remove(Spare,Trunk),PutOn(Spare,Axle)] is a solution to the problem.
11.1.3 Example domain: The blocks world
One of the most famous planning domains is the blocks world. This domain consists of a set
of cube-shaped blocks sitting on an arbitrarily-large table.1 The blocks can be stacked, but
only one block can ﬁt directly on top of another. A robot arm can pick up a block and move it
to another position, either on the table or on top of another block. The arm can pick up only
one block at a time, so it cannot pick up a block that has another one on top of it. A typical
goal to get block A on B and block B on C (see Figure 11.3).
1
The blocks world commonly used in planning research is much simpler than SHRDLU’s version (page 38).
