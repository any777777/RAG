---
chunk_id: "book-ca4fca8dd8-chunk-1337"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1337
confidence: "first-pass"
extraction_method: "structured-local"
---

816
Chapter 22
Deep Learning
where the penultimate step follows because ReLU(ReLU(x))=ReLU(x). In other words,
in residual nets with ReLU activations, a layer with zero weights simply passes its inputs
through with no change. The rest of the network functions just as if the layer had never
existed. Whereas traditional networks must learn to propagate information and are subject
to catastrophic failure of information propagation for bad choices of the parameters, residual
networks propagate information by default.
Residual networks are often used with convolutional layers in vision applications, but
they are in fact a general-purpose tool that makes deep networks more robust and allows
researchers to experiment more freely with complex and heterogeneous network designs. At
the time of writing, it is not uncommon to see residual networks with hundreds of layers.
The design of such networks is evolving rapidly, so any additional speciﬁcs we might provide
would probably be outdated before reaching printed form. Readers desiring to know the best
architectures for speciﬁc applications should consult recent research publications.
22.4 Learning Algorithms
Training a neural network consists of modifying the network’s parameters so as to minimize
the loss function on the training set. In principle, any kind of optimization algorithm could
be used. In practice, modern neural networks are almost always trained with some variant of
stochastic gradient descent (SGD).
We covered standard gradient descent and its stochastic version in Section 19.6.2. Here,
the goal is to minimize the loss L(w), where w represents all of the parameters of the network.
Each update step in the gradient descent process looks like this:
w ←w−α∇wL(w),
where α is the learning rate. For standard gradient descent, the loss L is deﬁned with respect
to the entire training set. For SGD, it is deﬁned with respect to a minibatch of m examples
chosen randomly at each step.
As noted in Section 4.2, the literature on optimization methods for high-dimensional
continuous spaces includes innumerable enhancements to basic gradient descent. We will
not cover all of them here, but it is worth mentioning a few important considerations that are
particularly relevant to training neural networks:
• For most networks that solve real-world problems, both the dimensionality of w and the
size of the training set are very large. These considerations militate strongly in favor
of using SGD with a relatively small minibatch size m: stochasticity helps the algo-
rithm escape small local minima in the high-dimensional weight space (as in simulated
annealing—see page 132); and the small minibatch size ensures that the computational
cost of each weight update step is a small constant, independent of the training set size.
• Because the gradient contribution of each training example in the SGD minibatch can
be computed independently, the minibatch size is often chosen so as to take maximum
advantage of hardware parallelism in GPUs or TPUs.
• To improve convergence, it is usually a good idea to use a learning rate that decreases
over time. Choosing the right schedule is usually a matter of trial and error.
• Near a local or global minimum of the loss function with respect to the entire training
set, the gradients estimated from small minibatches will often have high variance and
