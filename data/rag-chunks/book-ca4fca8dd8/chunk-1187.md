---
chunk_id: "book-ca4fca8dd8-chunk-1187"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1187
confidence: "first-pass"
extraction_method: "structured-local"
---

716
Chapter 19
Learning from Examples
default choice is that each split randomly picks √n attributes to consider for classiﬁcation
problems, or n/3 for regression problems.
A further improvement is to use randomness in selecting the split point value: for each
selected attribute, we randomly sample several candidate values from a uniform distribution
over the attribute’s range. Then we select the value that has the highest information gain.
That makes it more likely that every tree in the forest will be different. Trees constructed in
this fashion are called extremely randomized trees (ExtraTrees).
Extremely
randomized trees
(ExtraTrees)
Random forests are efﬁcient to create. You might think that it would take K times longer
to create an ensemble of K trees, but it is not that bad, for three reasons: (a) each split point
runs faster because we are considering fewer attributes, (b) we can skip the pruning step for
each individual tree, because the ensemble as a whole decreases overﬁtting, and (c) if we
happen to have K computers available, we can build all the trees in parallel. For example,
Adele Cutler reports that for a 100-attribute problem, if we have just three CPUs we can grow
a forest of K =100 trees in about the same time as it takes to create a single decision tree on
a single CPU.
All the hyperparameters of random forests can be trained by cross-validation: the number
of trees K, the number of examples used by each tree N (often expressed as a percentage of
the complete data set), the number of attributes used at each split point (often expressed as a
function of the total number of attributes, such as √n), and the number of random split points
tried if we are using ExtraTrees. In place of the regular cross-validation strategy, we could
measure the out-of-bag error: the mean error on each example, using only the trees whose
Out-of-bag error
example set didn’t include that particular example.
We have been warned that more complex models can be prone to overﬁtting, and ob-
served that to be true for decision trees, where we found that pruning was an answer to
prevent overﬁtting. Random forests are complex, unpruned models. Yet they are resistant to
overﬁtting. As you increase capacity by adding more trees to the forest they tend to improve
on validation-set error rate. The curve typically looks like Figure 19.9(b), not (a).
Breiman (2001) gives a mathematical proof that (in almost all cases) as you add more
trees to the forest, the error converges; it does not grow. One way to think of it is that the
random selection of attributes yields a variety of trees, thus reducing variance, but because we
don’t need to prune the trees, they can cover the full input space at higher resolution. Some
number of trees can cover unique cases that appear only a few times in the data, and their
votes can prove decisive, but they can be outvoted when they do not apply. That said, random
forests are not totally immune to overﬁtting. Although the error can’t increase in the limit,
that does not mean that the error will go to zero.
Random forests have been very successful across a wide variety of application prob-
lems. In Kaggle data science competitions they were the most popular approach of winning
teams from 2011 through 2014, and remain a common approach to this day (although deep
learning and gradient boosting have become even more common among recent winners).
The randomForest package in R has been a particular favorite. In ﬁnance, random forests
have been used for credit card default prediction, household income prediction, and option
pricing. Mechanical applications include machine fault diagnosis and remote sensing. Bioin-
formatic and medical applications include diabetic retinopathy, microarray gene expression,
mass spectrum protein expression analysis, biomarker discovery, and protein–protein inter-
action prediction.
