---
chunk_id: "book-ca4fca8dd8-chunk-1629"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1629
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.2
Image Formation
989
we cannot tell if what we see is a toy Godzilla tearing up a toy building, or a real monster
destroying a real building.
There are two main ways to manage these ambiguities. First, some interpretations are
more likely than others. For example, we can be conﬁdent that the picture doesn’t show a
real Godzilla destroying a real building, because there are no real Godzillas. Second, some
ambiguities are insigniﬁcant. For example, distant scenery may be trees or may be a ﬂat
painted surface. For most applications, the difference is unimportant, because the objects are
far away and so we will not bump into them or interact with them soon.
The two core problems of computer vision are reconstruction, where an agent builds
Reconstruction
a model of the world from an image or a set of images, and recognition, where an agent
Recognition
draws distinctions among the objects it encounters based on visual and other information.
Both problems should be interpreted very broadly. Building a geometric model from images
is obviously reconstruction (and solutions are very valuable), but sometimes we need to build
a map of the different textures on a surface, and this is reconstruction, too. Attaching names
to objects that appear in an image is clearly recognition. Sometimes we need to answer
questions like: Is it asleep? Does it eat meat? Which end has teeth? Answering these
questions is recognition, too.
The last thirty years of research have produced powerful tools and methods for addressing
these core problems. Understanding these methods requires an understanding of the processes
by which images are formed.
27.2 Image Formation
Imaging distorts the appearance of objects. A picture taken looking down a long straight set
of railway tracks will suggest that the rails converge and meet. If you hold your hand in front
of your eye, you can block out the moon, even though the moon is larger than your hand (this
works with the sun too, but you could damage your eyes checking it). If you hold a book
ﬂat in front of your face and tilt it backward and forward, it will seem to shrink and grow in
the image. This effect is known as foreshortening (Figure 27.1). Models of these effects are
essential for building competent object recognition systems and also yield powerful cues for
reconstructing geometry.
27.2.1 Images without lenses: The pinhole camera
Image sensors gather light scattered from objects in a scene and create a two-dimensional
Scene
(2D) image. In the eye, these sensors consist of two types of cell: There are about 100
Image
million rods, which are sensitive to light at a wide range of wavelengths, and 5 million cones.
Cones, which are essential for color vision, are of three main types, each of which is sensitive
to a different set of wavelengths. In cameras, the image is formed on an image plane. In ﬁlm
cameras the image plane is coated with silver halides. In digital cameras, the image plane is
subdivided into a grid of a few million pixels.
Pixels
We refer to the whole image plane as a sensor, but each pixel is an individual tiny
Sensor
sensor—usually a charge-coupled device (CCD) or complementary metal-oxide semiconduc-
tor (CMOS). Each photon arriving at the sensor produces an electrical effect, whose strength
depends on the wavelength of the photon. The output of the sensor is the sum of all these
effects in some time window, meaning that image sensors report a weighted average of the
