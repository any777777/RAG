---
chunk_id: "book-ca4fca8dd8-chunk-1121"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1121
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 672

672
Chapter 19
Learning from Examples
Data set 1
Linear
Sinusoidal
Piecewise linear
Degree-12 polynomial
Data set 2
Figure 19.1 Finding hypotheses to ﬁt data. Top row: four plots of best-ﬁt functions from
four different hypothesis spaces trained on data set 1. Bottom row: the same four functions,
but trained on a slightly different data set (sampled from the same f(x) function).
look for a best-ﬁt function for which each h(xi) is close to yi (in a way that we will formalize
in Section 19.4.2).
The true measure of a hypothesis is not how it does on the training set, but rather how
well it handles inputs it has not yet seen. We can evaluate that with a second sample of (xi,yi)
pairs called a test set. We say that h generalizes well if it accurately predicts the outputs of
Test set
Generalization
the test set.
Figure 19.1 shows that the function h that a learning algorithm discovers depends on the
hypothesis space H it considers and on the training set it is given. Each of the four plots in
the top row have the same training set of 13 data points in the (x,y) plane. The four plots
in the bottom row have a second set of 13 data points; both sets are representative of the
same unknown function f(x). Each column shows the best-ﬁt hypothesis h from a different
hypothesis space:
• Column 1: Straight lines; functions of the form h(x) = w1x+w0. There is no line that
would be a consistent hypothesis for the data points.
• Column 2: Sinusoidal functions of the form h(x) = w1x+sin(w0x). This choice is not
quite consistent, but ﬁts both data sets very well.
• Column 3: Piecewise-linear functions where each line segment connects the dots from
one data point to the next. These functions are always consistent.
• Column 4: Degree-12 polynomials, h(x) = ∑12
i=0 wixi. These are consistent: we can
always get a degree-12 polynomial to perfectly ﬁt 13 distinct points. But just because
the hypothesis is consistent does not mean it is a good guess.
One way to analyze hypothesis spaces is by the bias they impose (regardless of the train-
ing data set) and the variance they produce (from one training set to another).
By bias we mean (loosely) the tendency of a predictive hypothesis to deviate from the
Bias
expected value when averaged over different training sets. Bias often results from restrictions

## Page 673
