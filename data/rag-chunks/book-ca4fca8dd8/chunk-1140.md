---
chunk_id: "book-ca4fca8dd8-chunk-1140"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1140
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.4
Model Selection and Optimization
685
function MODEL-SELECTION(Learner,examples,k) returns a (hypothesis, error rate) pair
err←an array, indexed by size, storing validation-set error rates
training set, test set←a partition of examples into two sets
for size = 1 to ∞do
err[size]←CROSS-VALIDATION(Learner,size,training set,k)
if err is starting to increase signiﬁcantly then
best size←the value of size with minimum err[size]
h←Learner(best size,training set)
return h, ERROR-RATE(h, test set)
function CROSS-VALIDATION(Learner,size,examples,k) returns error rate
N ←the number of examples
errs←0
for i = 1 to k do
validation set←examples[(i −1) × N/k:i × N/k]
training set←examples −validation set
h←Learner(size,training set)
errs←errs + ERROR-RATE(h,validation set)
return errs / k
// average error rate on validation sets, across k-fold cross-validation
Figure 19.8 An algorithm to select the model that has the lowest validation error. It builds
models of increasing complexity, and choosing the one with best empirical error rate, err,
on the validation data set. Learner(size,examples) returns a hypothesis whose complexity
is set by the parameter size, and which is trained on examples. In CROSS-VALIDATION,
each iteration of the for loop selects a different slice of the examples as the validation set,
and keeps the other examples as the training set. It then returns the average validation set
error over all the folds. Once we have determined which value of the size parameter is best,
MODEL-SELECTION returns the model (i.e., learner/hypothesis) of that size, trained on all
the training examples, along with its error rate on the held-out test examples.
than decision trees based on something that we know about the problem. And part is quan-
titative and empirical: within the class of polynomials, we might select Degree = 2, because
that value performs best on the validation data set.
19.4.1 Model selection
Figure 19.8 describes a simple MODEL-SELECTION algorithm. It takes as argument a learn-
ing algorithm, Learner (for example, it could be LEARN-DECISION-TREE). Learner takes
one hyperparameter, which is named size in the ﬁgure. For decision trees it could be the
number of nodes in the tree; for polynomials size would be Degree. MODEL-SELECTION
starts with the smallest value of size, yielding a simple model (which will probably underﬁt
the data) and iterates through larger values of size, considering more complex models. In
the end MODEL-SELECTION selects the model that has the lowest average error rate on the
held-out validation data.
In Figure 19.9 we see two typical patterns that occur in model selection. In both (a)
and (b) the training set error decreases monotonically (with slight random ﬂuctuation) as we
