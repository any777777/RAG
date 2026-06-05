---
chunk_id: "book-ca4fca8dd8-chunk-1627"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1627
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 27
COMPUTER VISION
In which we connect the computer to the raw, unwashed world through the eyes of a camera.
Most animals have eyes, often at signiﬁcant cost: eyes take up a lot of space; use energy;
and are quite fragile. This cost is justiﬁed by the immense value that eyes provide. An agent
that can see can predict the future—it can tell what it might bump into; it can tell whether to
attack or to ﬂee or to court; it can guess whether the ground ahead is swampy or ﬁrm; and
it can tell how far away the fruit is. In this chapter, we describe how to recover information
from the ﬂood of data that comes from eyes or cameras.
27.1 Introduction
Vision is a perceptual channel that accepts a stimulus and reports some representation of the
world. Most agents that use vision use passive sensing—they do not need to send out light
to see. In contrast, active sensing involves sending out a signal such as radar or ultrasound,
and sensing a reﬂection. Examples of agents that use active sensing include bats (ultrasound),
dolphins (sound), abyssal ﬁshes (light), and some robots (light, sound, radar). To understand
a perceptual channel, one must study both the physical and statistical phenomena that occur
in sensing and what the perceptual process should produce. We concentrate on vision in this
chapter, but robots in the real world use a variety of sensors to perceive sound, touch, distance,
temperature, global position, and acceleration.
A feature is a number obtained by applying simple computations to an image. Very use-
Feature
ful information can be obtained directly from features. The wumpus agent had ﬁve sensors,
each of which extracted a single bit of information. These bits, which are features, could
be interpreted directly by the program. As another example, many ﬂying animals compute a
simple feature that gives a good estimate of time to contact with a nearby object; this feature
can be passed directly to muscles that control steering or wings, allowing very fast changes of
direction. This feature extraction approach emphasizes simple, direct computations applied
to sensor responses.
The model-based approach to vision uses two kinds of models. An object model could
be the kind of precise geometric model produced by computer aided design systems. It could
also be a vague statement about general properties of objects, for example, the claim that all
faces viewed in low resolution look approximately the same. A rendering model describes
the physical, geometric, and statistical processes that produce the stimulus from the world.
While rendering models are now sophisticated and exact, the stimulus is usually ambiguous.
A white object under low light may look like a black object under intense light. A small,
nearby object may look the same as a large, distant object. Without additional evidence,
