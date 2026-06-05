---
chunk_id: "book-ca4fca8dd8-chunk-1527"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1527
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 921

Section 25.4
The Transformer Architecture
921
Transformer
Layer
Input Vectors
Output Vectors
Feedforward
+
+
Self-Attention
Residual
Connection
Residual
Connection
Figure 25.9 A single-layer transformer consists of self-attention, a feedforward network,
and residual connections.
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
Positional
Embedding 1
Positional
Embedding 2
Positional
Embedding 3
Positional
Embedding 4
Positional
Embedding 5
Feedforward
Feedforward
Feedforward
Feedforward
Feedforward
Class =
Adverb
Class =
Pronoun
Class =
PastTenseVerb
Class =
Determiner
Class =
Noun
Transformer Layer
Transformer Layer
Transformer Layer
+
+
+
+
+
Figure 25.10 Using the transformer architecture for POS tagging.
have six or more layers. As with the other models that we’ve learned about, the output of
layer i is used as the input to layer i+1.
The transformer architecture does not explicitly capture the order of words in the se-
quence, since context is modeled only through self-attention, which is agnostic to word order.
To capture the ordering of the words, the transformer uses a technique called positional em-
bedding. If our input sequence has a maximum length of n, then we learn n new embedding
Positional
embedding

## Page 922
