---
chunk_id: "book-ca4fca8dd8-chunk-1678"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1678
confidence: "first-pass"
extraction_method: "structured-local"
---

1026
Chapter 27
Computer Vision
Action to 
Execute
Goal (3m, 4m)
Mapper
Planner
Action to 
Execute
Ego-motion
Mapper
Planner
Belief about the world
Figure 27.29 Navigation is tackled by decomposition into two problems: mapping and plan-
ning. With each successive time step, information from sensors is used to incrementally build
an uncertain model of the world. This model along with the goal speciﬁcation is passed to
a planner that outputs the next action that the robot should take in order to achieve the goal.
Models of the world can be purely geometric (as in classical SLAM), or semantic (as ob-
tained via learning), or even topological (based on landmarks). The actual robot appears on
the right. Figures courtesy of Saurabh Gupta.
Summary
Although perception appears to be an effortless activity for humans, it requires a signiﬁcant
amount of sophisticated computation. The goal of vision is to extract information needed for
tasks such as manipulation, navigation, and object recognition.
• The geometry and optics of image formation is well understood. Given a description of
a 3D scene, we can easily produce a picture of it from some arbitrary camera position—
this is the graphics problem. The inverse problem, the computer vision problem—
taking a picture and turning it into a 3D description—is more difﬁcult.
• Representations of images capture edges, texture, optical ﬂow, and regions. These yield
cues to the boundaries of objects and to correspondence between images.
• Convolutional neural networks produce accurate image classiﬁers that use learned fea-
tures. Rather roughly, the features are patterns of patterns of patterns.... It is hard to
predict when these classiﬁers will work well, because the test data may be unlike the
training data in some important way. Experience teaches that they are often accurate
enough to use in practice.
• Image classiﬁers can be turned into object detectors. One classiﬁer scores boxes in an
image for objectness; another then decides whether an object is in the box, and what
object it is. Object detection methods aren’t perfect, but are usable for a wide variety of
applications.
• With more than one view of a scene, it is possible to recover the 3D structure of the
scene and the relationship between views. In many cases, it is possible to recover 3D
geometry from a single view.
• The methods of computer vision are being very widely applied.

## Page 1027
