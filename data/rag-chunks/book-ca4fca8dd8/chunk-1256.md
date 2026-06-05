---
chunk_id: "book-ca4fca8dd8-chunk-1256"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1256
confidence: "first-pass"
extraction_method: "structured-local"
---

760
Chapter 20
Knowledge in Learning
Grandparent(⟨Mum,Charles⟩)...
Then we get stuck in trying to represent the example descriptions. The only possible attributes
are horrible things such as
FirstElementIsMotherOfElizabeth(⟨Mum,Charles⟩) .
The deﬁnition of Grandparent in terms of these attributes simply becomes a large disjunction
of speciﬁc cases that does not generalize to new examples at all. Attribute-based learning
▶
algorithms are incapable of learning relational predicates. Thus, one of the principal advan-
tages of ILP algorithms is their applicability to a much wider range of problems, including
relational problems.
The reader will certainly have noticed that a little bit of background knowledge would
help in the representation of the Grandparent deﬁnition. For example, if Background included
the sentence
Parent(x,y) ⇔[Mother(x,y)∨Father(x,y)] ,
then the deﬁnition of Grandparent would be reduced to
Grandparent(x,y) ⇔[∃z Parent(x,z)∧Parent(z,y)] .
This shows how background knowledge can dramatically reduce the size of hypotheses re-
quired to explain the observations.
It is also possible for ILP algorithms to create new predicates in order to facilitate the
expression of explanatory hypotheses. Given the example data shown earlier, it is entirely
reasonable for the ILP program to propose an additional predicate, which we would call
“Parent,” in order to simplify the deﬁnitions of the target predicates. Algorithms that can
generate new predicates are called constructive induction algorithms. Clearly, constructive
Constructive
induction
induction is a necessary part of the picture of cumulative learning. It has been one of the
hardest problems in machine learning, but some ILP techniques provide effective mechanisms
for achieving it.
In the rest of this chapter, we will study the two principal approaches to ILP. The ﬁrst uses
a generalization of decision tree methods, and the second uses techniques based on inverting
a resolution proof.
Beatrice
Andrew
Eugenie
William Harry
Charles
Diana
Mum
George
Philip
Elizabeth
Margaret
Kydd
Spencer
Peter
Mark
Zara
Anne
Sarah
Edward
Sophie
Louise
James
Figure 20.11 A typical family tree.

## Page 761
