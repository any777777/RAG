---
chunk_id: "book-ca4fca8dd8-chunk-1465"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1465
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.1
Language Models
883
Logistic regression on the other hand is a discriminative model. It learns a conditional
probability distribution P(C|W), meaning that it can assign categories given a sequence of
words, but it can’t generate random sentences. Generally, researchers have found that dis-
criminative models have a lower error rate, perhaps because they model the intended output
directly, and perhaps because they make it easier for an analyst to create additional features.
However, generative models tend to converge more quickly, and so may be preferred when
the available training time is short, or when there is limited training data.
24.1.7 Comparing language models
To get a feeling for what different n-gram models are like, we built unigram (i.e., bag-of-
words), bigram, trigram, and 4-gram models over the words in this book and then randomly
sampled word sequences from each of the four models:
• n = 1: logical are as are confusion a may right tries agent goal the was
• n = 2: systems are very similar computational approach would be represented
• n = 3: planning and scheduling are integrated the success of naive Bayes model is
• n = 4: taking advantage of the structure of Bayesian networks and developed various languages
for writing “templates” with logical variables, from which large networks could be constructed
automatically for each problem instance
From this small sample it should be clear that the unigram model is a very poor approximation
of either English in general or an AI textbook in particular, and that the 4-gram model is
imperfect but much better. Next, to demonstrate how samples switch between training sources
(and deﬁnitely not just for fun) we added the text of the King James Bible to the 4-gram model
yielding these random samples:
• Prove that any 3-SAT problem can be reduced to simpler ones using the laws of thy God.
• Masters, give unto your servants that which is true iff both P and Q in any model m by a simple
experiment: put your hand unto, ye and your households for it is pleasant.
• Many will intreat the LORD your God, Saying, No; but we will ignore this issue for now;
Chapters 7 and 8 suggest methods for compactly representing very large belief states.
• And it came to pass, as if it had no successors.
• The direct utility estimation is just an instance of the general or algorithm in which new function
symbols are constructed “on the ﬂy.” For example, the ﬁrst child of the Holy Ghost.
There is a limit to n-gram models—as n increases, they will produce language that is more
ﬂuent, but they tend to reproduce long passages from their training data verbatim, rather
than generate novel text. Language models with more complex representations of words and
context can do better. The rest of this chapter demonstrates how grammar can improve a
language model, and Chapter 25 shows how deep learning methods have recently produced
impressive language models. One such deep learning model, GPT-2, can produce ﬂuent En-
glish samples when given a prompt. We gave GPT-2 the ﬁrst two sentences of this paragraph
as a prompt; it produced the following two samples:
• Numerous studies have shown that the best language models that can generate language are
those that use neural networks, and in particular that use deep learning to model speech. I have
used one of these models to generate hundreds of sentences in multiple languages, and it has
the ability to generate almost perfect translations of my training sentences. It’s a great model
to have, and will save you a lot of time in the future when you need to translate between many
languages.
