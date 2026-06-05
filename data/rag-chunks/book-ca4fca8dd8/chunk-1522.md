---
chunk_id: "book-ca4fca8dd8-chunk-1522"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1522
confidence: "first-pass"
extraction_method: "structured-local"
---

918
Chapter 25
Deep Learning for Natural Language Processing
where hi−1 is the target RNN vector that is going to be used for predicting the word at timestep
i, and sj is the output of the source RNN vector for the source word (or timestep) j. Both hi−1
and sj are d-dimensional vectors, where d is the hidden size. The value of ri j is therefore the
raw “attention score” between the current target state and the source word j. These scores are
then normalized into a probability ai j using a softmax over all source words. Finally, these
probabilities are used to generate a weighted average of the source RNN vectors, ci (another
d-dimensional vector).
An example of an attentional sequence-to-sequence model is given in Figure 25.7 (a).
There are a few important details to understand. First, the attention component itself has no
learned weights and supports variable-length sequences on both the source and target side.
Second, like most of the other neural network modeling techniques we’ve learned about,
attention is entirely latent. The programmer does not dictate what information gets used
when; the model learns what to use. Attention can also be combined with multilayer RNNs.
Typically attention is applied at each layer in that case.
The probabilistic softmax formulation for attention serves three purposes. First, it makes
attention differentiable, which is necessary for it to be used with back-propagation. Even
though attention itself has no learned weights, the gradients still ﬂow back through attention
to the source and target RNNs. Second, the probabilistic formulation allows the model to
capture certain types of long-distance contextualization that may have not been captured by
the source RNN, since attention can consider the entire source sequence at once, and learn to
keep what is important and ignore the rest. Third, probabilistic attention allows the network
to represent uncertainty—if the network does not know exactly what source word to translate
next, it can distribute the attention probabilities over several options, and then actually choose
the word using the target RNN.
Unlike most components of neural networks, attention probabilities are often interpretable
by humans and intuitively meaningful. For example, in the case of machine translation, the
attention probabilities often correspond to the word-to-word alignments that a human would
generate. This is shown in Figure 25.7(b).
Sequence-to-sequence models are a natural for machine translation, but almost any nat-
ural language task can be encoded as a sequence-to-sequence problem.
For example, a
question-answering system can be trained on input consisting of a question followed by a
delimiter followed by the answer.
25.3.2 Decoding
At training time, a sequence-to-sequence model attempts to maximize the probability of each
word in the target training sentence, conditioned on the source and all of the previous target
words. Once training is complete, we are given a source sentence, and our goal is to generate
the corresponding target sentence. As shown in Figure 25.7, we can generate the target one
word at a time, and then feed back in the word that we generated at the next timestep. This
procedure is called decoding.
Decoding
The simplest form of decoding is to select the highest probability word at each timestep
and then feed this word as input to the next timestep. This is called greedy decoding because
Greedy decoding
after each target word is generated, the system has fully committed to the hypothesis that it
has produced so far. The problem is that the goal of decoding is to maximize the probability
of the entire target sequence, which greedy decoding may not achieve. For example, consider
