---
chunk_id: "book-ca4fca8dd8-chunk-1142"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1142
confidence: "first-pass"
extraction_method: "structured-local"
---

686
Chapter 19
Learning from Examples
 0
 10
 20
 30
 40
 50
 60
 1
 2
 3
 4
 5
 6
 7
 8
 9
 10
Error rate (%)
Tree size in nodes
Validation Set Error
Training Set Error
 0
 10
 20
 30
 40
 50
 60
 10
 100
 1000
Error rate (%)
Thousands of parameters
Validation Set Error
Training Set Error
(a)
(b)
Figure 19.9 Error rates on training data (lower, green line) and validation data (upper, orange
line) for models of different complexity on two different problems. MODEL-SELECTION
picks the hyperparameter value with the lowest validation-set error. In (a) the model class is
decision trees and the hyperparameter is the number of nodes. The data is from a version of
the restaurant problem. The optimal size is 7. In (b) the model class is convolutional neural
networks (see Section 22.3) and the hyperparameter is the number of regular parameters in
the network. The data is the MNIST data set of images of digits; the task is to identify each
digit. The optimal number of parameters is 1,000,000 (note the log scale).
increase the complexity of the model. Complexity is measured by the number of decision tree
nodes in (a) and by the number of neural network parameters (wi) in (b). For many model
classes, the training set error reaches zero as the complexity increases.
The two cases differ markedly in validation set error. In (a) we see a U-shaped validation-
error curve: error decreases for a while as model complexity increases, but then we reach a
point where the model begins to overﬁt, and validation error rises. MODEL-SELECTION
picks the value at the bottom of the U-shaped validation-error curve: in this case a tree with
size 7. This is the spot that best balances underﬁtting and overﬁtting. In (b) we see an initial
U-shaped curve just as in (a) but then the validation error starts to decrease again; the lowest
validation error rate is the ﬁnal point in the plot, with 1,000,000 parameters.
Why are some validation-error curves like (a) and some like (b)? It comes down to how
the different model classes make use of excess capacity, and how well that matches up with
the problem at hand. As we add capacity to a model class, we often reach the point where
all the training examples can be represented perfectly within the model. For example, given
a training set with n distinct examples, there is always a decision tree with n leaf nodes that
can represent all the examples.
We say that a model that exactly ﬁts all the training data has interpolated the data.5
Interpolated
Model classes typically start to overﬁt as the capacity approaches the point of interpolation.
That seems to be because most of the model’s capacity is concentrated on the training ex-
amples, and the capacity that remains is allocated rather randomly in a way that is not rep-
resentative of the patterns in the validation data set. Some model classes never recover from
5
Some authors say the model has “memorized” the data.
