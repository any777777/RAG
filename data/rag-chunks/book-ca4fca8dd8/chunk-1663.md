---
chunk_id: "book-ca4fca8dd8-chunk-1663"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1663
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 1014

1014
Chapter 27
Computer Vision
Figure 27.16 Reconstructing humans from a single image is now practical. Each row shows
a reconstruction of 3D body shape obtained using a single image. These reconstructions are
possible because methods can estimate the location of joints, the joint angles in 3D, the shape
of the body, and the pose of the body with respect to an image. Each row shows the follow-
ing: far left a picture; center left the picture with the reconstructed body superimposed;
center right another view of the reconstructed body; and far right yet another view of the
reconstructed body. The different views of the body make it much harder to conceal errors
in reconstruction. Figure courtesy of Angjoo Kanazawa, produced by a system described in
Kanazawa et al. (2018a).
difﬁculty is that similar behaviors look different, and different behaviors look similar, as
Figure 27.17 shows.
Another difﬁculty is caused by time scale. What someone is doing depends quite strongly
on the time scale, as Figure 27.18 illustrates. Another important effect shown in that ﬁgure
is that behavior composes—several recognized behaviors may be combined to form a single
higher-level behavior such as ﬁxing a snack.
It may also be that unrelated behaviors are going on at the same time, such as singing a
song while ﬁxing a snack. A challenge is that we don’t have a common vocabulary for the
pieces of behavior. People tend to think they know a lot of behavior names but can’t produce
long lists of such words on demand. That makes it harder to get data sets of consistently
labeled behaviors.
Learned classiﬁers are guaranteed to behave well only if the training and test data come
from the same distribution. We have no way of checking that this constraint applies to images,
but empirically we observe that image classiﬁers and object detectors work very well. But for
activity data, the relationship between training and test data is more untrustworthy because

## Page 1015
