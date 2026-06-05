---
chunk_id: "book-ca4fca8dd8-chunk-0464"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 464
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 8.3
Using First-Order Logic
283
. . .
R
J
J
R
R
J
R
J
R
J
R
J
R
J
R
J
R
J
R
J
Figure 8.5 Some members of the set of all models for a language with two constant symbols,
R and J, and one binary relation symbol, under database semantics. The interpretation of the
constant symbols is ﬁxed, and there is a distinct object for each constant symbol.
Under the resulting semantics, Equation (8.3) does indeed state that Richard has exactly
two brothers, John and Geoffrey. We call this database semantics to distinguish it from the
Database semantics
standard semantics of ﬁrst-order logic. Database semantics is also used in logic programming
systems, as explained in Section 9.4.4.
It is instructive to consider the set of all possible models under database semantics for the
same case as shown in Figure 8.4 (page 277). Figure 8.5 shows some of the models, ranging
from the model with no tuples satisfying the relation to the model with all tuples satisfying
the relation. With two objects, there are four possible two-element tuples, so there are 24 =16
different subsets of tuples that can satisfy the relation. Thus, there are 16 possible models in
all—a lot fewer than the inﬁnitely many models for the standard ﬁrst-order semantics. On the
other hand, the database semantics requires deﬁnite knowledge of what the world contains.
This example brings up an important point: there is no one “correct” semantics for logic.
The usefulness of any proposed semantics depends on how concise and intuitive it makes the
expression of the kinds of knowledge we want to write down, and on how easy and natural
it is to develop the corresponding rules of inference. Database semantics is most useful
when we are certain about the identity of all the objects described in the knowledge base and
when we have all the facts at hand; in other cases, it is quite awkward. For the rest of this
chapter, we assume the standard semantics while noting instances in which this choice leads
to cumbersome expressions.
8.3 Using First-Order Logic
Now that we have deﬁned an expressive logical language, let’s learn how to use it. In this sec-
tion, we provide example sentences in some simple domains. In knowledge representation,
Domain
a domain is just some part of the world about which we wish to express some knowledge.
We begin with a brief description of the TELL/ASK interface for ﬁrst-order knowledge
bases. Then we look at the domains of family relationships, numbers, sets, and lists, and at
the wumpus world. Section 8.4.2 contains a more substantial example (electronic circuits)
and Chapter 10 covers everything in the universe.
8.3.1 Assertions and queries in ﬁrst-order logic
Sentences are added to a knowledge base using TELL, exactly as in propositional logic. Such
sentences are called assertions. For example, we can assert that John is a king, Richard is a
Assertion
