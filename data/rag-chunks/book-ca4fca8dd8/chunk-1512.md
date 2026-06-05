---
chunk_id: "book-ca4fca8dd8-chunk-1512"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1512
confidence: "first-pass"
extraction_method: "structured-local"
---

912
Chapter 25
Deep Learning for Natural Language Processing
Δ
Figure 25.4 (a) Schematic diagram of an RNN where the hidden layer z has recurrent con-
nections; the ∆symbol indicates a delay. Each input x is the word embedding vector of the
next word in the sentence. Each output y is the output for that time step. (b) The same net-
work unrolled over three timesteps to create a feedforward network. Note that the weights
are shared across all timesteps.
In Section 22.6, we introduced the recurrent neural network or RNN, which is designed
to process time-series data, one datum at a time. This suggests that RNNs might be useful for
processing language, one word at a time. We repeat Figure 22.8 here as Figure 25.4.
In an RNN language model each input word is encoded as a word embedding vector, xi.
There is a hidden layer zt which gets passed as input from one time step to the next. We are
interested in doing multiclass classiﬁcation: the classes are the words of the vocabulary. Thus
the output yt will be a softmax probability distribution over the possible values of the next
word in the sentence.
The RNN architecture solves the problem of too many parameters. The number of param-
eters in the weight matrixes w,z,z, w,x,z, and w,z,y stays constant, regardless of the number of
words—it is O(1). This is in contrast to feedforward networks, which have O(n) parameters,
and n-gram models, which have O(vn) parameters, where v is the size of the vocabulary.
The RNN architecture also solves the problem of asymmetry, because the weights are the
same for every word position.
The RNN architecture can sometimes solve the limited context problem as well. In theory
there is no limit to how far back in the input the model can look. Each update of the hidden
layer zt has access to both the current input word xt and the previous hidden layer zt−1,
which means that information about any word in the input can be kept in the hidden layer
indeﬁnitely, copied over (or modiﬁed as appropriate) from one time step to the next. Of
course, there is a limited amount of storage in z, so it can’t remember everything about all the
previous words.
In practice RNN models perform well on a variety of tasks, but not on all tasks. It can be
hard to predict whether they will be succesful for a given problem. One factor that contributes
to success is that the training process encourages the network to allocate storage space in z to
the aspects of the input that will actually prove to be useful.
To train an RNN language model, we use the training process described in Section 22.6.1.
The inputs, xt, are the words in a training corpus of text, and the observed outputs are the same
