---
chunk_id: "book-ca4fca8dd8-chunk-0391"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 391
confidence: "first-pass"
extraction_method: "structured-local"
---

240
Chapter 7
Logical Agents
enumeration of a ﬁnite space of assignments to symbols. The algorithm is sound because it
implements directly the deﬁnition of entailment, and complete because it works for any KB
and α and always terminates—there are only ﬁnitely many models to examine.
Of course, “ﬁnitely many” is not always the same as “few.” If KB and α contain n symbols
in all, then there are 2n models. Thus, the time complexity of the algorithm is O(2n). (The
space complexity is only O(n) because the enumeration is depth-ﬁrst.) Later in this chapter
we show algorithms that are much more efﬁcient in many cases. Unfortunately, propositional
entailment is co-NP-complete (i.e., probably no easier than NP-complete—see Appendix A),
so every known inference algorithm for propositional logic has a worst-case complexity that
▶
is exponential in the size of the input.
7.5 Propositional Theorem Proving
So far, we have shown how to determine entailment by model checking: enumerating models
and showing that the sentence must hold in all models. In this section, we show how entail-
ment can be done by theorem proving—applying rules of inference directly to the sentences
Theorem proving
in our knowledge base to construct a proof of the desired sentence without consulting models.
If the number of models is large but the length of the proof is short, then theorem proving can
be more efﬁcient than model checking.
Before we plunge into the details of theorem-proving algorithms, we will need some
additional concepts related to entailment. The ﬁrst concept is logical equivalence: two sen-
Logical equivalence
tences α and β are logically equivalent if they are true in the same set of models. We write
this as α ≡β. (Note that ≡is used to make claims about sentences, while ⇔is used as part
of a sentence.) For example, we can easily show (using truth tables) that P∧Q and Q∧P are
logically equivalent; other equivalences are shown in Figure 7.11. These equivalences play
much the same role in logic as arithmetic identities do in ordinary mathematics. An alterna-
tive deﬁnition of equivalence is as follows: any two sentences α and β are equivalent if and
only if each of them entails the other:
α ≡β
if and only if
α |= β and β |= α.
The second concept we will need is validity. A sentence is valid if it is true in all models. For
Validity
example, the sentence P∨¬P is valid. Valid sentences are also known as tautologies—they
Tautology
are necessarily true. Because the sentence True is true in all models, every valid sentence is
logically equivalent to True. What good are valid sentences? From our deﬁnition of entail-
ment, we can derive the deduction theorem, which was known to the ancient Greeks:
Deduction theorem▶
For any sentences α and β, α |= β if and only if the sentence (α ⇒β) is valid.
(Exercise 7.DEDU asks for a proof.) Hence, we can decide if α |= β by checking that (α ⇒β)
is true in every model—which is essentially what the inference algorithm in Figure 7.10
does—or by proving that (α ⇒β) is equivalent to True. Conversely, the deduction theorem
states that every valid implication sentence describes a legitimate inference.
The ﬁnal concept we will need is satisﬁability. A sentence is satisﬁable if it is true
Satisﬁability
in, or satisﬁed by, some model. For example, the knowledge base given earlier, (R1 ∧R2 ∧
R3 ∧R4 ∧R5), is satisﬁable because there are three models in which it is true, as shown in
Figure 7.9. Satisﬁability can be checked by enumerating the possible models until one is
found that satisﬁes the sentence. The problem of determining the satisﬁability of sentences
