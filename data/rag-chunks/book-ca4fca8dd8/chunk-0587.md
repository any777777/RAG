---
chunk_id: "book-ca4fca8dd8-chunk-0587"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 587
confidence: "first-pass"
extraction_method: "structured-local"
---

356
Chapter 10
Knowledge Representation
• The closed-world assumption, as implemented in logic programs, provides a simple
way to avoid having to specify lots of negative information. It is best interpreted as a
default that can be overridden by additional information.
• Nonmonotonic logics, such as circumscription and default logic, are intended to cap-
ture default reasoning in general.
• Truth maintenance systems handle knowledge updates and revisions efﬁciently.
• It is difﬁcult to construct large ontologies by hand; extracting knowledge from text
makes the job easier.
Bibliographical and Historical Notes
Briggs (1985) claims that knowledge representation research began with ﬁrst millennium BCE
Indian theorizing about the grammar of Shastric Sanskrit. Western philosophers trace their
work on the subject back to c. 300 BCE in Aristotle’s Metaphysics (literally, what comes after
the book on physics). The development of technical terminology in any ﬁeld can be regarded
as a form of knowledge representation.
Early discussions of representation in AI tended to focus on “problem representation”
rather than “knowledge representation.” (See, for example, Amarel’s (1968) discussion of
the “Missionaries and Cannibals” problem.) In the 1970s, AI emphasized the development of
“expert systems” (also called “knowledge-based systems”) that could, if given the appropriate
domain knowledge, match or exceed the performance of human experts on narrowly deﬁned
tasks. For example, the ﬁrst expert system, DENDRAL (Feigenbaum et al., 1971; Lindsay
et al., 1980), interpreted the output of a mass spectrometer (a type of instrument used to ana-
lyze the structure of organic chemical compounds) as accurately as expert chemists. Although
the success of DENDRAL was instrumental in convincing the AI research community of the
importance of knowledge representation, the representational formalisms used in DENDRAL
are highly speciﬁc to the domain of chemistry.
Over time, researchers became interested in standardized knowledge representation for-
malisms and ontologies that could assist in the creation of new expert systems. This brought
them into territory previously explored by philosophers of science and of language. The disci-
pline imposed in AI by the need for one’s theories to “work” has led to more rapid and deeper
progress than when these problems were the exclusive domain of philosophy (although it has
at times also led to the repeated reinvention of the wheel).
But to what extent can we trust expert knowledge? As far back as 1955, Paul Meehl
(see also Grove and Meehl, 1996) studied the decision-making processes of trained experts
at subjective tasks such as predicting the success of a student in a training program or the
recidivism of a criminal. In 19 out of the 20 studies he looked at, Meehl found that simple
statistical learning algorithms (such as linear regression or naive Bayes) predict better than
the experts. Tetlock (2017) also studies expert knowledge and ﬁnds it lacking in difﬁcult
cases. The Educational Testing Service has used an automated program to grade millions of
essay questions on the GMAT exam since 1999. The program agrees with human graders
97% of the time, about the same level that two human graders agree (Burstein et al., 2001).
(This does not mean the program understands essays, just that it can distinguish good ones
from bad ones about as well as human graders can.)
