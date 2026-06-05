---
chunk_id: "book-ca4fca8dd8-chunk-1343"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1343
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.5
Generalization
819
22.4.2 Batch normalization
Batch normalization is a commonly used technique that improves the rate of convergence of
Batch normalization
SGD by rescaling the values generated at the internal layers of the network from the examples
within each minibatch. Although the reasons for its effectiveness are not well understood at
the time of writing, we include it because it confers signiﬁcant beneﬁts in practice. To some
extent, batch normalization seems to have effects similar to those of the residual network.
Consider a node z somewhere in the network: the values of z for the m examples in a
minibatch are z1,...,zm. Batch normalization replaces each zi with a new quantity ˆzi:
ˆzi = γ zi −µ
√
ϵ+σ2 +β ,
where µ is the mean value of z across the minibatch, σ is the standard deviation of z1,...,zm,
ϵ is a small constant added to prevent division by zero, and γ and β are learned parameters.
Batch normalization standardizes the mean and variance of the values, as determined by
the values of β and γ. This makes it much simpler to train a deep network. Without batch
normalization, information can get lost if a layer’s weights are too small, and the standard
deviation at that layer decays to near zero. Batch normalization prevents this from happening.
It also reduces the need for careful initialization of all the weights in the network to make sure
that the nodes in each layer are in the right operating region to allow information to propagate.
With batch normalization, we usually include β and γ, which may be node-speciﬁc or
layer-speciﬁc, among the parameters of the network, so that they are included in the learning
process. After training, β and γ are ﬁxed at their learned values.
22.5 Generalization
So far we have described how to ﬁt a neural network to its training set, but in machine learn-
ing the goal is to generalize to new data that has not been seen previously, as measured by
performance on a test set. In this section, we focus on three approaches to improving gener-
alization performance: choosing the right network architecture, penalizing large weights, and
randomly perturbing the values passing through the network during training.
22.5.1 Choosing a network architecture
A great deal of effort in deep learning research has gone into ﬁnding network architectures
that generalize well. Indeed, for each particular kind of data—images, speech, text, video,
and so on—a good deal of the progress in performance has come from exploring different
kinds of network architectures and varying the number of layers, their connectivity, and the
types of node in each layer.6
Some neural network architectures are explicitly designed to generalize well on particular
types of data: convolutional networks encode the idea that the same feature extractor is useful
at all locations across a spatial grid, and recurrent networks encode the idea that the same
update rule is useful at all points in a stream of sequential data. To the extent that these
assumptions are valid, we expect convolutional architectures to generalize well on images
and recurrent networks to generalize well on text and audio signals.
6
Noting that much of this incremental, exploratory work is carried out by graduate students, some have called
the process graduate student descent (GSD).
