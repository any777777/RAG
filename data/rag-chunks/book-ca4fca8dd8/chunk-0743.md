---
chunk_id: "book-ca4fca8dd8-chunk-0743"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 743
confidence: "first-pass"
extraction_method: "structured-local"
---

450
Chapter 13
Probabilistic Reasoning
function ELIMINATION-ASK(X,e,bn) returns a distribution over X
inputs: X, the query variable
e, observed values for variables E
bn, a Bayesian network with variables vars
factors←[]
for each V in ORDER(vars) do
factors←[MAKE-FACTOR(V,e)] + factors
if V is a hidden variable then factors←SUM-OUT(V,factors)
return NORMALIZE(POINTWISE-PRODUCT(factors))
Figure 13.13 The variable elimination algorithm for exact inference in Bayes nets.
This is potentially much more efﬁcient than computing the larger pointwise product h ﬁrst
and then summing X out from that.
Notice that matrices are not multiplied until we need to sum out a variable from the
accumulated product. At that point, we multiply just those matrices that include the variable
to be summed out. Given functions for pointwise product and summing out, the variable
elimination algorithm itself can be written quite simply, as shown in Figure 13.13.
Variable ordering and variable relevance
The algorithm in Figure 13.13 includes an unspeciﬁed ORDER function to choose an ordering
for the variables. Every choice of ordering yields a valid algorithm, but different orderings
cause different intermediate factors to be generated during the calculation. For example, in
the calculation shown previously, we eliminated A before E; if we do it the other way, the
calculation becomes
P(B| j,m) = αf1(B)× ∑
a
f4(A)×f5(A)× ∑
e
f2(E)×f3(A,B,E),
during which a new factor f6(A,B) will be generated.
In general, the time and space requirements of variable elimination are dominated by
the size of the largest factor constructed during the operation of the algorithm. This in turn
is determined by the order of elimination of variables and by the structure of the network.
It turns out to be intractable to determine the optimal ordering, but several good heuristics
are available. One fairly effective method is a greedy one: eliminate whichever variable
minimizes the size of the next factor to be constructed.
Let us consider one more query: P(JohnCalls|Burglary=true). As usual (see Equa-
tion (13.5)), the ﬁrst step is to write out the nested summation:
P(J |b) = αP(b)∑
e
P(e)∑
a
P(a|b,e)P(J |a)∑
m
P(m|a).
Evaluating this expression from right to left, we notice something interesting: ∑m P(m|a) is
equal to 1 by deﬁnition! Hence, there was no need to include it in the ﬁrst place; the vari-
able M is irrelevant to this query. Another way of saying this is that the result of the query
P(JohnCalls|Burglary=true) is unchanged if we remove MaryCalls from the network alto-
gether. In general, we can remove any leaf node that is not a query variable or an evidence
