---
chunk_id: "book-ca4fca8dd8-chunk-0637"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 637
confidence: "first-pass"
extraction_method: "structured-local"
---

386
Chapter 11
Automated Planning
2. If the action deletes ℓ, then ℓwill be false in b′ regardless of its initial value.
3. If the action does not affect ℓ, then ℓwill retain its initial value (which is unknown) and
will not appear in b′.
Hence, we see that the calculation of b′ is almost identical to the observable case, which was
speciﬁed by Equation (11.1) on page 363:
b′ = RESULT(b,a) = (b−DEL(a))∪ADD(a).
We cannot quite use the set semantics because (1) we must make sure that b′ does not con-
tain both ℓand ¬ℓ, and (2) atoms may contain unbound variables. But it is still the case
that RESULT(b,a) is computed by starting with b, setting any atom that appears in DEL(a)
to false, and setting any atom that appears in ADD(a) to true. For example, if we apply
RemoveLid(Can1) to the initial belief state b0, we get
b1 = Color(x,C(x))∧Open(Can1).
When we apply the action Paint(Chair,Can1), the precondition Color(Can1,c) is satisﬁed
by the literal Color(x,C(x)) with binding {x/Can1,c/C(Can1)} and the new belief state is
b2 = Color(x,C(x))∧Open(Can1)∧Color(Chair,C(Can1)).
Finally, we apply the action Paint(Table,Can1) to obtain
b3 = Color(x,C(x))∧Open(Can1)∧Color(Chair,C(Can1))
∧Color(Table,C(Can1)).
The ﬁnal belief state satisﬁes the goal, Color(Table,c)∧Color(Chair,c), with the variable c
bound to C(Can1).
The preceding analysis of the update rule has shown a very important fact: the family
▶
of belief states deﬁned as conjunctions of literals is closed under updates deﬁned by PDDL
action schemas. That is, if the belief state starts as a conjunction of literals, then any update
will yield a conjunction of literals. That means that in a world with n ﬂuents, any belief
state can be represented by a conjunction of size O(n). This is a very comforting result,
considering that there are 2n states in the world. It says we can compactly represent all the
subsets of those 2n states that we will ever need. Moreover, the process of checking for belief
states that are subsets or supersets of previously visited belief states is also easy, at least in
the propositional case.
The ﬂy in the ointment of this pleasant picture is that it only works for action schemas
that have the same effects for all states in which their preconditions are satisﬁed. It is this
property that enables the preservation of the 1-CNF belief-state representation. As soon as
the effect can depend on the state, dependencies are introduced between ﬂuents, and the 1-
CNF property is lost.
Consider, for example, the simple vacuum world deﬁned in Section 3.2.1. Let the ﬂuents
be AtL and AtR for the location of the robot and CleanL and CleanR for the state of the
squares. According to the deﬁnition of the problem, the Suck action has no precondition—it
can always be done. The difﬁculty is that its effect depends on the robot’s location: when the
robot is AtL, the result is CleanL, but when it is AtR, the result is CleanR. For such actions,
our action schemas will need something new: a conditional effect. These have the syntax
Conditional eﬀect
