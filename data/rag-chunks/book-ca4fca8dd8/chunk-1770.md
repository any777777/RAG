---
chunk_id: "book-ca4fca8dd8-chunk-1770"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1770
confidence: "first-pass"
extraction_method: "structured-local"
---

1076
Appendix A
Mathematical Background
that solves all satisﬁability problems in polynomial time. However, AI is more interested in
whether there are algorithms that perform efﬁciently on typical problems drawn from a pre-
determined distribution; as we saw in Chapter 7, there are algorithms such as WALKSAT that
do quite well on many problems.
The class of NP-hard problems consists of those problems that are reducible (in poly-
NP-hard
nomial time) to all the problems in NP, so if you solved any NP-hard problem, you could
solve all the problems in NP. The NP-complete problems are all NP-hard, but there are some
NP-hard problems that are even harder than NP-complete.
The class co-NP is the complement of NP, in the sense that, for every decision problem
Co-NP
in NP, there is a corresponding problem in co-NP with the “yes” and “no” answers reversed.
We know that P is a subset of both NP and co-NP, and it is believed that there are problems
in co-NP that are not in P. The co-NP-complete problems are the hardest problems in co-NP.
Co-NP-complete
The class #P (pronounced “number P” according to Garey and Johnson (1979), but often
pronounced “sharp P”) is the set of counting problems corresponding to the decision problems
in NP. Decision problems have a yes-or-no answer: is there a solution to this 3-SAT formula?
Counting problems have an integer answer: how many solutions are there to this 3-SAT
formula? In some cases, the counting problem is much harder than the decision problem.
For example, deciding whether a bipartite graph has a perfect matching can be done in time
O(VE) (where the graph has V vertices and E edges), but the counting problem “how many
perfect matches does this bipartite graph have” is #P-complete, meaning that it is hard as any
problem in #P and thus at least as hard as any NP problem.
Another class is the class of PSPACE problems—those that require a polynomial amount
of space, even on a nondeterministic machine. It is believed that PSPACE-hard problems are
worse than NP-complete problems, although it could turn out that NP = PSPACE, just as it
could turn out that P = NP.
A.2 Vectors, Matrices, and Linear Algebra
Mathematicians deﬁne a vector as a member of a vector space, but we will use a more con-
Vector
crete deﬁnition: a vector is an ordered sequence of values. For example, in two-dimensional
space, we have vectors such as x=⟨3,4⟩and y=⟨0,2⟩. We follow the convention of boldface
characters for vector names, although some authors use arrows or bars over the names: ⃗x or
¯y. The elements of a vector can be accessed using subscripts: z=⟨z1,z2,...,zn⟩. One con-
fusing point: this book is synthesizing work from many subﬁelds, which variously call their
sequences vectors, lists, or tuples, and variously use the notations ⟨1,2⟩, [1, 2], or (1, 2).
The two fundamental operations on vectors are vector addition and scalar multiplication.
The vector addition x + y is the elementwise sum: x + y=⟨3 + 0,4 + 2⟩=⟨3,6⟩. Scalar
multiplication multiplies each element by a constant: 5x=⟨5×3,5×4⟩=⟨15,20⟩.
The length of a vector is denoted |x| and is computed by taking the square root of the
sum of the squares of the elements: |x|=
p
(32 +42)=5. The dot product x · y (also called
scalar product) of two vectors is the sum of the products of corresponding elements, that is,
x·y= ∑i xiyi, or in our particular case, x·y=3×0+4×2=8.
Vectors are often interpreted as directed line segments (arrows) in an n-dimensional Eu-
clidean space. Vector addition is then equivalent to placing the tail of one vector at the head
of the other, and the dot product x·y is |x||y| cosθ, where θ is the angle between x and y.
