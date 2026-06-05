---
chunk_id: "book-ca4fca8dd8-chunk-0398"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 398
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 245

Section 7.5
Propositional Theorem Proving
245
CNFSentence
→
Clause1 ∧···∧Clausen
Clause
→
Literal1 ∨···∨Literalm
Fact
→
Symbol
Literal
→
Symbol | ¬Symbol
Symbol
→
P | Q | R | ...
HornClauseForm
→
DeﬁniteClauseForm | GoalClauseForm
DeﬁniteClauseForm
→
Fact | (Symbol1 ∧···∧Symboll) ⇒Symbol
GoalClauseForm
→
(Symbol1 ∧···∧Symboll) ⇒False
Figure 7.12 A grammar for conjunctive normal form, Horn clauses, and deﬁnite clauses. A
CNF clause such as ¬A∨¬B∨C can be written in deﬁnite clause form as A∧B ⇒C.
1. Eliminate ⇔, replacing α ⇔β with (α ⇒β)∧(β ⇒α).
(B1,1 ⇒(P1,2 ∨P2,1))∧((P1,2 ∨P2,1) ⇒B1,1).
2. Eliminate ⇒, replacing α ⇒β with ¬α∨β:
(¬B1,1 ∨P1,2 ∨P2,1)∧(¬(P1,2 ∨P2,1)∨B1,1).
3. CNF requires ¬ to appear only in literals, so we “move ¬ inwards” by repeated appli-
cation of the following equivalences from Figure 7.11:
¬(¬α) ≡α (double-negation elimination)
¬(α∧β) ≡(¬α∨¬β) (De Morgan)
¬(α∨β) ≡(¬α∧¬β) (De Morgan)
In the example, we require just one application of the last rule:
(¬B1,1 ∨P1,2 ∨P2,1)∧((¬P1,2 ∧¬P2,1)∨B1,1).
4. Now we have a sentence containing nested ∧and ∨operators applied to literals. We
apply the distributivity law from Figure 7.11, distributing ∨over ∧wherever possible.
(¬B1,1 ∨P1,2 ∨P2,1)∧(¬P1,2 ∨B1,1)∧(¬P2,1 ∨B1,1).
The original sentence is now in CNF, as a conjunction of three clauses. It is much harder to
read, but it can be used as input to a resolution procedure.
A resolution algorithm
Inference procedures based on resolution work by using the principle of proof by contra-
diction introduced on page 241. That is, to show that KB |= α, we show that (KB ∧¬α) is
unsatisﬁable. We do this by proving a contradiction.
A resolution algorithm is shown in Figure 7.13. First, (KB∧¬α) is converted into CNF.
Then, the resolution rule is applied to the resulting clauses. Each pair that contains com-
plementary literals is resolved to produce a new clause, which is added to the set if it is not
already present. The process continues until one of two things happens:
• there are no new clauses that can be added, in which case KB does not entail α; or,
• two clauses resolve to yield the empty clause, in which case KB entails α.

## Page 246
