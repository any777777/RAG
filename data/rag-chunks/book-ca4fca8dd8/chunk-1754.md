---
chunk_id: "book-ca4fca8dd8-chunk-1754"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1754
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 29.1
AI Components
1067
need advances in transfer learning so that we can take advantage of data in one domain to
improve performance on a related domain.
The vast majority of machine learning research today assumes a factored representation,
learning a function h : Rn →R for regression and h : Rn →{0,1} for classiﬁcation. Machine
learning has been less successful for problems that have only a small amount of data, or
problems that require the construction of new structured, hierarchical representations. Deep
learning, especially with convolutional networks applied to computer vision problems, has
demonstrated some success in going from low-level pixels to intermediate-level concepts like
Eye and Mouth, then to Face, and ﬁnally to Person or Cat.
A challenge for the future is to more smoothly combine learning and prior knowledge.
If we give a computer a problem it has not encountered before—say, recognizing different
models of cars—we don’t want the system to be powerless until it has been fed millions of
labeled examples.
The ideal system should be able to draw on what it already knows: it should already have
a model of how vision works, and how the design and branding of products in general work;
now it should use transfer learning to apply that to the new problem of car models. It should
be able to ﬁnd on its own information about car models, drawing from text, images, and
video available on the Internet. It should be capable of apprenticeship learning: having a
conversation with a teacher, and not just asking “may I have a thousand images of a Corolla,”
but rather being able to understand advice like “the Insight is similar to the Prius, but the
Insight has a larger grille.” It should know that each model comes in a small range of possible
colors, but that a car can be repainted, so there is a chance that it might see a car in a color
that was not in the training set. (If it didn’t know that, it should be capable of learning it, or
being told about it.)
All this requires a communication and representation language that humans and comput-
ers can share; we can’t expect a human analyst to directly modify a model with millions of
weights. Probabilistic models (including probabilistic programming languages) give humans
some ability to describe what we know, but these models are not yet well integrated with
other learning mechanisms.
The work of Bengio and LeCun (2007) is one step towards this integration. Recently
Yann LeCun has suggested that the term “deep learning” should be replaced with the more
general differentiable programming (Siskind and Pearlmutter, 2016; Li et al., 2018); this
Diﬀerentiable
programming
suggests that our general programming languages and our machine learning models could be
merged together.
Right now, it is common to build a deep learning model that is differentiable, and thus can
be trained to minimize loss, and retrained when circumstances change. But that deep learning
model is only one part of a larger software system that takes in data, massages the data, feeds
it to the model, and ﬁgures out what to do with the model’s output. All these other parts of the
larger system were written by hand by a programmer, and thus are nondifferentiable, which
means that when circumstances change, it is up to the programmer to recognize any problems
and ﬁx them by hand. With differentiable programming, the hope is that the entire system is
subject to automated optimization.
The end goal is to be able to express what we know in whatever form is convenient to us:
informal advice given in natural language, a strong mathematical law like F = ma, a statistical
model accompanied by data, or a probabilistic program with unknown parameters that can
