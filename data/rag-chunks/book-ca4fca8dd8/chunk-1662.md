---
chunk_id: "book-ca4fca8dd8-chunk-1662"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1662
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.7
Using Computer Vision
1013
know where the horizon is in an image, we can rank pedestrians by distance to the camera.
This works because we know where their feet are, and pedestrians whose feet are closer to
the horizon in the image are farther away from the camera, and so must be smaller in the
image. This means we can rule out some detector responses—if a detector ﬁnds a pedestrian
who is large in the image and whose feet are close to the horizon, it has found an enormous
pedestrian; these don’t exist, so the detector is wrong. In turn, a reasonably reliable pedestrian
detector is capable of producing estimates of the horizon, if there are several pedestrians in
the scene at different distances from the camera. This is because the relative scaling of the
pedestrians is a cue to where the horizon is. So we can extract a horizon estimate from the
detector, then use this estimate to prune the pedestrian detector’s mistakes.
27.7 Using Computer Vision
Here we survey a range of computer vision applications. There are now many reliable com-
puter vision tools and toolkits, so the range of applications that are successful and useful is
extraordinary. Many are developed at home by enthusiasts for special purposes, which is
testimony to how usable the methods are and how much impact they have. (For example, an
enthusiast created a great object-detection-based pet door that refuses entry to a cat if it is
bringing in a dead mouse–a Web search will ﬁnd it for you).
27.7.1 Understanding what people are doing
If we could build systems that understood what people are doing by analyzing video, we could
build human-computer interfaces that watch people and react to their behavior. With these
interfaces, we could: design buildings and public places better, by collecting and using data
about what people do in public; build more accurate and less intrusive security surveillance
systems; build automated sports commentators; make construction sites and workplaces safer
by generating warnings when people and machines get dangerously close; build computer
games that make a player get up and move around; and save energy by managing heat and
light in a building to match where the occupants are and what they are doing.
The state of the art for some problems is now extremely strong. There are methods that
can predict the locations of a person’s joints in an image very accurately. Quite good estimates
of the 3D conﬁguration of that person’s body follow (see Figure 27.16). This works because
pictures of the body tend to have weak perspective effects, and body segments don’t vary
much in length, so the foreshortening of a body segment in an image is a good cue to the
angle between it and the camera plane. With a depth sensor, these estimates can be made fast
enough to build them into computer game interfaces.
Classifying what people are doing is harder. Video that shows rather structured behaviors,
like ballet, gymnastics, or tai chi, where there are quite speciﬁc vocabularies that refer to very
precisely delineated activities on simple backgrounds, is quite easy to deal with. Good results
can be obtained with a lot of labeled data and an appropriate convolutional neural network.
However, it can be difﬁcult to prove that the methods actually work, because they rely so
strongly on context. For example, a classiﬁer that labels “swimming” sequences very well
might just be a swimming pool detector, which wouldn’t work for (say) swimmers in rivers.
More general problems remain open—for example, how to link observations of the body
and the objects nearby to the goals and intentions of the moving people. One source of
