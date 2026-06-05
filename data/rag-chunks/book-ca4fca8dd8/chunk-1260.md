---
chunk_id: "book-ca4fca8dd8-chunk-1260"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1260
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 764

764
Chapter 20
Knowledge in Learning
The early steps in an inverse resolution process are shown in Figure 20.13, where we
focus on the positive example Grandparent(George,Anne). The process begins at the end
of the proof (shown at the bottom of the ﬁgure).
We take the resolvent C to be empty
clause (i.e. a contradiction) and C2 to be ¬Grandparent(George,Anne), which is the nega-
tion of the goal example. The ﬁrst inverse step takes C and C2 and generates the clause
Grandparent(George,Anne) for C1. The next step takes this clause as C and the clause
Parent(Elizabeth,Anne) as C2, and generates the clause
¬Parent(Elizabeth,y)∨Grandparent(George,y)
as C1. The ﬁnal step treats this clause as the resolvent. With Parent(George,Elizabeth) as C2,
one possible clause C1 is the hypothesis
Parent(x,z)∧Parent(z,y) ⇒Grandparent(x,y) .
Now we have a resolution proof that the hypothesis, descriptions, and background knowledge
entail the classiﬁcation Grandparent(George,Anne).
Clearly, inverse resolution involves a search. Each inverse resolution step is nonde-
terministic, because for any C, there can be many or even an inﬁnite number of clauses
C1 and C2 that resolve to C.
For example, instead of choosing ¬Parent(Elizabeth,y) ∨
Grandparent(George,y) for C1 in the last step of Figure 20.13, the inverse resolution step
might have chosen any of the following sentences:
¬Parent(Elizabeth,Anne)∨Grandparent(George,Anne) .
¬Parent(z,Anne)∨Grandparent(George,Anne) .
¬Parent(z,y)∨Grandparent(George,y) .
...
(See Exercises 20.4 and 20.5.) Furthermore, the clauses that participate in each step can be
chosen from the Background knowledge, from the example Descriptions, from the negated
Classiﬁcations, or from hypothesized clauses that have already been generated in the inverse
resolution tree. The large number of possibilities means a large branching factor (and therefore
{y/Anne}
Parent(Elizabeth,Anne)
Grandparent(George,Anne)
Grandparent(George,Anne)
Grandparent(George,y)
Parent(Elizabeth,y)
>
{x/George, z/Elizabeth}
Parent(George,Elizabeth)
>
Parent(z,y)
Grandparent(x,y)
>
Parent(x,z)
¬
¬
¬
¬
Figure 20.13 Early steps in an inverse resolution process. The shaded clauses are generated
by inverse resolution steps from the clause to the right and the clause below. The unshaded
clauses are from the Descriptions and Classiﬁcations (including negated Classiﬁcations).

## Page 765
