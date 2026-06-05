---
chunk_id: "book-ca4fca8dd8-chunk-1313"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1313
confidence: "first-pass"
extraction_method: "structured-local"
---

CHAPTER 22
DEEP LEARNING
In which gradient descent learns multistep programs, with signiﬁcant implications for the
major subﬁelds of artiﬁcial intelligence.
Deep learning is a broad family of techniques for machine learning in which hypotheses
Deep learning
take the form of complex algebraic circuits with tunable connection strengths. The word
“deep” refers to the fact that the circuits are typically organized into many layers, which
Layer
means that computation paths from inputs to outputs have many steps. Deep learning is
currently the most widely used approach for applications such as visual object recognition,
machine translation, speech recognition, speech synthesis, and image synthesis; it also plays
a signiﬁcant role in reinforcement learning applications (see Chapter 23).
Deep learning has its origins in early work that tried to model networks of neurons in
the brain (McCulloch and Pitts, 1943) with computational circuits. For this reason, the net-
works trained by deep learning methods are often called neural networks, even though the
Neural network
resemblance to real neural cells and structures is superﬁcial.
While the true reasons for the success of deep learning have yet to be fully elucidated,
it has self-evident advantages over some of the methods covered in Chapter 19—particularly
for high-dimensional data such as images. For example, although methods such as linear
and logistic regression can handle a large number of input variables, the computation path
from each input to the output is very short: multiplication by a single weight, then adding
into the aggregate output. Moreover, the different input variables contribute independently to
the output, without interacting with each other (Figure 22.1(a)). This signiﬁcantly limits the
expressive power of such models. They can represent only linear functions and boundaries in
the input space, whereas most real-world concepts are far more complex.
Decision lists and decision trees, on the other hand, allow for long computation paths that
can depend on many input variables—but only for a relatively small fraction of the possible
input vectors (Figure 22.1(b)). If a decision tree has long computation paths for a signiﬁcant
fraction of the possible inputs, it must be exponentially large in the number of input variables.
The basic idea of deep learning is to train circuits such that the computation paths are long,
allowing all the input variables to interact in complex ways (Figure 22.1(c)). These circuit
models turn out to be sufﬁciently expressive to capture the complexity of real-world data for
many important kinds of learning problems.
Section 22.1 describes simple feedforward networks, their components, and the essentials
of learning in such networks. Section 22.2 goes into more detail on how deep networks
are put together, and Section 22.3 covers a class of networks called convolutional neural
networks that are especially important in vision applications. Sections 22.4 and 22.5 go
into more detail on algorithms for training networks from data and methods for improving
