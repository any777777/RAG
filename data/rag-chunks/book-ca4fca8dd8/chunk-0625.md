---
chunk_id: "book-ca4fca8dd8-chunk-0625"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 625
confidence: "first-pass"
extraction_method: "structured-local"
---

378
Chapter 11
Automated Planning
The key to HTN planning is a plan library containing known methods for implementing
complex, high-level actions. One way to construct the library is to learn the methods from
problem-solving experience. After the excruciating experience of constructing a plan from
scratch, the agent can save the plan in the library as a method for implementing the high-level
action deﬁned by the task. In this way, the agent can become more and more competent over
time as new methods are built on top of old methods. One important aspect of this learning
process is the ability to generalize the methods that are constructed, eliminating detail that
is speciﬁc to the problem instance (e.g., the name of the builder or the address of the plot of
land) and keeping just the key elements of the plan. It seems to us inconceivable that humans
could be as competent as they are without some such mechanism.
11.4.3 Searching for abstract solutions
The hierarchical search algorithm in the preceding section reﬁnes HLAs all the way to primi-
tive action sequences to determine if a plan is workable. This contradicts common sense: one
should be able to determine that the two-HLA high-level plan
[Drive(Home,SFOLongTermParking),Shuttle(SFOLongTermParking,SFO)]
gets one to the airport without having to determine a precise route, choice of parking spot,
and so on. The solution is to write precondition–effect descriptions of the HLAs, just as we
do for primitive actions. From the descriptions, it ought to be easy to prove that the high-level
plan achieves the goal. This is the holy grail, so to speak, of hierarchical planning, because if
we derive a high-level plan that provably achieves the goal, working in a small search space
of high-level actions, then we can commit to that plan and work on the problem of reﬁning
each step of the plan. This gives us the exponential reduction we seek.
For this to work, it has to be the case that every high-level plan that “claims” to achieve
the goal (by virtue of the descriptions of its steps) does in fact achieve the goal in the sense
deﬁned earlier: it must have at least one implementation that does achieve the goal. This
property has been called the downward reﬁnement property for HLA descriptions.
Downward
reﬁnement property
Writing HLA descriptions that satisfy the downward reﬁnement property is, in principle,
easy: as long as the descriptions are true, then any high-level plan that claims to achieve
the goal must in fact do so—otherwise, the descriptions are making some false claim about
what the HLAs do. We have already seen how to write true descriptions for HLAs that have
exactly one implementation (Exercise 11.HLAU); a problem arises when the HLA has multiple
implementations. How can we describe the effects of an action that can be implemented in
many different ways?
One safe answer (at least for problems where all preconditions and goals are positive) is
to include only the positive effects that are achieved by every implementation of the HLA and
the negative effects of any implementation. Then the downward reﬁnement property would
be satisﬁed. Unfortunately, this semantics for HLAs is much too conservative.
Consider again the HLA Go(Home,SFO), which has two reﬁnements, and suppose, for
the sake of argument, a simple world in which one can always drive to the airport and park,
but taking a taxi requires Cash as a precondition. In that case, Go(Home,SFO) doesn’t al-
ways get you to the airport. In particular, it fails if Cash is false, and so we cannot assert
At(Agent,SFO) as an effect of the HLA. This makes no sense, however; if the agent didn’t
have Cash, it would drive itself. Requiring that an effect hold for every implementation is
equivalent to assuming that someone else—an adversary—will choose the implementation.
