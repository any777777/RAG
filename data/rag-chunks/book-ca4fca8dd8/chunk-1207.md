---
chunk_id: "book-ca4fca8dd8-chunk-1207"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1207
confidence: "first-pass"
extraction_method: "structured-local"
---

728
Chapter 19
Learning from Examples
Logistic regression does well when the data are linearly separable, or can be converted
to be so with clever feature engineering. Support vector machines are a good method to try
when the data set is not too large; they perform similarly to logistic regression on separable
data and can be better for high-dimensional data. Problems dealing with pattern recognition,
such as image or speech processing, are most often approached with deep neural networks
(see Chapter 22).
Choosing hyperparameters can be done with a combination of experience—do what
worked well in similar past problems—and search: run experiments with multiple possi-
ble values for hyperparameters. As you run more experiments you will get ideas for different
models to try. However, if you measure performance on the validation data, get a new idea,
and run more experiments, then you run the risk of overﬁtting on the validation data. If you
have enough data, you may want to have several separate validation data sets to avoid this
problem. This is especially true if you inspect the validation data by eye, rather than just run
evaluations on it.
Suppose you are building a classiﬁer—for example a system to classify spam email. La-
beling a legitimate piece of mail as spam is called a false positive. There will be a tradeoff
False positive
between false positives and false negatives (labeling a piece of spam as legitimate); if you
want to keep more legitimate mail out of the spam folder, you will necessarily end up sending
more spam to the inbox. But what is the best way to make the tradeoff? You can try different
values of hyperparameters and get different rates for the two types of errors—different points
on this tradeoff. A chart called the receiver operating characteristic (ROC) curve plots
Receiver operating
characteristic (ROC)
curve
false positives versus true positives for each value of the hyperparameter, helping you visu-
alize values that would be good choices for the tradeoff. A metric called the “area under the
ROC curve” or AUC provides a single-number summary of the ROC curve, which is useful
AUC
if you want to deploy a system and let each user choose their tradeoff point.
Another helpful visualization tool for classiﬁcation problems is a confusion matrix: a
Confusion matrix
two-dimensional table of counts of how often each category is classiﬁed or misclassiﬁed as
each other category.
There can be tradeoffs in factors other than the loss function. If you can train a stock
market prediction model that makes you $10 on every trade, that’s great—but not if it costs
you $20 in computation cost for each prediction. A machine translation program that runs
on your phone and allows you to read signs in a foreign city is helpful—but not if it runs
down the battery after an hour of use. Keep track of all the factors that lead to acceptance or
rejection of your system, and design a process where you can quickly iterate the process of
getting a new idea, running an experiment, and evaluating the results of the experiment to see
if you have made progress. Making this iteration process fast is one of the most important
factors for success in machine learning.
19.9.4 Trust, interpretability, and explainability
We have described a machine learning methodology where you develop your model with
training data, choose hyperparameters with validation data, and get a ﬁnal metric with test
data. Doing well on that metric is a necessary but not sufﬁcient condition for you to trust
your model. And it is not just you—other stakeholders including regulators, lawmakers, the
press, and your users are also interested in the trustworthiness of your system (as well as in
related attributes such as reliability, accountability, and safety).
