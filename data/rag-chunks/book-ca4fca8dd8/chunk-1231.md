---
chunk_id: "book-ca4fca8dd8-chunk-1231"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1231
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 742

742
Chapter 20
Knowledge in Learning
(a)
(b)
(c)
(d)
(e)
+
+
+
+
+
++
–
–
–
–
–
–
–
– –
–
+
+
+
+
+
++
–
–
–
–
–
–
–
– –
–
+
+
+
+
+
+
++
–
–
–
–
–
–
–
– –
–
+
+
+
+
+
+
++
–
–
–
–
–
–
–
–
–
+
–
+
+
+
+
+
++
–
–
–
–
–
–
–
–
–
+
–
–
Figure 20.1 (a) A consistent hypothesis. (b) A false negative. (c) The hypothesis is general-
ized. (d) A false positive. (e) The hypothesis is specialized.
function CURRENT-BEST-LEARNING(examples,h) returns a hypothesis or fail
if examples is empty then
return h
e←FIRST(examples)
if e is consistent with h then
return CURRENT-BEST-LEARNING(REST(examples), h)
else if e is a false positive for h then
for each h′ in specializations of h consistent with examples seen so far do
h′′ ←CURRENT-BEST-LEARNING(REST(examples), h′)
if h′′ ̸= fail then return h′′
else if e is a false negative for h then
for each h′ in generalizations of h consistent with examples seen so far do
h′′ ←CURRENT-BEST-LEARNING(REST(examples), h′)
if h′′ ̸= fail then return h′′
return fail
Figure 20.2 The current-best-hypothesis learning algorithm.
It searches for a consis-
tent hypothesis that ﬁts all the examples and backtracks when no consistent specializa-
tion/generalization can be found. To start the algorithm, any hypothesis can be passed in;
it will be specialized or gneralized as needed.
We have deﬁned generalization and specialization as operations that change the extension
of a hypothesis. Now we need to determine exactly how they can be implemented as syntactic
operations that change the candidate deﬁnition associated with the hypothesis, so that a pro-
gram can carry them out. This is done by ﬁrst noting that generalization and specialization
are also logical relationships between hypotheses. If hypothesis h1, with deﬁnition C1, is a
generalization of hypothesis h2 with deﬁnition C2, then we must have
∀x C2(x) ⇒C1(x) .
Therefore in order to construct a generalization of h2, we simply need to ﬁnd a deﬁnition C1
that is logically implied by C2. This is easily done. For example, if C2(x) is Alternate(x) ∧

## Page 743
