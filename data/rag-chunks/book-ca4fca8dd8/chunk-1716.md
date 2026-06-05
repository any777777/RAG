---
chunk_id: "book-ca4fca8dd8-chunk-1716"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1716
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 28.3
The Ethics of AI
1047
world. The issue is that given this data set, it is easy to apply the label “bride” to a woman
in a standard Western wedding dress, but harder to recognize traditional African and Indian
matrimonial dress.
A third idea is to invent new machine learning models and algorithms that are more resis-
tant to bias; and the ﬁnal idea is to let a system make initial recommendations that may be bi-
ased, but then train a second system to de-bias the recommendations of the ﬁrst one. Bellamy
et al. (2018) introduced the IBM AI FAIRNESS 360 system, which provides a framework for
all of these ideas. We expect there will be increased use of tools like this in the future.
How do you make sure that the systems you build will be fair? A set of best practices has
been emerging (although they are not always followed):
• Make sure that the software engineers talk with social scientists and domain experts to
understand the issues and perspectives, and consider fairness from the start.
• Create an environment that fosters the development of a diverse pool of software engi-
neers that are representative of society.
• Deﬁne what groups your system will support: different language speakers, different age
groups, different abilities with sight and hearing, etc.
• Optimize for an objective function that incorporates fairness.
• Examine your data for prejudice and for correlations between protected attributes and
other attributes.
• Understand how any human annotation of data is done, design goals for annotation
accuracy, and verify that the goals are met.
• Don’t just track overall metrics for your system; make sure you track metrics for sub-
groups that might be victims of bias.
• Include system tests that reﬂect the experience of minority group users.
• Have a feedback loop so that when fairness problems come up, they are dealt with.
28.3.4 Trust and transparency
It is one challenge to make an AI system accurate, fair, safe, and secure; a different chal-
lenge to convince everyone else that you have done so. People need to be able to trust the
Trust
systems they use. A PwC survey in 2017 found that 76% of businesses were slowing the
adoption of AI because of trustworthiness concerns. In Section 19.9.4 we covered some of
the engineering approaches to trust; here we discuss the policy issues.
To earn trust, any engineered systems must go through a veriﬁcation and validation
Veriﬁcation and
validation
(V&V) process. Veriﬁcation means that the product satisﬁes the speciﬁcations. Validation
means ensuring that the speciﬁcations actually meet the needs of the user and other affected
parties. We have an elaborate V&V methodology for engineering in general, and for tradi-
tional software development done by human coders; much of that is applicable to AI systems.
But machine learning systems are different and demand a different V&V process, which has
not yet been fully developed. We need to verify the data that these systems learn from; we
need to verify the accuracy and fairness of the results, even in the face of uncertainty that
makes an exact result unknowable; and we need to verify that adversaries cannot unduly
inﬂuence the model, nor steal information by querying the resulting model.
One instrument of trust is certiﬁcation; for example, Underwriters Laboratories (UL)
Certiﬁcation
was founded in 1894 at a time when consumers were apprehensive about the risks of electric
