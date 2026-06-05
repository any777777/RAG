---
chunk_id: "book-ca4fca8dd8-chunk-0739"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 739
confidence: "first-pass"
extraction_method: "structured-local"
---

446
Chapter 13
Probabilistic Reasoning
Now, a Bayes net gives a complete representation of the full joint distribution. More speciﬁ-
cally, Equation (13.2) on page 433 shows that the terms P(x,e,y) in the joint distribution can
be written as products of conditional probabilities from the network. Therefore, a query can
▶
be answered using a Bayes net by computing sums of products of conditional probabilities
from the network.
Consider the query P(Burglary|JohnCalls=true,MaryCalls=true). The hidden vari-
ables for this query are Earthquake and Alarm. From Equation (12.9), using initial letters for
the variables to shorten the expressions, we have
P(B| j,m) = αP(B, j,m) = α ∑
e ∑
a
P(B, j,m,e,a).
The semantics of Bayes nets (Equation (13.2)) then gives us an expression in terms of CPT
entries. For simplicity, we do this just for Burglary=true:
P(b| j,m) = α ∑
e ∑
a
P(b)P(e)P(a|b,e)P(j|a)P(m|a).
(13.4)
To compute this expression, we have to add four terms, each computed by multiplying ﬁve
numbers. In the worst case, where we have to sum out almost all the variables, there will be
O(2n) terms in the sum, each a product of O(n) probability values. A naive implementation
would therefore have complexity O(n2n).
This can be reduced to O(2n) by taking advantage of the nested structure of the compu-
tation. In symbolic terms, this means moving the summations inwards as far as possible in
expressions such as Equation (13.4). We can do this because not all the factors in the product
of probabilities depend on all the variables. Thus we have
P(b| j,m) = αP(b)∑
e
P(e)∑
a
P(a|b,e)P(j|a)P(m|a).
(13.5)
This expression can be evaluated by looping through the variables in order, multiplying CPT
entries as we go. For each summation, we also need to loop over the variable’s possible val-
ues. The structure of this computation is shown as a tree in Figure 13.10. Using the numbers
from Figure 13.2, we obtain P(b| j,m) = α×0.00059224. The corresponding computation
for ¬b yields α×0.0014919; hence,
P(B| j,m) = α⟨0.00059224,0.0014919⟩≈⟨0.284,0.716⟩.
That is, the chance of a burglary, given calls from both neighbors, is about 28%.
The ENUMERATION-ASK algorithm in Figure 13.11 evaluates these expression trees us-
ing depth-ﬁrst, left-to-right recursion. The algorithm is very similar in structure to the back-
tracking algorithm for solving CSPs (Figure 5.5) and the DPLL algorithm for satisﬁability
(Figure 7.17). Its space complexity is only linear in the number of variables: the algorithm
sums over the full joint distribution without ever constructing it explicitly. Unfortunately, its
time complexity for a network with n Boolean variables (not counting the evidence variables)
is always O(2n)—better than the O(n2n) for the simple approach described earlier, but still
rather grim. For the insurance network in Figure 13.9, which is relatively small, exact infer-
ence using enumeration requires around 227 million arithmetic operations for a typical query
on the cost variables.
If you look carefully at the tree in Figure 13.10, however, you will see that it contains
repeated subexpressions. The products P(j|a)P(m|a) and P(j|¬a)P(m|¬a) are computed
twice, once for each value of E. The key to efﬁcient inference in Bayes nets is avoiding such
wasted computations. The next section describes a general method for doing this.
