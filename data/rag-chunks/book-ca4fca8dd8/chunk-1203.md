---
chunk_id: "book-ca4fca8dd8-chunk-1203"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1203
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 19.9
Developing Machine Learning Systems
725
When data are limited, data augmentation can help. For example, with a data set of
Data augmentation
images, you can create multiple versions of each image by rotating, translating, cropping, or
scaling each image, or by changing the brightness or color balance or adding noise. As long
as these are small changes, the image label should remain the same, and a model trained on
such augmented data will be more robust.
Sometimes data are plentiful but are classiﬁed into unbalanced classes. For example,
Unbalanced classes
a training set of credit card transactions might consist of 10,000,000 valid transactions and
1,000 fraudulent ones. A classiﬁer that says “valid” regardless of the input will achieve
99.99% accuracy on this data set. To go beyond that, a classiﬁer will have to pay more
attention to the fraudulent examples. To help it do that, you can undersample the majority
Undersampling
class (i.e., ignore some of the “valid” class examples) or over-sample the minority class (i.e.,
Over-sample
duplicate some of the “fraudulent” class examples). You can use a weighted loss function
that gives a larger penalty to missing a fraudulent case.
Boosting can also help you focus on the minority class. If you are using an ensemble
method, you can change the rules by which the ensemble votes and give “fraudulent” as the
response even if only a minority of the ensemble votes for “fraudulent.” You can help balance
unbalanced classes by generating synthetic data with techniques such as SMOTE (Chawla
et al., 2002) or ADASYN (He et al., 2008).
You should carefully consider outliers in your data. An outlier is a data point that is
Outlier
far from other points. For example, in the restaurant problem, if price were a numeric value
rather than a categorical one, and if one example had a price of $316 while all the others
were $30 or less, that example would be an outlier. Methods such as linear regression are
susceptible to outliers because they must form a single global linear model that takes all
inputs into account—they can’t treat the outlier differently from other example points, and
thus a single outlier can have a large effect on all the parameters of the model.
With attributes like price that are positive numbers, we can diminish the effect of outliers
by transforming the data, taking the logarithm of each value, so $20, $25, and $316 become
1.3, 1.4, and 2.5. This makes sense from a practical point of view because the high value now
has less inﬂuence on the model, and from a theoretical point of view because, as we saw in
Section 15.3.2, the utility of money is logarithmic.
Methods such as decision trees that are built from multiple local models can treat outliers
individually: it doesn’t matter if the biggest value is $300 or $31; either way it can be treated
in its own local node after a test of the form cost ≤30. That makes decision trees (and thus
random forests and gradient boosting) more robust to outliers.
Feature engineering
After correcting overt errors, you may also want to preprocess your data to make it easier to
digest. We have already seen the process of quantization: forcing a continuous valued input,
such as the wait time, into ﬁxed bins (0–10 minutes, 10–30, 30–60, or >60). Domain knowl-
edge can tell you what thresholds are important, such as comparing age ≥18 when studying
voting patterns. We also saw (page 706) that nearest-neighbor algorithms perform better
when data are normalized to have a standard deviation of 1. With categorical attributes such
as sunny/cloudy/rainy, it is often helpful to transform the data into three separate Boolean
attributes, exactly one of which is true (we call this a one-hot encoding). This is particularly
One-hot encoding
useful when the machine learning model is a neural network.
