---
chunk_id: "book-ca4fca8dd8-chunk-0627"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 627
confidence: "first-pass"
extraction_method: "structured-local"
---

380
Chapter 11
Automated Planning
of an HLA—the reachable set for each possible initial state—are represented. A primitive
action can set a ﬂuent to true or false or leave it unchanged. (With conditional effects (see
Section 11.5.1) there is a fourth possibility: ﬂipping a variable to its opposite.)
An HLA under angelic semantics can do more: it can control the value of a ﬂuent, setting
it to true or false depending on which implementation is chosen. That means that an HLA can
have nine different effects on a ﬂuent: if the variable starts out true, it can always keep it true,
always make it false, or have a choice; if the ﬂuent starts out false, it can always keep it false,
always make it true, or have a choice; and the three choices for both cases can be combined
arbitrarily, making nine.
Notationally, this is a bit challenging. We’ll use the language of add lists and delete
lists (rather than true/false ﬂuents) along with the e symbol to mean “possibly, if the agent
so chooses.” Thus, the effect e+A means “possibly add A,” that is, either leave A unchanged
or make it true. Similarly, e−A means “possibly delete A” and e±A means “possibly add
or delete A.” For example, the HLA Go(Home,SFO), with the two reﬁnements shown in
Figure 11.7, possibly deletes Cash (if the agent decides to take a taxi), so it should have the
effect e−Cash. Thus, we see that the descriptions of HLAs are derivable from the descriptions
of their reﬁnements. Now, suppose we have the following schemas for the HLAs h1 and h2:
Action(h1,PRECOND:¬A,EFFECT:A∧e−B),
Action(h2,PRECOND:¬B,EFFECT:e+A∧e±C).
That is, h1 adds A and possibly deletes B, while h2 possibly adds A and has full control over
C. Now, if only B is true in the initial state and the goal is A ∧C then the sequence [h1,h2]
achieves the goal: we choose an implementation of h1 that makes B false, then choose an
implementation of h2 that leaves A true and makes C true.
The preceding discussion assumes that the effects of an HLA—the reachable set for any
given initial state—can be described exactly by describing the effect on each ﬂuent. It would
be nice if this were always true, but in many cases we can only approximate the effects be-
cause an HLA may have inﬁnitely many implementations and may produce arbitrarily wig-
gly reachable sets—rather like the wiggly-belief-state problem illustrated in Figure 7.21 on
page 261. For example, we said that Go(Home,SFO) possibly deletes Cash; it also possibly
adds At(Car,SFOLongTermParking); but it cannot do both—in fact, it must do exactly one.
As with belief states, we may need to write approximate descriptions. We will use two kinds
of approximation: an optimistic description REACH+(s,h) of an HLA h may overstate the
Optimistic
description
reachable set, while a pessimistic description REACH−(s,h) may understate the reachable
Pessimistic
description
set. Thus, we have
REACH−(s,h) ⊆REACH(s,h) ⊆REACH+(s,h).
For example, an optimistic description of Go(Home,SFO) says that it possibly deletes Cash
and possibly adds At(Car,SFOLongTermParking). Another good example arises in the 8-
puzzle, half of whose states are unreachable from any given state (see Exercise 11.PART):
the optimistic description of Act might well include the whole state space, since the exact
reachable set is quite wiggly.
With approximate descriptions, the test for whether a plan achieves the goal needs to
be modiﬁed slightly. If the optimistic reachable set for the plan doesn’t intersect the goal,
then the plan doesn’t work; if the pessimistic reachable set intersects the goal, then the plan
does work (Figure 11.10(a)). With exact descriptions, a plan either works or it doesn’t, but
