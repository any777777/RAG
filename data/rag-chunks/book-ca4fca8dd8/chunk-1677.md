---
chunk_id: "book-ca4fca8dd8-chunk-1677"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1677
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1025

Section 27.7
Using Computer Vision
1025
Figure 27.28 Mobileye’s camera-based sensing for autonomous vehicles. Top row: Two
images from a front-facing camera, taken a few seconds apart. The green area is the free
space—the area to which the vehicle could physically move in the immediate future. Objects
are displayed with 3D bounding boxes deﬁning their sides (red for the rear, blue for the right
side, yellow for the left side, and green for the front). Objects include vehicles, pedestrians,
the inner edge of the self-lane marks (necessary for lateral control), other painted road and
crosswalk marks, trafﬁc signs, and trafﬁc lights. Not shown are animals, poles and cones,
sidewalks, railings, and general objects (e.g., a couch that fell from the back of a truck). Each
object is then marked with a 3D position and velocity. Bottom row: A full physical model of
the environment, rendered from the detected objects. (Images show Mobileye’s vision-only
system results). Images courtesy of Mobileye.
• Path planning: Once the robot has access to this 3D map and can localize itself in it,
the objective becomes one of ﬁnding a collision-free trajectory from the current position
to the goal location (see Section 26.6).
Many variants of this general approach have been explored. For instance, in the cognitive
mapping and planning approach, the two stages of map building and path planning are two
modules in a neural network that is trained end-to-end to minimize a loss function. Such a
system does not have to build a complete map—which is often redundant and unnecessary—
if all you need is enough information to navigate from point A to point B without colliding
with obstacles.

## Page 1026
