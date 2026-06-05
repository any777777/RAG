---
chunk_id: "book-ca4fca8dd8-chunk-1520"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1520
confidence: "first-pass"
extraction_method: "structured-local"
---

916
Chapter 25
Deep Learning for Natural Language Processing
we have to process the entire source sentence before starting to generate the target. In other
words, the generation of each target word is conditional on the entire source sentence and on
all previously generated target words.
This gives text generation for MT a close connection to a standard RNN language model,
as described in Section 25.2. Certainly, if we had trained an RNN on English text, it would
be more likely to generate “big dog” than “dog big.” However, we don’t want to generate
just any random target language sentence; we want to generate a target language sentence
that corresponds to the source language sentence. The simplest way to do that is to use two
RNNs, one for the source and one for the target. We run the source RNN over the source
sentence and then use the ﬁnal hidden state from the source RNN as the initial hidden state
for the target RNN. This way, each target word is implicitly conditioned on both the entire
source sentence and the previous target words.
This neural network architecture is called a basic sequence-to-sequence model, an ex-
Sequence-to-
sequence
model
ample of which is shown in Figure 25.6. Sequence-to-sequence models are most commonly
used for machine translation, but can also be used for a number of other tasks, like automati-
cally generating a text caption from an image, or summarization: rewriting a long text into a
shorter one that maintains the same meaning.
Basic sequence-to-sequence models were a signiﬁcant breakthrough in NLP and MT
speciﬁcally. According to Wu et al. (2016b) the approach led to a 60% error reduction over
the previous MT methods. But these models suffer from three major shortcomings:
• Nearby context bias: whatever RNNs want to remember about the past, they have to ﬁt
into their hidden state. For example, let’s say an RNN is processing word (or timestep)
57 in a 70-word sequence. The hidden state will likely contain more information about
the word at timestep 56 than the word at timestep 5, because each time the hidden vector
is updated it has to replace some amount of existing information with new information.
This behavior is part of the intentional design of the model, and often makes sense for
NLP, since nearby context is typically more important. However, far-away context can
be crucial as well, and can get lost in an RNN model; even LSTMs have difﬁculty with
this task.
• Fixed context size limit: In an RNN translation model the entire source sentence is
compressed into a single ﬁxed-dimensional hidden state vector. An LSTM used in
a state-of-the-art NLP model typically has around 1024 dimensions, and if we have to
represent, say, a 64-word sentence in 1024 dimensions, this only gives us 16 dimensions
per word—not enough for complex sentences. Increasing the hidden state vector size
can lead to slow training and overﬁtting.
• Slower sequential processing: As discussed in Section 22.3, neural networks realize
considerable efﬁciency gains by processing the training data in batches so as to take
advantage of efﬁcient hardware support for matrix arithmetic. RNNs, on the other hand,
seem to be constrained to operate on the training data one word at a time.
25.3.1 Attention
What if the target RNN were conditioned on all of the hidden vectors from the source RNN,
rather than just the last one? This would mitigate the shortcomings of nearby context bias and
ﬁxed context size limits, allowing the model to access any previous word equally well. One
way to achieve this access is to concatenate all of the source RNN hidden vectors. However,
