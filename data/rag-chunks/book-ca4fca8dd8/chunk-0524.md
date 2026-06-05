---
chunk_id: "book-ca4fca8dd8-chunk-0524"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 524
confidence: "first-pass"
extraction_method: "structured-local"
---

320
Chapter 9
Inference in First-Order Logic
exactly what happens in backward chaining. Thus, backward chaining is just a special case
of resolution with a particular control strategy to decide which resolution to perform next.
Our second example makes use of Skolemization and involves clauses that are not deﬁnite
clauses. This results in a somewhat more complex proof structure. In English:
Everyone who loves all animals is loved by someone.
Anyone who kills an animal is loved by no one.
Jack loves all animals.
Either Jack or Curiosity killed the cat, who is named Tuna.
Did Curiosity kill the cat?
First, we express the original sentences, some background knowledge, and the negated goal
G in ﬁrst-order logic:
A.
∀x [∀y Animal(y) ⇒Loves(x,y)] ⇒[∃y Loves(y,x)]
B.
∀x [∃z Animal(z)∧Kills(x,z)] ⇒[∀y ¬Loves(y,x)]
C.
∀x Animal(x) ⇒Loves(Jack,x)
D.
Kills(Jack,Tuna)∨Kills(Curiosity,Tuna)
E.
Cat(Tuna)
F.
∀x Cat(x) ⇒Animal(x)
¬G.
¬Kills(Curiosity,Tuna)
Now we apply the conversion procedure to convert each sentence to CNF:
A1.
Animal(F(x))∨Loves(G(x),x)
A2.
¬Loves(x,F(x))∨Loves(G(x),x)
B.
¬Loves(y,x)∨¬Animal(z)∨¬Kills(x,z)
C.
¬Animal(x)∨Loves(Jack,x)
D.
Kills(Jack,Tuna)∨Kills(Curiosity,Tuna)
E.
Cat(Tuna)
F.
¬Cat(x)∨Animal(x)
¬G.
¬Kills(Curiosity,Tuna)
The resolution proof that Curiosity killed the cat is given in Figure 9.11. In English, the proof
could be paraphrased as follows:
Suppose Curiosity did not kill Tuna. We know that either Jack or Curiosity did; thus
Jack must have. Now, Tuna is a cat and cats are animals, so Tuna is an animal. Because
anyone who kills an animal is loved by no one, we know that no one loves Jack. On the
other hand, Jack loves all animals, so someone loves him; so we have a contradiction.
Therefore, Curiosity killed the cat.
The proof answers the question “Did Curiosity kill the cat?” but often we want to pose
more general questions, such as “Who killed the cat?” Resolution can do this, but it takes a
little more work to obtain the answer. The goal is ∃w Kills(w,Tuna), which, when negated,
becomes ¬Kills(w,Tuna) in CNF. Repeating the proof in Figure 9.11 with the new negated
goal, we obtain a similar proof tree, but with the substitution {w/Curiosity} in one of the
steps. So, in this case, ﬁnding out who killed the cat is just a matter of keeping track of
the bindings for the query variables in the proof. Unfortunately, resolution can sometimes
produce nonconstructive proofs for existential goals, where we know a query is true, but
Nonconstructive
proof
there isn’t a unique binding for the variable.
