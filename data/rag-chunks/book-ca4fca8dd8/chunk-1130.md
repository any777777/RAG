---
chunk_id: "book-ca4fca8dd8-chunk-1130"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1130
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.3
Learning Decision Trees
679
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
Figure 19.7 A learning curve for the decision tree learning algorithm on 100 randomly gen-
erated examples in the restaurant domain. Each data point is the average of 20 trials.
a case where the wait is 0–10 minutes but the restaurant is full. In that case it says not to wait
when Hungry is false, but SR would certainly wait. With more training examples the learning
program could correct this mistake.
We can evaluate the performance of a learning algorithm with a learning curve, as shown
Learning curve
in Figure 19.7. For this ﬁgure we have 100 examples at our disposal, which we split randomly
into a training set and a test set. We learn a hypothesis h with the training set and measure its
accuracy with the test set. We can do this starting with a training set of size 1 and increasing
one at a time up to size 99. For each size, we actually repeat the process of randomly splitting
into training and test sets 20 times, and average the results of the 20 trials. The curve shows
that as the training set size grows, the accuracy increases. (For this reason, learning curves
are also called happy graphs.) In this graph we reach 95% accuracy, and it looks as if the
Happy graphs
curve might continue to increase if we had more data.
19.3.3 Choosing attribute tests
The decision tree learning algorithm chooses the attribute with the highest IMPORTANCE. We
will now show how to measure importance, using the notion of information gain, which is de-
ﬁned in terms of entropy, which is the fundamental quantity in information theory (Shannon
Entropy
and Weaver, 1949).
Entropy is a measure of the uncertainty of a random variable; the more information, the
less entropy. A random variable with only one possible value—a coin that always comes
up heads—has no uncertainty and thus its entropy is deﬁned as zero. A fair coin is equally
likely to come up heads or tails when ﬂipped, and we will soon show that this counts as “1
bit” of entropy. The roll of a fair four-sided die has 2 bits of entropy, because there are 22
equally probable choices. Now consider an unfair coin that comes up heads 99% of the time.
Intuitively, this coin has less uncertainty than the fair coin—if we guess heads we’ll be wrong
only 1% of the time—so we would like it to have an entropy measure that is close to zero,
but positive. In general, the entropy of a random variable V with values vk having probability
