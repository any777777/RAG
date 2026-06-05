---
chunk_id: "book-ca4fca8dd8-chunk-1254"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1254
confidence: "first-pass"
extraction_method: "structured-local"
---

758
Chapter 20
Knowledge in Learning
20.5 Inductive Logic Programming
Inductive logic programming (ILP) combines inductive methods with the power of ﬁrst-order
representations, concentrating in particular on the representation of hypotheses as logic pro-
grams.3 It has gained popularity for three reasons. First, ILP offers a rigorous approach to
the general knowledge-based inductive learning problem. Second, it offers complete algo-
rithms for inducing general, ﬁrst-order theories from examples, which can therefore learn
successfully in domains where attribute-based algorithms are hard to apply. An example is
in learning how protein structures fold (Figure 20.10). The three-dimensional conﬁguration
of a protein molecule cannot be represented reasonably by a set of attributes, because the
conﬁguration inherently refers to relationships between objects, not to attributes of a single
object. First-order logic is an appropriate language for describing the relationships. Third,
inductive logic programming produces hypotheses that are (relatively) easy for humans to
read. For example, the English translation in Figure 20.10 can be scrutinized and criticized
by working biologists. This means that inductive logic programming systems can participate
in the scientiﬁc cycle of experimentation, hypothesis generation, debate, and refutation. Such
participation would not be possible for systems that generate “black-box” classiﬁers, such as
neural networks.
20.5.1 An example
Recall from Equation (20.5) that the general knowledge-based induction problem is to “solve”
the entailment constraint
Background ∧Hypothesis∧Descriptions |= Classiﬁcations
for the unknown Hypothesis, given the Background knowledge and examples described by
Descriptions and Classiﬁcations. To illustrate this, we will use the problem of learning fam-
ily relationships from examples. The descriptions will consist of an extended family tree,
described in terms of Mother, Father, and Married relations and Male and Female proper-
ties. As an example, we will use the family tree from Exercise 8.15, shown here in Figure
20.11. The corresponding descriptions are as follows:
Father(Philip,Charles)
Father(Philip,Anne)
...
Mother(Mum,Margaret) Mother(Mum,Elizabeth)
...
Married(Diana,Charles) Married(Elizabeth,Philip) ...
Male(Philip)
Male(Charles)
...
Female(Beatrice)
Female(Margaret)
...
The sentences in Classiﬁcations depend on the target concept being learned. We might want
to learn Grandparent, BrotherInLaw, or Ancestor, for example. For Grandparent, the com-
plete set of Classiﬁcations contains 20×20=400 conjuncts of the form
Grandparent(Mum,Charles) Grandparent(Elizabeth,Beatrice) ...
¬Grandparent(Mum,Harry) ¬Grandparent(Spencer,Peter)
...
We could of course learn from a subset of this complete set.
The object of an inductive learning program is to come up with a set of sentences for the
Hypothesis such that the entailment constraint is satisﬁed. Suppose, for the moment, that the
3
It might be appropriate at this point for the reader to refer to Chapter 7 for some of the underlying concepts,
including Horn clauses, conjunctive normal form, uniﬁcation, and resolution.
