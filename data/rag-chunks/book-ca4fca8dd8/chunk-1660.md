---
chunk_id: "book-ca4fca8dd8-chunk-1660"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1660
confidence: "first-pass"
extraction_method: "structured-local"
---

1012
Chapter 27
Computer Vision
1. Suppose you are a ﬂy trying to land on a wall and you want useful information from
the optical ﬂow ﬁeld. The optical ﬂow ﬁeld cannot tell you the distance to the wall or
the velocity to the wall, because of the scale ambiguity. But if you divide the distance
by the velocity, the scale ambiguity cancels. The result is the time to contact, given by
Z/Tz, and is very useful indeed to control the landing approach. There is considerable
experimental evidence that many different animal species exploit this cue.
2. Consider two points at depths Z1, Z2 respectively. We may not know the absolute value
of either of these, but by considering the inverse of the ratio of the optical ﬂow magni-
tudes at these points, we can determine the depth ratio Z1/Z2. This is the cue of motion
parallax, one we use when we look out of the side window of a moving car or train and
infer that the slower-moving parts of the landscape are farther away.
27.6.4 3D cues from one view
Even a single image provides a rich collection of information about the 3D world. This is
true even if the image is just a line drawing. Line drawings have fascinated vision scientists,
because people have a sense of 3D shape and layout even though the drawing seems to contain
very little information to choose from the vast collection of scenes that could produce the
same drawing. Occlusion is one key source of information: if there is evidence in the picture
that one object occludes another, then the occluding object is closer to the eye.
In images of real scenes, texture is a strong cue to 3D structure. Section 27.3.2 stated that
texture is a repetitive pattern of texels. Although the distribution of texels may be uniform on
objects in the scene—for example, pebbles on a beach—it may not be uniform in image—
the farther pebbles appear smaller than the nearer pebbles. As another example, think about
a piece of polka-dot fabric. All the dots are the same size and shape on the fabric, but in
a perspective view some dots are ellipses due to foreshortening. Modern methods exploit
these cues by learning a mapping from images to 3D structure (Section 27.7.4), rather than
reasoning directly about the underlying mathematics of texture.
Shading—variation in the intensity of light received from different portions of a surface
in a scene—is determined by the geometry of the scene and by the reﬂectance properties of
the surfaces. There is very good evidence that shading is a cue to 3D shape. The physical
argument is easy. From the physical model of section 27.2.4, we know that if a surface normal
points toward the light source, the surface is brighter, and if it points away, the surface is
darker. This argument gets more complicated if the reﬂectance of the surface isn’t known,
and the illumination ﬁeld isn’t even, but humans seem to be able to get a useful perception of
shape from shading. We know frustratingly little about algorithms to do this.
If there is a familiar object in the picture, what it looks like depends very strongly on its
pose, that is, its position and orientation with respect to the viewer. There are straightforward
Pose
algorithms for recovering pose from correspondences between points on an object and points
on a model of the object. Recovering the pose of a known object has many applications. For
instance, in an industrial manipulation task, the robot arm cannot pick up an object until the
pose is known. Robotic surgery applications depend on exactly computing the transforma-
tions between the camera’s position and the positions of the surgical tool and the patient (to
yield the transformation from the tool’s position to the patient’s position).
Spatial relations between objects are another important cue. Here is an example. All
pedestrians are about the same height, and they tend to stand on a ground plane. If we
