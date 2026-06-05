---
chunk_id: "book-ca4fca8dd8-chunk-1323"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1323
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.2
Computation Graphs for Deep Learning
809
In the deep learning literature, it is common to talk about minimizing the cross-entropy
Cross-entropy
loss. Cross-entropy, written as H(P,Q), is a kind of measure of dissimilarity between two
distributions P and Q.2 The general deﬁnition is
H(P,Q) = Ez∼P(z)[logQ(z)] =
Z
P(z)logQ(z)dz.
(22.7)
In machine learning, we typically use this deﬁnition with P being the true distribution over
training examples, P∗(x,y), and Q being the predictive hypothesis Pw(y|x). Minimizing the
cross-entropy H(P∗(x,y),Pw(y|x)) by adjusting w makes the hypothesis agree as closely as
possible with the true distribution. In reality, we cannot minimize this cross-entropy because
we do not have access to the true data distribution P∗(x,y); but we do have access to samples
from P∗(x,y), so the sum over the actual data in Equation (22.6) approximates the expectation
in Equation (22.7).
To minimize the negative log likelihood (or the cross-entropy), we need to be able to
interpret the output of the network as a probability. For example, if the network has one
output unit with a sigmoid activation function and is learning a Boolean classiﬁcation, we can
interpret the output value directly as the probability that the example belongs to the positive
class. (Indeed, this is exactly how logistic regression is used; see page 702.) Thus, for
Boolean classiﬁcation problems, we commonly use a sigmoid output layer.
Multiclass classiﬁcation problems are very common in machine learning. For example,
classiﬁers used for object recognition often need to recognize thousands of distinct categories
of objects. Natural language models that try to predict the next word in a sentence may have
to choose among tens of thousands of possible words. For this kind of prediction, we need
the network to output a categorical distribution—that is, if there are d possible answers, we
need d output nodes that represent probabilities summing to 1.
To achieve this, we use a softmax layer, which outputs a vector of d values given a vector
Softmax
of input values in=⟨in1,...,ind⟩. The kth element of that output vector is given by
softmax(in)k =
eink
∑d
k′ =1 eink′ .
By construction, the softmax function outputs a vector of nonnegative numbers that sum to 1.
As usual, the input ink to each of the output nodes will be a weighted linear combination of
the outputs of the preceding layer. Because of the exponentials, the softmax layer accentuates
differences in the inputs: for example, if the vector of inputs is given by in=⟨5,2,0,−2⟩, then
the outputs are ⟨0.946,0.047,0.006,0.001⟩. The softmax, is, nonetheless, smooth and differ-
entiable (Exercise 22.SOFG), unlike the max function. It is easy to show (Exercise 22.SMSG)
that the sigmoid is a softmax with d =2. In other words, just as sigmoid units propagate
binary class information through a network, softmax units propagate multiclass information.
For a regression problem, where the target value y is continuous, it is common to use a
linear output layer—in other words, ˆyj =in j, without any activation function g—and to inter-
pret this as the mean of a Gaussian prediction with ﬁxed variance. As we noted on page 780,
maximizing likelihood (i.e., minimizing negative log likelihood) with a ﬁxed-variance Gaus-
sian is the same as minimizing squared error. Thus, a linear output layer interpreted in this
2
Cross-entropy is not a distance in the usual sense because H(P,P) is not zero; rather, it equals the entropy
H(P). It is easy to show that H(P,Q) = H(P) + DKL(P∥Q), where DKL is the Kullback–Leibler divergence,
which does satisfy DKL(P∥P)=0. Thus, for ﬁxed P, varying Q to minimize the cross-entropy also minimizes the
KL divergence.
