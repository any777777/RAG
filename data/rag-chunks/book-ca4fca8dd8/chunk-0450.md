---
chunk_id: "book-ca4fca8dd8-chunk-0450"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 450
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 275

Section 8.2
Syntax and Semantics of First-Order Logic
275
R
J
$
left leg
on head
brother
brother
person
person
king
crown
left leg
Figure 8.2 A model containing ﬁve objects, two binary relations (brother and on-head), three
unary relations (person, king, and crown), and one unary function (left-leg).
includes the following mappings:
⟨Richard the Lionheart⟩→Richard’s left leg
⟨King John⟩→John’s left leg.
(8.2)
Strictly speaking, models in ﬁrst-order logic require total functions, that is, there must be a
Total functions
value for every input tuple. Thus the crown must have a left leg and so must each of the left
legs. There is a technical solution to this awkward problem involving an additional “invisible”
object that is the left leg of everything that has no left leg, including itself. Fortunately, as
long as one makes no assertions about the left legs of things that have no left legs, these
technicalities are of no import.
So far, we have described the elements that populate models for ﬁrst-order logic. The
other essential part of a model is the link between those elements and the vocabulary of the
logical sentences, which we explain next.
8.2.2 Symbols and interpretations
We turn now to the syntax of ﬁrst-order logic. The impatient reader can obtain a complete
description from the formal grammar in Figure 8.3.
The basic syntactic elements of ﬁrst-order logic are the symbols that stand for objects,
relations, and functions. The symbols, therefore, come in three kinds: constant symbols,
Constant symbol
which stand for objects; predicate symbols, which stand for relations; and function sym-
Predicate symbol
bols, which stand for functions. We adopt the convention that these symbols will begin with
Function symbol
uppercase letters. For example, we might use the constant symbols Richard and John; the
predicate symbols Brother, OnHead, Person, King, and Crown; and the function symbol
LeftLeg. As with proposition symbols, the choice of names is entirely up to the user. Each
predicate and function symbol comes with an arity that ﬁxes the number of arguments.
Arity

## Page 276
