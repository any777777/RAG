---
chunk_id: "book-ca4fca8dd8-chunk-1195"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1195
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.8
Ensemble Learning
721
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
Boosted decision stumps
Decision stump
 0.6
 0.65
 0.7
 0.75
 0.8
 0.85
 0.9
 0.95
 1
 0
 50
 100
 150
 200
Training/test accuracy
Number of hypotheses K
Training accuracy
Test accuracy
(a)
(b)
Figure 19.26 (a) Graph showing the performance of boosted decision stumps with K =5
versus unboosted decision stumps on the restaurant data. (b) The proportion correct on the
training set and the test set as a function of K, the number of hypotheses in the ensemble.
Notice that the test set accuracy improves slightly even after the training accuracy reaches 1,
i.e., after the ensemble ﬁts the data exactly.
hand, it is too strong an assumption: we know that there are correlations between the past and
the future, and in complex scenarios it is unlikely that we will capture all the data that would
make the future independent of the past given the data.
In this section we examine what to do when the data are not i.i.d.—when they can change
over time. In this case, it matters when we make a prediction, so we will adopt the perspective
called online learning: an agent receives an input xj from nature, predicts the corresponding
Online learning
yj, and then is told the correct answer. Then the process repeats with xj+1, and so on. One
might think this task is hopeless—if nature is adversarial, all the predictions may be wrong.
It turns out that there are some guarantees we can make.
Let us consider the situation where our input consists of predictions from a panel of
experts. For example, each day K pundits predict whether the stock market will go up or
down, and our task is to pool those predictions and make our own. One way to do this is
to keep track of how well each expert performs, and choose to believe them in proportion to
their past performance. This is called the randomized weighted majority algorithm. We
Randomized
weighted majority
algorithm
can describe it more formally:
Initialize a set of weights {w1,...,wK} all to 1.
for each problem to be solved do
1. Receive the predictions {ˆy1,..., ˆyK} from the experts.
2. Randomly choose an expert k∗in proportion to its weight: P(k)=wk.
3. yield ˆyk∗as the answer to this problem.
4. Receive the correct answer y.
5. For each expert k such that ˆyk ̸= y, update wk ←βwk
6. Normalize the weights so that ∑k wk =1.
Here β is a number, 0 < β < 1, that tells how much to penalize an expert for each mistake.
