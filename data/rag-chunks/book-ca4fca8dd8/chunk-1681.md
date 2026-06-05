---
chunk_id: "book-ca4fca8dd8-chunk-1681"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1681
confidence: "first-pass"
extraction_method: "structured-local"
---

1028
Chapter 27
Computer Vision
see depth if the images presented to the left and right eyes are slightly different was demon-
strated by Wheatstone’s (1838) invention of the stereoscope. The device immediately became
popular in parlors and salons throughout Europe.
The essential concept of binocular stereopsis—that two images of a scene taken from
slightly different viewpoints carry information sufﬁcient to obtain a three-dimensional re-
construction of the scene—was exploited in the ﬁeld of photogrammetry. Key mathematical
results were obtained; for example, Kruppa (1913) proved that, given two views of ﬁve dis-
tinct points in a scene, one could reconstruct the rotation and translation between the two
camera positions as well as the depth of the scene (up to a scale factor).
Although the geometry of stereopsis had been understood for a long time, the corre-
spondence problem in photogrammetry used to be solved by humans trying to match up
corresponding points. The amazing ability of humans in solving the correspondence problem
was illustrated by Julesz’s (1971) random dot stereograms. The ﬁeld of computer vision has
devoted much effort towards an automatic solution of the correspondence problem.
In the ﬁrst half of the 20th century, the most signiﬁcant research results in vision were
obtained by the Gestalt school of psychology, led by Max Wertheimer. They pointed out the
importance of perceptual organization: for a human, the image is not a collection of pointillist
photoreceptor outputs (pixels), rather it is organized into coherent groups. The computer
vision task of ﬁnding regions and curves traces back to this insight. The Gestaltists also drew
attention to the “ﬁgure-ground” phenomenon—a contour separating two image regions that
in the world are at different depths appears to belong only to the nearer region, the “ﬁgure,”
and not to the farther region, the “ground.”
The gestalt work was carried on by J. J. Gibson (1950, 1979), who pointed out the impor-
tance of optical ﬂow and texture gradients in the estimation of environmental variables such
as surface slant and tilt. He reemphasized the importance of the stimulus and how rich it was.
Gibson, Olum, and Rosenblatt (1955) pointed out that the optical ﬂow ﬁeld contained enough
information to determine the motion of the observer relative to the environment. Gibson par-
ticularly emphasized the role of the active observer, whose self-directed movement facilitates
the pickup of information about the external environment.
Computer vision dates back to the 1960s. Roberts’s (1963) thesis at MIT on perceiving
cubes and other blocks-world objects was one of the earliest publications in the ﬁeld. Roberts
introduced several key ideas, including edge detection and model-based matching.
In the 1960s and 1970s progress was slow, hampered by the lack of computational and
storage resources. Low-level visual processing received a lot of attention, with techniques
drawn from related ﬁelds such as signal processing, pattern recognition, and data clustering.
Edge detection was treated as an essential ﬁrst step in image processing, as it reduced
the amount of data to be processed. The widely used Canny edge detection technique was
introduced by John Canny (1986). Martin, Fowlkes, and Malik (2004) showed how to com-
bine multiple clues, such as brightness, texture and color, in a machine learning framework
to better ﬁnd boundary curves.
The closely related problem of ﬁnding regions of coherent brightness, color, and texture
naturally lends itself to formulations where ﬁnding the best partition becomes an optimization
problem. Three leading examples are based on Markov Random Fields due to Geman and
Geman (1984), the variational formulation of Mumford and Shah (1989), and normalized
cuts by Shi and Malik (2000).
