---
chunk_id: "book-ca4fca8dd8-chunk-1281"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1281
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 779

Section 21.2
Learning with Complete Data
779
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
 1
 0
 20
 40
 60
 80
 100
Proportion correct on test set
Training set size
Decision tree
Naive Bayes
Figure 21.3 The learning curve for naive Bayes learning applied to the restaurant problem
from Chapter 19; the learning curve for decision tree learning is shown for comparison.
A discriminative model directly learns the decision boundary between classes. That is,
Discriminative model
it learns P(Category|Inputs). Given example inputs, a discriminative model will come up
with an output category, but you cannot use a discriminative model to, say, generate random
words that are representative of a category. Logistic regression, decision trees, and support
vector machines are all discriminative models.
Since discriminative models put all their emphasis on deﬁning the decision boundary—
that is, actually doing the classiﬁcation task they were asked to do—they tend to perform
better in the limit, with an arbitrary amount of training data. However, with limited data, in
some cases a generative model performs better. (Ng and Jordan, 2002) compare the generative
naive Bayes classiﬁer to the discriminative logistic regression classiﬁer on 15 (small) data
sets, and ﬁnd that with the maximum amount of data, the discriminative model does better on
9 out of 15 data sets, but with only a small amount of data, the generative model does better
on 14 out of 15 data sets.
21.2.4 Maximum-likelihood parameter learning: Continuous models
Continuous probability models such as the linear–Gaussian model were shown on page 440.
Because continuous variables are ubiquitous in real-world applications, it is important to
know how to learn the parameters of continuous models from data.
The principles for
maximum-likelihood learning are identical in the continuous and discrete cases.
Let us begin with a very simple case: learning the parameters of a Gaussian density
function on a single variable. That is, we assume the data are generated as follows:
P(x) =
1
σ
√
2π
e−(x−µ)2
2σ2 .
The parameters of this model are the mean µ and the standard deviation σ. (Notice that the
normalizing “constant” depends on σ, so we cannot ignore it.) Let the observed values be

## Page 780
