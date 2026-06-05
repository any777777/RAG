---
chunk_id: "book-ca4fca8dd8-chunk-1533"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1533
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 925

Section 25.5
Pretraining and Transfer Learning
925
Feedforward
red
car
is
big
<eos>
The
red
car
is
big
Feedforward
Feedforward
Feedforward
Feedforward
Non-contextual
representations
(word embeddings)
Contextual
representations
(RNN output)
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
RNN
RNN
RNN
RNN
RNN
Figure 25.11 Training contextual representations using a left-to-right language model.
The
river
rose
five
feet
Embedding
lookup
RNN
Embedding
lookup
Embedding
lookup
Embedding
lookup
RNN
RNN
RNN
RNN
RNN
RNN
RNN
RNN
RNN
Feedforward
MLM
embedding
[masked]
Figure 25.12 Masked language modeling: pretrain a bidirectional model—for example, a
multilayer RNN—by masking input words and predicting only those masked words.
One straightforward workaround is to train a separate right-to-left language model that
contextualizes each word based on subsequent words in the sentence, and then concatenate
the left-to-right and right-to-left representations. However, such a model fails to combine
evidence from both directions.
Instead, we can use a masked language model (MLM). MLMs are trained by masking
Masked language
model (MLM)
(hiding) individual words in the input and asking the model to predict the masked words. For
this task, one can use a deep bidirectional RNN or transformer on top of the masked sentence.
For example, given the input sentence “The river rose ﬁve feet” we can mask the middle word
to get “The river
ﬁve feet” and ask the model to ﬁll in the blank.

## Page 926
