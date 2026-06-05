---
chunk_id: "book-ca4fca8dd8-chunk-1118"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1118
confidence: "first-pass"
extraction_method: "structured-local"
---

670
Chapter 19
Learning from Examples
4. Utility information indicating the desirability of world states.
5. Action-value information indicating the desirability of actions.
6. Goals that describe the most desirable states.
7. A problem generator, critic, and learning element that enable the system to improve.
Each of these components can be learned. Consider a self-driving car agent that learns by
observing a human driver. Every time the driver brakes, the agent might learn a condition–
action rule for when to brake (component 1). By seeing many camera images that it is told
contain buses, it can learn to recognize them (component 2). By trying actions and ob-
serving the results—for example, braking hard on a wet road—it can learn the effects of its
actions (component 3). Then, when it receives complaints from passengers who have been
thoroughly shaken up during the trip, it can learn a useful component of its overall utility
function (component 4).
The technology of machine learning has become a standard part of software engineering.
Any time you are building a software system, even if you don’t think of it as an AI agent,
components of the system can potentially be improved with machine learning. For example,
software to analyze images of galaxies under gravitational lensing was speeded up by a factor
of 10 million with a machine-learned model (Hezaveh et al., 2017), and energy use for cooling
data centers was reduced by 40% with another machine-learned model (Gao, 2014). Turing
Award winner David Patterson and Google AI head Jeff Dean declared the dawn of a “Golden
Age” for computer architecture due to machine learning (Dean et al., 2018).
We have seen several examples of models for agent components: atomic, factored, and
relational models based on logic or probability, and so on. Learning algorithms have been
devised for all of these.
This chapter assumes little prior knowledge on the part of the agent: it starts from scratch
Prior knowledge
and learns from the data. In Section 22.7.2 we consider transfer learning, in which knowl-
edge from one domain is transferred to a new domain, so that learning can proceed faster
with less data. We do assume, however, that the designer of the system chooses a model
framework that can lead to effective learning.
Going from a speciﬁc set of observations to a general rule is called induction; from the
observations that the sun rose every day in the past, we induce that the sun will come up
tomorrow. This differs from the deduction we studied in Chapter 7 because the inductive
conclusions may be incorrect, whereas deductive conclusions are guaranteed to be correct if
the premises are correct.
This chapter concentrates on problems where the input is a factored representation—a
vector of attribute values. It is also possible for the input to be any kind of data structure,
including atomic and relational.
When the output is one of a ﬁnite set of values (such as sunny/cloudy/rainy or true/false),
the learning problem is called classiﬁcation. When it is a number (such as tomorrow’s tem-
Classiﬁcation
perature, measured either as an integer or a real number), the learning problem has the (ad-
mittedly obscure1) name regression.
Regression
1
A better name would have been function approximation or numeric prediction. But in 1886 Francis Galton
wrote an inﬂuential article on the concept of regression to the mean (e.g., the children of tall parents are likely to
be taller than average, but not as tall as the parents). Galton showed plots with what he called “regression lines,”
and readers came to associate the word “regression” with the statistical technique of function approximation
rather than with the topic of regression to the mean.
