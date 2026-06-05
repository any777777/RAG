---
chunk_id: "book-ca4fca8dd8-chunk-0395"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 395
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.5
Propositional Theorem Proving
243
One ﬁnal property of logical systems is monotonicity, which says that the set of en-
Monotonicity
tailed sentences can only increase as information is added to the knowledge base.9 For any
sentences α and β,
if
KB |= α
then
KB∧β |= α.
For example, suppose the knowledge base contains the additional assertion β stating that there
are exactly eight pits in the world. This knowledge might help the agent draw additional con-
clusions, but it cannot invalidate any conclusion α already inferred—such as the conclusion
that there is no pit in [1,2]. Monotonicity means that inference rules can be applied whenever
suitable premises are found in the knowledge base—the conclusion of the rule must follow
regardless of what else is in the knowledge base.
7.5.2 Proof by resolution
We have argued that the inference rules covered so far are sound, but we have not discussed
the question of completeness for the inference algorithms that use them. Search algorithms
such as iterative deepening search (page 99) are complete in the sense that they will ﬁnd
any reachable goal, but if the available inference rules are inadequate, then the goal is not
reachable—no proof exists that uses only those inference rules. For example, if we removed
the biconditional elimination rule, the proof in the preceding section would not go through.
The current section introduces a single inference rule, resolution, that yields a complete
inference algorithm when coupled with any complete search algorithm.
We begin by using a simple version of the resolution rule in the wumpus world. Let us
consider the steps leading up to Figure 7.4(a): the agent returns from [2,1] to [1,1] and then
goes to [1,2], where it perceives a stench, but no breeze. We add the following facts to the
knowledge base:
R11 :
¬B1,2 .
R12 :
B1,2 ⇔(P1,1 ∨P2,2 ∨P1,3).
By the same process that led to R10 earlier, we can now derive the absence of pits in [2,2] and
[1,3] (remember that [1,1] is already known to be pitless):
R13 :
¬P2,2 .
R14 :
¬P1,3 .
We can also apply biconditional elimination to R3, followed by Modus Ponens with R5, to
obtain the fact that there is a pit in [1,1], [2,2], or [3,1]:
R15 :
P1,1 ∨P2,2 ∨P3,1 .
Now comes the ﬁrst application of the resolution rule: the literal ¬P2,2 in R13 resolves with
the literal P2,2 in R15 to give the resolvent
Resolvent
R16 :
P1,1 ∨P3,1 .
In English; if there’s a pit in one of [1,1], [2,2], and [3,1] and it’s not in [2,2], then it’s in [1,1]
or [3,1]. Similarly, the literal ¬P1,1 in R1 resolves with the literal P1,1 in R16 to give
R17 :
P3,1 .
In English: if there’s a pit in [1,1] or [3,1] and it’s not in [1,1], then it’s in [3,1]. These last
two inference steps are examples of the unit resolution inference rule
Unit resolution
9
Nonmonotonic logics, which violate the monotonicity property, capture a common property of human rea-
soning: changing one’s mind. They are discussed in Section 10.6.
