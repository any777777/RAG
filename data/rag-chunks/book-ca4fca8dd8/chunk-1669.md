---
chunk_id: "book-ca4fca8dd8-chunk-1669"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1669
confidence: "first-pass"
extraction_method: "structured-local"
---

1018
Chapter 27
Computer Vision
27.7.3 Reconstruction from many views
Reconstructing a set of points from many views—which could come from video or from an
aggregation of tourist photographs—is similar to reconstructing the points from two views,
but there are some important differences. There is far more work to be done to establish cor-
respondence between points in different views, and points can go in and out of view, making
the matching and reconstruction process messier. But more views means more constraints
on the reconstruction and on the recovered viewing parameters, so it is usually possible to
produce extremely accurate estimates of both the position of the points and of the viewing
parameters. Rather roughly, reconstruction proceeds by matching points over pairs of im-
ages, extending these matches to groups of images, coming up with a rough solution for both
geometry and viewing parameters, then polishing that solution. Polishing means minimizing
the error between points predicted by the model (of geometry and viewing parameters) and
the locations of image features. The detailed procedures are too complex to cover fully, but
are now very well understood and quite reliable.
All the geometric constraints on correspondences are known for any conceivably useful
form of camera. The procedures can be generalized to deal with views that are not ortho-
graphic; to deal with points that are observed in only some views; to deal with unknown
camera parameters (like focal length); and to exploit various sophisticated searches for ap-
propriate correspondences. It is practical to accurately reconstruct a model of an entire city
from images. Some applications are:
• Model building: For example, one might build a modeling system that takes many
views depicting an object and produces a very detailed 3D mesh of textured polygons
for use in computer graphics and virtual reality applications. It is routine to build models
like this from video, but such models can now be built from apparently random sets of
pictures. For example, you can build a 3D model of the Statue of Liberty from pictures
found on the Internet.
• Mix animation with live actors in video: To place computer graphics characters into
real video, we need to know how the camera moved for the real video, so we can render
the character correctly, changing the view as the camera moves.
• Path reconstruction: Mobile robots need to know where they have been. If the robot
has a camera, we can build a model of the camera’s path through the world; that will
serve as a representation of the robot’s path.
• Construction management: Buildings are enormously complicated artifacts, and keep-
ing track of what is happening during construction is difﬁcult and expensive. One way
to keep track is to ﬂy drones through the construction site once a week, ﬁlming the
current state. Then build a 3D model of the current state and explore the difference
between the plans and the reconstruction using visualization techniques. Figure 27.21
illustrates this application.
27.7.4 Geometry from a single view
Geometric representations are particularly useful if you want to move, because they can reveal
where you are, where you can go, and what you are likely bump into. But it is not always
convenient to use multiple views to produce a geometric model. For example, when you open
the door and step into a room, your eyes are too close together to recover a good representation
