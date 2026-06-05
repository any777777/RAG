---
chunk_id: "book-ca4fca8dd8-chunk-1639"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1639
confidence: "first-pass"
extraction_method: "structured-local"
---

998
Chapter 27
Computer Vision
So the smoothing function is achieved by convolving the image with the Gaussian, I ∗Gσ. A
σ of 1 pixel is enough to smooth over a small amount of noise, whereas 2 pixels will smooth
a larger amount, but at the loss of some detail. Because the Gaussian’s inﬂuence fades rapidly
with distance, in practice we can replace the ±∞in the sums with something like ±3σ.
We have a chance to make an optimization here: we can combine the smoothing and
the edge ﬁnding into a single operation. It is a theorem that for any functions f and g, the
derivative of the convolution, (f ∗g)′, is equal to the convolution with the derivative, f ∗(g′).
So rather than smoothing the image and then differentiating, we can just convolve the image
with the derivative of the Gaussian smoothing function, G′
σ. We then mark as edges those
peaks in the response that are above some threshold, chosen to eliminate spurious peaks due
to noise.
There is a natural generalization of this algorithm from one-dimensional crosssections to
general 2D images. In two dimensions edges may be at any angle θ. Considering the image
brightness as a scalar function of the variables x, y, its gradient is a vector
∇I =


∂I
∂x
∂I
∂y


Edges correspond to locations in images where the brightness undergoes a sharp change,
and thus the magnitude of the gradient, ||∇I|| should be large at an edge point. When the
image gets brighter or darker, the gradient vector at each point gets longer or shorter, but the
direction of the gradient
∇I
||∇I|| =
 cosθ
sinθ

does not change. This gives us a θ = θ(x,y) at every pixel, which deﬁnes the edge orientation
Orientation
at that pixel. This feature is often useful, because it does not depend on image intensity.
As you might expect from the discussion on detecting edges in one-dimensional signals,
to form the gradient, we don’t actually compute ∇I, but rather ∇(I ∗Gσ), after smoothing the
image by convolving it with a Gaussian. A property of convolutions is that this is equivalent
to convolving the image with the partial derivatives of the Gaussian. Once we have computed
the gradient, we can obtain edges by ﬁnding edge points and linking them together. To tell
whether a point is an edge point, we must look at other points a small distance forward and
back along the direction of the gradient. If the gradient magnitude at one of these points is
larger, then we could get a better edge point by shifting the edge curve very slightly. Further-
more, if the gradient magnitude is too small, the point cannot be an edge point. So at an edge
point, the gradient magnitude is a local maximum along the direction of the gradient, and the
gradient magnitude is above a suitable threshold.
Once we have marked edge pixels by this algorithm, the next stage is to link those pixels
that belong to the same edge curves. This can be done by assuming that any two neighboring
pixels that are both edge pixels with consistent orientations belong to the same edge curve.
Edge detection isn’t perfect. Figure 27.8(a) shows an image of a scene containing a
stapler resting on a desk, and Figure 27.8(b) shows the output of an edge detection algorithm
on this image. As you can see, the output is not perfect: there are gaps where no edge appears,
and there are “noise” edges that do not correspond to anything of signiﬁcance in the scene.
Later stages of processing will have to correct for these errors.
