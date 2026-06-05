---
chunk_id: "book-ca4fca8dd8-chunk-1638"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1638
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.3
Simple Image Features
997
0
10
20
30
40
50
60
70
80
90
100
−1
0
1
2
0
10
20
30
40
50
60
70
80
90
100
−1
0
1
0
10
20
30
40
50
60
70
80
90
100
−1
0
1
Figure 27.7 Top: Intensity proﬁle I(x) along a one-dimensional section across a step edge.
Middle: The derivative of intensity, I′(x). Large values of this function correspond to edges,
but the function is noisy. Bottom: The derivative of a smoothed version of the intensity. The
noisy candidate edge at x=75 has disappeared.
there could be thermal noise in the camera; there could be scratches on the object surface that
change the surface normal at the ﬁnest scale; there could be minor variations in the surface
albedo; and so on. Each of these effects make the gradient look big, but don’t mean that an
edge is present. If we “smooth” the image ﬁrst, the spurious peaks are diminished, as we see
in Figure 27.7 (bottom).
Smoothing involves using surrounding pixels to suppress noise. We will predict the “true”
value of our pixel as a weighted sum of nearby pixels, with more weight for the closest pixels.
A natural choice of weights is a Gaussian ﬁlter. Recall that the zero-mean Gaussian function
Gaussian ﬁlter
with standard deviation σ is
Gσ(x) =
1
√
2πσe−x2/2σ2
in one dimension, or
Gσ(x,y) =
1
2πσ2 e−(x2+y2)/2σ2 in two dimensions.
Applying a Gaussian ﬁlter means replacing the intensity I(x0,y0) with the sum, over all (x,y)
pixels, of I(x,y)Gσ(d), where d is the distance from (x0,y0) to (x,y). This kind of weighted
sum is so common that there is a special name and notation for it. We say that the function h
is the convolution of two functions f and g (denoted as h = f ∗g) if we have
Convolution
h(x) =
+∞
∑
u=−∞
f(u)g(x−u)
in one dimension, or
h(x,y) =
+∞
∑
u=−∞
+∞
∑
v=−∞
f(u,v)g(x−u,y−v)
in two dimensions.

## Page 998
