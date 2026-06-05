---
chunk_id: "book-ca4fca8dd8-chunk-1157"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1157
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 694

694
Chapter 19
Learning from Examples
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
Decision tree
Decision list
Figure 19.12 Learning curve for DECISION-LIST-LEARNING algorithm on the restaurant
data. The curve for LEARN-DECISION-TREE is shown for comparison; decision trees do
slightly better on this particular problem.
constructs the remainder of the decision list, using just the remaining examples. This is
repeated until there are no examples left. The algorithm is shown in Figure 19.11.
This algorithm does not specify the method for selecting the next test to add to the de-
cision list. Although the formal results given earlier do not depend on the selection method,
it would seem reasonable to prefer small tests that match large sets of uniformly classiﬁed
examples, so that the overall decision list will be as compact as possible. The simplest strat-
egy is to ﬁnd the smallest test t that matches any uniformly classiﬁed subset, regardless of
the size of the subset. Even this approach works quite well, as Figure 19.12 suggests. For
this problem, the decision tree learns a bit faster than the decision list, but has more variation.
Both methods are over 90% accurate after 100 trials.
19.6 Linear Regression and Classiﬁcation
Now it is time to move on from decision trees and lists to a different hypothesis space, one
that has been used for hundreds of years: the class of linear functions of continuous-valued
Linear function
inputs. We’ll start with the simplest case: regression with a univariate linear function, oth-
erwise known as “ﬁtting a straight line.” Section 19.6.3 covers the multivariable case. Sec-
tions 19.6.4 and 19.6.5 show how to turn linear functions into classiﬁers by applying hard and
soft thresholds.
19.6.1 Univariate linear regression
A univariate linear function (a straight line) with input x and output y has the form y=w1x+
w0, where w0 and w1 are real-valued coefﬁcients to be learned. We use the letter w because
we think of the coefﬁcients as weights; the value of y is changed by changing the relative
Weight
weight of one term or another. We’ll deﬁne w to be the vector ⟨w0,w1⟩, and deﬁne the linear
function with those weights as
hw(x)=w1x+w0 .

## Page 695
