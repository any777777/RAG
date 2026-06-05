---
chunk_id: "book-ca4fca8dd8-chunk-1657"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1657
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.6
The 3D World
1009
the cameras to construct a 3D model. Two views of two points gives you four x,y co-
ordinates, and you only need three coordinates to specify a point in 3D space; the extra
coordinate comes in helpful to ﬁgure out what you need to know about the cameras.
This is true for almost all pairs of viewing directions and almost all kinds of camera.
The key problem is to establish which point in the ﬁrst view corresponds to which in the
second view. Detailed descriptions of the local appearance of a point using simple texture
features (like those in section 27.3.2) are often enough to match points. For example, in a
scene of trafﬁc on a street, there might be only one green light visible in two images taken
of the scene; we can then hypothesize that these correspond to each other. The geometry of
multiple camera views is very well understood (but sadly too complicated to expound here).
The theory produces geometric constraints on which point in one image can match with which
point in the other. Other constraints can be obtained by reasoning about the smoothness of
the reconstructed surfaces.
There are two ways of getting multiple views of a scene. One is to have two cameras
or two eyes (section 27.6.2). Another is to move (section 27.6.3). If you have more than
two views, you can recover both the geometry of the world and the details of the view very
accurately. Section 27.7.3 discusses some applications for this technology.
27.6.2 Binocular stereopsis
Most vertebrates have two eyes. This is useful for redundancy in case of a lost eye, but it
helps in other ways too. Most prey have eyes on the side of the head to enable a wider ﬁeld of
vision. Predators have the eyes in the front, enabling them to use binocular stereopsis. Hold
Binocular stereopsis
both index ﬁngers up in front of your face, with one eye closed, and adjust them so the front
ﬁnger occludes the other ﬁnger in the open eye’s view. Now swap eyes; you should notice that
the ﬁngers have shifted position with respect to one another. This shifting of position from
left view to right view is known as disparity. In the right choice of coordinate system, if we
Disparity
superimpose left and right images of an object at some depth, the object shifts horizontally in
the superimposed image, and the size of the shift is the reciprocal of the depth. You can see
this in Figure 27.14, where the nearest point of the pyramid is shifted to the left in the right
image and to the right in the left image.
To measure disparity we need to solve the correspondence problem—to determine for a
point in the left image, its “partner” in the right image which results from the projection of
the same scene point. This is analogous to what is done in measuring optical ﬂow, and the
most simple-minded approaches are somewhat similar. These methods search for blocks of
left and right pixels that match, using the sum of squared differences (as in Section 27.3.3).
More sophisticated methods use more detailed texture representations of blocks of pixels (as
in Section 27.3.2). In practice, we use much more sophisticated algorithms, which exploit
additional constraints.
Assuming that we can measure disparity, how does this yield information about depth
in the scene? We will need to work out the geometrical relationship between disparity and
depth. We will consider ﬁrst the case when both the eyes (or cameras) are looking forward
with their optical axes parallel. The relationship of the right camera to the left camera is then
just a displacement along the x-axis by an amount b, the baseline. We can use the optical
Baseline
ﬂow equations from Section 27.3.3, if we think of this as resulting from a translation vector
T acting for time δt, with Tx = b/δt and Ty = Tz = 0. The horizontal and vertical disparity
