---
chunk_id: "book-ca4fca8dd8-chunk-0451"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 451
confidence: "first-pass"
extraction_method: "structured-local"
---

276
Chapter 8
First-Order Logic
Sentence
→
AtomicSentence | ComplexSentence
AtomicSentence
→
Predicate | Predicate(Term,...) | Term = Term
ComplexSentence
→
( Sentence )
|
¬ Sentence
|
Sentence ∧Sentence
|
Sentence ∨Sentence
|
Sentence ⇒Sentence
|
Sentence ⇔Sentence
|
Quantiﬁer Variable,... Sentence
Term
→
Function(Term,...)
|
Constant
|
Variable
Quantiﬁer
→
∀| ∃
Constant
→
A | X1 | John | ···
Variable
→
a | x | s | ···
Predicate
→
True | False | After | Loves | Raining | ···
Function
→
Mother | LeftLeg | ···
OPERATOR PRECEDENCE
:
¬,=,∧,∨,⇒,⇔
Figure 8.3 The syntax of ﬁrst-order logic with equality, speciﬁed in Backus–Naur form (see
page 1081 if you are not familiar with this notation). Operator precedences are speciﬁed,
from highest to lowest. The precedence of quantiﬁers is such that a quantiﬁer holds over
everything to the right of it.
Every model must provide the information required to determine if any given sentence is
true or false. Thus, in addition to its objects, relations, and functions, each model includes an
interpretation that speciﬁes exactly which objects, relations and functions are referred to by
Interpretation
the constant, predicate, and function symbols. One possible interpretation for our example—
which a logician would call the intended interpretation—is as follows:
Intended
interpretation
• Richard refers to Richard the Lionheart and John refers to the evil King John.
• Brother refers to the brotherhood relation—that is, the set of tuples of objects given
in Equation (8.1); OnHead is a relation that holds between the crown and King John;
Person, King, and Crown are unary relations that identify persons, kings, and crowns.
• LeftLeg refers to the “left leg” function as deﬁned in Equation (8.2).
There are many other possible interpretations, of course. For example, one interpretation
maps Richard to the crown and John to King John’s left leg. There are ﬁve objects in the
model, so there are 25 possible interpretations just for the constant symbols Richard and John.

## Page 277
