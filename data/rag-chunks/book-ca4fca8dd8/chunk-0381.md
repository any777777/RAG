---
chunk_id: "book-ca4fca8dd8-chunk-0381"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 381
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 7.3
Logic
233
1
2
3
1
2
PIT
1
2
3
1
2
PIT
1
2
3
1
2
PIT
PIT
PIT
1
2
3
1
2
PIT
PIT
1
2
3
1
2
PIT
1
2
3
1
2
PIT
PIT
1
2
3
1
2
PIT
PIT
1
2
3
1
2
1
2
3
1
2
PIT
1
2
3
1
2
PIT
PIT
1
2
3
1
2
PIT
KB
a1
B
r
eez
e
 
B
r
eez
e
 
B
r
eez
e
 
B
r
eez
e
 
B
r
eez
e
 
B
r
eez
e
 
B
r
eez
e
 
B
r
eez
e
 
(a)
1
2
3
1
2
PIT
1
2
3
1
2
PIT
PIT
PIT
1
2
3
PIT
1
2
3
1
2
PIT
PIT
1
2
3
1
2
PIT
PIT
1
2
3
1
2
KB
B
r
eez
e
a2
B
r
eez
e
B
r
eez
e
B
r
eez
e
B
r
eez
e
1
2
3
1
2
PIT
1
2
3
1
2
PIT
PIT
B
r
eez
e
B
r
eez
e
1
2
B
r
eez
e
1
2
3
1
2
PIT
1
2
3
1
2
3
1
2
PIT
PIT
1
2
3
1
2
α2
B
r
e
r
ez
e
B
r
e
r
ez
e
B
r
e
r
ez
e
1
2
B
r
e
r
ez
e
(b)
Figure 7.5 Possible models for the presence of pits in squares [1,2], [2,2], and [3,1]. The
KB corresponding to the observations of nothing in [1,1] and a breeze in [2,1] is shown by
the solid line. (a) Dotted line shows models of α1 (no pit in [1,2]). (b) Dotted line shows
models of α2 (no pit in [2,2]).
not contain a pit, so (ignoring other aspects of the world for now) there are 23 =8 possible
models. These eight models are shown in Figure 7.5.3
The KB can be thought of as a set of sentences or as a single sentence that asserts all
the individual sentences. The KB is false in models that contradict what the agent knows—
for example, the KB is false in any model in which [1,2] contains a pit, because there is
no breeze in [1,1]. There are in fact just three models in which the KB is true, and these are
shown surrounded by a solid line in Figure 7.5. Now let us consider two possible conclusions:
α1 = “There is no pit in [1,2].”
α2 = “There is no pit in [2,2].”
We have surrounded the models of α1 and α2 with dotted lines in Figures 7.5(a) and 7.5(b),
respectively. By inspection, we see the following:
in every model in which KB is true, α1 is also true.
Hence, KB |= α1: there is no pit in [1,2]. We can also see that
in some models in which KB is true, α2 is false.
Hence, KB does not entail α2: the agent cannot conclude that there is no pit in [2,2]. (Nor
can it conclude that there is a pit in [2,2].)4
The preceding example not only illustrates entailment but also shows how the deﬁnition
of entailment can be applied to derive conclusions—that is, to carry out logical inference.
Logical inference
The inference algorithm illustrated in Figure 7.5 is called model checking, because it enu-
Model checking
merates all possible models to check that α is true in all models in which KB is true, that is,
that M(KB) ⊆M(α).
3
Although the ﬁgure shows the models as partial wumpus worlds, they are really nothing more than assignments
of true and false to the sentences “there is a pit in [1,2]” etc. Models, in the mathematical sense, do not need to
have ’orrible ’airy wumpuses in them.
4
The agent can calculate the probability that there is a pit in [2,2]; Chapter 12 shows how.
