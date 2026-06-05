---
chunk_id: "book-ca4fca8dd8-chunk-1673"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1673
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.7
Using Computer Vision
1021
Figure 27.23 On the left, an image of a real scene. On the right, a computer graphics object
has been inserted into the scene. You can see that the light appears to be coming from the
right direction, and that the object seems to cast appropriate shadows. The generated image
is convincing even if there are small errors in the lighting and shadows, because people are
not expert at identifying these errors. Figure courtesy of Kevin Karsch, produced by a system
described in Karsch et al. (2011).
xi
yi
…
Training data
Input
i
xi
X
Y
regression error
xi
yi
yi
Objective
Result
Training
Test
,
,
y^
^
Figure 27.24 Paired image translation where the input consists of aerial images and the
corresponding map tiles, and the goal is to train a network to produce a map tile from an
aerial image. (The system can also learn to generate aerial images from map tiles.) The
network is trained by comparing ˆyi (the output for example xi of type X) to the right output yi
of type Y. Then at test time, the network must make new images of type Y from new inputs
of type X. Figure courtesy of Phillip Isola, Jun-Yan Zhu and Alexei A. Efros, produced by a
system described in Isola et al. (2017). Map data © 2019 Google.
(say, pictures of zebras). Imagine an artist who is tasked with creating an image of a zebra
running in a ﬁeld. The artist would appreciate being able to select just the right image of
a horse, and then having the computer automatically transform the horse into a zebra (Fig-
ure 27.25). To achieve this we can train two transformation networks, with an additional
constraint called a cycle constraint. The ﬁrst network maps horses to zebras; the second net-
work maps zebras to horses; and the cycle constraint requires that when you map X to Y to

## Page 1022
