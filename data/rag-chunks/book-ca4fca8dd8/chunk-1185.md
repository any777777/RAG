---
chunk_id: "book-ca4fca8dd8-chunk-1185"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1185
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.8
Ensemble Learning
715
The second reason is to reduce variance. Consider an ensemble of K =5 binary classiﬁers
that we combine using majority voting. For the ensemble to misclassify a new example, at
least three of the ﬁve classiﬁers have to misclassify it. The hope is that this is less likely than
a single misclassiﬁcation by a single classiﬁer. To quantify that, suppose you have trained a
single classiﬁer that is correct in 80% of cases. Now create an ensemble of 5 classiﬁers, each
trained on a different subset of the data so that they are independent. Let’s assume this leads
to some reduction in quality, and each individual classiﬁer is correct in only 75% of cases.
But together, the majority vote of the ensemble will be correct in 89% of cases (and 99% with
17 classiﬁers), assuming true independence.
In practice the independence assumption is unreasonable—individual classiﬁers share
some of the same data and assumptions, and thus are not completely independent, and will
share some of the same errors. But if the component classiﬁers are at least somewhat un-
correlated then ensemble learning will make fewer misclassiﬁcations. We will now consider
four ways of creating ensembles: bagging, random forests, stacking, and boosting.
19.8.1 Bagging
In bagging,15 we generate K distinct training sets by sampling with replacement from the
Bagging
original training set. That is, we randomly pick N examples from the training set, but each
of those picks might be an example we picked before. We then run our machine learning
algorithm on the N examples to get a hypothesis. We repeat this process K times, getting K
different hypotheses. Then, when asked to predict the value of a new input, we aggregate
the predictions from all K hypotheses. For classiﬁcation problems, that means taking the
plurality vote (the majority vote for binary classiﬁcation). For regression problems, the ﬁnal
output is the average:
h(x) = 1
K
K
∑
i=1
hi(x)
Bagging tends to reduce variance and is a standard approach when there is limited data or
when the base model is seen to be overﬁtting. Bagging can be applied to any class of model,
but is most commonly used with decision trees. It is appropriate because decision trees are
unstable: a slightly different set of examples can lead to a wildly different tree. Bagging
smoothes out this variance. If you have access to multiple computers then bagging is efﬁcient,
because the hypotheses can be computed in parallel.
19.8.2 Random forests
Unfortunately, bagging decision trees often ends up giving us K trees that are highly corre-
lated. If there is one attribute with a very high information gain, it is likely to be the root of
most of the trees. The random forest model is a form of decision tree bagging in which we
Random forest
take extra steps to make the ensemble of K trees more diverse, to reduce variance. Random
forests can be used for classiﬁcation or regression.
The key idea is to randomly vary the attribute choices (rather than the training examples).
At each split point in constructing the tree, we select a random sampling of attributes, and then
compute which of those gives the highest information gain. If there are n attributes, a common
15 Note on terminology: In statistics, a sample with replacement is called a bootstrap, and “bagging” is short for
“bootstrap aggregating.”
