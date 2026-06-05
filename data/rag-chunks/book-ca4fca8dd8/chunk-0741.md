---
chunk_id: "book-ca4fca8dd8-chunk-0741"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 741
confidence: "first-pass"
extraction_method: "structured-local"
---

448
Chapter 13
Probabilistic Reasoning
13.3.2 The variable elimination algorithm
The enumeration algorithm can be improved substantially by eliminating repeated calcula-
tions of the kind illustrated in Figure 13.10. The idea is simple: do the calculation once
and save the results for later use. This is a form of dynamic programming. There are sev-
eral versions of this approach; we present the variable elimination algorithm, which is the
Variable elimination
simplest. Variable elimination works by evaluating expressions such as Equation (13.5) in
right-to-left order (that is, bottom up in Figure 13.10). Intermediate results are stored, and
summations over each variable are done only for those portions of the expression that depend
on the variable.
Let us illustrate this process for the burglary network. We evaluate the expression
P(B| j,m) = α P(B)
|{z}
f1(B)
∑
e
P(e)
|{z}
f2(E)
∑
a
P(a|B,e)
|
{z
}
f3(A,B,E)
P(j|a)
| {z }
f4(A)
P(m|a)
| {z }
f5(A)
.
Notice that we have annotated each part of the expression with the name of the corresponding
factor; each factor is a matrix indexed by the values of its argument variables. For example,
Factor
the factors f4(A) and f5(A) corresponding to P(j|a) and P(m|a) depend just on A because J
and M are ﬁxed by the query. They are therefore two-element vectors:
f4(A) =
 P(j|a)
P(j|¬a)

=
 0.90
0.05

f5(A) =
 P(m|a)
P(m|¬a)

=
 0.70
0.01

.
f3(A,B,E) will be a 2×2×2 matrix, which is hard to show on the printed page. (The “ﬁrst”
element is given by P(a|b,e)=0.95 and the “last” by P(¬a|¬b,¬e)=0.999.) In terms of
factors, the query expression is written as
P(B| j,m) = αf1(B)× ∑
e
f2(E)× ∑
a
f3(A,B,E)×f4(A)×f5(A).
Here the “×” operator is not ordinary matrix multiplication but instead the pointwise product
Pointwise product
operation, to be described shortly.
The evaluation process sums out variables (right to left) from pointwise products of fac-
tors to produce new factors, eventually yielding a factor that constitutes the solution—that is,
the posterior distribution over the query variable. The steps are as follows:
• First, we sum out A from the product of f3, f4, and f5. This gives us a new 2×2 factor
f6(B,E) whose indices range over just B and E:
f6(B,E) = ∑
a
f3(A,B,E)×f4(A)×f5(A)
= (f3(a,B,E)×f4(a)×f5(a))+(f3(¬a,B,E)×f4(¬a)×f5(¬a)).
Now we are left with the expression
P(B| j,m) = αf1(B)× ∑
e
f2(E)×f6(B,E).
• Next, we sum out E from the product of f2 and f6:
f7(B) = ∑
e
f2(E)×f6(B,E)
= f2(e)×f6(B,e)+f2(¬e)×f6(B,¬e).
This leaves the expression
P(B| j,m) = αf1(B)×f7(B)
which can be evaluated by taking the pointwise product and normalizing the result.
