---
chunk_id: "book-ca4fca8dd8-chunk-1227"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1227
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 20
KNOWLEDGE IN LEARNING
In which we examine the problem of learning when you know something already.
In all of the approaches to learning described in the previous chapter, the idea is to construct
a function that has the input–output behavior observed in the data. In each case, the learning
methods can be understood as searching a hypothesis space to ﬁnd a suitable function, starting
from only a very basic assumption about the form of the function, such as “second-degree
polynomial” or “decision tree” and perhaps a preference for simpler hypotheses. Doing this
amounts to saying that before you can learn something new, you must ﬁrst forget (almost)
everything you know. In this chapter, we study learning methods that can take advantage
of prior knowledge about the world. In most cases, the prior knowledge is represented
Prior knowledge
as general ﬁrst-order logical theories; thus for the ﬁrst time we bring together the work on
knowledge representation and learning.
20.1 A Logical Formulation of Learning
Chapter 19 deﬁned pure inductive learning as a process of ﬁnding a hypothesis that agrees
with the observed examples. Here, we specialize this deﬁnition to the case where the hypoth-
esis is represented by a set of logical sentences. Example descriptions and classiﬁcations will
also be logical sentences, and a new example can be classiﬁed by inferring a classiﬁcation
sentence from the hypothesis and the example description. This approach allows for incre-
mental construction of hypotheses, one sentence at a time. It also allows for prior knowledge,
because sentences that are already known can assist in the classiﬁcation of new examples.
The logical formulation of learning may seem like a lot of extra work at ﬁrst, but it turns
out to clarify many of the issues in learning. It enables us to go well beyond the simple
learning methods of Chapter 19 by using the full power of logical inference in the service of
learning.
20.1.1 Examples and hypotheses
Recall from Chapter 19 the restaurant learning problem: learning a rule for deciding whether
to wait for a table. Examples were described by attributes such as Alternate, Bar, Fri/Sat,
and so on. In a logical setting, an example is described by a logical sentence; the attributes
become unary predicates. Let us generically call the ith example Xi. For instance, the ﬁrst
example from Figure 19.3 (page 676) is described by the sentences
Alternate(X1)∧¬Bar(X1)∧¬Fri/Sat(X1)∧Hungry(X1)∧...

## Page 740
