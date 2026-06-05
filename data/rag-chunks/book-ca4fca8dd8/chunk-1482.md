---
chunk_id: "book-ca4fca8dd8-chunk-1482"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1482
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.4
Augmented Grammars
895
Operator(÷)
3
(
)
4
2
+
Number(2)
Digit(2)
Number(4)
Digit(4)
Operator(+)
Digit(3)
Number(3)
Exp(5)
Exp(2)
Exp(2)
Exp(4)
Exp(2)
Exp(3)
÷
Figure 24.11 Parse tree with semantic interpretations for the string “3+(4÷2)”.
S(pred(n)) →NP(n) VP(pred)
VP(pred(n)) →Verb(pred) NP(n)
NP(n) →Name(n)
Name(Ali) →Ali
Name(Bo) →Bo
Verb(λy λx Loves(x,y)) →loves
Ali
loves
Bo
Name(Ali)
Name(Bo)
NP(Bo)
NP(Ali)
S(Loves(Ali, Bo))
Verb(λy λ x Loves(x, y))
VP(λx Loves(x, Bo))
(a)
(b)
Figure 24.12 (a) A grammar that can derive a parse tree and semantic interpretation for “Ali
loves Bo” (and three other sentences). Each category is augmented with a single argument
representing the semantics. (b) A parse tree with semantic interpretations for the string “Ali
loves Bo.”
which is equivalent to Loves(Ali,Bo). Technically, we say that this is a β-reduction of the
lambda function application.
The rest of the semantics follows in a straightforward way from the choices we have made
so far. Because VPs are represented as predicates, verbs should be predicates as well. The
verb “loves” is represented as λy λx Loves(x,y), the predicate that, when given the argument
Bo, returns the predicate λx Loves(x,Bo). We end up with the grammar and parse tree shown
in Figure 24.12. In a more complete grammar, we would put all the augmentations (seman-
tics, case, person-number, and head) together into one set of rules. Here we show only the
semantic augmentation to make it clearer how the rules work.

## Page 896
