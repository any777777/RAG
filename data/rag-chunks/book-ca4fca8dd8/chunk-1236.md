---
chunk_id: "book-ca4fca8dd8-chunk-1236"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1236
confidence: "first-pass"
extraction_method: "structured-local"
---

746
Chapter 20
Knowledge in Learning
+
+
+
+
+
+
+
+
+
+
–
–
–
–
–
–
–
–
–
–
–
–
–
–
S1
G1
G2
Figure 20.5 The extensions of the members of G and S. No known examples lie in between
the two sets of boundaries.
the situation: there are no known examples outside S but inside G, so any hypothesis in
the gap must be consistent.
We have therefore shown that if S and G are maintained according to their deﬁnitions, then
they provide a satisfactory representation of the version space. The only remaining problem
is how to update S and G for a new example (the job of the VERSION-SPACE-UPDATE func-
tion). This may appear rather complicated at ﬁrst, but from the deﬁnitions and with the help
of Figure 20.4, it is not too hard to reconstruct the algorithm.
We need to worry about the members Si and Gi of the S- and G-sets. For each one, the
new example may be a false positive or a false negative.
1. False positive for Si: This means Si is too general, but there are no consistent special-
izations of Si (by deﬁnition), so we throw it out of the S-set.
2. False negative for Si: This means Si is too speciﬁc, so we replace it by all its immediate
generalizations, provided they are more speciﬁc than some member of G.
3. False positive for Gi: This means Gi is too general, so we replace it by all its immediate
specializations, provided they are more general than some member of S.
4. False negative for Gi: This means Gi is too speciﬁc, but there are no consistent gener-
alizations of Gi (by deﬁnition) so we throw it out of the G-set.
We continue these operations for each new example until one of three things happens:
1. We have exactly one hypothesis left in the version space, in which case we return it as
the unique hypothesis.
2. The version space collapses—either S or G becomes empty, indicating that there are
no consistent hypotheses for the training set. This is the same case as the failure of the
simple version of the decision tree algorithm.
3. We run out of examples and have several hypotheses remaining in the version space.
This means the version space represents a disjunction of hypotheses. For any new
example, if all the disjuncts agree, then we can return their classiﬁcation of the example.
If they disagree, one possibility is to take the majority vote.
We leave as an exercise the application of the VERSION-SPACE-LEARNING algorithm to the
restaurant data.

## Page 747
