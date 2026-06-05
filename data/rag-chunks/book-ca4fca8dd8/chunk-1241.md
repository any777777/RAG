---
chunk_id: "book-ca4fca8dd8-chunk-1241"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1241
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 20.2
Knowledge in Learning
749
• Finally, consider the case of a pharmacologically ignorant but diagnostically sophisti-
cated medical student observing a consulting session between a patient and an expert
internist. After a series of questions and answers, the expert tells the patient to take a
course of a particular antibiotic. The medical student infers the general rule that that
particular antibiotic is effective for a particular type of infection.
These are all cases in which the use of background knowledge allows much faster learning ◀
than one might expect from a pure induction program.
20.2.2 Some general schemes
In each of the preceding examples, one can appeal to prior knowledge to try to justify the
generalizations chosen. We will now look at what kinds of entailment constraints are operat-
ing in each case. The constraints will involve the Background knowledge, in addition to the
Hypothesis and the observed Descriptions and Classiﬁcations.
In the case of lizard toasting, the cavemen generalize by explaining the success of the
pointed stick: it supports the lizard while keeping the hand away from the ﬁre. From this
explanation, they can infer a general rule: that any long, rigid, sharp object can be used to toast
small, soft-bodied edibles. This kind of generalization process has been called explanation-
based learning, or EBL. Notice that the general rule follows logically from the background
Explanation-based
learning
knowledge possessed by the cavemen. Hence, the entailment constraints satisﬁed by EBL are
the following:
Hypothesis∧Descriptions |= Classiﬁcations
Background |= Hypothesis .
Because EBL uses Equation (20.3), it was initially thought to be a way to learn from ex-
amples. But because it requires that the background knowledge be sufﬁcient to explain the
Hypothesis, which in turn explains the observations, the agent does not actually learn any- ◀
thing factually new from the example. The agent could have derived the example from what
it already knew, although that might have required an unreasonable amount of computation.
EBL is now viewed as a method for converting ﬁrst-principles theories into useful, special-
purpose knowledge. We describe algorithms for EBL in Section 20.3.
The situation of our traveler in Brazil is quite different, for she cannot necessarily explain
why Fernando speaks the way he does, unless she knows her papal bulls. Moreover, the same
generalization would be forthcoming from a traveler entirely ignorant of colonial history. The
relevant prior knowledge in this case is that, within any given country, most people tend to
speak the same language; on the other hand, Fernando is not assumed to be the name of all
Brazilians because this kind of regularity does not hold for names. Similarly, the freshman
physics student also would be hard put to explain the particular values that she discovers for
the conductance and density of copper. She does know, however, that the material of which an
object is composed and its temperature together determine its conductance. In each case, the
prior knowledge Background concerns the relevance of a set of features to the goal predicate.
Relevance
This knowledge, together with the observations, allows the agent to infer a new, general rule
that explains the observations:
Hypothesis∧Descriptions |= Classiﬁcations ,
Background ∧Descriptions∧Classiﬁcations |= Hypothesis .
(20.4)
