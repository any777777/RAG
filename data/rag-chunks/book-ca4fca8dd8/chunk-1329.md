---
chunk_id: "book-ca4fca8dd8-chunk-1329"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1329
confidence: "first-pass"
extraction_method: "structured-local"
---

812
Chapter 22
Deep Learning
5
6
6
2
5
6
5
5
9
4
+1
–1
+1
+1
–1
+1
+1
–1
+1
Figure 22.4 An example of a one-dimensional convolution operation with a kernel of size
l =3 and a stride s=2. The peak response is centered on the darker (lower intensity) input
pixel. The results would usually be fed through a nonlinear activation function (not shown)
before going to the next hidden layer.
dimensional image, and a vector kernel k of size l. (For simplicity we will assume that l is an
odd number.) All the ideas carry over straightforwardly to higher-dimensional cases.
We write the convolution operation using the ∗symbol, for example: z = x ∗k. The
operation is deﬁned as follows:
zi =
l
∑
j=1
kjxj+i−(l+1)/2 .
(22.8)
In other words, for each output position i, we take the dot product between the kernel k and a
snippet of x centered on xi with width l.
The process is illustrated in Figure 22.4 for a kernel vector [+1,−1,+1], which detects
a darker point in the 1D image. (The 2D version might detect a darker line.) Notice that in
this example the pixels on which the kernels are centered are separated by a distance of 2
pixels; we say the kernel is applied with a stride s=2. Notice that the output layer has fewer
Stride
pixels: because of the stride, the number of pixels is reduced from n to roughly n/s. (In two
dimensions, the number of pixels would be roughly n/sxsy, where sx and sy are the strides in
the x and y directions in the image.) We say “roughly” because of what happens at the edge
of the image: in Figure 22.4 the convolution stops at the edges of the image, but one can also
pad the input with extra pixels (either zeroes or copies of the outer pixels) so that the kernel
can be applied exactly ⌊n/s⌋times. For small kernels, we typically use s=1, so the output
has the same dimensions as the image (see Figure 22.5).
The operation of applying a kernel across an image can be implemented in the obvious
way by a program with suitable nested loops; but it can also be formulated as a single matrix
operation, just like the application of the weight matrix in Equation (22.1). For example, the
convolution illustrated in Figure 22.4 can be viewed as the following matrix multiplication:
 +1 −1 +1
0
0
0
0
0
0
+1 −1 +1
0
0
0
0
0
0
+1 −1 +1
!









5
6
6
2
5
6
5










=
 5
9
4
!
.
(22.9)
In this weight matrix, the kernel appears in each row, shifted according to the stride relative
to the previous row, One wouldn’t necessarily construct the weight matrix explicitly—it is
