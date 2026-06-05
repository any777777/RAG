---
chunk_id: "book-ca4fca8dd8-chunk-1206"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1206
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 727

Section 19.9
Developing Machine Learning Systems
727
Figure 19.27 A two-dimensional t-SNE map of the MNIST data set, a collection of 60,000
images of handwritten digits, each 28×28 pixels and thus 784 dimensions. You can clearly
see clusters for the ten digits, with a few confusions in each cluster; for example the top
cluster is for the digit 0, but within the bounds of the cluster are a few data points representing
the digits 3 and 6. The t-SNE algorithm ﬁnds a representation that accentuates the differences
between clusters.
The map can’t maintain all relationships between data points, but should have the prop-
erty that similar points in the original data set are close together in the map. A technique
called t-distributed stochastic neighbor embedding (t-SNE) does just that. Figure 19.27
T-distributed
stochastic neighbor
embedding (t-SNE)
shows a t-SNE map of the MNIST digit recognition data set. Data analysis and visualization
packages such as Pandas, Bokeh, and Tableau can make it easier to work with your data.
19.9.3 Model selection and training
With cleaned data in hand and an intuitive feel for it, it is time to build a model. That means
choosing a model class (random forests? deep neural networks? an ensemble?), training
your model with the training data, tuning any hyperparameters of the class (number of trees?
number of layers?) with the validation data, debugging the process, and ﬁnally evaluating the
model on the test data.
There is no guaranteed way to pick the best model class, but there are some rough guide-
lines. Random forests are good when there are a lot of categorical features and you believe
that many of them may be irrelevant. Nonparametric methods are good when you have a lot
of data and no prior knowledge, and when you don’t want to worry too much about choosing
just the right features (as long as there are fewer than 20 or so). However, nonparametric
methods usually give you a function h that is more expensive to run.

## Page 728
