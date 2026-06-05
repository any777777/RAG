---
chunk_id: "book-ca4fca8dd8-chunk-1199"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1199
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.9
Developing Machine Learning Systems
723
To make this concrete, you need to specify a loss function for your machine learning
component, perhaps measuring the system’s accuracy at predicting a correct label. This ob-
jective should be correlated with your true goals, but usually will be distinct—the true goal
might be to maximize the number of users you gain and keep on your system, and the revenue
that they produce. Those are metrics you should track, but not necessarily ones that you can
directly build a machine learning model for.
When you have decomposed your problem into parts, you may ﬁnd that there are multiple
components that can be handled by old-fashioned software engineering, not machine learning.
For example, for a user who asks for “best photos,” you could implement a simple procedure
that sorts photos by the number of likes and views. Once you have developed your overall
system to the point where it is viable, you can then go back and optimize, replacing the simple
components with more sophisticated machine learning models.
Part of problem formulation is deciding whether you are dealing with supervised, unsu-
pervised, or reinforcement learning. The distinctions are not always so crisp. In semisuper-
vised learning we are given a few labeled examples and use them to mine more information
Semisupervised
learning
from a large collection of unlabeled examples. This has become a common approach, with
companies emerging whose missions are to quickly label some examples, in order to help
machine learning systems make better use of the remaining unlabeled examples.
Sometimes you have a choice of which approach to use. Consider a system to recommend
songs or movies to customers. We could approach this as a supervised learning problem,
where the inputs include a representation of the customer and the labeled output is whether
or not they liked the recommendation, or we could approach it as a reinforcement learning
problem, where the system makes a series of recommendation actions, and occasionally gets
a reward from the customer for making a good suggestion.
The labels themselves may not be the oracular truths that we hope for. Imagine that you
are trying to build a system to guess a person’s age from a photo. You gather some labeled
examples by having people upload photos and state their age. That’s supervised learning. But
in reality some of the people lied about their age. It’s not just that there is random noise in the
data; rather the inaccuracies are systematic, and to uncover them is an unsupervised learning
problem involving images, self-reported ages, and true (unknown) ages. Thus, both noise and
lack of labels create a continuum between supervised and unsupervised learning. The ﬁeld
of weakly supervised learning focuses on using labels that are noisy, imprecise, or supplied
Weakly supervised
learning
by non-experts.
19.9.2 Data collection, assessment, and management
Every machine learning project needs data; in the case of our photo identiﬁcation project there
are freely available image data sets, such as ImageNet, which has over 14 million photos with
ImageNet
about 20,000 different labels. Sometimes we may have to manufacture our own data, which
can be done by our own labor, or by crowdsourcing to paid workers or unpaid volunteers
operating over an Internet service. Sometimes data come from your users. For example, the
Waze navigation service encourages users to upload data about trafﬁc jams, and uses that to
provide up-to-date navigation directions for all users. Transfer learning (see Section 22.7.2)
can be used when you don’t have enough of your own data: start with a publicly available
general-purpose data set (or a model that has been pretrained on this data), and then add
speciﬁc data from your users and retrain.
