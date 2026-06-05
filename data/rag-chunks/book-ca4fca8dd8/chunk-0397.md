---
chunk_id: "book-ca4fca8dd8-chunk-0397"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 397
confidence: "first-pass"
extraction_method: "structured-local"
---

244
Chapter 7
Logical Agents
ℓ1 ∨···∨ℓk,
m
ℓ1 ∨···∨ℓi−1 ∨ℓi+1 ∨···∨ℓk
where each ℓis a literal and ℓi and m are complementary literals (i.e., one is the negation
Complementary
literals
of the other). Thus, the unit resolution rule takes a clause—a disjunction of literals—and a
Clause
literal and produces a new clause. Note that a single literal can be viewed as a disjunction of
one literal, also known as a unit clause.
Unit clause
The unit resolution rule can be generalized to the full resolution rule
Resolution
ℓ1 ∨···∨ℓk,
m1 ∨···∨mn
ℓ1 ∨···∨ℓi−1 ∨ℓi+1 ∨···∨ℓk ∨m1 ∨···∨m j−1 ∨m j+1 ∨···∨mn
where ℓi and mj are complementary literals. This says that resolution takes two clauses and
produces a new clause containing all the literals of the two original clauses except the two
complementary literals. For example, we have
P1,1 ∨P3,1,
¬P1,1 ∨¬P2,2
P3,1 ∨¬P2,2
.
You can resolve only one pair of complementary literals at a time. For example, we can
resolve P and ¬P to deduce
P∨¬Q∨R,
¬P∨Q
¬Q∨Q∨R
,
but you can’t resolve on both P and Q at once to infer R. There is one more technical aspect
of the resolution rule: the resulting clause should contain only one copy of each literal.10 The
removal of multiple copies of literals is called factoring. For example, if we resolve (A∨B)
Factoring
with (A∨¬B), we obtain (A∨A), which is reduced to just A by factoring.
The soundness of the resolution rule can be seen easily by considering the literal ℓi that
is complementary to literal m j in the other clause. If ℓi is true, then m j is false, and hence
m1 ∨··· ∨mj−1 ∨mj+1 ∨··· ∨mn must be true, because m1 ∨··· ∨mn is given. If ℓi is false,
then ℓ1 ∨···∨ℓi−1 ∨ℓi+1 ∨···∨ℓk must be true because ℓ1 ∨···∨ℓk is given. Now ℓi is either
true or false, so one or other of these conclusions holds—exactly as the resolution rule states.
What is more surprising about the resolution rule is that it forms the basis for a family of
complete inference procedures. A resolution-based theorem prover can, for any sentences α
▶
and β in propositional logic, decide whether α |= β. The next two subsections explain how
resolution accomplishes this.
Conjunctive normal form
The resolution rule applies only to clauses (that is, disjunctions of literals), so it would seem
to be relevant only to knowledge bases and queries consisting of clauses. How, then, can it
lead to a complete inference procedure for all of propositional logic? The answer is that every
▶
sentence of propositional logic is logically equivalent to a conjunction of clauses.
A sentence expressed as a conjunction of clauses is said to be in conjunctive normal
form or CNF (see Figure 7.12). We now describe a procedure for converting to CNF. We
Conjunctive normal
form
CNF
illustrate the procedure by converting the sentence B1,1 ⇔(P1,2 ∨P2,1) into CNF. The steps
are as follows:
10 If a clause is viewed as a set of literals, then this restriction is automatically respected. Using set notation for
clauses makes the resolution rule much cleaner, at the cost of introducing additional notation.
