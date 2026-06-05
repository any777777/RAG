---
chunk_id: "book-ca4fca8dd8-chunk-1631"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1631
confidence: "first-pass"
extraction_method: "structured-local"
---

990
Chapter 27
Computer Vision
Figure 27.1 Geometry in the scene appears distorted in images. Parallel lines appear to
meet, like the railway tracks in a desolate town. Buildings that have right angles in the real
world scene have distorted angles in the image.
intensity of light arriving at the sensor. The average is over wavelength, direction from which
photons can arrive, time, and the area of the sensor.
To see a focused image, we must ensure that all the photons arriving at a sensor come
from approximately the same spot on the object in the world. The simplest way to form a fo-
cused image is to view stationary objects with a pinhole camera, which consists of a pinhole
Pinhole camera
opening, O, at the front of a box, and an image plane at the back of the box (Figure 27.2).
The opening is called the aperture. If the pinhole is small enough, each tiny sensor in the
Aperture
image plane will see only photons that come from approximately the same spot on the object,
and so the image is focused. We can form focused images of moving objects with a pinhole
camera, too, as long as the object moves only a short distance in the sensors’ time window.
Otherwise, the image of the moving object is defocused, an effect known as motion blur.
Motion blur
One way to manipulate the time window is to open and close the pinhole.
Pinhole cameras make it easy to understand the geometric model of camera behavior
(which is more complicated—but similar—with most other imaging devices). We will use a
three-dimensional (3D) coordinate system with the origin at O, and will consider a point P
in the scene, with coordinates (X,Y,Z). P gets projected to the point P′ in the image plane
with coordinates (x,y,z). If f is the focal length—the distance from the pinhole to the image
Focal length
plane—then by similar triangles, we can derive the following equations:
−x
f
= X
Z , −y
f
= Y
Z
⇒
x = −fX
Z
, y = −fY
Z
.
These equations deﬁne an image formation process known as perspective projection. Note
Perspective
projection
that the Z in the denominator means that the farther away an object is, the smaller its image
will be. Also, note that the minus signs mean that the image is inverted, both left–right and
up–down, compared with the scene.
Perspective imaging has a number of geometric effects. Distant objects look small. Par-
allel lines converge to a point on the horizon. (Think of railway tracks, Figure 27.1.) A line
in the scene in the direction (U,V,W) and passing through the point (X0,Y0,Z0) can be de-
scribed as the set of points (X0+λU,Y0+λV,Z0+λW), with λ varying between −∞and +∞.
Different choices of (X0,Y0,Z0) yield different lines parallel to one another. The projection
