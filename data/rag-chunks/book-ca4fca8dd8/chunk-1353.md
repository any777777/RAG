---
chunk_id: "book-ca4fca8dd8-chunk-1353"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1353
confidence: "first-pass"
extraction_method: "structured-local"
---

824
Chapter 22
Deep Learning
Δ
Figure 22.8 (a) Schematic diagram of a basic RNN where the hidden layer z has recurrent
connections; the ∆symbol indicates a delay. (b) The same network unrolled over three time
steps to create a feedforward network. Note that the weights are shared across all time steps.
the computation. (Without the delay, a cyclic circuit may reach an inconsistent state.) This
allows the RNN to have internal state, or memory: inputs received at earlier time steps affect
Memory
the RNN’s response to the current input.
RNNs can also be used to perform more general computations—after all, ordinary com-
puters are just Boolean circuits with memory—and to model real neural systems, many of
which contain cyclic connections. Here we focus on the use of RNNs to analyze sequential
data, where we assume that a new input vector xt arrives at each time step.
As tools for analyzing sequential data, RNNs can be compared to the hidden Markov
models, dynamic Bayesian networks, and Kalman ﬁlters described in Chapter 14. (The reader
may ﬁnd it helpful to refer back to that chapter before proceeding.) Like those models, RNNs
make a Markov assumption (see page 481): the hidden state zt of the network sufﬁces
to capture the information from all previous inputs. Furthermore, suppose we describe the
RNN’s update process for the hidden state by the equation zt = fw(zt−1,xt) for some param-
eterized function fw. Once trained, this function represents a time-homogeneous process
(page 481)—effectively a universally quantiﬁed assertion that the dynamics represented by
fw hold for all time steps. Thus, RNNs add expressive power compared to feedforward net-
works, just as convolutional networks do, and just as dynamic Bayes nets add expressive
power compared to regular Bayes nets. Indeed, if you tried to use a feedforward network
to analyze sequential data, the ﬁxed size of the input layer would force the network to ex-
amine only a ﬁnite-length window of data, in which case the network would fail to detect
long-distance dependencies.
22.6.1 Training a basic RNN
The basic model we will consider has an input layer x, a hidden layer z with recurrent con-
nections, and an output layer y, as shown in Figure 22.8(a). We assume that both x and y are
observed in the training data at each time step. The equations deﬁning the model refer to the
values of the variables indexed by time step t:
zt = fw(zt−1,xt) = gz(Wz,zzt−1 +Wx,zxt) ≡gz(inz,t)
ˆyt = gy(Wz,yzt) ≡gy(iny,t),
(22.13)
