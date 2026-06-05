---
chunk_id: "book-ca4fca8dd8-chunk-0579"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 579
confidence: "first-pass"
extraction_method: "structured-local"
---

352
Chapter 10
Knowledge Representation
assumption. The idea is to specify particular predicates that are assumed to be “as false as
possible”—that is, false for every object except those for which they are known to be true.
For example, suppose we want to assert the default rule that birds ﬂy. We would introduce a
predicate, say Abnormal1(x), and write
Bird(x)∧¬Abnormal1(x) ⇒Flies(x).
If we say that Abnormal1 is to be circumscribed, a circumscriptive reasoner is entitled to
assume ¬Abnormal1(x) unless Abnormal1(x) is known to be true. This allows the conclusion
Flies(Tweety) to be drawn from the premise Bird(Tweety), but the conclusion no longer holds
if Abnormal1(Tweety) is asserted.
Circumscription can be viewed as an example of a model preference logic. In such
Model preference
logics, a sentence is entailed (with default status) if it is true in all preferred models of the KB,
as opposed to the requirement of truth in all models in classical logic. For circumscription,
one model is preferred to another if it has fewer abnormal objects.9 Let us see how this idea
works in the context of multiple inheritance in semantic networks. The standard example for
which multiple inheritance is problematic is called the “Nixon diamond.” It arises from the
observation that Richard Nixon was both a Quaker (and hence by default a paciﬁst) and a
Republican (and hence by default not a paciﬁst). We can write this as follows:
Republican(Nixon)∧Quaker(Nixon).
Republican(x)∧¬Abnormal2(x) ⇒¬Paciﬁst(x).
Quaker(x)∧¬Abnormal3(x) ⇒Paciﬁst(x).
If we circumscribe Abnormal2 and Abnormal3, there are two preferred models: one in which
Abnormal2(Nixon) and Paciﬁst(Nixon) are true and one in which Abnormal3(Nixon) and
¬Paciﬁst(Nixon) are true. Thus, the circumscriptive reasoner remains properly agnostic as
to whether Nixon was a paciﬁst. If we wish, in addition, to assert that religious beliefs take
precedence over political beliefs, we can use a formalism called prioritized circumscription
Prioritized
circumscription
to give preference to models where Abnormal3 is minimized.
Default logic is a formalism in which default rules can be written to generate contingent,
Default logic
Default rules
nonmonotonic conclusions. A default rule looks like this:
Bird(x) : Flies(x)/Flies(x).
This rule means that if Bird(x) is true, and if Flies(x) is consistent with the knowledge base,
then Flies(x) may be concluded by default. In general, a default rule has the form
P : J1,...,Jn/C
where P is called the prerequisite, C is the conclusion, and Ji are the justiﬁcations—if any one
of them can be proven false, then the conclusion cannot be drawn. Any variable that appears
in Ji or C must also appear in P. The Nixon-diamond example can be represented in default
logic with one fact and two default rules:
Republican(Nixon)∧Quaker(Nixon).
Republican(x) : ¬Paciﬁst(x)/¬Paciﬁst(x).
Quaker(x) : Paciﬁst(x)/Paciﬁst(x).
9
For the closed-world assumption, one model is preferred to another if it has fewer true atoms—that is, preferred
models are minimal models. There is a natural connection between the closed-world assumption and deﬁnite-
clause KBs, because the ﬁxed point reached by forward chaining on deﬁnite-clause KBs is the unique minimal
model. See page 249 for more on this point.
