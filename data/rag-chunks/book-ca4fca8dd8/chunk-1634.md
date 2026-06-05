---
chunk_id: "book-ca4fca8dd8-chunk-1634"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1634
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.2
Image Formation
993
27.2.4 Light and shading
The brightness of a pixel in the image is a function of the brightness of the surface patch in
the scene that projects to the pixel. For modern cameras, this function is linear for middling
intensities of light, but has pronounced nonlinearities for darker and brighter illumination. We
will use a linear model. Image brightness is a strong, if ambiguous, cue to both the shape and
the identity of objects. The ambiguity occurs because there are three factors that contribute
to the amount of light that comes from a point on an object to the image: the overall intensity
of ambient light); whether the point is facing the light or is in shadow); and the amount of
Ambient light
light reﬂected from the point.
Reﬂection
People are surprisingly good at disambiguating brightness—they usually can tell the dif-
ference between a black object in bright light and a white object in shadow, even if both have
the same overall brightness. However, people sometimes get shading and markings mixed
up—-a streak of dark makeup under a cheekbone will often look like a shading effect, mak-
ing the face look thinner.
Most surfaces reﬂect light by a process of diffuse reﬂection. Diffuse reﬂection scatters
Diﬀuse reﬂection
light evenly across the directions leaving a surface, so the brightness of a diffuse surface
doesn’t depend on the viewing direction. Most cloth has this property, as do most paints,
rough wooden surfaces, most vegetation, and rough stone or concrete.
Specular reﬂection causes incoming light to leave a surface in a lobe of directions that
Specular reﬂection
is determined by the direction the light arrived from. A mirror is one example. What you see
depends on the direction in which you look at the mirror. In this case, the lobe of directions
is very narrow, which is why you can resolve different objects in a mirror.
For many surfaces, the lobe is broader. These surfaces display small bright patches,
usually called specularities. As the surface or the light moves, the specularities move, too.
Specularities
Away from these patches, the surface behaves as if it is diffuse. Specularities are often seen on
metal surfaces, painted surfaces, plastic surfaces, and wet surfaces. These are easy to identify,
because they are small and bright (Figure 27.4). For almost all purposes, it is enough to model
all surfaces as being diffuse with specularities.
The main source of illumination outside is the sun, whose rays all travel parallel to one
another in a known direction because it is so far away. We model this behavior with a distant
point light source. This is the most important model of lighting, and is quite effective for
Distant point light
source
indoor scenes as well as outdoor scenes. The amount of light collected by a surface patch in
this model depends on the angle θ between the illumination direction and the normal (per-
pendicular) to the surfaces (Figure 27.5).
A diffuse surface patch illuminated by this model will reﬂect some fraction of the light it
collects, given by the diffuse albedo. For practical surfaces, this lies in the range 0.05-0.95.
Diﬀuse albedo
Lambert’s cosine law states the brightness of a diffuse patch is given by
Lambert’s cosine law
I = ρI0 cosθ,
where I0 is the intensity of the light source, θ is the angle between the light source direction
and the surface normal, and ρ is the diffuse albedo. This law predicts that bright image pixels
come from surface patches that face the light directly and dark pixels come from patches
that see the light only tangentially, so that the shading on a surface provides some shape
information. If the surface cannot see the source, then it is in shadow. Shadows are very
Shadow
seldom a uniform black, because the shadowed surface usually receives some light from
