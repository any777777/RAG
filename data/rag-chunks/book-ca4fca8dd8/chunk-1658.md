---
chunk_id: "book-ca4fca8dd8-chunk-1658"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1658
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1010

1010
Chapter 27
Computer Vision
Perceived object
Right image
(a)
(b)
Left image
Disparity
Left
Right
Figure 27.14 Translating a camera parallel to the image plane causes image features to move
in the camera plane. The disparity in positions that results is a cue to depth. If we superimpose
left and right images, as in (b), we see the disparity.
are given by the optical ﬂow components, multiplied by the time step δt, H = vx δt, V = vy δt.
Carrying out the substitutions, we get the result that H = b/Z, V = 0. In other words, the
horizontal disparity is equal to the ratio of the baseline to the depth, and the vertical disparity
is zero. We can recover the depth Z given that we know b, and can measure H.
Under normal viewing conditions, humans ﬁxate; that is, there is some point in the scene
Fixate
at which the optical axes of the two eyes intersect. Figure 27.15 shows two eyes ﬁxated
at a point P0, which is at a distance Z from the midpoint of the eyes. For convenience,
we will compute the angular disparity, measured in radians. The disparity at the point of
ﬁxation P0 is zero. For some other point P in the scene that is δZ farther away, we can
compute the angular displacements of the left and right images of P, which we will call PL
and PR, respectively. If each of these is displaced by an angle δθ/2 relative to P0, then the
displacement between PL and PR, which is the disparity of P, is just δθ. From Figure 27.15,
tanθ = b/2
Z and tan(θ −δθ/2) =
b/2
Z+δZ, but for small angles, tanθ ≈θ, so
δθ/2 = b/2
Z −
b/2
Z +δZ ≈bδZ
2Z2
and, since the actual disparity is δθ, we have
disparity = bδZ
Z2
In humans, the baseline b is about 6 cm. Suppose that Z is about 100 cm and that the
smallest detectable δθ (corresponding to the size of a single pixel) is about 5 seconds of arc,
giving a δZ of 0.4 mm. For Z = 30 cm, we get the impressively small value δZ = 0.036 mm.
That is, at a distance of 30 cm, humans can discriminate depths that differ by as little as 0.036
mm, enabling us to thread needles and the like.

## Page 1011
