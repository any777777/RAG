---
chunk_id: "book-ca4fca8dd8-chunk-1528"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1528
confidence: "first-pass"
extraction_method: "structured-local"
---

922
Chapter 25
Deep Learning for Natural Language Processing
vectors—one for each word position. The input to the ﬁrst transformer layer is the sum of the
word embedding at position t plus the positional embedding corresponding to position t.
Figure 25.10 illustrates the transformer architecture for POS tagging, applied to the same
sentence used in Figure 25.3. At the bottom, the word embedding and the positional embed-
dings are summed to form the input for a three-layer transformer. The transformer produces
one vector per word, as in RNN-based POS tagging. Each vector is fed into a ﬁnal output
layer and softmax layer to produce a probability distribution over the tags.
In this section, we have actually only told half the transformer story: the model we de-
scribed here is called the transformer encoder. It is useful for text classiﬁcation tasks. The
Transformer encoder
full transformer architecture was originally designed as a sequence-to-sequence model for
machine translation. Therefore, in addition to the encoder, it also includes a transformer
decoder. The encoder and decoder are nearly identical, except that the decoder uses a ver-
Transformer decoder
sion of self-attention where each word can only attend to the words before it, since text is
generated left-to-right. The decoder also has a second attention module in each transformer
layer that attends to the output of the transformer encoder.
25.5 Pretraining and Transfer Learning
Getting enough data to build a robust model can be a challenge. In computer vision (see
Chapter 27), that challenge was addressed by assembling large collections of images (such as
ImageNet) and hand-labeling them.
For natural language, it is more common to work with text that is unlabeled. The dif-
ference is in part due to the difﬁculty of labeling: an unskilled worker can easily label an
image as “cat” or “sunset,” but it requires extensive training to annotate a sentence with part-
of-speech tags or parse trees. The difference is also due to the abundance of text: the Internet
adds over 100 billion words of text each day, including digitized books, curated resources
such as Wikipedia, and uncurated social media posts.
Projects such as Common Crawl provide easy access to this data. Any running text can
be used to build n-gram or word embedding models, and some text comes with structure that
can be helpful for a variety of tasks—for example, there are many FAQ sites with question-
answer pairs that can be used to train a question-answering system. Similarly, many Web
sites publish side-by-side translations of texts, which can be used to train machine translation
systems. Some text even comes with labels of a sort, such as review sites where users annotate
their text reviews with a 5-star rating system.
We would prefer not to have to go to the trouble of creating a new data set every time
we want a new NLP model. In this section, we introduce the idea of pretraining: a form
Pretraining
of transfer learning (see Section 22.7.2) in which we use a large amount of shared general-
domain language data to train an initial version of an NLP model. From there, we can use a
smaller amount of domain-speciﬁc data (perhaps including some labeled data) to reﬁne the
model. The reﬁned model can learn the vocabulary, idioms, syntactic structures, and other
linguistic phenomena that are speciﬁc to the new domain.
25.5.1 Pretrained word embeddings
In Section 25.1, we brieﬂy introduced word embeddings. We saw that how similar words
like banana and apple end up with similar vectors, and we saw that we can solve analogy
