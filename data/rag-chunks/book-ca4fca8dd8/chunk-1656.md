---
chunk_id: "book-ca4fca8dd8-chunk-1656"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1656
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1008

1008
Chapter 27
Computer Vision
Box non-max
suppression
ROI pool
Neural net
feature 
stack
Crop
ROIs
Image
Box proposal
network
Non-max
suppression
Bounding box
regression
Neural net
classifier
0.9
0.7
Figure 27.13 Faster RCNN uses two networks. A picture of a young Nelson Mandela is
fed into the object detector. One network computes “objectness” scores of candidate image
boxes, called “anchor boxes,” centered at a grid point. There are nine anchor boxes (three
scales, three aspect ratios) at each grid point. For the example image, an inner green box and
an outer blue box have passed the objectness test. The second network is a feature stack that
computes a representation of the image suitable for classiﬁcation. The boxes with highest
objectness score are cut from the feature map, standardized in size with ROI pooling, and
passed to a classiﬁer. The blue box has a higher score than the green box and overlaps it, so
the green box is rejected by non-maximum suppression. Finally, bounding box regression the
blue box so that it ﬁts the face. This means that the relatively coarse sampling of locations,
scales, and aspect ratios does not weaken accuracy. Photo by Sipa/Shutterstock.
27.6 The 3D World
Images show a 2D picture of a 3D world. But this 2D picture is rich with cues about the 3D
world. One kind of cue occurs when we have multiple pictures of the same world, and can
match points between pictures. Another kind of cue is available within a single picture.
27.6.1 3D cues from multiple views
Two pictures of objects in a 3D world are better than one for several reasons:
• If you have two images of the same scene taken from different viewpoints and you know
enough about the two cameras, you can construct a 3D model—a collection of points
with their coordinates in 3 dimensions—by ﬁguring out which point in the ﬁrst view
corresponds to which point in the second view and applying some geometry. This is
true for almost all pairs of viewing directions and almost all kinds of camera.
• If you have two views of enough points, and you know which point in the ﬁrst view
corresponds to which point in the second view, you do not need to know much about

## Page 1009
