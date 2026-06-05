---
chunk_id: "book-ca4fca8dd8-chunk-1636"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1636
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.3
Simple Image Features
995
27.2.5 Color
Fruit is a bribe that a tree offers to animals to carry its seeds around. Trees that can signal
when this bribe is ready have an advantage, as do animals that can read these signals. As a
result, most fruits start green, and turn red or yellow when ripe, and most fruit-eating animals
can see these color changes. Generally, light arriving at the eye has different amounts of
energy at different wavelengths, and is represented by a spectral energy density.
Cameras and the human vision system respond to light at wavelengths ranging from about
380nm (violet) to about 750nm (red). In color imaging systems, there are different types of
receptor that respond more or less strongly to different wavelengths. In humans, the sensation
of color occurs when the vision system compares the responses of receptors near each other
on the retina. Animal color vision systems typically have relatively few types of receptor,
and so represent relatively little of the detail in the spectral energy density function (some
animals have only one type of receptor; some have as many as six types). Human color
vision is produced by three types of receptor. Most color camera systems use only three types
of receptor, too, because the images are produced for humans, but some specialized systems
can produce very detailed measurements of the spectral energy density.
Because most humans have three types of color-sensitive receptors, the principle of
trichromacy applies. This idea, ﬁrst proposed by Thomas Young in 1802, states that a human
Principle of
trichromacy
observer can match the visual appearance of any spectral energy density, however complex,
by mixing appropriate amounts of just three primaries. Primaries are colored light sources,
Primaries
chosen so that no mixture of any two will match the third. A common choice is to have one
red primary, one green, and one blue, abbreviated as RGB. Although a given colored object
RGB
may have many component frequencies of light, we can match the color by mixing just the
three primaries, and most people will agree on the proportions of the mixture. That means
we can represent color images with just three numbers per pixel—the RGB values.
For most computer vision applications, it is accurate enough to model a surface as having
three different (RGB) diffuse albedos and to model light sources as having three (RGB) in-
tensities. We then apply Lambert’s cosine law to each to get red, green, and blue pixel values.
This model predicts, correctly, that the same surface will produce different colored image
patches under different colored lights. In fact, human observers are quite good at ignoring
the effects of different colored lights and appear to estimate the color the surface would have
under white light, an effect known as color constancy.
Color constancy
27.3 Simple Image Features
Light reﬂects off objects in the scene to form an image consisting of, say, twelve million
three-byte pixels. As with all sensors there will be noise in the image, and in any case there is
a lot of data to deal with. The way to get started analyzing this data is to produce simpliﬁed
representations that expose what’s important, but reduce detail. Much current practice learns
these representations from data. But there are four properties of images and video that are
particularly general: edges, texture, optical ﬂow and segmentation into regions.
An edge occurs where there is a big difference in pixel intensity across part of an image.
Building representations of edges involves local operations on an image—you need to com-
pare a pixel value to some values nearby—and doesn’t require any knowledge about what is
