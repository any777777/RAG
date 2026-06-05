---
chunk_id: "book-ca4fca8dd8-chunk-1223"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1223
confidence: "first-pass"
extraction_method: "structured-local"
---

736
Chapter 19
Learning from Examples
colleagues (Boser et al., 1992). SVMs were made practical with the introduction of the soft-
margin classiﬁer for handling noisy data in a paper that won the 2008 ACM Theory and Prac-
tice Award (Cortes and Vapnik, 1995), and of the Sequential Minimal Optimization (SMO)
algorithm for efﬁciently solving SVM problems using quadratic programming (Platt, 1999).
SVMs have proven to be very effective for tasks such as text categorization (Joachims, 2001),
computational genomics (Cristianini and Hahn, 2007), and handwritten digit recognition of
DeCoste and Sch¨olkopf (2002).
As part of this process, many new kernels have been designed that work with strings,
trees, and other nonnumerical data types.
A related technique that also uses the kernel
trick to implicitly represent an exponential feature space is the voted perceptron (Freund
and Schapire, 1999; Collins and Duffy, 2002). Textbooks on SVMs include Cristianini and
Shawe-Taylor (2000) and Sch¨olkopf and Smola (2002). A friendlier exposition appears in
the AI Magazine article by Cristianini and Sch¨olkopf (2002). Bengio and LeCun (2007)
show some of the limitations of SVMs and other local, nonparametric methods for learning
functions that have a global structure but do not have local smoothness.
The ﬁrst mathematical proof of the value of an ensemble was Condorcet’s jury theorem
(1785), which proved that if jurors are independent and an individual juror has at least a 50%
chance of deciding a case correctly, then the more jurors you add, the better the chance of
deciding the case correctly. More recently, ensemble learning has become an increasingly
popular technique for improving the performance of learning algorithms.
The ﬁrst random forest algorithm, using random attribution selection, is by Ho (1995);
an independent version was introduced by Amit and Geman (1997). Breiman (2001) added
the ideas of bagging and “out-of-bag error.” Friedman (2001) introduced the terminology
Gradient Boosting Machine (GBM), expanding the approach to allow for multiclass classiﬁ-
cation, regression, and ranking problems.
Michel Kearns (1988) deﬁned the Hypothesis Boosting Problem: given a learner that
predicts only slightly better than random guessing, is it possible to derive a learner that per-
forms arbitrarily well? The problem was answered in the afﬁrmative in a theoretical paper
by Schapire (1990) that led to the ADABOOST algorithm Freund and Schapire (1996) and
to further theoretical work Schapire (2003). Friedman et al. (2000) explain boosting from
a statistician’s viewpoint. Chen and Guestrin (2016) describe the XGBOOST system, which
has been used with great success in many large-scale applications.
Online learning is covered in a survey by Blum (1996) and a book by Cesa-Bianchi and
Lugosi (2006). Dredze et al. (2008) introduce the idea of conﬁdence-weighted online learning
for classiﬁcation: in addition to keeping a weight for each parameter, they also maintain a
measure of conﬁdence, so that a new example can have a large effect on features that were
rarely seen before (and thus had low conﬁdence) and a small effect on common features that
have already been well estimated. Yu et al. (2011) describe how a team of students work
together to build an ensemble classiﬁer in the KDD competition. One exciting possibility
is to create an “outrageously large” mixture-of-experts ensemble that uses a sparse subset
of experts for each incoming example (Shazeer et al., 2017). Seni and Elder (2010) survey
ensemble methods.
In terms of practical advice for building machine learning systems, Pedro Domingos
describes a few things to know (2012). Andrew Ng gives hints for developing and debugging
a product using machine learning (Ng, 2019). O’Neil and Schutt (2013) describe the process
