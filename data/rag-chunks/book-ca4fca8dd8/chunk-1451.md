---
chunk_id: "book-ca4fca8dd8-chunk-1451"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1451
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 24.1
Language Models
875
• Natural language is ambiguous (“He saw her duck” can mean either that she owns a
waterfowl, or that she made a downwards evasive move) and vague (“That’s great!”
does not specify precisely how great it is, nor what it is).
• The mapping from symbols to objects is not formally deﬁned. In ﬁrst-order logic, two
uses of the symbol “Richard” must refer to the same person, but in natural language two
occurrences of the same word or phrase may refer to different things in the world.
If we can’t make a deﬁnitive Boolean distinction between grammatical and ungrammati-
cal strings, we can at least say how likely or unlikely each one is.
We deﬁne a language model as a probability distribution describing the likelihood of
Language model
any string. Such a model should say that “Do I dare disturb the universe?” has a reasonable
probability as a string of English, but “Universe dare the I disturb do?” is extremely unlikely.
With a language model, we can predict what words are likely to come next in a text, and
thereby suggest completions for an email or text message. We can compute which alterations
to a text would make it more probable, and thereby suggest spelling or grammar corrections.
With a pair of models, we can compute the most probable translation of a sentence. With
some example question/answer pairs as training data, we can compute the most likely answer
to a question. So language models are at the heart of a broad range of natural language tasks.
The language modeling task itself also serves as a common benchmark to measure progress
in language understanding.
Natural languages are complex, so any language model will be, at best, an approximation.
The linguist Edward Sapir said “No language is tyrannically consistent. All grammars leak”
(Sapir, 1921). The philosopher Donald Davidson said “there is no such thing as language, not
if a language is . . . a clearly deﬁned shared structure” (Davidson, 1986), by which he meant
there is no one deﬁnitive language model for English in the way that there is for Python 3.8;
we all have different models, but we still somehow manage to muddle through and commu-
nicate. In this section we cover simplistic language models that are clearly wrong, but still
manage to be useful for certain tasks.
24.1.1 The bag-of-words model
Section 12.6.1 explained how a naive Bayes model based on the presence of speciﬁc words
could reliably classify sentences into categories; for example sentence (1) below is catego-
rized as business, and (2) as weather.
1. Stocks rallied on Monday, with major indexes gaining 1% as optimism persisted over
the ﬁrst quarter earnings season.
2. Heavy rain continued to pound much of the east coast on Monday, with ﬂood warnings
issued in New York City and other locations.
This section revisits the naive Bayes model, casting it as a full language model. That means
we don’t just want to know what category is most likely for each sentence; we want a joint
probability distribution over all sentences and categories. That suggests we should consider
all the words in the sentence. Given a sentence consisting of the words w1,w2,...wN (which
we will write as w1:N, as in Chapter 14), the naive Bayes formula (Equation (12.21)) gives us
P(Class|w1:N) = α P(Class)∏
j
P(w j |Class).
The application of naive Bayes to strings of words is called the bag-of-words model. It is
Bag-of-words model
