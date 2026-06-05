---
chunk_id: "book-ca4fca8dd8-chunk-1718"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1718
confidence: "first-pass"
extraction_method: "structured-local"
---

1048
Chapter 28
Philosophy, Ethics, and Safety of AI
power. UL certiﬁcation of appliances gave consumers increased trust, and in fact UL is now
considering entering the business of product testing and certiﬁcation for AI.
Other industries have long had safety standards. For example, ISO 26262 is an interna-
tional standard for the safety of automobiles, describing how to develop, produce, operate,
and service vehicles in a safe way. The AI industry is not yet at this level of clarity, although
there are some frameworks in progress, such as IEEE P7001, a standard deﬁning ethical de-
sign for artiﬁcial intelligence and autonomous systems (Bryson and Winﬁeld, 2017). There is
ongoing debate about what kind of certiﬁcation is necessary, and to what extent it should be
done by the government, by professional organizations like IEEE, by independent certiﬁers
such as UL, or through self-regulation by the product companies.
Another aspect of trust is transparency: consumers want to know what is going on
Transparency
inside a system, and that the system is not working against them, whether due to intentional
malice, an unintentional bug, or pervasive societal bias that is recapitulated by the system. In
some cases this transparency is delivered directly to the consumer. In other cases their are
intellectual property issues that keep some aspects of the system hidden to consumers, but
open to regulators and certiﬁcation agencies.
When an AI system turns you down for a loan, you deserve an explanation. In Europe,
the GDPR enforces this for you. An AI system that can explain itself is called explainable AI
(XAI). A good explanation has several properties: it should be understandable and convincing
Explainable AI (XAI)
to the user, it should accurately reﬂect the reasoning of the system, it should be complete, and
it should be speciﬁc in that different users with different conditions or different outcomes
should get different explanations.
It is quite easy to give a decision algorithm access to its own deliberative processes,
simply by recording them and making them available as data structures. This means that
machines may eventually be able to give better explanations of their decisions than humans
can. Moreover, we can take steps to certify that the machine’s explanations are not deceptions
(intentional or self-deception), something that is more difﬁcult with a human.
An explanation is a helpful but not sufﬁcient ingredient to trust. One issue is that expla-
nations are not decisions: they are stories about decisions. As discussed in Section 19.9.4, we
say that a system is interpretable if we can inspect the source code of the model and see what
it is doing, and we say it is explainable if we can make up a story about what it is doing—even
if the system itself is an uninterpretable black box. To explain an uninterpretable black box,
we need to build, debug, and test a separate explanation system, and make sure it is in sync
with the original system. And because humans love a good story, we are all too willing to be
swayed by an explanation that sounds good. Take any political controversy of the day, and
you can always ﬁnd two so-called experts with diametrically opposed explanations, both of
which are internally consistent.
A ﬁnal issue is that an explanation about one case does not give you a summary over
other cases. If the bank explains, “Sorry, you didn’t get the loan because you have a history
of previous ﬁnancial problems,” you don’t know if that explanation is accurate or if the bank is
secretly biased against you for some reason. In this case, you require not just an explanation,
but also an audit of past decisions, with aggregated statistics across various demographic
groups, to see if their approval rates are balanced.
Part of transparency is knowing whether you are interacting with an AI system or a hu-
man. Toby Walsh (2015) proposed that “an autonomous system should be designed so that
