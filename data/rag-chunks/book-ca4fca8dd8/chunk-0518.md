---
chunk_id: "book-ca4fca8dd8-chunk-0518"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 518
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 9.5
Resolution
317
9.5.1 Conjunctive normal form for ﬁrst-order logic
The ﬁrst step is to convert sentences to conjunctive normal form (CNF)—that is, a conjunc-
tion of clauses, where each clause is a disjunction of literals.5 In CNF, literals can contain
variables, which are assumed to be universally quantiﬁed. For example, the sentence
∀x,y,z American(x)∧Weapon(y)∧Sells(x,y,z)∧Hostile(z) ⇒Criminal(x)
becomes, in CNF,
¬American(x)∨¬Weapon(y)∨¬Sells(x,y,z)∨¬Hostile(z)∨Criminal(x).
The key is that Every sentence of ﬁrst-order logic can be converted into an inferentially ◀
equivalent CNF sentence.
The procedure for conversion to CNF is similar to the propositional case, which we saw
on page 244. The principal difference arises from the need to eliminate existential quantiﬁers.
We illustrate the procedure by translating the sentence “Everyone who loves all animals is
loved by someone,” or
∀x [∀y Animal(y) ⇒Loves(x,y)] ⇒[∃y Loves(y,x)].
The steps are as follows:
• Eliminate implications: Replace P ⇒Q with ¬P ∨Q. For our sample sentence, this
needs to be done twice:
∀x ¬[∀y Animal(y) ⇒Loves(x,y)]∨[∃y Loves(y,x)]
∀x ¬[∀y ¬Animal(y)∨Loves(x,y)]∨[∃y Loves(y,x)].
• Move ¬ inwards: In addition to the usual rules for negated connectives, we need rules
for negated quantiﬁers. Thus, we have
¬∀x p
becomes
∃x ¬p
¬∃x p
becomes
∀x ¬p.
Our sentence goes through the following transformations:
∀x [∃y ¬(¬Animal(y)∨Loves(x,y))]∨[∃y Loves(y,x)].
∀x [∃y ¬¬Animal(y)∧¬Loves(x,y)]∨[∃y Loves(y,x)].
∀x [∃y Animal(y)∧¬Loves(x,y)]∨[∃y Loves(y,x)].
Notice how a universal quantiﬁer (∀y) in the premise of the implication has become
an existential quantiﬁer. The sentence now reads “Either there is some animal that x
doesn’t love, or (if this is not the case) someone loves x.” Clearly, the meaning of the
original sentence has been preserved.
• Standardize variables: For sentences like (∃xP(x)) ∨(∃xQ(x)) that use the same
variable name twice, change the name of one of the variables. This avoids confusion
later when we drop the quantiﬁers. Thus, we have
∀x [∃y Animal(y)∧¬Loves(x,y)]∨[∃z Loves(z,x)].
• Skolemize: Skolemization is the process of removing existential quantiﬁers by elimi-
Skolemization
5
A clause can also be represented as an implication with a conjunction of atoms in the premise and a disjunc-
tion of atoms in the conclusion (Exercise 9.DISJ). This is called implicative normal form or Kowalski form
(especially when written with a right-to-left implication symbol (Kowalski, 1979)) and is generally much easier
to read than a disjunction with many negated literals.
