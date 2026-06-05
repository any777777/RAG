---
chunk_id: "book-ca4fca8dd8-chunk-1181"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1181
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 711

Section 19.7
Nonparametric Models
711
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 0.2
 0.4
 0.6
 0.8
 1
 0
 0.2
 0.4
 0.6
 0.8
 1
(a)
(b)
Figure 19.21 Support vector machine classiﬁcation: (a) Two classes of points (orange open
and green ﬁlled circles) and three candidate linear separators. (b) The maximum margin
separator (heavy line), is at the midpoint of the margin (area between dashed lines). The
support vectors (points with large black circles) are the examples closest to the separator;
here there are three.
from the same distribution as the previously seen examples, there are some arguments from
computational learning theory (Section 19.5) suggesting that we minimize generalization loss
by choosing the separator that is farthest away from the examples we have seen so far. We
call this separator, shown in Figure 19.21(b) the maximum margin separator. The margin
Maximum margin
separator
Margin
is the width of the area bounded by dashed lines in the ﬁgure—twice the distance from the
separator to the nearest example point.
Now, how do we ﬁnd this separator? Before showing the equations, some notation: Tra-
ditionally SVMs use the convention that class labels are +1 and -1, instead of the +1 and 0
we have been using so far. Also, whereas we previously put the intercept into the weight
vector w (and a corresponding dummy 1 value into xj,0), SVMs do not do that; they keep the
intercept as a separate parameter, b.
With that in mind, the separator is deﬁned as the set of points {x : w · x + b=0}. We
could search the space of w and b with gradient descent to ﬁnd the parameters that maximize
the margin while correctly classifying all the examples.
However, it turns out there is another approach to solving this problem. We won’t show
the details, but will just say that there is an alternative representation called the dual repre-
sentation, in which the optimal solution is found by solving
argmax
α
∑
j
αj −1
2 ∑
j,k
αjαkyjyk(xj ·xk)
(19.10)
subject to the constraints αj ≥0 and ∑j αjyj =0. This is a quadratic programming op-
Quadratic
programming
timization problem, for which there are good software packages. Once we have found the

## Page 712
