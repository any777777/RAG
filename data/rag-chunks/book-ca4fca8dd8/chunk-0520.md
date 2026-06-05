---
chunk_id: "book-ca4fca8dd8-chunk-0520"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 520
confidence: "first-pass"
extraction_method: "structured-local"
---

318
Chapter 9
Inference in First-Order Logic
nation. In the simple case, it is just like the Existential Instantiation rule of Section 9.1:
translate ∃x P(x) into P(A), where A is a new constant. However, we can’t apply Ex-
istential Instantiation to our sentence above because it doesn’t match the pattern ∃v α;
only parts of the sentence match the pattern. If we blindly apply the rule to the two
matching parts we get
∀x [Animal(A)∧¬Loves(x,A)]∨Loves(B,x),
which has the wrong meaning entirely: it says that everyone either fails to love a par-
ticular animal A or is loved by some particular entity B. In fact, our original sentence
allows each person to fail to love a different animal or to be loved by a different person.
Thus, we want the Skolem entities to depend on x:
∀x [Animal(F(x))∧¬Loves(x,F(x))]∨Loves(G(x),x).
Here F and G are Skolem functions. The general rule is that the arguments of the
Skolem function
Skolem function are all the universally quantiﬁed variables in whose scope the exis-
tential quantiﬁer appears. As with Existential Instantiation, the Skolemized sentence is
satisﬁable exactly when the original sentence is satisﬁable.
• Drop universal quantiﬁers: At this point, all remaining variables must be universally
quantiﬁed. Therefore, we don’t lose any information if we drop the quantiﬁer:
[Animal(F(x))∧¬Loves(x,F(x))]∨Loves(G(x),x).
• Distribute ∨over ∧:
[Animal(F(x))∨Loves(G(x),x)]∧[¬Loves(x,F(x))∨Loves(G(x),x)].
This step may also require ﬂattening out nested conjunctions and disjunctions.
The sentence is now in CNF and consists of two clauses. It is much more difﬁcult to read than
the original sentence with implications. (It may help to explain that the Skolem function F(x)
refers to the animal potentially unloved by x, whereas G(x) refers to someone who might
love x.) Fortunately, humans seldom need to look at CNF sentences—the translation process
is easily automated.
9.5.2 The resolution inference rule
The resolution rule for ﬁrst-order clauses is simply a lifted version of the propositional reso-
lution rule given on page 244. Two clauses, which are assumed to be standardized apart so
that they share no variables, can be resolved if they contain complementary literals. Propo-
sitional literals are complementary if one is the negation of the other; ﬁrst-order literals are
complementary if one uniﬁes with the negation of the other. Thus, we have
ℓ1 ∨···∨ℓk,
m1 ∨···∨mn
SUBST(θ,ℓ1 ∨···∨ℓi−1 ∨ℓi+1 ∨···∨ℓk ∨m1 ∨···∨m j−1 ∨m j+1 ∨···∨mn)
where UNIFY(ℓi,¬m j)=θ. For example, we can resolve the two clauses
[Animal(F(x))∨Loves(G(x),x)]
and
[¬Loves(u,v)∨¬Kills(u,v)]
by eliminating the complementary literals Loves(G(x),x) and ¬Loves(u,v), with the uniﬁer
θ={u/G(x),v/x}, to produce the resolvent clause
[Animal(F(x))∨¬Kills(G(x),x)].
This rule is called the binary resolution rule because it resolves exactly two literals. The
Binary resolution
