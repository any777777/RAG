---
chunk_id: "book-ca4fca8dd8-chunk-1164"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1164
confidence: "first-pass"
extraction_method: "structured-local"
---

700
Chapter 19
Learning from Examples
 2.5
 3
 3.5
 4
 4.5
 5
 5.5
 6
 6.5
 7
 7.5
 4.5
 5
 5.5
 6
 6.5
 7
x2
x1
 2.5
 3
 3.5
 4
 4.5
 5
 5.5
 6
 6.5
 7
 7.5
 4.5
 5
 5.5
 6
 6.5
 7
x2
x1
(a)
(b)
Figure 19.15 (a) Plot of two seismic data parameters, body wave magnitude x1 and surface
wave magnitude x2, for earthquakes (open orange circles) and nuclear explosions (green cir-
cles) occurring between 1982 and 1990 in Asia and the Middle East (Kebeasy et al., 1998).
Also shown is a decision boundary between the classes. (b) The same domain with more data
points. The earthquakes and explosions are no longer linearly separable.
invariant: Imagine a set of points in a plane, measured by their x and y coordinates. Now
imagine rotating the axes by 45o. You’d get a different set of (x′,y′) values representing
the same points. If you apply L2 regularization before and after rotating, you get exactly
the same point as the answer (although the point would be described with the new (x′,y′)
coordinates). That is appropriate when the choice of axes really is arbitrary—when it doesn’t
matter whether your two dimensions are distances north and east; or distances northeast and
southeast. With L1 regularization you’d get a different answer, because the L1 function is not
rotationally invariant. That is appropriate when the axes are not interchangeable; it doesn’t
make sense to rotate “number of bathrooms” 45o towards “lot size.”
19.6.4 Linear classiﬁers with a hard threshold
Linear functions can be used to do classiﬁcation as well as regression. For example, Fig-
ure 19.15(a) shows data points of two classes: earthquakes (which are of interest to seismolo-
gists) and underground explosions (which are of interest to arms control experts). Each point
is deﬁned by two input values, x1 and x2, that refer to body and surface wave magnitudes
computed from the seismic signal. Given these training data, the task of classiﬁcation is to
learn a hypothesis h that will take new (x1,x2) points and return either 0 for earthquakes or 1
for explosions.
A decision boundary is a line (or a surface, in higher dimensions) that separates the
Decision boundary
two classes. In Figure 19.15(a), the decision boundary is a straight line. A linear decision
boundary is called a linear separator and data that admit such a separator are called linearly
Linear separator
separable. The linear separator in this case is deﬁned by
Linear separability
x2 = 1.7x1 −4.9
or
−4.9+1.7x1 −x2 = 0.
The explosions, which we want to classify with value 1, are below and to the right of this line;
they are points for which −4.9+1.7x1 −x2 > 0, while earthquakes have −4.9+1.7x1 −x2 <
