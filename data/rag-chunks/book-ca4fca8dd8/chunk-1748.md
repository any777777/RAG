---
chunk_id: "book-ca4fca8dd8-chunk-1748"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1748
confidence: "first-pass"
extraction_method: "structured-local"
---

1064
Chapter 29
The Future of AI
and a single-chip version may reach $10 per unit (Poulton and Watts, 2016). Radar sensors,
once capable of only coarse-grained detection, are now sensitive enough to count the number
of sheets in a stack of paper (Yeo et al., 2018).
The demand for better image processing in cellphone cameras has given us inexpensive
high-resolution cameras for use in robotics. MEMS (micro-electromechanical systems) tech-
nology has supplied miniaturized accelerometers, gyroscopes, and actuators small enough to
ﬁt in artiﬁcial ﬂying insects (Floreano et al., 2009; Fuller et al., 2014). It may be possible to
combine millions of MEMS devices to produce powerful macroscopic actuators. 3-D printing
(Muth et al., 2014) and bioprinting (Kolesky et al., 2014) have made it easier to experiment
with prototypes.
Thus, we see that AI systems are at the cusp of moving from primarily software-only sys-
tems to useful embedded robotic systems. The state of robotics today is roughly comparable
to the state of personal computers in the early 1980s: at that time personal computers were
becoming available, but it would take another decade before they became commonplace. It is
likely that ﬂexible, intelligent robots will ﬁrst make strides in industry (where environments
are more controlled, tasks are more repetitive, and the value of an investment is easier to
measure) before the home market (where there is more variability in environment and tasks).
Representing the state of the world
Keeping track of the world requires perception as well as updating of internal representations.
Chapter 4 showed how to keep track of atomic state representations; Chapter 7 described
how to do it for factored (propositional) state representations; Chapter 10 extended this to
ﬁrst-order logic; and Chapter 14 described probabilistic reasoning over time in uncertain
environments. Chapter 22 introduced recurrent neural networks, which are also capable of
maintaining a state representation over time.
Current ﬁltering and perception algorithms can be combined to do a reasonable job of rec-
ognizing objects (“that’s a cat”) and reporting low-level predicates (“the cup is on the table”).
Recognizing higher-level actions, such as “Dr. Russell is having a cup of tea with Dr. Norvig
while discussing plans for next week,” is more difﬁcult. Currently it can sometimes be done
(see Figure 27.17 on page 1015) given enough training examples, but future progress will
require techniques that generalize to novel situations without requiring exhaustive examples
(Poppe, 2010; Kang and Wildes, 2016).
Another problem is that although the approximate ﬁltering algorithms from Chapter 14
can handle quite large environments, they are still dealing with a factored representation—
they have random variables, but do not represent objects and relations explicitly. Also, their
notion of time is restricted to step-by-step change; given the recent trajectory of a ball, we
can predict where it will be at time t + 1, but it is difﬁcult to represent the abstract idea that
what goes up must come down.
Section 18.1 explained how probability and ﬁrst-order logic can be combined to solve
these problems; Section 18.2 showed how we can handle uncertainty about the identity of
objects; and Chapter 27 showed how recurrent neural networks enable computer vision to
track the world; but we don’t yet have a good way of putting all these techniques together.
Chapter 25 showed how word embeddings and similar representations can free us from the
strict bounds of concepts deﬁned by necessary and sufﬁcient conditions. It remains a daunting
task to deﬁne general, reusable representation schemes for complex domains.
