---
chunk_id: "book-ca4fca8dd8-chunk-0387"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 387
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.4
Propositional Logic: A Very Simple Logic
237
P
Q
¬P
P∧Q
P∨Q
P ⇒Q
P ⇔Q
false
false
true
false
false
true
true
false
true
true
false
true
true
false
true
false
false
false
true
false
false
true
true
false
true
true
true
true
Figure 7.8 Truth tables for the ﬁve logical connectives. To use the table to compute, for
example, the value of P ∨Q when P is true and Q is false, ﬁrst look on the left for the row
where P is true and Q is false (the third row). Then look in that row under the P∨Q column
to see the result: true.
For complex sentences, we have ﬁve rules, which hold for any subsentences P and Q (atomic
or complex) in any model m (here “iff” means “if and only if”):
• ¬P is true iff P is false in m.
• P∧Q is true iff both P and Q are true in m.
• P∨Q is true iff either P or Q is true in m.
• P ⇒Q is true unless P is true and Q is false in m.
• P ⇔Q is true iff P and Q are both true or both false in m.
The rules can also be expressed with truth tables that specify the truth value of a complex
Truth table
sentence for each possible assignment of truth values to its components. Truth tables for the
ﬁve connectives are given in Figure 7.8. From these tables, the truth value of any sentence
s can be computed with respect to any model m by a simple recursive evaluation. For ex-
ample, the sentence ¬P1,2 ∧(P2,2 ∨P3,1), evaluated in m1, gives true ∧(false ∨true)=true ∧
true=true. Exercise 7.TRUV asks you to write the algorithm PL-TRUE?(s,m), which com-
putes the truth value of a propositional logic sentence s in a model m.
The truth tables for “and,” “or,” and “not” are in close accord with our intuitions about
the English words. The main point of possible confusion is that P∨Q is true when P is true
or Q is true or both. A different connective, called “exclusive or” (“xor” for short), yields
false when both disjuncts are true.8 There is no consensus on the symbol for exclusive or;
some choices are ˙∨or ̸= or ⊕.
The truth table for ⇒may not quite ﬁt one’s intuitive understanding of “P implies Q” or
“if P then Q.” For one thing, propositional logic does not require any relation of causation
or relevance between P and Q. The sentence “5 is odd implies Tokyo is the capital of Japan”
is a true sentence of propositional logic (under the normal interpretation), even though it is
a decidedly odd sentence of English. Another point of confusion is that any implication is
true whenever its antecedent is false. For example, “5 is even implies Sam is smart” is true,
regardless of whether Sam is smart. This seems bizarre, but it makes sense if you think of
“P ⇒Q” as saying, “If P is true, then I am claiming that Q is true; otherwise I am making
no claim.” The only way for this sentence to be false is if P is true but Q is false.
The biconditional, P ⇔Q, is true whenever both P ⇒Q and Q ⇒P are true. In English,
this is often written as “P if and only if Q.” Many of the rules of the wumpus world are best
8
Latin uses two separate words: “vel” is inclusive or and “aut” is exclusive or.
