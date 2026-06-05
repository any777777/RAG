---
chunk_id: "book-ca4fca8dd8-chunk-0460"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 460
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 8.2
Syntax and Semantics of First-Order Logic
281
Nested quantiﬁers
We will often want to express more complex sentences using multiple quantiﬁers. The sim-
plest case is where the quantiﬁers are of the same type. For example, “Brothers are siblings”
can be written as
∀x ∀y Brother(x,y) ⇒Sibling(x,y).
Consecutive quantiﬁers of the same type can be written as one quantiﬁer with several vari-
ables. For example, to say that siblinghood is a symmetric relationship, we can write
∀x,y Sibling(x,y) ⇔Sibling(y,x).
In other cases we will have mixtures. “Everybody loves somebody” means that for every
person, there is someone that person loves:
∀x ∃y Loves(x,y).
On the other hand, to say “There is someone who is loved by everyone,” we write
∃y ∀x Loves(x,y).
The order of quantiﬁcation is therefore very important. It becomes clearer if we insert paren-
theses. ∀x (∃y Loves(x,y)) says that everyone has a particular property, namely, the property
that they love someone. On the other hand, ∃y (∀x Loves(x,y)) says that someone in the
world has a particular property, namely the property of being loved by everybody.
Some confusion can arise when two quantiﬁers are used with the same variable name.
Consider the sentence
∀x (Crown(x)∨(∃x Brother(Richard,x))).
Here the x in Brother(Richard,x) is existentially quantiﬁed. The rule is that the variable
belongs to the innermost quantiﬁer that mentions it; then it will not be subject to any other
quantiﬁcation. Another way to think of it is this: ∃x Brother(Richard,x) is a sentence about
Richard (that he has a brother), not about x; so putting a ∀x outside it has no effect. It
could equally well have been written ∃z Brother(Richard,z). Because this can be a source of
confusion, we will always use different variable names with nested quantiﬁers.
Connections between ∀and ∃
The two quantiﬁers are actually intimately connected with each other, through negation. As-
serting that everyone dislikes parsnips is the same as asserting there does not exist someone
who likes them, and vice versa:
∀x ¬Likes(x,Parsnips)
is equivalent to
¬∃x Likes(x,Parsnips).
We can go one step further: “Everyone likes ice cream” means that there is no one who does
not like ice cream:
∀x Likes(x,IceCream)
is equivalent to
¬∃x ¬Likes(x,IceCream).
Because ∀is really a conjunction over the universe of objects and ∃is a disjunction, it should
not be surprising that they obey De Morgan’s rules. The De Morgan rules for quantiﬁed and
unquantiﬁed sentences are as follows:
¬∃x P ≡∀x ¬P
¬(P∨Q) ≡¬P∧¬Q
¬∀x P ≡∃x ¬P
¬(P∧Q) ≡¬P∨¬Q
∀x P
≡¬∃x ¬P
P∧Q
≡¬(¬P∨¬Q)
∃x P
≡¬∀x ¬P
P∨Q
≡¬(¬P∧¬Q).
