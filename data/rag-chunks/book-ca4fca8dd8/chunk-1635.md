---
chunk_id: "book-ca4fca8dd8-chunk-1635"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1635
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 994

994
Chapter 27
Computer Vision
Specularities
Cast shadow
Diffuse reflection, dark
Diffuse reflection, bright
Figure 27.4 This photograph illustrates a variety of illumination effects. There are specular-
ities on the stainless steel cruet. The onions and carrots are bright diffuse surfaces because
they face the light direction. The shadows appear at surface points that cannot see the light
source at all. Inside the pot are some dark diffuse surfaces where the light strikes at a tangen-
tial angle. (There are also some shadows inside the pot.) Photo by Ryman Cabannes/Image
Professionals GmbH/Alamy Stock Photo.
A
B
u
u
Figure 27.5 Two surface patches are illuminated by a distant point source, whose rays are
shown as light arrows. Patch A is tilted away from the source (θ is close to 90◦) and collects
less energy, because it cuts fewer light rays per unit surface area. Patch B, facing the source
(θ is close to 0◦), collects more energy.
other sources. Outdoors, the most important source other than the sun is the sky, which
is quite bright. Indoors, light reﬂected from other surfaces illuminates shadowed patches.
These interreﬂections can have a signiﬁcant effect on the brightness of other surfaces, too.
Interreﬂections
These effects are sometimes modeled by adding a constant ambient illumination term to the
Ambient illumination
predicted intensity.

## Page 995
