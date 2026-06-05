---
chunk_id: "book-ca4fca8dd8-chunk-1235"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1235
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 745

Section 20.1
A Logical Formulation of Learning
745
This region all inconsistent
This region all inconsistent
More general
More specific
S1
G1
S2
G2
G3
 . . . 
Gm
 . . .
Sn
Figure 20.4 The version space contains all hypotheses consistent with the examples.
• The current version space is the set of hypotheses consistent with all the examples so
far. It is represented by the S-set and G-set, each of which is a set of hypotheses.
• Every member of the S-set is consistent with all observations so far, and there are no
consistent hypotheses that are more speciﬁc.
• Every member of the G-set is consistent with all observations so far, and there are no
consistent hypotheses that are more general.
We want the initial version space (before any examples have been seen) to represent all pos-
sible hypotheses. We do this by setting the G-set to contain True (the hypothesis that contains
everything), and the S-set to contain False (the hypothesis whose extension is empty).
Figure 20.4 shows the general structure of the boundary-set representation of the version
space. To show that the representation is sufﬁcient, we need the following two properties:
1. Every consistent hypothesis (other than those in the boundary sets) is more speciﬁc than
some member of the G-set, and more general than some member of the S-set. (That is,
there are no “stragglers” left outside.) This follows directly from the deﬁnitions of S
and G. If there were a straggler h, then it would have to be no more speciﬁc than any
member of G, in which case it belongs in G; or no more general than any member of S,
in which case it belongs in S.
2. Every hypothesis more speciﬁc than some member of the G-set and more general than
some member of the S-set is a consistent hypothesis. (That is, there are no “holes”
between the boundaries.) Any h between S and G must reject all the negative examples
rejected by each member of G (because it is more speciﬁc), and must accept all the pos-
itive examples accepted by any member of S (because it is more general). Thus, h must
agree with all the examples, and therefore cannot be inconsistent. Figure 20.5 shows

## Page 746
