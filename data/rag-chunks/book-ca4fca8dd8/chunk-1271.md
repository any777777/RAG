---
chunk_id: "book-ca4fca8dd8-chunk-1271"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1271
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 21
LEARNING PROBABILISTIC MODELS
In which we view learning as a form of uncertain reasoning from observations, and devise
models to represent the uncertain world.
Chapter 12 pointed out the prevalence of uncertainty in real environments. Agents can handle
uncertainty by using the methods of probability and decision theory, but ﬁrst they must learn
their probabilistic theories of the world from experience. This chapter explains how they
can do that, by formulating the learning task itself as a process of probabilistic inference
(Section 21.1). We will see that a Bayesian view of learning is extremely powerful, providing
general solutions to the problems of noise, overﬁtting, and optimal prediction. It also takes
into account the fact that a less-than-omniscient agent can never be certain about which theory
of the world is correct, yet must still make decisions by using some theory of the world.
We describe methods for learning probability models—primarily Bayesian networks—in
Sections 21.2 and 21.3. Some of the material in this chapter is fairly mathematical, although
the general lessons can be understood without plunging into the details. It may beneﬁt the
reader to review Chapters 12 and 13 and peek at Appendix A.
21.1 Statistical Learning
The key concepts in this chapter, just as in Chapter 19, are data and hypotheses. Here, the
data are evidence—that is, instantiations of some or all of the random variables describing the
domain. The hypotheses in this chapter are probabilistic theories of how the domain works,
including logical theories as a special case.
Consider a simple example. Our favorite surprise candy comes in two ﬂavors: cherry
(yum) and lime (ugh). The manufacturer has a peculiar sense of humor and wraps each piece
of candy in the same opaque wrapper, regardless of ﬂavor. The candy is sold in very large
bags, of which there are known to be ﬁve kinds—again, indistinguishable from the outside:
h1: 100% cherry,
h2: 75% cherry + 25% lime,
h3: 50% cherry + 50% lime,
h4: 25% cherry + 75% lime,
h5: 100% lime.
Given a new bag of candy, the random variable H (for hypothesis) denotes the type of the
bag, with possible values h1 through h5. H is not directly observable, of course. As the
pieces of candy are opened and inspected, data are revealed—D1, D2, ..., DN, where each Di
is a random variable with possible values cherry and lime. The basic task faced by the agent

## Page 773
