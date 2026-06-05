---
chunk_id: "book-ca4fca8dd8-chunk-1255"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1255
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 759

Section 20.5
Inductive Logic Programming
759
2mhr - Four-helical up-and-down bundle
H:1[19-37]
H:2[41-64]
H:3[71-84]
H:4[93-108]
H:5[111-113]
H:1[8-17]
H:2[26-33]
H:3[40-50]
H:4[61-64]
H:5[66-70]
H:6[79-88]
H:7[99-106]
E:1[57-59]
E:2[96-98]
1omd - EF-Hand
(a)
(b)
Figure 20.10 (a) and (b) show positive and negative examples, respectively, of the
“four-helical up-and-down bundle” concept in the domain of protein folding.
Each
example structure is coded into a logical expression of about 100 conjuncts such as
TotalLength(D2mhr,118) ∧NumberHelices(D2mhr,6) ∧.... From these descriptions and
from classiﬁcations such as Fold(FOUR-HELICAL-UP-AND-DOWN-BUNDLE,D2mhr), the
ILP system PROGOL (Muggleton, 1995) learned the following rule:
Fold(FOUR-HELICAL-UP-AND-DOWN-BUNDLE, p) ⇐
Helix(p,h1)∧Length(h1,HIGH)∧Position(p,h1,n)
∧(1 ≤n ≤3)∧Adjacent(p,h1,h2)∧Helix(p,h2) .
This kind of rule could not be learned, or even represented, by an attribute-based mechanism
such as we saw in previous chapters. The rule can be translated into English as “ Protein p
has fold class “Four-helical up-and-down-bundle” if it contains a long helix h1 at a secondary
structure position between 1 and 3 and h1 is next to a second helix.”
agent has no background knowledge: Background is empty. Then one possible solution for
Hypothesis is the following:
Grandparent(x,y)
⇔
[∃z Mother(x,z)∧Mother(z,y)]
∨
[∃z Mother(x,z)∧Father(z,y)]
∨
[∃z Father(x,z)∧Mother(z,y)]
∨
[∃z Father(x,z)∧Father(z,y)] .
Notice that an attribute-based learning algorithm, such as DECISION-TREE-LEARNING, will
get nowhere in solving this problem. In order to express Grandparent as an attribute (i.e., a
unary predicate), we would need to make pairs of people into objects:

## Page 760
