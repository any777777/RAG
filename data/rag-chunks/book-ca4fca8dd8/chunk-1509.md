---
chunk_id: "book-ca4fca8dd8-chunk-1509"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1509
confidence: "first-pass"
extraction_method: "structured-local"
---

910
Chapter 25
Deep Learning for Natural Language Processing
Yesterday
they
cut
the
rope
Embedding
lookup
Embedding
lookup
Embedding
lookup
Embedding
lookup
Embedding
lookup
Hidden Layer 1
Class = PastTenseVerb
Hidden Layer 2
Output Layer
Figure 25.3 Feedforward part-of-speech tagging model. This model takes a 5-word window
as input and predicts the tag of the word in the middle—here, cut. The model is able to
account for word position because each of the 5 input embeddings is multiplied by a different
part of the ﬁrst hidden layer. The parameter values for the word embeddings and for the three
layers are all learned simultaneously during training.
suggests that this particular occurrence of cut is a past-tense verb; and we might hope, then,
that the embedding will capture the past-referring aspect of adverbs.
POS tagging serves as a good introduction to the application of deep learning to NLP,
without the complications of more complex tasks like question answering (see Section 25.5.3).
Given a corpus of sentences with POS tags, we learn the parameters for the word embeddings
and the POS tagger simultaneously. The process works as follows:
1. Choose the width w (an odd number of words) for the prediction window to be used
to tag each word. A typical value is w=5, meaning that the tag is predicted based on
the word plus the two words to the left and the two words to the right. Split every
sentence in your corpus into overlapping windows of length w. Each window produces
one training example consisting of the w words as input and the POS category of the
middle word as output.
2. Create a vocabulary of all of the unique word tokens that occur more than, say, 5 times
in the training data. Denote the total number of words in the vocabulary as v.
3. Sort this vocabulary in any arbitrary order (perhaps alphabetically).
4. Choose a value d as the size of each word embedding vector.
5. Create a new v-by-d weight matrix called E. This is the word embedding matrix. Row
i of E is the word embedding of the ith word in the vocabulary. Initialize E randomly
(or from pretrained vectors).
6. Set up a neural network that outputs a part of speech label, as shown in Figure 25.3. The
ﬁrst layer will consist of w copies of the embedding matrix. We might use two additional
hidden layers, z1 and z2 (with weight matrices W1 and W2, respectively), followed by

## Page 911
