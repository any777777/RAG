---
chunk_id: "book-ca4fca8dd8-chunk-0581"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 581
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 10.6
Reasoning with Default Information
353
To interpret what the default rules mean, we deﬁne the notion of an extension of a default
Extension
theory to be a maximal set of consequences of the theory. That is, an extension S consists
of the original known facts and a set of conclusions from the default rules, such that no
additional conclusions can be drawn from S, and the justiﬁcations of every default conclusion
in S are consistent with S. As in the case of the preferred models in circumscription, we have
two possible extensions for the Nixon diamond: one wherein he is a paciﬁst and one wherein
he is not. Prioritized schemes exist in which some default rules can be given precedence over
others, allowing some ambiguities to be resolved.
Since 1980, when nonmonotonic logics were ﬁrst proposed, a great deal of progress
has been made in understanding their mathematical properties. There are still unresolved
questions, however. For example, if “Cars have four wheels” is false, what does it mean to
have it in one’s knowledge base? What is a good set of default rules to have? If we cannot
decide, for each rule separately, whether it belongs in our knowledge base, then we have a
serious problem of nonmodularity. Finally, how can beliefs that have default status be used
to make decisions? This is probably the hardest issue for default reasoning.
Decisions often involve tradeoffs, and one therefore needs to compare the strengths of be-
lief in the outcomes of different actions, and the costs of making a wrong decision. In cases
where the same kinds of decisions are being made repeatedly, it is possible to interpret default
rules as “threshold probability” statements. For example, the default rule “My brakes are al-
ways OK” really means “The probability that my brakes are OK, given no other information,
is sufﬁciently high that the optimal decision is for me to drive without checking them.” When
the decision context changes—for example, when one is driving a heavily laden truck down a
steep mountain road—the default rule suddenly becomes inappropriate, even though there is
no new evidence of faulty brakes. These considerations have led researchers to consider how
to embed default reasoning within probability theory or utility theory.
10.6.2 Truth maintenance systems
We have seen that many of the inferences drawn by a knowledge representation system will
have only default status, rather than being absolutely certain. Inevitably, some of these in-
ferred facts will turn out to be wrong and will have to be retracted in the face of new infor-
mation. This process is called belief revision.10 Suppose that a knowledge base KB contains
Belief revision
a sentence P—perhaps a default conclusion recorded by a forward-chaining algorithm, or
perhaps just an incorrect assertion—and we want to execute TELL(KB, ¬P). To avoid cre-
ating a contradiction, we must ﬁrst execute RETRACT(KB, P). This sounds easy enough.
Problems arise, however, if any additional sentences were inferred from P and asserted in
the KB. For example, the implication P ⇒Q might have been used to add Q. The obvious
“solution”—retracting all sentences inferred from P—fails because such sentences may have
other justiﬁcations besides P. For example, if R and R ⇒Q are also in the KB, then Q does
not have to be removed after all. Truth maintenance systems, or TMSs, are designed to
Truth maintenance
system
handle exactly these kinds of complications.
One simple approach to truth maintenance is to keep track of the order in which sen-
tences are told to the knowledge base by numbering them from P1 to Pn. When the call
10 Belief revision is often contrasted with belief update, which occurs when a knowledge base is revised to reﬂect
a change in the world rather than new information about a ﬁxed world. Belief update combines belief revision
with reasoning about time and change; it is also related to the process of ﬁltering described in Chapter 14.
