---
chunk_id: "book-ca4fca8dd8-chunk-0452"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 452
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 8.2
Syntax and Semantics of First-Order Logic
277
. . .
. . .
. . .
R
J
R
R
R
R
R
J
J
J
J
J
Figure 8.4 Some members of the set of all models for a language with two constant symbols,
R and J, and one binary relation symbol. The interpretation of each constant symbol is shown
by a gray arrow. Within each model, the related objects are connected by arrows.
Notice that not all the objects need have a name—for example, the intended interpretation
does not name the crown or the legs. It is also possible for an object to have several names;
there is an interpretation under which both Richard and John refer to the crown.2 If you ﬁnd
this possibility confusing, remember that, in propositional logic, it is perfectly possible to
have a model in which Cloudy and Sunny are both true; it is the job of the knowledge base to
rule out models that are inconsistent with our knowledge.
In summary, a model in ﬁrst-order logic consists of a set of objects and an interpretation
that maps constant symbols to objects, function symbols to functions on those objects, and
predicate symbols to relations. Just as with propositional logic, entailment, validity, and so
on are deﬁned in terms of all possible models. To get an idea of what the set of all possible
models looks like, see Figure 8.4. It shows that models vary in how many objects they
contain—from one to inﬁnity—and in the way the constant symbols map to objects.
Because the number of ﬁrst-order models is unbounded, we cannot check entailment by
enumerating them all (as we did for propositional logic). Even if the number of objects is
restricted, the number of combinations can be very large. (See Exercise 8.MCNT.) For the
example in Figure 8.4, there are 137,506,194,466 models with six or fewer objects.
8.2.3 Terms
A term is a logical expression that refers to an object. Constant symbols are terms, but it is
Term
not always convenient to have a distinct symbol to name every object. In English we might
use the expression “King John’s left leg” rather than giving a name to his leg. This is what
function symbols are for: instead of using a constant symbol, we use LeftLeg(John).3
In the general case, a complex term is formed by a function symbol followed by a paren-
thesized list of terms as arguments to the function symbol. It is important to remember that a
complex term is just a complicated kind of name. It is not a “subroutine call” that “returns a
value.” There is no LeftLeg subroutine that takes a person as input and returns a leg. We can
reason about left legs (e.g., stating the general rule that everyone has one and then deducing
2
Later, in Section 8.2.8, we examine a semantics in which every object must have exactly one name.
3
λ-expressions (lambda expressions) provide a useful notation in which new function symbols are constructed
“on the ﬂy.” For example, the function that squares its argument can be written as (λx : x×x) and can be applied
to arguments just like any other function symbol. A λ-expression can also be deﬁned and used as a predicate
symbol. The lambda operator in Lisp and Python plays exactly the same role. Notice that the use of λ in this
way does not increase the formal expressive power of ﬁrst-order logic, because any sentence that includes a
λ-expression can be rewritten by “plugging in” its arguments to yield an equivalent sentence.
