---
chunk_id: "book-ca4fca8dd8-chunk-1351"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1351
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.6
Recurrent Neural Networks
823
22.5.4 Dropout
Another way that we can intervene to reduce the test-set error of a network—at the cost of
making it harder to ﬁt the training set—is to use dropout. At each step of training, dropout
Dropout
applies one step of back-propagation learning to a new version of the network that is created
by deactivating a randomly chosen subset of the units. This is a rough and very low-cost
approximation to training a large ensemble of different networks (see Section 19.8).
More speciﬁcally, let us suppose we are using stochastic gradient descent with minibatch
size m. For each minibatch, the dropout algorithm applies the following process to every
node in the network: with probability p, the unit output is multiplied by a factor of 1/p;
otherwise, the unit output is ﬁxed at zero. Dropout is typically applied to units in the hidden
layers with p=0.5; for input units, a value of p=0.8 turns out to be most effective. This
process produces a thinned network with about half as many units as the original, to which
back-propagation is applied with the minibatch of m training examples. The process repeats
in the usual way until training is complete. At test time, the model is run with no dropout.
We can think of dropout from several perspectives:
• By introducing noise at training time, the model is forced to become robust to noise.
• As noted above, dropout approximates the creation of a large ensemble of thinned net-
works. This claim can be veriﬁed analytically for linear models, and appears to hold
experimentally for deep learning models.
• Hidden units trained with dropout must learn not only to be useful hidden units; they
must also learn to be compatible with many other possible sets of other hidden units
that may or may not be included in the full model. This is similar to the selection
processes that guide the evolution of genes: each gene must not only be effective in its
own function, but must work well with other genes, whose identity in future organisms
may vary considerably.
• Dropout applied to later layers in a deep network forces the ﬁnal decision to be made
robustly by paying attention to all of the abstract features of the example rather than
focusing on just one and ignoring the others. For example, a classiﬁer for animal images
might be able to achieve high performance on the training set just by looking at the
animal’s nose, but would presumably fail on a test case where the nose was obscured or
damaged. With dropout, there will be training cases where the internal “nose unit” is
zeroed out, causing the learning process to ﬁnd additional identifying features. Notice
that trying to achieve the same degree of robustness by adding noise to the input data
would be difﬁcult: there is no easy way to know in advance that the network is going to
focus on noses, and no easy way to delete noses automatically from each image.
Altogether, dropout forces the model to learn multiple, robust explanations for each input.
This causes the model to generalize well, but also makes it more difﬁcult to ﬁt the training
set—it is usually necessary to use a larger model and to train it for more iterations.
22.6 Recurrent Neural Networks
Recurrent neural networks (RNNs) are distinct from feedforward networks in that they allow
cycles in the computation graph. In all the cases we will consider, each cycle has a delay,
so that units may take as input a value computed from their own output at an earlier step in
