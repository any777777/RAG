---
chunk_id: "book-ca4fca8dd8-chunk-0583"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 583
confidence: "first-pass"
extraction_method: "structured-local"
---

354
Chapter 10
Knowledge Representation
RETRACT(KB, Pi) is made, the system reverts to the state just before Pi was added, thereby
removing both Pi and any inferences that were derived from Pi. The sentences Pi+1 through
Pn can then be added again. This is simple, and it guarantees that the knowledge base will
be consistent, but retracting Pi requires retracting and reasserting n −i sentences as well as
undoing and redoing all the inferences drawn from those sentences. For systems to which
many facts are being added—such as large commercial databases—this is impractical.
A more efﬁcient approach is the justiﬁcation-based truth maintenance system, or JTMS.
JTMS
In a JTMS, each sentence in the knowledge base is annotated with a justiﬁcation consisting
Justiﬁcation
of the set of sentences from which it was inferred. For example, if the knowledge base already
contains P ⇒Q, then TELL(P) will cause Q to be added with the justiﬁcation {P, P ⇒Q}.
In general, a sentence can have any number of justiﬁcations. Justiﬁcations make retraction
efﬁcient. Given the call RETRACT(P), the JTMS will delete exactly those sentences for
which P is a member of every justiﬁcation. So, if a sentence Q had the single justiﬁcation
{P, P ⇒Q}, it would be removed; if it had the additional justiﬁcation {P, P ∨R ⇒Q}, it
would still be removed; but if it also had the justiﬁcation {R, P ∨R ⇒Q}, then it would
be spared. In this way, the time required for retraction of P depends only on the number of
sentences derived from P rather than on the number of sentences added after P.
The JTMS assumes that sentences that are considered once will probably be considered
again, so rather than deleting a sentence from the knowledge base entirely when it loses
all justiﬁcations, we merely mark the sentence as being out of the knowledge base. If a
subsequent assertion restores one of the justiﬁcations, then we mark the sentence as being
back in. In this way, the JTMS retains all the inference chains that it uses and need not
rederive sentences when a justiﬁcation becomes valid again.
In addition to handling the retraction of incorrect information, TMSs can be used to
speed up the analysis of multiple hypothetical situations. Suppose, for example, that the
Romanian Olympic Committee is choosing sites for the swimming, athletics, and equestrian
events at the 2048 Games to be held in Romania. For example, let the ﬁrst hypothesis be
Site(Swimming,Pitesti), Site(Athletics,Bucharest), and Site(Equestrian,Arad).
A great deal of reasoning must then be done to work out the logistical consequences
and hence the desirability of this selection. If we want to consider Site(Athletics,Sibiu)
instead, the TMS avoids the need to start again from scratch. Instead, we simply retract
Site(Athletics,Bucharest) and assert Site(Athletics,Sibiu) and the TMS takes care of the nec-
essary revisions. Inference chains generated from the choice of Bucharest can be reused with
Sibiu, provided that the conclusions are the same.
An assumption-based truth maintenance system, or ATMS, makes this type of context-
ATMS
switching between hypothetical worlds particularly efﬁcient. In a JTMS, the maintenance of
justiﬁcations allows you to move quickly from one state to another by making a few retrac-
tions and assertions, but at any time only one state is represented. An ATMS represents all the
states that have ever been considered at the same time. Whereas a JTMS simply labels each
sentence as being in or out, an ATMS keeps track, for each sentence, of which assumptions
would cause the sentence to be true. In other words, each sentence has a label that consists of
a set of assumption sets. The sentence is true just in those cases in which all the assumptions
in one of the assumption sets are true.
Truth maintenance systems also provide a mechanism for generating explanations. Tech-
Explanation
nically, an explanation of a sentence P is a set of sentences E such that E entails P. If the
