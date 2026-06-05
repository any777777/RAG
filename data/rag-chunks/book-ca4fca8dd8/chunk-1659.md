---
chunk_id: "book-ca4fca8dd8-chunk-1659"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1659
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.6
The 3D World
1011
b
du/2
dZ
P
P0
PR
PL
Left
eye
Z
Right
eye
u
Figure 27.15 The relation between disparity and depth in stereopsis. The centers of projec-
tion of the two eyes are distance b apart, and the optical axes intersect at the ﬁxation point
P0. The point P in the scene projects to points PL and PR in the two eyes. In angular terms,
the disparity between these is δθ (the diagram shows two angles of δθ/2).
27.6.3 3D cues from a moving camera
Assume we have a camera moving in a scene. Take Figure 27.14 and label the left image
“Time t” and the right image “Time t +1”. The geometry has not changed, so all the material
from the discussion of stereopsis also applies when a camera moves. What we called disparity
in that section is now thought of as apparent motion in the image, and called optical ﬂow. This
is a source of information for both the movement of the camera and the geometry of the scene.
To understand this, we state (without proof) an equation that relates the optical ﬂow to the
viewer’s translational velocity T and the depth in the scene.
The optical ﬂow ﬁeld is a vector ﬁeld of velocities in the image, (vx(x,y),vy(x,y)). Ex-
pressions for these components, in a coordinate frame centered on the camera and assuming
a focal length of f =1, are
vx(x,y) = −Tx +xTz
Z(x,y)
and
vy(x,y) = −Ty +yTz
Z(x,y)
.
where Z(x,y) is the z-coordinate (that is, depth) of the point in the scene corresponding to the
point in the image at (x,y).
Note that both components of the optical ﬂow, vx(x,y) and vy(x,y), are zero at the point
x = Tx/Tz,y = Ty/Tz. This point is called the focus of expansion of the ﬂow ﬁeld. Suppose
Focus of expansion
we change the origin in the x–y plane to lie at the focus of expansion; then the expressions
for optical ﬂow take on a particularly simple form. Let (x′,y′) be the new coordinates deﬁned
by x′ = x−Tx/Tz, y′ = y−Ty/Tz. Then
vx(x′,y′) =
x′Tz
Z(x′,y′),
vy(x′,y′) =
y′Tz
Z(x′,y′) .
Note that there is a scale factor ambiguity here (which is why assuming a focal length of
f =1 is harmless). If the camera was moving twice as fast, and every object in the scene was
twice as big and at twice the distance to the camera, the optical ﬂow ﬁeld would be exactly
the same. But we can still extract quite useful information.

## Page 1012
