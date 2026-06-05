---
chunk_id: "book-ca4fca8dd8-chunk-1197"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1197
confidence: "first-pass"
extraction_method: "structured-local"
---

722
Chapter 19
Learning from Examples
We measure the success of this algorithm in terms of regret, which is deﬁned as the
Regret
number of additional mistakes we make compared to the expert who, in hindsight, had the
best prediction record. Let M∗be the number of mistakes made by the best expert. Then the
number of mistakes, M, made by the random weighted majority algorithm, is bounded by16
M < M∗ln(1/β)+lnK
1−β
.
This bound holds for any sequence of examples, even ones chosen by adversaries trying to
do their worst. To be speciﬁc, when there are K =10 experts, if we choose β =1/2 then our
number of mistakes is bounded by 1.39M∗+4.6, and if β =3/4 by 1.15M∗+9.2. In general,
if β is close to 1 then we are responsive to change over the long run; if the best expert changes,
we will pick up on it before too long. However, we pay a penalty at the beginning, when we
start with all experts trusted equally; we may accept the advice of the bad experts for too
long. When β is closer to 0, these two factors are reversed. Note that we can choose β so that
M gets asymptotically close to M∗in the long run; this is called no-regret learning (because
No-regret learning
the average amount of regret per trial tends to 0 as the number of trials increases).
Online learning is helpful when the data may be changing rapidly over time. It is also
useful for applications that involve a large collection of data that is constantly growing, even
if changes are gradual. For example, with a data set of millions of Web images, you wouldn’t
want to retrain from scratch every time a single new image is added. It would be more
practical to have an online algorithm that allows images to be added incrementally. For most
learning algorithms based on minimizing loss, there is an online version based on minimizing
regret. Many of these online algorithms come with guaranteed bounds on regret.
It may seem surprising that there are such tight bounds on how well we can do compared
to a panel of experts. What is even more surprising is that when such panels convene to
prognosticate about political contests or sporting events, the viewing public is so willing to
listen to their predictions and so uninterested in knowing their error rates.
19.9 Developing Machine Learning Systems
In this chapter we have concentrated on explaining the theory of machine learning. The
practice of using machine learning to solve practical problems is a separate discipline. Over
the last 50 years, the software industry has evolved a software development methodology that
makes it more likely that a (traditional) software project will be a success. But we are still
in the early stages of deﬁning a methodology for machine learning projects; the tools and
techniques are not as well-developed. Here is a breakdown of typical steps in the process.
19.9.1 Problem formulation
The ﬁrst step is to ﬁgure out what problem you want to solve. There are two parts to this.
First ask, “what problem do I want to solve for my users?” An answer such as “make it easier
for users to organize and access their photos” is too vague; “help a user ﬁnd all photos that
match a speciﬁc term, such as Paris” is better. Then ask, “what part(s) of the problem can be
solved by machine learning?” perhaps settling on “learn a function that maps a photo to a set
of labels; then, when given a label as a query, retrieve all photos with that label.”
16 Blum (1996) gives an elegant proof.
