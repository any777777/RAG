---
chunk_id: "book-ca4fca8dd8-chunk-1228"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1228
confidence: "first-pass"
extraction_method: "structured-local"
---

740
Chapter 20
Knowledge in Learning
We will use the notation Di(Xi) to refer to the description of Xi, where Di can be any logical
expression taking a single argument. The classiﬁcation of the example is given by a literal
using the goal predicate, in this case
WillWait(X1)
or
¬WillWait(X1) .
The complete training set can thus be expressed as the conjunction of all the example descrip-
tions and goal literals.
The aim of inductive learning in general is to ﬁnd a hypothesis that classiﬁes the examples
well and generalizes well to new examples. Here we are concerned with hypotheses expressed
in logic; each hypothesis hj will have the form
∀x Goal(x) ⇔Cj(x) ,
where Cj(x) is a candidate deﬁnition—some expression involving the attribute predicates.
For example, a decision tree can be interpreted as a logical expression of this form. Thus, the
tree in Figure 19.6 (page 678) expresses the following logical deﬁnition (which we will call
hr for future reference):
∀r WillWait(r) ⇔Patrons(r,Some)
∨Patrons(r,Full)∧Hungry(r)∧Type(r,French)
∨Patrons(r,Full)∧Hungry(r)∧Type(r,Thai)
∧Fri/Sat(r)
∨Patrons(r,Full)∧Hungry(r)∧Type(r,Burger) .
(20.1)
Each hypothesis predicts that a certain set of examples—namely, those that satisfy its candi-
date deﬁnition—will be examples of the goal predicate. This set is called the extension of
Extension
the predicate. Two hypotheses with different extensions are therefore logically inconsistent
with each other, because they disagree on their predictions for at least one example. If they
have the same extension, they are logically equivalent.
The hypothesis space H is the set of all hypotheses {h1,...,hn} that the learning algo-
rithm is designed to entertain. For example, the DECISION-TREE-LEARNING algorithm can
entertain any decision tree hypothesis deﬁned in terms of the attributes provided; its hypoth-
esis space therefore consists of all these decision trees. Presumably, the learning algorithm
believes that one of the hypotheses is correct; that is, it believes the sentence
h1 ∨h2 ∨h3 ∨...∨hn .
(20.2)
As the examples arrive, hypotheses that are not consistent with the examples can be ruled
out. Let us examine this notion of consistency more carefully. Obviously, if hypothesis hj is
consistent with the entire training set, it has to be consistent with each example in the training
set. What would it mean for it to be inconsistent with an example? There are two possible
ways that this can happen:
• An example can be a false negative for the hypothesis, if the hypothesis says it should
False negative
be negative but in fact it is positive. For instance, the new example X13 described by
Patrons(X13,Full)∧¬Hungry(X13)∧...∧WillWait(X13)
would be a false negative for the hypothesis hr given earlier. From hr and the example
description, we can deduce both WillWait(X13), which is what the example says, and
¬WillWait(X13), which is what the hypothesis predicts. The hypothesis and the example
are therefore logically inconsistent.
