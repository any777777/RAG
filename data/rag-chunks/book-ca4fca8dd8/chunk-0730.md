---
chunk_id: "book-ca4fca8dd8-chunk-0730"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 730
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 439

Section 13.2
The Semantics of Bayesian Networks
439
Cold
Flu
Malaria P(fever|·) P(¬fever|·)
f
f
f
0.0
1.0
f
f
t
0.9
0.1
f
t
f
0.8
0.2
f
t
t
0.98
0.02 = 0.2×0.1
t
f
f
0.4
0.6
t
f
t
0.94
0.06 = 0.6×0.1
t
t
f
0.88
0.12 = 0.6×0.2
t
t
t
0.988
0.012 = 0.6×0.2×0.1
Figure 13.5 A complete conditional probability table for P(Fever|Cold,Flu,Malaria), as-
suming a noisy-OR model with the the three q-values shown in bold.
are true. The noisy-OR model allows for uncertainty about the ability of each parent to cause
the child to be true—the causal relationship between parent and child may be inhibited, and
so a patient could have a cold, but not exhibit a fever.
The model makes two assumptions. First, it assumes that all the possible causes are listed.
(If some are missing, we can always add a so-called leak node that covers “miscellaneous
Leak node
causes.”) Second, it assumes that inhibition of each parent is independent of inhibition of any
other parents: for example, whatever inhibits Malaria from causing a fever is independent of
whatever inhibits Flu from causing a fever. Given these assumptions, Fever is false if and only
if all its true parents are inhibited, and the probability of this is the product of the inhibition
probabilities qj for each parent. Let us suppose these individual inhibition probabilities are
as follows:
qcold = P(¬fever|cold,¬ﬂu,¬malaria) = 0.6,
qﬂu = P(¬fever|¬cold,ﬂu,¬malaria) = 0.2,
qmalaria = P(¬fever|¬cold,¬ﬂu,malaria) = 0.1.
Then, from this information and the noisy-OR assumptions, the entire CPT can be built. The
general rule is that
P(xi | parents(Xi)) = 1−
∏
{ j:Xj =true}
qj ,
where the product is taken over the parents that are set to true for that row of the CPT.
Figure 13.5 illustrates this calculation.
In general, noisy logical relationships in which a variable depends on k parents can be
described using O(k) parameters instead of O(2k) for the full conditional probability table.
This makes assessment and learning much easier. For example, the CPCS network (Prad-
han et al., 1994) uses noisy-OR and noisy-MAX distributions to model relationships among
diseases and symptoms in internal medicine. With 448 nodes and 906 links, it requires only
8,254 parameters instead of 133,931,430 for a network with full CPTs.

## Page 440
