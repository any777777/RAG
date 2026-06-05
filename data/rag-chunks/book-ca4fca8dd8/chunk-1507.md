---
chunk_id: "book-ca4fca8dd8-chunk-1507"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1507
confidence: "first-pass"
extraction_method: "structured-local"
---

908
Chapter 25
Deep Learning for Natural Language Processing
eralization if we reduced this to a smaller-size vector, perhaps with just a few hundred di-
mensions. We call this smaller, dense vector a word embedding: a low-dimensional vector
Word embedding
representing a word. Word embeddings are learned automatically from the data. (We will see
later how this is done.) What are these learned word embeddings like? On the one hand, each
one is just a vector of numbers, where the individual dimensions and their numeric values do
not have discernible meanings:
“aardvark” =
[−0.7,+0.2,−3.2,...]
“abacus”
=
[+0.5,+0.9,−1.3,...]
···
“zyzzyva” = [−0.1,+0.8,−0.4,...].
On the other hand, the feature space has the property that similar words end up having similar
vectors. We can see that in Figure 25.1, where there are separate clusters for country, kinship,
transportation, and food words.
It turns out, for reasons we do not completely understand, that the word embedding vec-
tors have additional properties beyond mere proximity for similar words. For example, sup-
pose we look at the vectors A for Athens and B for Greece. For these words the vector
difference B−A seems to encode the country/capital relationship. Other pairs—France and
Paris, Russia and Moscow, Zambia and Lusaka—have essentially the same vector difference.
We can use this property to solve word analogy problems such as “Athens is to Greece
as Oslo is to [what]?” Writing C for the Oslo vector and D for the unknown, we hypothesize
that B −A=D −C, giving us D=C + (B −A). And when we compute this new vector D,
we ﬁnd that it is closer to “Norway” than to any other word. Figure 25.2 shows that this type
of vector arithmetic works for many relationships.
However, there is no guarantee that a particular word embedding algorithm run on a par-
ticular corpus will capture a particular semantic relationship. Word embeddings are popular
because they have proven to be a good representation for downstream language tasks (such
as question answering or translation or summarization), not because they are guaranteed to
answer analogy questions on their own.
Using word embedding vectors rather than one-hot encodings of words turns out to be
helpful for essentially all applications of deep learning to NLP tasks. Indeed, in many cases
it is possible to use generic pretrained vectors, obtained from any of several suppliers, for
one’s particular NLP task. At the time of writing, the commonly used vector dictionaries
include WORD2VEC, GloVe (Global Vectors), and FASTTEXT, which has embeddings for
157 languages. Using a pretrained model can save a great deal of time and effort. For more
on these resources, see Section 25.5.1.
It is also possible to train your own word vectors; this is usually done at the same time as
training a network for a particular task. Unlike generic pretrained embeddings, word embed-
dings produced for a speciﬁc task can be trained on a carefully selected corpus and will tend
to emphasize aspects of words that are useful for the task. Suppose, for example, that the
task is part-of-speech (POS) tagging (see Section 24.1.6). Recall that this involves predicting
the correct part of speech for each word in a sentence. Although this is a simple task, it is
nontrivial because many words can be tagged in multiple ways—for example, the word cut
can be a present-tense verb (transitive or intransitive), a past-tense verb, an inﬁnitive verb, a
past participle, an adjective, or a noun. If a nearby temporal adverb refers to the past, that
