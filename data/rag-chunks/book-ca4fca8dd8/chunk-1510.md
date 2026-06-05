---
chunk_id: "book-ca4fca8dd8-chunk-1510"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1510
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 25.2
Recurrent Neural Networks for NLP
911
a softmax layer yielding an output probability distribution ˆy over the possible part-of-
speech categories for the middle word:
z1 = σ(W1x)
z2 = σ(W2z1)
ˆy = softmax(Woutz2).
7. To encode a sequence of w words into an input vector, simply look up the embedding
for each word and concatenate the embedding vectors. The result is a real-valued in-
put vector x of length wd. Even though a given word will have the same embedding
vector whether it occurs in the ﬁrst position, the last, or somewhere in between, each
embedding will be multiplied by a different part of the ﬁrst hidden layer; therefore we
are implicitly encoding the relative position of each word.
8. Train the weights E and the other weight matrices W1, W2, and Wout using gradient
descent. If all goes well, the middle word, cut, will be labeled as a past-tense verb, based
on the evidence in the window, which includes the temporal past word “yesterday,” the
third-person subject pronoun “they” immediately before cut, and so on.
An alternative to word embeddings is a character-level model in which the input is a se-
quence of characters, each encoded as a one-hot vector. Such a model has to learn how
characters come together to form words. The majority of work in NLP sticks with word-level
rather than character-level encodings.
25.2 Recurrent Neural Networks for NLP
We now have a good representation for single words in isolation, but language consists of
an ordered sequence of words in which the context of surrounding words is important. For
simple tasks like part of speech tagging, a small, ﬁxed-size window of perhaps ﬁve words
usually provides enough context.
More complex tasks such as question answering or reference resolution may require
dozens of words as context. For example, in the sentence “Eduardo told me that Miguel
was very sick so I took him to the hospital,” knowing that him refers to Miguel and not
Eduardo requires context that spans from the ﬁrst to the last word of the 14-word sentence.
25.2.1 Language models with recurrent neural networks
We’ll start with the problem of creating a language model with sufﬁcient context. Recall that
a language model is a probability distribution over sequences of words. It allows us to predict
the next word in a text given all the previous words, and is often used as a building block for
more complex tasks.
Building a language model with either an n-gram model (as in Section 24.1) or a feedfor-
ward network with a ﬁxed window of n words can run into difﬁculty due to the problem of
context: either the required context will exceed the ﬁxed window size or the model will have
too many parameters, or both.
In addition, a feedforward network has the problem of asymmetry: whatever it learns
about, say, the appearance of the word him as the 12th word of the sentence it will have to
relearn for the appearance of him at other positions in the sentence, because the weights are
different for each word position.
