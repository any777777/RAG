---
chunk_id: "book-ca4fca8dd8-chunk-1532"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1532
confidence: "first-pass"
extraction_method: "structured-local"
---

924
Chapter 25
Deep Learning for Natural Language Processing
near “chalcogenide,” “band gap,” and “optoelectric,” which are all clues enabling it to be
classiﬁed as similar to “thermoelectric.” Furthermore, when trained only on abstracts up
to the year 2008 and asked to pick compounds that are “thermoelectric” but have not yet
appeared in abstracts, three of the model’s top ﬁve picks were discovered to be thermoelectric
in papers published between 2009 and 2019.
25.5.2 Pretrained contextual representations
Word embeddings are better representations than atomic word tokens, but there is an impor-
tant issue with polysemous words. For example, the word rose can refer to a ﬂower or the
past tense of rise. Thus, we expect to ﬁnd at least two entirely distinct clusters of word con-
texts for rose: one similar to ﬂower names such as dahlia, and one similar to upsurge. No
single embedding vector can capture both of these simultaneously. Rose is a clear example of
a word with (at least) two distinct meanings, but other words have subtle shades of meaning
that depend on context, such as the word need in you need to see this movie versus humans
need oxygen to survive. And some idiomatic phrases like break the bank are better analyzed
as a whole rather than as component words.
Therefore, instead of just learning a word-to-embedding table, we want to train a model to
generate contextual representations of each word in a sentence. A contextual representation
Contextual
representations
maps both a word and the surrounding context of words into a word embedding vector. In
other words, if we feed this model the word rose and the context the gardener planted a rose
bush, it should produce a contextual embedding that is similar (but not necessarily identical)
to the representation we get with the context the cabbage rose had an unusual fragrance, and
very different from the representation of rose in the context the river rose ﬁve feet.
Figure 25.11 shows a recurrent network that creates contextual word embeddings—the
boxes that are unlabeled in the ﬁgure. We assume we have already built a collection of
noncontextual word embeddings. We feed in one word at a time, and ask the model to predict
the next word. So for example in the ﬁgure at the point where we have reached the word
“car,” the the RNN node at that time step will receive two inputs: the noncontextual word
embedding for “car” and the context, which encodes information from the previous words
“The red.” The RNN node will then output a contextual representation for “car.” The network
as a whole then outputs a prediction for the next word, “is.” We then update the network’s
weights to minimize the error between the prediction and the actual next word.
This model is similar to the one for POS tagging in Figure 25.5, with two important
differences. First, this model is unidirectional (left-to-right), whereas the POS model is bidi-
rectional. Second, instead of predicting the POS tags for the current word, this model predicts
the next word using the prior context. Once the model is built, we can use it to retrieve rep-
resentations for words and pass them on to some other task; we need not continue to predict
the next word. Note that computing a contextual representations always requires two inputs,
the current word and the context.
25.5.3 Masked language models
A weakness of standard language models such as n-gram models is that the contextualization
of each word is based only on the previous words of the sentence. Predictions are made from
left to right. But sometimes context from later in a sentence—for example, feet in the phrase
rose ﬁve feet—helps to clarify earlier words.
