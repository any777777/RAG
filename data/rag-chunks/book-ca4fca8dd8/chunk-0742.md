---
chunk_id: "book-ca4fca8dd8-chunk-0742"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 742
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 449

Section 13.3
Exact Inference in Bayesian Networks
449
X
Y
f(X,Y)
Y
Z
g(Y,Z)
X
Y
Z
h(X,Y,Z)
t
t
.3
t
t
.2
t
t
t
.3×.2=.06
t
f
.7
t
f
.8
t
t
f
.3×.8=.24
f
t
.9
f
t
.6
t
f
t
.7×.6=.42
f
f
.1
f
f
.4
t
f
f
.7×.4=.28
f
t
t
.9×.2=.18
f
t
f
.9×.8=.72
f
f
t
.1×.6=.06
f
f
f
.1×.4=.04
Figure 13.12 Illustrating pointwise multiplication: f(X,Y)×g(Y,Z) = h(X,Y,Z).
Examining this sequence, we see that two basic computational operations are required: point-
wise product of a pair of factors, and summing out a variable from a product of factors. The
next section describes each of these operations.
Operations on factors
The pointwise product of two factors f and g yields a new factor h whose variables are the
union of the variables in f and g and whose elements are given by the product of the corre-
sponding elements in the two factors. Suppose the two factors have variables Y1,...,Yk in
common. Then we have
f(X1 ...Xj,Y1 ...Yk)×g(Y1 ...Yk,Z1,...Zℓ) = h(X1 ...Xj,Y1 ...Yk,Z1 ...Zℓ)
If all the variables are binary, then f and g have 2j+k and 2k+ℓentries, respectively, and the
pointwise product has 2j+k+ℓentries. For example, given two factors f(X,Y) and g(Y,Z),
the pointwise product f×g=h(X,Y,Z) has 21+1+1 =8 entries, as illustrated in Figure 13.12.
Notice that the factor resulting from a pointwise product can contain more variables than any
of the factors being multiplied and that the size of a factor is exponential in the number of
variables. This is where both space and time complexity arise in the variable elimination
algorithm.
Summing out a variable from a product of factors is done by adding up the submatrices
formed by ﬁxing the variable to each of its values in turn. For example, to sum out X from
h(X,Y,Z), we write
h2(Y,Z) = ∑
x
h(X,Y,Z) = h(x,Y,Z)+h(¬x,Y,Z)
=
 .06 .24
.42 .28

+
 .18 .72
.06 .04

=
 .24 .96
.48 .32

.
The only trick is to notice that any factor that does not depend on the variable to be summed
out can be moved outside the summation. For example, to sum out X from the product of f
and g, we can move g outside the summation:
∑
x
f(X,Y)×g(Y,Z) = g(Y,Z)× ∑
x
f(X,Y).

## Page 450
