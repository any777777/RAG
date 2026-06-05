---
chunk_id: "book-ca4fca8dd8-chunk-1633"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1633
confidence: "first-pass"
extraction_method: "structured-local"
---

992
Chapter 27
Computer Vision
Iris
Cornea
Fovea
Visual Axis
Optical Axis
Lens
Retina
Optic Nerve
Lens
System
Image plane
Focal plane
Depth of field
Figure 27.3 Lenses collect the light leaving a point in the scene (here, the tip of the candle
ﬂame) in a range of directions, and steer all the light to arrive at a single point on the image
plane. Points in the scene near the focal plane—within the depth of ﬁeld—will be focused
properly. In cameras, elements of the lens system move to change the focal plane, whereas
in the eye, the shape of the lens is changed by specialized muscles.
Lens systems do not focus all the light from everywhere in the real world; the lens design
restricts them to focusing light only from points that lie within a range of Z depths from the
lens. The center of this range—where focus is sharpest—is called the focal plane, and the
Focal plane
range of depths for which focus remains sharp enough is called the depth of ﬁeld. The larger
Depth of ﬁeld
the lens aperture (opening), the smaller the depth of ﬁeld.
What if you want to focus on something at a different distance? To move the focal plane,
the lens elements in a camera can move back and forth, and the lens in the eye can change
shape—but with age the eye lens tends to harden, making it less able to adjust focal distances,
and requiring many humans to augment their vision with external lens—eyeglasses.
27.2.3 Scaled orthographic projection
The geometric effects of perspective imaging aren’t always pronounced. For example, win-
dows on a building across the street look much smaller than ones right nearby, but two win-
dows that are next to each other will have about the same size even though one is slightly
farther away. We have the option to handle the windows with a simpliﬁed model called
scaled orthographic projection, rather than perspective projection. If the depth Z of all
Scaled orthographic
projection
points on an object fall within the range Z0 ±∆Z, with ∆Z ≪Z0, then the perspective scaling
factor f/Z can be approximated by a constant s = f/Z0. The equations for projection from
the scene coordinates (X,Y,Z) to the image plane become x = sX and y = sY. Foreshortening
still occurs in the scaled orthographic projection model, because it is caused by the object
tilting away from the view.

## Page 993
