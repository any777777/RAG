---
chunk_id: "ml-07-07-improve-nn-performance-b48fd9de83-chunk-0003"
source_id: "ml-07-07-improve-nn-performance-b48fd9de83"
source_file: "_ML_07_07_Improve NN performance.pdf"
source_type: "pdf"
topics:
  - "Machine Learning"
chunk_index: 3
confidence: "first-pass"
extraction_method: "structured-local"
---

Cross Validation
•
Often the availability of training data is limited, and it is not practical to take a large part of it for a
validation set.
–
An alternative is to use the procedure of cross-validation.
•
In K-fold cross-validation the full set of training data is randomly divided into K distinct subsets, and
the network is trained using K–1 subsets, and tested on the remaining subset.
–
The process of training and testing is then repeated for each of the K possible choices of the subset omitted
from the training.
–
The average performance on the K omitted subsets is then the estimate of the generalization performance.
•
This procedure has the advantage that is allows the use of a high proportion of the available
training data (a fraction 1–1/K) for training, while making use of all the data points in estimating the
generalization error.
•
The disadvantage is that the network needs to be trained K times.
–
Typically K ~ 10 is considered reasonable.
•
If K is made equal to the full sample size, it is called leave-one-out cross validation.

## Page 6

Optimal Network Architectures
•
Identifying
a
good
neural
network
architecture
(e.g.,
setting
an
appropriate number of hidden units) is clearly very important, but it is also
very problem dependent.
•
There are various different criteria for what is optimal.
– Usually
it
is
the
generalization
ability,
but
learning
time,
memory
requirements, and so on, may also be important.
•
In the same way that we can have our networks learn their weights
incrementally, we can modify our network architecture, to suit its given
task, in an incremental fashion.
•
There are two obvious ways to proceed:
1. Start with too few hidden units, and add some more ⇒Constructive algorithms
2. Start with too many hidden units, and take some away ⇒Pruning algorithms

## Page 7
