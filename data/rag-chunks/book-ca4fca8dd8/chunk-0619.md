---
chunk_id: "book-ca4fca8dd8-chunk-0619"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 619
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 11.4
Hierarchical Planning
375
these actions, in turn, can be decomposed further, until we reach the low-level motor control
actions like a button-press.
In this example, planning and acting are interleaved; for example, one would defer the
problem of planning the walk from the curb to the gate until after being dropped off. Thus,
that particular action will remain at an abstract level prior to the execution phase. We defer
discussion of this topic until Section 11.5. Here, we concentrate on the idea of hierarchi-
cal decomposition, an idea that pervades almost all attempts to manage complexity. For
Hierarchical
decomposition
example, complex software is created from a hierarchy of subroutines and classes; armies,
governments and corporations have organizational hierarchies. The key beneﬁt of hierarchi-
cal structure is that at each level of the hierarchy, a computational task, military mission, or
administrative function is reduced to a small number of activities at the next lower level, so
the computational cost of ﬁnding the correct way to arrange those activities for the current
problem is small.
11.4.1 High-level actions
The basic formalism we adopt to understand hierarchical decomposition comes from the area
of hierarchical task networks or HTN planning. For now we assume full observability and
Hierarchical task
network
determinism and a set of actions, now called primitive actions, with standard precondition–
Primitive action
effect schemas. The key additional concept is the high-level action or HLA—for example,
High-level action
the action “Go to San Francisco airport.” Each HLA has one or more possible reﬁnements,
Reﬁnement
into a sequence of actions, each of which may be an HLA or a primitive action. For example,
the action “Go to San Francisco airport,” represented formally as Go(Home,SFO), might
have two possible reﬁnements, as shown in Figure 11.7. The same ﬁgure shows a recursive
reﬁnement for navigation in the vacuum world: to get to a destination, take a step, and then
go to the destination.
These examples show that high-level actions and their reﬁnements embody knowledge
about how to do things. For instance, the reﬁnements for Go(Home,SFO) say that to get to
the airport you can drive or take a ride-hailing service; buying milk, sitting down, and moving
the knight to e4 are not to be considered.
An HLA reﬁnement that contains only primitive actions is called an implementation
Implementation
of the HLA. In a grid world, the sequences [Right,Right,Down] and [Down,Right,Right]
both implement the HLA Navigate([1,3],[3,2]). An implementation of a high-level plan (a
sequence of HLAs) is the concatenation of implementations of each HLA in the sequence.
Given the precondition–effect deﬁnitions of each primitive action, it is straightforward to
determine whether any given implementation of a high-level plan achieves the goal.
We can say, then, that a high-level plan achieves the goal from a given state if at least ◀
one of its implementations achieves the goal from that state.
The “at least one” in this
deﬁnition is crucial—not all implementations need to achieve the goal, because the agent gets
to decide which implementation it will execute. Thus, the set of possible implementations in
HTN planning—each of which may have a different outcome—is not the same as the set of
possible outcomes in nondeterministic planning. There, we required that a plan work for all
outcomes because the agent doesn’t get to choose the outcome; nature does.
The simplest case is an HLA that has exactly one implementation. In that case, we can
compute the preconditions and effects of the HLA from those of the implementation (see
Exercise 11.HLAU) and then treat the HLA exactly as if it were a primitive action itself. It
