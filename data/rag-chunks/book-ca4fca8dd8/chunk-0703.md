---
chunk_id: "book-ca4fca8dd8-chunk-0703"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 703
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 12.6
Naive Bayes Models
421
From Equation (12.20), we then obtain
P(Cause|e) = α∑
y
P(Cause)P(y|Cause)

∏
j
P(e j |Cause)

= αP(Cause)

∏
j
P(ej |Cause)

∑
y
P(y|Cause)
= αP(Cause)∏
j
P(ej |Cause)
(12.21)
where the last line follows because the summation over y is 1. Reinterpreting this equation
in words: for each possible cause, multiply the prior probability of the cause by the product
of the conditional probabilities of the observed effects given the cause; then normalize the
result. The run time of this calculation is linear in the number of observed effects and does
not depend on the number of unobserved effects (which may be very large in domains such
as medicine). We will see in the next chapter that this is a common phenomenon in proba-
bilistic inference: evidence variables whose values are unobserved usually “disappear” from
the computation altogether.
12.6.1 Text classiﬁcation with naive Bayes
Let’s see how a naive Bayes model can be used for the task of text classiﬁcation: given a
Text classiﬁcation
text, decide which of a predeﬁned set of classes or categories it belongs to. Here the “cause”
is the Category variable, and the “effect” variables are the presence or absence of certain key
words, HasWordi. Consider these two example sentences, taken from newspaper articles:
1. Stocks rallied on Monday, with major indexes gaining 1% as optimism persisted over
the ﬁrst quarter earnings season.
2. Heavy rain continued to pound much of the east coast on Monday, with ﬂood warnings
issued in New York City and other locations.
The task is to classify each sentence into a Category—the major sections of the newspa-
per: news, sports, business, weather, or entertainment. The naive Bayes model consists of
the prior probabilities P(Category) and the conditional probabilities P(HasWordi |Category).
For each category c, P(Category=c) is estimated as the fraction of all previously seen doc-
uments that are of category c. For example, if 9% of articles are about weather, we set
P(Category=weather)=0.09. Similarly, P(HasWordi |Category) is estimated as the fraction
of documents of each category that contain word i; perhaps 37% of articles about business
contain word 6, “stocks,” so P(HasWord6 =true|Category=business) is set to 0.37.8
To categorize a new document, we check which key words appear in the document and
then apply Equation (12.21) to obtain the posterior probability distribution over categories. If
we have to predict just one category, we take the one with the highest posterior probability.
Notice that, for this task, every effect variable is observed, since we can always tell whether
a given word appears in the document.
8
One needs to be careful not to assign probability zero to words that have not been seen previously in a given
category of documents, since the zero would wipe out all the other evidence in Equation (12.21). Just because
you haven’t seen a word yet doesn’t mean you will never see it. Instead, reserve a small portion of the probability
distribution to represent “previously unseen” words. See Chapter 21 for more on this issue in general, and
Section 24.1.4 for the particular case of word models.
