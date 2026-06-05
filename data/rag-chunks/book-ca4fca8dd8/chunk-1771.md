---
chunk_id: "book-ca4fca8dd8-chunk-1771"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1771
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1077

Section A.2
Vectors, Matrices, and Linear Algebra
1077
A matrix is a rectangular array of values arranged into rows and columns. Here is a
Matrix
matrix A of size 3×4:


A1,1 A1,2 A1,3 A1,4
A2,1 A2,2 A2,3 A2,4
A3,1 A3,2 A3,3 A3,4


The ﬁrst index of Ai,j speciﬁes the row and the second the column. In programming lan-
guages, Ai,j is often written A[i,j] or A[i][j].
The sum of two matrices is deﬁned by adding their corresponding elements; for example
(A+B)i,j =Ai,j +Bi,j. (The sum is undeﬁned if A and B have different sizes.) We can also
deﬁne the multiplication of a matrix by a scalar: (cA)i,j =cAi,j. Matrix multiplication (the
product of two matrices) is more complicated. The product AB is deﬁned only if A is of size
a×b and B is of size b×c (i.e., the second matrix has the same number of rows as the ﬁrst
has columns); the result is a matrix of size a×c. If the matrices are of appropriate size, then
the result is
(AB)i,k = ∑
j
Ai,jB j,k .
Matrix multiplication is not commutative, even for square matrices: AB ̸= BA in general. It
is, however, associative: (AB)C = A(BC). Note that the dot product can be expressed in
terms of a transpose and a matrix multiplication: x·y = x⊤y.
The identity matrix I has elements Ii,j equal to 1 when i= j and equal to 0 otherwise. It
Identity matrix
has the property that AI=A for all A. The transpose of A, written A⊤is formed by turning
Transpose
rows into columns and vice versa, or, more formally, by A⊤i,j =A j,i. The inverse of a square
Inverse
matrix A is another square matrix A−1 such that A−1A=I. For a singular matrix, the inverse
Singular
does not exist. For a nonsingular matrix, it can be computed in O(n3) time.
Matrices are used to solve systems of linear equations in O(n3) time; the time is domi-
nated by inverting a matrix of coefﬁcients. Consider the following set of equations, for which
we want a solution in x, y, and z:
+2x+y−z = 8
−3x−y+2z = −11
−2x+y+2z = −3.
We can represent this system as the matrix equation Ax = b, where
A =


2
1 −1
−3 −1
2
−2
1
2

,
x =


x
y
z

,
b =


8
−11
−3

.
To solve Ax = b we multiply both sides by A−1, yielding A−1Ax = A−1b, which simpliﬁes
to x = A−1b. After inverting A and multiplying by b, we get the answer
x =


x
y
z

=


2
3
−1

.
A few more miscellaneous points: we use log(x) for the natural logarithm, loge(x). We
use argmaxx f(x) for the value of x for which f(x) is maximal.

## Page 1078
