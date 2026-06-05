---
chunk_id: "book-ca4fca8dd8-chunk-1357"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1357
confidence: "first-pass"
extraction_method: "structured-local"
---

826
Chapter 22
Deep Learning
22.6.2 Long short-term memory RNNs
Several specialized RNN architectures have been designed with the goal of enabling informa-
tion to be preserved over many time steps. One of the most popular is the long short-term
memory or LSTM. The long-term memory component of an LSTM, called the memory cell
Long short-term
memory
Memory cell
and denoted by c, is essentially copied from time step to time step. (In contrast, the basic RNN
multiplies its memory by a weight matrix at every time step, as shown in Equation (22.13).)
New information enters the memory by adding updates; in this way, the gradient expressions
do not accumulate multiplicatively over time. LSTMs also include gating units, which are
Gating unit
vectors that control the ﬂow of information in the LSTM via elementwise multiplication of
the corresponding information vector:
• The forget gate f determines if each element of the memory cell is remembered (copied
Forget gate
to the next time step) or forgotten (reset to zero).
• The input gate i determines if each element of the memory cell is updated additively
Input gate
by new information from the input vector at the current time step.
• The output gate o determines if each element of the memory cell is transferred to the
Output gate
short-term memory z, which plays a similar role to the hidden state in basic RNNs.
Whereas the word “gate” in circuit design usually connotes a Boolean function, gates in
LSTMs are soft—for example, elements of the memory cell vector will be partially forgotten
if the corresponding elements of the forget-gate vector are small but not zero. The values for
the gating units are always in the range [0,1] and are obtained as the outputs of a sigmoid
function applied to the current input and the previous hidden state. In detail, the update
equations for the LSTM are as follows:
ft = σ(Wx,f xt +Wz,f zt−1)
it = σ(Wx,ixt +Wz,izt−1)
ot = σ(Wx,oxt +Wz,ozt−1)
ct = ct−1 ⊙ft +it ⊙tanh(Wx,cxt +Wz,czt−1)
zt = tanh(ct)⊙ot ,
where the subscripts on the various weight matrices W indicate the origin and destination of
the corresponding links. The ⊙symbol denotes elementwise multiplication.
LSTMs were among the ﬁrst practically usable forms of RNN. They have demonstrated
excellent performance on a wide range of tasks including speech recognition and handwriting
recognition. Their use in natural language processing is discussed in Chapter 25.
22.7 Unsupervised Learning and Transfer Learning
The deep learning systems we have discussed so far are based on supervised learning, which
requires each training example to be labeled with a value for the target function. Although
such systems can reach a high level of test-set accuracy—as shown by the ImageNet com-
petition results, for example—they often require far more labeled data than a human would
for the same task. For example, a child needs to see only one picture of a giraffe, rather
than thousands, in order to be able to recognize giraffes reliably in a wide range of settings
and views. Clearly, something is missing in our deep learning story; indeed, it may be the
