---
chunk_id: "book-ca4fca8dd8-chunk-1641"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1641
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 27.3
Simple Image Features
999
Figure 27.8 (a) Photograph of a stapler. (b) Edges computed from (a).
27.3.2 Texture
In everyday language, the texture of surfaces hints at what they feel like when you run a
Texture
ﬁnger over them (the words “texture,” “textile,” and “text” have the same Latin root, a word
for weaving). In computational vision, texture refers to a pattern on a surface that can be
sensed visually. Usually, these patterns are roughly regular. Examples include the pattern of
windows on a building, the stitches on a sweater, the spots on a leopard’s skin, blades of grass
on a lawn, pebbles on a beach, and a crowd of people in a stadium.
Sometimes the arrangement is quite periodic, as in the stitches on a sweater; in other
instances, such as pebbles on a beach, the regularity is only in a statistical sense: the density
of pebbles is roughly the same on different parts of the beach. A usual rough model of texture
is a repetitive pattern of elements, sometimes called texels. This model is quite useful because
Texels
it is surprisingly hard to make or ﬁnd real textures that never repeat.
Texture is a property of an image patch, rather than a pixel in isolation. A good descrip-
tion of a patch’s texture should summarize what the patch looks like. The description should
not change when the lighting changes. This rules out using edge points; if a texture is brightly
lit, many locations within the patch will have high contrast and will generate edge points; but
if the same texture is viewed under less bright light, many of these edges will not be above
the threshold. The description should change in a sensible way when the patch rotates. It is
important to preserve the difference between vertical stripes and horizontal stripes but not if
the vertical stripes are rotated to the horizontal.
Texture representations with these properties have been shown to be useful for two key
tasks. The ﬁrst is identifying objects—a zebra and horse have similar shape, but different
textures. The second is matching patches in one image to patches in another image, a key
step in recovering 3D information from multiple images (Section 27.6.1).
Here is a basic construction for a texture representation. Given an image patch, compute
the gradient orientation at each pixel in the patch, and then characterize the patch by a his-
togram of orientations. Gradient orientations are largely invariant to changes in illumination
(the gradient will get longer, but it will not change direction). The histogram of orientations
seems to capture important aspects of the texture. For example, vertical stripes will have two
peaks in the histogram (one for the left side of each stripe and one for the right); leopard spots
will have more uniformly distributed orientations.
But we do not know how big a patch to describe. There are two strategies. In specialized
applications, image information reveals how big the patch should be (for example, one might
