---
chunk_id: "book-ca4fca8dd8-chunk-1671"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1671
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.7
Using Computer Vision
1019
Figure 27.21 3D models of construction sites are produced from images by structure-from-
motion and multiview stereo algorithms. They help construction companies to coordinate
work on large buildings by comparing a 3D model of the actual construction to date with
the building plans. Left: A visualization of a geometric model captured by drones. The
reconstructed 3D points are rendered in color, so the result looks like progress to date (note
the partially completed building with crane). The small pyramids show the pose of a drone
when it captured an image, to allow visualization of the ﬂight path. Right: These systems
are actually used by construction teams; this team views the model of the as-built site, and
compares it with building plans as part of the coordination meeting. Figure courtesy of Derek
Hoiem, Mani Golparvar-Fard and Reconstruct, produced by a commercial system described
in a blog post at medium.com/reconstruct-inc.
of the depth to distant objects across the room. You could move your head back and forth,
but that is time-consuming and inconvenient.
An alternative is to predict a depth map—an array giving the depth to each pixel in the
Depth map
image, nominally from the camera—from a single image. For many kinds of scenes, this is
surprisingly easy to do accurately, because the depth map has quite a simple structure. This is
particularly true of rooms and indoor scenes in general. The mechanics are straightforward.
One obtains a data set of images and depth maps, then trains a network to predict depth
maps from images. A variety of interesting variations of the problem can be solved. The
problem with a depth map is that it doesn’t tell you anything about the backs of objects, or
the space behind the objects. But there are methods that can predict what voxels (3D pixels)
are occupied by known objects (the object geometry is known) and what a depth map would
look like if an object were removed (and so where you could hide objects). These methods
work because object shapes are quite strongly stylized.
As we saw in Section 27.6.4, recovering the pose of a known object using a 3D model
is straightforward. Now imagine you see a single image of, say, a sparrow. If you have seen
many images of sparrow-like birds in the past, you can reconstruct a reasonable estimate of
both the pose of the sparrow and its geometric model from that single image. Using the past
images you build a small, parametric family of geometric models for sparrow-like birds; then
an optimization procedure is used to ﬁnd the best set of parameters and viewpoints to explain
the image that you see. This argument works to supply texture for that model, too, even for
the parts you cannot see (Figure 27.22).
