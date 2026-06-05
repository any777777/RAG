---
chunk_id: "book-ca4fca8dd8-chunk-1518"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1518
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 25.3
Sequence-to-Sequence Models
915
Source
LSTM
Source
LSTM
Target
LSTM
Source
LSTM
Source
LSTM
Target
LSTM
Target
LSTM
Target
LSTM
Target
LSTM
The
man
is
tall
<start>
El
hombre
es
alto
El
hombre
es
alto
<end>
Figure 25.6 Basic sequence-to-sequence model. Each block represents one LSTM timestep.
(For simplicity, the embedding and output layers are not shown.) On successive steps we feed
the network the words of the source sentence “The man is tall,” followed by the <start> tag
to indicate that the network should start producing the target sentence. The ﬁnal hidden state
at the end of the source sentence is used as the hidden state for the start of the target sentence.
After that, each target sentence word at time t is used as input at time t +1, until the network
produces the <end> tag to indicate that sentence generation is ﬁnished.
a message from one time step to the next. Rather, an LSTM can choose to remember some
parts of the input, copying it over to the next timestep, and to forget other parts. Consider a
language model handling a text such as
The athletes, who all won their local qualiﬁers and advanced to the ﬁnals in Tokyo, now ...
At this point if we asked the model which next word was more probable, “compete” or “com-
petes,” we would expect it to pick “compete” because it agrees with the subject “The athletes.”
An LSTM can learn to create a latent feature for the subject person and number and copy that
feature forward without alteration until it is needed to make a choice like this. A regular
RNN (or an n-gram model for that matter) often gets confused in long sentences with many
intervening words between the subject and verb.
25.3 Sequence-to-Sequence Models
One of the most widely studied tasks in NLP is machine translation (MT), where the goal
Machine translation
(MT)
is to translate a sentence from a source language to a target language—for example, from
Source language
Target language
Spanish to English. We train an MT model with a large corpus of source/target sentence pairs.
The goal is to then accurately translate new sentences that are not in our training data.
Can we use RNNs to create an MT system? We can certainly encode the source sentence
with an RNN. If there were a one-to-one correspondence between source words and target
words, then we could treat MT as a simple tagging task—given the source word “perro” in
Spanish, we tag it as the corresponding English word “dog.” But in fact, words are not one-
to-one: in Spanish the three words “caballo de mar” corresponds to the single English word
“seahorse,” and the two words “perro grande” translate to “big dog,” with the word order
reversed. Word reordering can be even more extreme; in English the subject is usually at the
start of a sentence, but in Fijian the subject is usually at the end. So how do we generate a
sentence in the target language?
It seems like we should generate one word at a time, but keep track of the context so that
we can remember parts of the source that haven’t been translated yet, and keep track of what
has been translated so that we don’t repeat ourselves. It also seems that for some sentences
