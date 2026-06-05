---
chunk_id: "book-ca4fca8dd8-chunk-1191"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1191
confidence: "first-pass"
extraction_method: "structured-local"
---

718
Chapter 19
Learning from Examples
algorithm in the sense that it does not backtrack; once it has chosen a hypothesis hi it will
never undo that choice; rather it will add new hypotheses. It is also a sequential algorithm, so
we can’t compute all the hypotheses in parallel as we could with bagging.
The ﬁnal ensemble lets each hypothesis vote, as in bagging, except that each hypothesis
gets a weighted number of votes—the hypotheses that did better on their respective weighted
training sets are given more voting weight. For regression or binary classiﬁcation we have
h(x) =
K
∑
i=1
zihi(x)
where zi is the weight of the ith hypothesis. (This weighting of hypotheses is distinct from
the weighting of examples.)
Figure 19.24 shows how the algorithm works conceptually. There are many variants of
the basic boosting idea, with different ways of adjusting the example weights and combining
the hypotheses. The variants all share the general idea that difﬁcult examples get more weight
as we move from one hypothesis to the next. Like the Bayesian learning methods we will see
in Chapter 21, they also give more weight to more accurate hypotheses.
One speciﬁc algorithm, called ADABOOST, is shown in Figure 19.25. It is usually ap-
plied with decision trees as the component hypotheses; often the trees are limited in size.
ADABOOST has a very important property: if the input learning algorithm L is a weak learn-
ing algorithm—which means that L always returns a hypothesis with accuracy on the training
Weak learning
set that is slightly better than random guessing (that is, 50%+ϵ for Boolean classiﬁcation)—
then ADABOOST will return a hypothesis that classiﬁes the training data perfectly for large
enough K. Thus, the algorithm boosts the accuracy of the original learning algorithm on the
training data.
In other words, boosting can overcome any amount of bias in the base model, as long
as the base model is ϵ better than random guessing. (In our pseudocode we stop generat-
ing hypotheses if we get one that is worse than random.) This result holds no matter how
inexpressive the original hypothesis space and no matter how complex the function being
learned. The exact formulas for weights in Figure 19.25 (with error/(1 −error, etc.) are
chosen to make the proof of this property easy (see Freund and Schapire, 1996). Of course,
this property does not guarantee accuracy on previously unseen examples.
Let us see how well boosting does on the restaurant data. We will choose as our original
hypothesis space the class of decision stumps, which are decision trees with just one test, at
Decision stump
the root. The lower curve in Figure 19.26(a) shows that unboosted decision stumps are not
very effective for this data set, reaching a prediction performance of only 81% on 100 training
examples. When boosting is applied (with K =5), the performance is better, reaching 93%
after 100 examples.
An interesting thing happens as the ensemble size K increases. Figure 19.26(b) shows the
training set performance (on 100 examples) as a function of K. Notice that the error reaches
zero when K is 20; that is, a weighted-majority combination of 20 decision stumps sufﬁces
to ﬁt the 100 examples exactly—this is the interpolation pont. As more stumps are added to
the ensemble, the error remains at zero. The graph also shows that the test set performance
▶
continues to increase long after the training set error has reached zero. At K = 20, the test
performance is 0.95 (or 0.05 error), and the performance increases to 0.98 as late as K = 137,
before gradually dropping to 0.95.
