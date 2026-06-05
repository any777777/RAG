---
chunk_id: "book-ca4fca8dd8-chunk-0571"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 571
confidence: "first-pass"
extraction_method: "structured-local"
---

346
Chapter 10
Knowledge Representation
Now that we have a modal operator for knowledge, we can write axioms for it. First,
we can say that agents are able to draw conclusions; if an agent knows P and knows that P
implies Q, then the agent knows Q:
(KaP∧Ka(P ⇒Q)) ⇒KaQ.
From this (and a few other rules about logical identities) we can establish that KA(P∨¬P) is
a tautology; every agent knows every proposition P is either true or false. On the other hand,
(KAP)∨(KA¬P) is not a tautology; in general, there will be lots of propositions that an agent
does not know to be true and does not know to be false.
It is said (going back to Plato) that knowledge is justiﬁed true belief. That is, if it is true,
if you believe it, and if you have an unassailably good reason, then you know it. That means
that if you know something, it must be true, and we have the axiom:
KaP ⇒P.
Furthermore, logical agents (but not all people) are able to introspect on their own knowledge.
If they know something, then they know that they know it:
KaP ⇒Ka(KaP).
We can deﬁne similar axioms for belief (often denoted by B) and other modalities. However,
one problem with the modal logic approach is that it assumes logical omniscience on the part
Logical omniscience
of agents. That is, if an agent knows a set of axioms, then it knows all consequences of those
axioms. This is on shaky ground even for the somewhat abstract notion of knowledge, but it
seems even worse for belief, because belief has more connotation of referring to things that
are physically represented in the agent, not just potentially derivable.
There have been attempts to deﬁne a form of limited rationality for agents—to say that
agents believe only those assertions that can be derived with the application of no more than
k reasoning steps, or no more than s seconds of computation. These attempts have been
generally unsatisfactory.
10.4.1 Other modal logics
Many modal logics have been proposed, for different modalities besides knowledge. One
proposal is to add modal operators for possibility and necessity: it is possibly true that one of
the authors of this book is sitting down right now, and it is necessarily true that 2+2 = 4.
As mentioned in Section 8.1.2, some logicians favor modalities related to time. In linear
temporal logic, we add the following modal operators:
Linear temporal logic
• X P: “P will be true in the next time step”
• F P: “P will eventually (Finally) be true in some future time step”
• G P: “P is always (Globally) true”
• P U Q: “P remains true until Q occurs”
Sometimes there are additional operators that can be derived from these. Adding these modal
operators makes the logic itself more complex (and thus makes it harder for a logical inference
algorithm to ﬁnd a proof). But the operators also allow us to state certain facts in a more
succinct form (which makes logical inference faster). The choice of which logic to use is
similar to the choice of which programming language to use: pick one that is appropriate to
your task, that is familiar to you and the others who will share your work, and that is efﬁcient
enough for your purposes.
