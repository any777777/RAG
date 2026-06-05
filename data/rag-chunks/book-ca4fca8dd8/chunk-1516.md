---
chunk_id: "book-ca4fca8dd8-chunk-1516"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1516
confidence: "first-pass"
extraction_method: "structured-local"
---

914
Chapter 25
Deep Learning for Natural Language Processing
Training an RNN to do classiﬁcation like this is done the same way as with the language
model. The only difference is that the training data will require labels—part of speech tags
or reference indications. That makes it much harder to collect the data than for the case of a
language model, where unlabelled text is all we need.
In a language model we want to predict the nth word given the previous words. But for
classiﬁcation, there is no reason we should limit ourselves to looking at only the previous
words. It can be very helpful to look ahead in the sentence. In our coreference example, the
referent him would be different if the sentence concluded “to see Miguel” rather than “to the
hospital,” so looking ahead is crucial. We know from eye-tracking experiments that human
readers do not go strictly left-to-right.
To capture the context on the right, we can use a bidirectional RNN, which concatenates
Bidirectional RNN
a separate right-to-left model onto the left-to-right model. An example of using a bidirectional
RNN for POS tagging is shown in Figure 25.5.
In the case of a multilayer RNN, zt will be the hidden vector of the last layer. For a
bidirectional RNN, zt is usually taken to be the concatenation of vectors from the left-to-right
and right-to-left models.
RNNs can also be used for sentence-level (or document-level) classiﬁcation tasks, in
which a single output comes at the end, rather than having a stream of outputs, one per
time step. For example in sentiment analysis the goal is to classify a text as having either
Positive or Negative sentiment. For example, “This movie was poorly written and poorly
acted” should be classiﬁed as Negative. (Some sentiment analysis schemes use more than
two categories, or use a numeric scalar value.)
Using RNNs for a sentence-level task is a bit more complex, since we need to obtain
an aggregate whole-sentence representation, y from the per-word outputs yt of the RNN.
The simplest way to do this is to use the RNN hidden state corresponding to the last word
of the input, since the RNN will have read the entire sentence at that timestep. However,
this can implicitly bias the model towards paying more attention to the end of the sentence.
Another common technique is to pool all of the hidden vectors. For instance, average pooling
Average pooling
computes the element-wise average over all of the hidden vectors:
˜z = 1
s
s
∑
t =1
zt .
The pooled d-dimensional vector ˜z can then be fed into one or more feedforward layers before
being fed into the output layer.
25.2.3 LSTMs for NLP tasks
We said that RNNs sometimes solve the limited context problem. In theory, any information
could be passed along from one hidden layer to the next for any number of time steps. But
in practice the information can get lost or distorted, just as in playing the game of telephone,
in which players stand in line and the ﬁrst player whispers a message to the second, who
repeats it to the third, and so on down the line. Usually, the message that comes out at the
end is quite corrupted from the original message. This problem for RNNs is similar to the
vanishing gradient problem we described on page 807, except that we are dealing now with
layers over time rather than with deep layers.
In Section 22.6.2 we introduced the long short-term memory (LSTM) model. This is a
kind of RNN with gating units that don’t suffer from the problem of imperfectly reproducing
