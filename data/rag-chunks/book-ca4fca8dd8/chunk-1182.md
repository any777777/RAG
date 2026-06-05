---
chunk_id: "book-ca4fca8dd8-chunk-1182"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1182
confidence: "first-pass"
extraction_method: "structured-local"
---

712
Chapter 19
Learning from Examples
vector α we can get back to w with the equation w= ∑j αjyjxj, or we can stay in the dual
representation. There are three important properties of Equation (19.10). First, the expres-
sion is convex; it has a single global maximum that can be found efﬁciently. Second, the data
▶
enter the expression only in the form of dot products of pairs of points. This second property
is also true of the equation for the separator itself; once the optimal αj have been calculated,
the equation is11
h(x) = sign
 
∑
j
αjyj(x·xj)−b
!
.
(19.11)
A ﬁnal important property is that the weights αj associated with each data point are zero ex-
cept for the support vectors—the points closest to the separator. (They are called “support”
Support vector
vectors because they “hold up” the separating plane.) Because there are usually many fewer
support vectors than examples, SVMs gain some of the advantages of parametric models.
What if the examples are not linearly separable? Figure 19.22(a) shows an input space
deﬁned by attributes x=(x1,x2), with positive examples (y= +1) inside a circular region and
negative examples (y= −1) outside. Clearly, there is no linear separator for this problem.
Now, suppose we re-express the input data—that is, we map each input vector x to a new
vector of feature values, F(x). In particular, let us use the three features
f1 =x2
1 ,
f2 =x2
2 ,
f3 =
√
2x1x2 .
(19.12)
We will see shortly where these came from, but for now, just look at what happens. Fig-
ure 19.22(b) shows the data in the new, three-dimensional space deﬁned by the three features;
the data are linearly separable in this space! This phenomenon is actually fairly general: if
data are mapped into a space of sufﬁciently high dimension, then they will almost always be
linearly separable—if you look at a set of points from enough directions, you’ll ﬁnd a way to
make them line up. Here, we used only three dimensions;12 Exercise 19.SVME asks you to
show that four dimensions sufﬁce for linearly separating a circle anywhere in the plane (not
just at the origin), and ﬁve dimensions sufﬁce to linearly separate any ellipse. In general (with
some special cases excepted) if we have N data points then they will always be separable in
spaces of N −1 dimensions or more (Exercise 19.EMBE).
Now, we would not usually expect to ﬁnd a linear separator in the input space x, but
we can ﬁnd linear separators in the high-dimensional feature space F(x) simply by replacing
xj ·xk in Equation (19.10) with F(xj)·F(xk). This by itself is not remarkable—replacing x by
F(x) in any learning algorithm has the required effect—but the dot product has some special
properties. It turns out that F(xj) · F(xk) can often be computed without ﬁrst computing F
for each point. In our three-dimensional feature space deﬁned by Equation (19.12), a little bit
of algebra shows that
F(xj)·F(xk) = (xj ·xk)2 .
(That’s why the
√
2 is in f3.) The expression (xj · xk)2 is called a kernel function,13 and
Kernel function
is usually written as K(xj,xk). The kernel function can be applied to pairs of input data to
11 The function sign(x) returns +1 for a positive x, −1 for a negative x.
12 The reader may notice that we could have used just f1 and f2, but the 3D mapping illustrates the idea better.
13 This usage of “kernel function” is slightly different from the kernels in locally weighted regression. Some
SVM kernels are distance metrics, but not all are.
