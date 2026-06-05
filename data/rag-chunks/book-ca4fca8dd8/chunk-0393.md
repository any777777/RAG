---
chunk_id: "book-ca4fca8dd8-chunk-0393"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 393
confidence: "first-pass"
extraction_method: "structured-local"
---

242
Chapter 7
Logical Agents
By considering the possible truth values of α and β, one can easily show once and for
all that Modus Ponens and And-Elimination are sound. These rules can then be used in
any particular instances where they apply, generating sound inferences without the need for
enumerating models.
All of the logical equivalences in Figure 7.11 can be used as inference rules. For example,
the equivalence for biconditional elimination yields the two inference rules
α ⇔β
(α ⇒β)∧(β ⇒α)
and
(α ⇒β)∧(β ⇒α)
α ⇔β
.
Not all inference rules work in both directions like this. For example, we cannot run Modus
Ponens in the opposite direction to obtain α ⇒β and α from β.
Let us see how these inference rules and equivalences can be used in the wumpus world.
We start with the knowledge base containing R1 through R5 and show how to prove ¬P1,2,
that is, there is no pit in [1,2]:
1. Apply biconditional elimination to R2 to obtain
R6 :
(B1,1 ⇒(P1,2 ∨P2,1)) ∧((P1,2 ∨P2,1) ⇒B1,1).
2. Apply And-Elimination to R6 to obtain
R7 :
((P1,2 ∨P2,1) ⇒B1,1).
3. Logical equivalence for contrapositives gives
R8 :
(¬B1,1 ⇒¬(P1,2 ∨P2,1)).
4. Apply Modus Ponens with R8 and the percept R4 (i.e., ¬B1,1), to obtain
R9 :
¬(P1,2 ∨P2,1).
5. Apply De Morgan’s rule, giving the conclusion
R10 :
¬P1,2 ∧¬P2,1 .
That is, neither [1,2] nor [2,1] contains a pit.
Any of the search algorithms in Chapter 3 can be used to ﬁnd a sequence of steps that
constitutes a proof like this. We just need to deﬁne a proof problem as follows:
• INITIAL STATE: the initial knowledge base.
• ACTIONS: the set of actions consists of all the inference rules applied to all the sen-
tences that match the top half of the inference rule.
• RESULT: the result of an action is to add the sentence in the bottom half of the inference
rule.
• GOAL: the goal is a state that contains the sentence we are trying to prove.
Thus, searching for proofs is an alternative to enumerating models. In many practical cases
ﬁnding a proof can be more efﬁcient because the proof can ignore irrelevant propositions, no
▶
matter how many of them there are. For example, the proof just given leading to ¬P1,2 ∧¬P2,1
does not mention the propositions B2,1, P1,1, P2,2, or P3,1. They can be ignored because the
goal proposition, P1,2, appears only in sentence R2; the other propositions in R2 appear only
in R4 and R2; so R1, R3, and R5 have no bearing on the proof. The same would hold even if
we added a million more sentences to the knowledge base; the simple truth-table algorithm,
on the other hand, would be overwhelmed by the exponential explosion of models.
