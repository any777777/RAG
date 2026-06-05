---
chunk_id: "book-ca4fca8dd8-chunk-1521"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1521
confidence: "first-pass"
extraction_method: "structured-local"
---

## Page 917

Section 25.3
Sequence-to-Sequence Models
917
(a)
The
front
door
is
red
<start>
La
La
puerta
Source
LSTM
Source
LSTM
Source
LSTM
Source
LSTM
Source
LSTM
Target
Attentional
LSTM
Target
Attentional
LSTM
…
La
puerta
de
entrada
es
roja
The
front
door
is
red
(b)
Figure 25.7 (a) Attentional sequence-to-sequence model for English-to-Spanish translation.
The dashed lines represent attention. (b) Example of attention probability matrix for a bilin-
gual sentence pair, with darker boxes representing higher values of aij. The attention proba-
bilities sum to one over each column.
this would cause a huge increase in the number of weights, with a concomitant increase in
computation time and potentially overﬁtting as well. Instead, we can take advantage of the
fact that when the target RNN is generating the target one word at a time, it is likely that only
a small part of the source is actually relevant to each target word.
Crucially, the target RNN must pay attention to different parts of the source for every
word. Suppose a network is trained to translate English to Spanish. It is given the words
“The front door is red” followed by an end of sentence marker, which means it is time to start
outputting Spanish words. So ideally it should ﬁrst pay attention to “The” and generate “La,”
then pay attention to “door” and output “puerta,” and so on.
We can formalize this concept with a neural network component called attention, which
Attention
can be used to create a “context-based summarization” of the source sentence into a ﬁxed-
dimensional representation. The context vector ci contains the most relevant information
for generating the next target word, and will be used as an additional input to the target
RNN. A sequence-to-sequence model that uses attention is called an attentional sequence-
to-sequence model. If the standard target RNN is written as:
Attentional
sequence-to-
sequence
model
hi = RNN(hi−1,xi),
the target RNN for attentional sequence-to-sequence models can be written as:
hi = RNN(hi−1,[xi;ci])
where [xi;ci] is the concatenation of the input and context vectors, ci, deﬁned as:
ri j = hi−1 ·sj
ai j = erij/(∑
k
erik)
ci = ∑
j
aij ·sj

## Page 918
