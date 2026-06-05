---
chunk_id: "book-ca4fca8dd8-chunk-1347"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1347
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.5
Generalization
821
be possible to alter just a few pixels in an image of a dog and cause the network to classify
the dog as an ostrich or a school bus—even though the altered image still looks exactly like a
dog. An altered image of this kind is called an adversarial example.
Adversarial example
In low-dimensional spaces it is hard to ﬁnd adversarial examples. But for an image with
a million pixel values, it is often the case that even though most of the pixels contribute to
the image being classiﬁed in the middle of the “dog” region of the space, there are a few
dimensions where the pixel value is near the boundary to another category. An adversary
with the ability to reverse engineer the network can ﬁnd the smallest vector difference that
would move the image over the border.
When adversarial examples were ﬁrst discovered, they set off two worldwide scrambles:
one to ﬁnd learning algorithms and network architectures that would not be susceptible to
adversarial attack, and another to create ever-more-effective adversarial attacks against all
kinds of learning systems. So far the attackers seem to be ahead. In fact, whereas it was
assumed initially that one would need access to the internals of the trained network in order
to construct an adversarial example speciﬁcally for that network, it has turned out that one
can construct robust adversarial examples that fool multiple networks with different architec-
tures, hyperparameters, and training sets. These ﬁndings suggest that deep learning models
recognize objects in ways that are quite different from the human visual system.
22.5.2 Neural architecture search
Unfortunately, we don’t yet have a clear set of guidelines to help you choose the best network
architecture for a particular problem. Success in deploying a deep learning solution requires
experience and good judgment.
From the earliest days of neural network research, attempts have been made to automate
the process of architecture selection. We can think of this as a case of hyperparameter tuning
(Section 19.4.4), where the hyperparameters determine the depth, width, connectivity, and
other attributes of the network. However, there are so many choices to be made that simple
approaches like grid search can’t cover all possibilities in a reasonable amount of time.
Therefore, it is common to use neural architecture search to explore the state space of
Neural architecture
search
possible network architectures. Many of the search techniques and learning techniques we
covered earlier in the book have been applied to neural architecture search.
Evolutionary algorithms have been popular because it is sensible to do both recombina-
tion (joining parts of two networks together) and mutation (adding or removing a layer or
changing a parameter value). Hill climbing can also be used with these same mutation op-
erations. Some researchers have framed the problem as reinforcement learning, and some
as Bayesian optimization. Another possibility is to treat the architectural possibilities as a
continuous differentiable space and use gradient descent to ﬁnd a locally optimal solution.
For all these search techniques, a major challenge is estimating the value of a candidate
network. The straightforward way to evaluate an architecture is to train it on a test set for
multiple batches and then evaluate its accuracy on a validation set. But with large networks
that could take many GPU-days.
Therefore, there have been many attempts to speed up this estimation process by elim-
inating or at least reducing the expensive training process. We can train on a smaller data
set. We can train for a small number of batches and predict how the network would improve
with more batches. We can use a reduced version of the network architecture that we hope
