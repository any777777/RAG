---
chunk_id: "book-ca4fca8dd8-chunk-1643"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1643
confidence: "first-pass"
extraction_method: "structured-local"
---

1000
Chapter 27
Computer Vision
grow a patch full of stripes until it covers the zebra). An alternative is to describe a patch
centered at each pixel for a range of scales. This range usually runs from a few pixels to the
extent of the image. Now divide the patch into bins, and in each bin construct an orientation
histogram, then summarize the pattern of histograms across bins. It is no longer usual to
construct these descriptions by hand. Instead, convolutional neural networks are used to
produce texture representations. But the representations constructed by the networks seem to
mirror this construction very roughly.
27.3.3 Optical ﬂow
Next, let us consider what happens when we have a video sequence, instead of just a single
static image. Whenever there is relative movement between the camera and one or more
objects in the scene, the resulting apparent motion in the image is called optical ﬂow. This
Optical ﬂow
describes the direction and speed of motion of features in the image as a result of relative
motion between the viewer and the scene. For example, distant objects viewed from a moving
car have much slower apparent motion than nearby objects, so the rate of apparent motion
can tell us something about distance.
In Figure 27.9 we show two frames from a video of a tennis player. On the right we
display the optical ﬂow vectors computed from these images. The optical ﬂow encodes useful
information about scene structure—the tennis player is moving and the background (largely)
isn’t. Furthermore, the ﬂow vectors reveal something about what the player is doing—one
arm and one leg are moving fast, and the other body parts aren’t.
The optical ﬂow vector ﬁeld can be represented by its components vx(x,y) in the x direc-
tion and vy(x,y) in the y direction. To measure optical ﬂow, we need to ﬁnd corresponding
points between one time frame and the next. A very simple-minded technique is based on the
fact that image patches around corresponding points have similar intensity patterns. Consider
a block of pixels centered at pixel p, (x0,y0), at time t. This block of pixels is to be compared
with pixel blocks centered at various candidate pixels qi at (x0 +Dx,y0 +Dy) at time t +Dt.
One possible measure of similarity is the sum of squared differences (SSD):
Sum of squared
diﬀerences (SSD)
SSD(Dx,Dy) = ∑
(x,y)
(I(x,y,t)−I(x+Dx,y+Dy,t +Dt))2 .
Figure 27.9 Two frames of a video sequence and the optical ﬂow ﬁeld corresponding to the
displacement from one frame to the other. Note how the movement of the tennis racket and
the front leg is captured by the directions of the arrows. (Images courtesy of Thomas Brox.)
