---
chunk_id: "book-ca4fca8dd8-chunk-0485"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 485
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
295
Debug the knowledge base
We can perturb the knowledge base in various ways to see what kinds of erroneous behaviors
emerge. For example, suppose we fail to read Section 8.2.8 and hence forget to assert that
1 ̸= 0. Suppose we ﬁnd that the system is unable to prove any outputs for the circuit, except
for the input cases 000 and 110. We can pinpoint the problem by asking for the outputs of
each gate. For example, we can ask
∃i1,i2,o Signal(In(1,C1))=i1 ∧Signal(In(2,C1))=i2 ∧Signal(Out(1,X1))=o,
which reveals that no outputs are known at X1 for the input cases 10 and 01. Then, we look
at the axiom for XOR gates, as applied to X1:
Signal(Out(1,X1))=1 ⇔Signal(In(1,X1)) ̸= Signal(In(2,X1)).
If the inputs are known to be, say, 1 and 0, then this reduces to
Signal(Out(1,X1))=1 ⇔1 ̸= 0.
Now the problem is apparent: the system is unable to infer that Signal(Out(1,X1))=1, so we
need to tell it that 1 ̸= 0.
Summary
This chapter has introduced ﬁrst-order logic, a representation language that is far more pow-
erful than propositional logic. The important points are as follows:
• Knowledge representation languages should be declarative, compositional, expressive,
context independent, and unambiguous.
• Logics differ in their ontological commitments and epistemological commitments.
While propositional logic commits only to the existence of facts, ﬁrst-order logic com-
mits to the existence of objects and relations and thereby gains expressive power, ap-
propriate for domains such as the wumpus world and electronic circuits.
• Both propositional logic and ﬁrst-order logic share a difﬁculty in representing vague
propositions. This difﬁculty limits their applicability in domains that require personal
judgments, like politics or cuisine.
• The syntax of ﬁrst-order logic builds on that of propositional logic. It adds terms to
represent objects, and has universal and existential quantiﬁers to construct assertions
about all or some of the possible values of the quantiﬁed variables.
• A possible world, or model, for ﬁrst-order logic includes a set of objects and an inter-
pretation that maps constant symbols to objects, predicate symbols to relations among
objects, and function symbols to functions on objects.
• An atomic sentence is true only when the relation named by the predicate holds between
the objects named by the terms. Extended interpretations, which map quantiﬁer vari-
ables to objects in the model, deﬁne the truth of quantiﬁed sentences.
• Developing a knowledge base in ﬁrst-order logic requires a careful process of analyzing
the domain, choosing a vocabulary, and encoding the axioms required to support the
desired inferences.
