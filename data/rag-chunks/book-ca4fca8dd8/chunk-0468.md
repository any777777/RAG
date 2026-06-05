---
chunk_id: "book-ca4fca8dd8-chunk-0468"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 468
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 8.3
Using First-Order Logic
285
A grandparent is a parent of one’s parent:
∀g,c Grandparent(g,c) ⇔∃p Parent(g, p)∧Parent(p,c).
A sibling is another child of one’s parent:
∀x,y Sibling(x,y) ⇔x ̸= y∧∃p Parent(p,x)∧Parent(p,y).
We could go on for several more pages like this, and Exercise 8.KINS asks you to do just that.
Each of these sentences can be viewed as an axiom of the kinship domain, as explained in
Section 7.1. Axioms are commonly associated with purely mathematical domains—we will
see some axioms for numbers shortly—but they are needed in all domains. They provide the
basic factual information from which useful conclusions can be derived. Our kinship axioms
are also deﬁnitions; they have the form ∀x,y P(x,y) ⇔.... The axioms deﬁne the Mother
Deﬁnition
function and the Husband, Male, Parent, Grandparent, and Sibling predicates in terms of
other predicates. Our deﬁnitions “bottom out” at a basic set of predicates (Child, Female,
etc.) in terms of which the others are ultimately deﬁned.
This is a natural way in which to build up the representation of a domain, and it is anal-
ogous to the way in which software packages are built up by successive deﬁnitions of sub-
routines from primitive library functions. Notice that there is not necessarily a unique set
of primitive predicates; we could equally well have used Parent instead of Child. In some
domains, as we show, there is no clearly identiﬁable basic set.
Not all logical sentences about a domain are axioms. Some are theorems—that is, they
Theorem
are entailed by the axioms. For example, consider the assertion that siblinghood is symmetric:
∀x,y Sibling(x,y) ⇔Sibling(y,x).
Is this an axiom or a theorem? In fact, it is a theorem that follows logically from the axiom
that deﬁnes siblinghood. If we ASK the knowledge base this sentence, it should return true.
From a purely logical point of view, a knowledge base need contain only axioms and
no theorems, because the theorems do not increase the set of conclusions that follow from
the knowledge base. From a practical point of view, theorems are essential to reduce the
computational cost of deriving new sentences. Without them, a reasoning system has to start
from ﬁrst principles every time, rather like a physicist having to rederive the rules of calculus
for every new problem.
Not all axioms are deﬁnitions. Some provide more general information about certain
predicates without constituting a deﬁnition. Indeed, some predicates have no complete deﬁ-
nition because we do not know enough to characterize them fully. For example, there is no
obvious deﬁnitive way to complete the sentence
∀x Person(x) ⇔...
Fortunately, ﬁrst-order logic allows us to make use of the Person predicate without completely
deﬁning it. Instead, we can write partial speciﬁcations of properties that every person has and
properties that make something a person:
∀x Person(x) ⇒...
∀x ... ⇒Person(x).
Axioms can also be “just plain facts,” such as Male(Jim) and Spouse(Jim,Laura). Such
facts form the descriptions of speciﬁc problem instances, enabling speciﬁc questions to be
