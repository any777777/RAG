---
chunk_id: "book-ca4fca8dd8-chunk-1189"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1189
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.8
Ensemble Learning
717
19.8.3 Stacking
Whereas bagging combines multiple base models of the same model class trained on different
data, the technique of stacked generalization (or stacking for short) combines multiple base
Stacked
generalization
models from different model classes trained on the same data. For example, suppose we are
given the restaurant data set, the ﬁrst row of which is shown here:
x1 =Yes, No, No, Yes, Some, $$$, No, Yes, French, 0–10;y1 =Yes
We separate the data into training, validation, and test sets and use the training set to train,
say, three separate base models—an SVM model, a logistic regression model, and a decision
tree model.
In the next step we take the validation data set and augment each row with the predictions
made from the three base models, giving us rows that look like this (where the predictions
are shown in bold):
x2 =Yes, No, No, Yes, Full, $, No, No, Thai, 30–60, Yes, No, No;y2 =No
We use this validation set to train a new ensemble model, let’s say a logistic regression model
(but it need not be one of the base model classes). The ensemble model can use the predictions
and the original data as it sees ﬁt. It might learn a weighted average of the base models, for
example that the predictions should be weighted in a ratio of 50%:30%:20%. Or it might
learn nonlinear interactions between the data and the predictions, perhaps trusting the SVM
model more when the wait time is long, for example. We used the same training data to train
each of the base models, and then used the held-out validation data (plus predictions) to train
the ensemble model. It is also possible to use cross-validation if desired.
The method is called “stacking” because it can be thought of as a layer of base models
with an ensemble model stacked above it, operating on the output of the base models. In fact,
it is possible to stack multiple layers, each one operating on the output of the previous layer.
Stacking reduces bias, and usually leads to performance that is better than any of the individ-
ual base models. Stacking is frequently used by winning teams in data science competitions
(such as Kaggle and the KDD Cup), because individuals can work independently, each reﬁn-
ing their own base model, and then come together to build the ﬁnal stacked ensemble model.
19.8.4 Boosting
The most popular ensemble method is called boosting. To understand how it works, we
Boosting
need ﬁrst to introduce the idea of a weighted training set, in which each example has an
Weighted training
set
associated weight w j ≥0 that describes how much the example should count during training.
For example, if one example had a weight of 3 and the other examples all had a weight of 1,
that would be equivalent to having 3 copies of the one example in the training set.
Boosting starts with equal weights w j =1 for all the examples. From this training set, it
generates the ﬁrst hypothesis, h1. In general, h1 will classify some of the training examples
correctly and some incorrectly. We would like the next hypothesis to do better on the misclas-
siﬁed examples, so we increase their weights while decreasing the weights of the correctly
classiﬁed examples.
From this new weighted training set, we generate hypothesis h2. The process continues in
this way until we have generated K hypotheses, where K is an input to the boosting algorithm.
Examples that are difﬁcult to classify will get increasingly larger weights until the algorithm
is forced to create a hypothesis that classiﬁes them correctly. Note that this is a greedy
