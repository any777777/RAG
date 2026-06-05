---
chunk_id: "book-ca4fca8dd8-chunk-1714"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1714
confidence: "first-pass"
extraction_method: "structured-local"
---

1046
Chapter 28
Philosophy, Ethics, and Safety of AI
disability, and familial status. Other local, state, and federal laws recognize other classes,
including sexual orientation, and pregnancy, marital, and veteran status. Is it fair that these
classes count for some laws and not others? International human rights law, which encom-
passes a broad set of protected classes, is a potential framework to harmonize protections
across various groups.
Even in the absence of societal bias, sample size disparity can lead to biased results.
Sample size disparity
In most data sets there will be fewer training examples of minority class individuals than
of majority class individuals. Machine learning algorithms give better accuracy with more
training data, so that means that members of minority classes will experience lower accuracy.
For example, Buolamwini and Gebru (2018) examined a computer vision gender identiﬁca-
tion service, and found that it had near-perfect accuracy for light-skinned males, and a 33%
error rate for dark-skinned females. A constrained model may not be able to simultaneously
ﬁt both the majority and minority class—a linear regression model might minimize average
error by ﬁtting just the majority class, and in an SVM model, the support vectors might all
correspond to majority class members.
Bias can also come into play in the software development process (whether or not the
software involves machine learning). Engineers who are debugging a system are more likely
to notice and ﬁx those problems that are applicable to themselves. For example, it is difﬁcult
to notice that a user interface design won’t work for colorblind people unless you are in fact
colorblind, or that an Urdu language translation is faulty if you don’t speak Urdu.
How can we defend against these biases? First, understand the limits of the data you are
using. It has been suggested that data sets (Gebru et al., 2018; Hind et al., 2018) and models
(Mitchell et al., 2019) should come with annotations: declarations of provenance, security,
conformity, and ﬁtness for use. This is similar to the data sheets that accompany electronic
Data sheet
components such as resistors; they allow designers to decide what components to use. In
addition to the data sheets, it is important to train engineers to be aware of issues of fairness
and bias, both in school and with on-the-job training. Having a diversity of engineers from
different backgrounds makes it easier for them to notice problems in the data or models. A
study by the AI Now Institute (West et al., 2019) found that only 18% of authors at leading
AI conferences and 20% of AI professors are women. Black AI workers are at less than 4%.
Rates at industry research labs are similar. Diversity could be increased by programs earlier
in the pipeline—in college or high school—and by greater awareness at the professional level.
Joy Buolamwini founded the Algorithmic Justice League to raise awareness of this issue and
develop practices for accountability.
A second idea is to de-bias the data (Zemel et al., 2013). We could over-sample from
minority classes to defend against sample size disparity. Techniques such as SMOTE, the
synthetic minority over-sampling technique (Chawla et al., 2002) or ADASYN, the adaptive
synthetic sampling approach for imbalanced learning (He et al., 2008), provide principled
ways of oversampling. We could examine the provenance of data and, for example, eliminate
examples from judges who have exhibited bias in their past court cases. Some analysts object
to the idea of discarding data, and instead would recommend building a hierarchical model of
the data that includes sources of bias, so they can be modeled and compensated for. Google
and NeurIPS have attempted to raise awareness of this issue by sponsoring the Inclusive
Images Competition, in which competitors train a network on a data set of labeled images
collected in North America and Europe, and then test it on images taken from all around the
