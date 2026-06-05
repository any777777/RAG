---
chunk_id: "book-ca4fca8dd8-chunk-0383"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 383
confidence: "first-pass"
extraction_method: "structured-local"
---

234
Chapter 7
Logical Agents
Follows
Sentences
Sentence
Entails
Semantics
Semantics
Representation
World
Aspects of the
    real world
Aspect of the
   real world
Figure 7.6 Sentences are physical conﬁgurations of the agent, and reasoning is a process of
constructing new physical conﬁgurations from old ones. Logical reasoning should ensure that
the new conﬁgurations represent aspects of the world that actually follow from the aspects
that the old conﬁgurations represent.
In understanding entailment and inference, it might help to think of the set of all conse-
quences of KB as a haystack and of α as a needle. Entailment is like the needle being in the
haystack; inference is like ﬁnding it. This distinction is embodied in some formal notation: if
an inference algorithm i can derive α from KB, we write
KB ⊢i α,
which is pronounced “α is derived from KB by i” or “i derives α from KB.”
An inference algorithm that derives only entailed sentences is called sound or truth-
Sound
preserving. Soundness is a highly desirable property. An unsound inference procedure es-
Truth-preserving
sentially makes things up as it goes along—it announces the discovery of nonexistent needles.
It is easy to see that model checking, when it is applicable,5 is a sound procedure.
The property of completeness is also desirable: an inference algorithm is complete if
Completeness
it can derive any sentence that is entailed. For real haystacks, which are ﬁnite in extent,
it seems obvious that a systematic examination can always decide whether the needle is in
the haystack. For many knowledge bases, however, the haystack of consequences is inﬁnite,
and completeness becomes an important issue.6 Fortunately, there are complete inference
procedures for logics that are sufﬁciently expressive to handle many knowledge bases.
We have described a reasoning process whose conclusions are guaranteed to be true in
any world in which the premises are true; in particular, if KB is true in the real world, then any
▶
sentence α derived from KB by a sound inference procedure is also true in the real world. So,
while an inference process operates on “syntax”—internal physical conﬁgurations such as
bits in registers or patterns of electrical blips in brains—the process corresponds to the real-
world relationship whereby some aspect of the real world is the case by virtue of other aspects
of the real world being the case.7 This correspondence between world and representation is
illustrated in Figure 7.6.
The ﬁnal issue to consider is grounding—the connection between logical reasoning pro-
Grounding
cesses and the real environment in which the agent exists. In particular, how do we know that
▶
5
Model checking works if the space of models is ﬁnite—for example, in wumpus worlds of ﬁxed size. For
arithmetic, on the other hand, the space of models is inﬁnite: even if we restrict ourselves to the integers, there
are inﬁnitely many pairs of values for x and y in the sentence x+y = 4.
6
Compare with the case of inﬁnite search spaces in Chapter 3, where depth-ﬁrst search is not complete.
7
As Wittgenstein (1922) put it in his famous Tractatus: “The world is everything that is the case.”
