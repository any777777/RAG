---
chunk_id: "book-ca4fca8dd8-chunk-1138"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1138
confidence: "first-pass"
extraction_method: "structured-local"
---

684
Chapter 19
Learning from Examples
The next step is to deﬁne “optimal ﬁt.” For now, we will say that the optimal ﬁt is the
hypothesis that minimizes the error rate: the proportion of times that h(x) ̸= y for an (x,y)
Error rate
example. (Later we will expand on this to allow different errors to have different costs, in
effect giving partial credit for answers that are “almost” correct.) We can estimate the error
rate of a hypothesis by giving it a test: measure its performance on a test set of examples. It
would be cheating for a hypothesis (or a student) to peek at the test answers before taking the
test. The simplest way to ensure this doesn’t happen is to split the examples you have into
two sets: a training set to create the hypothesis, and a test set to evaluate it.
If we are only going to create one hypothesis, then this approach is sufﬁcient. But often
we will end up creating multiple hypotheses: we might want to compare two completely
different machine learning models, or we might want to adjust the various “knobs” within
one model. For example, we could try different thresholds for χ2 pruning of decision trees,
or different degrees for polynomials. We call these “knobs” hyperparameters—parameters
Hyperparameters
of the model class, not of the individual model.
Suppose a researcher generates a hypotheses for one setting of the χ2 pruning hyperpa-
rameter, measures the error rates on the test set, and then tries different hyperparameters. No
individual hypothesis has peeked at the test set data, but the overall process did, through the
researcher.
The way to avoid this is to really hold out the test set—lock it away until you are
completely done with training, experimenting, hyperparameter-tuning, re-training, etc. That
means you need three data sets:
1. A training set to train candidate models.
2. A validation set, also known as a development set or dev set, to evaluate the candidate
Validation set
models and choose the best one.
3. A test set to do a ﬁnal unbiased evaluation of the best model.
What if we don’t have enough data to make all three of these data sets? We can squeeze more
out of the data using a technique called k-fold cross-validation. The idea is that each example
K-fold
cross-validation
serves double duty—as training data and validation data—but not at the same time. First we
split the data into k equal subsets. We then perform k rounds of learning; on each round 1/k
of the data are held out as a validation set and the remaining examples are used as the training
set. The average test set score of the k rounds should then be a better estimate than a single
score. Popular values for k are 5 and 10—enough to give an estimate that is statistically likely
to be accurate, at a cost of 5 to 10 times longer computation time. The extreme is k = n, also
known as leave-one-out cross-validation or LOOCV. Even with cross-validation, we still
LOOCV
need a separate test set.
In Figure 19.1 (page 672) we saw a linear function underﬁt the data set, and a high-
degree polynomial overﬁt the data. We can think of the task of ﬁnding a good hypothesis
as two subtasks: model selection4 chooses a good hypothesis space, and optimization (also
Model selection
Optimization
called training) ﬁnds the best hypothesis within that space.
Part of model selection is qualitative and subjective: we might select polynomials rather
4
Although the name “model selection” is in common use, a better name would have been “model class selec-
tion” or “hypothesis space selection.” The word “model” has been used in the literature to refer to three different
levels of speciﬁcity: a broad hypothesis space (like “polynomials”), a hypothesis space with hyperparameters
ﬁlled in (like “degree-2 polynomials”), and a speciﬁc hypothesis with all parameters ﬁlled in (like 5x2 +3x−2).
