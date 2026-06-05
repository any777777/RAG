---
chunk_id: "book-ca4fca8dd8-chunk-0585"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 585
confidence: "first-pass"
extraction_method: "structured-local"
---

Summary
355
sentences in E are already known to be true, then E simply provides a sufﬁcient basis for
proving that P must be the case. But explanations can also include assumptions—sentences
Assumption
that are not known to be true, but would sufﬁce to prove P if they were true. For example,
if your car won’t start, you probably don’t have enough information to deﬁnitively prove the
reason for the problem. But a reasonable explanation might include the assumption that the
battery is dead. This, combined with knowledge of how cars operate, explains the observed
nonbehavior. In most cases, we will prefer an explanation E that is minimal, meaning that
there is no proper subset of E that is also an explanation. An ATMS can generate explanations
for the “car won’t start” problem by making assumptions (such as “no gas in car” or “battery
dead”) in any order we like, even if some assumptions are contradictory. Then we look at the
label for the sentence “car won’t start” to read off the sets of assumptions that would justify
the sentence.
The exact algorithms used to implement truth maintenance systems are a little compli-
cated, and we do not cover them here. The computational complexity of the truth maintenance
problem is at least as great as that of propositional inference—that is, NP-hard. Therefore,
you should not expect truth maintenance to be a panacea. When used carefully, however, a
TMS can provide a substantial increase in the ability of a logical system to handle complex
environments and hypotheses.
Summary
By delving into the details of how one represents a variety of knowledge, we hope we have
given the reader a sense of how real knowledge bases are constructed and a feeling for the
interesting philosophical issues that arise. The major points are as follows:
• Large-scale knowledge representation requires a general-purpose ontology to organize
and tie together the various speciﬁc domains of knowledge.
• A general-purpose ontology needs to cover a wide variety of knowledge and should be
capable, in principle, of handling any domain.
• Building a large, general-purpose ontology is a signiﬁcant challenge that has yet to be
fully realized, although current frameworks seem to be quite robust.
• We presented an upper ontology based on categories and the event calculus.
We
covered categories, subcategories, parts, structured objects, measurements, substances,
events, time and space, change, and beliefs.
• Natural kinds cannot be deﬁned completely in logic, but properties of natural kinds can
be represented.
• Actions, events, and time can be represented with the event calculus. Such represen-
tations enable an agent to construct sequences of actions and make logical inferences
about what will be true when these actions happen.
• Special-purpose representation systems, such as semantic networks and description
logics, have been devised to help in organizing a hierarchy of categories. Inheritance
is an important form of inference, allowing the properties of objects to be deduced from
their membership in categories.
