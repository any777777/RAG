---
chunk_id: "book-ca4fca8dd8-chunk-1325"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1325
confidence: "first-pass"
extraction_method: "structured-local"
---

810
Chapter 22
Deep Learning
way does classical linear regression. The input features to this linear regression are the out-
puts from the preceding layer, which typically result from multiple nonlinear transformations
of the original inputs to the network.
Many other output layers are possible. For example, a mixture density layer represents
Mixture density
the outputs using a mixture of Gaussian distributions. (See Section 21.3.1 for more details on
Gaussian mixtures.) Such layers predict the relative frequency of each mixture component,
the mean of each component, and the variance of each component. As long as these output
values are interpreted appropriately by the loss function as deﬁning the probability for the
true output value y, the network will, after training, ﬁt a Gaussian mixture model in the space
of features deﬁned by the preceding layers.
22.2.3 Hidden layers
During the training process, a neural network is shown many input values x and many corre-
sponding output values y. While processing an input vector x, the neural network performs
several intermediate computations before producing the output y. We can think of the values
computed at each layer of the network as a different representation for the input x. Each
layer transforms the representation produced by the preceding layer to produce a new rep-
resentation. The composition of all these transformations succeeds—if all goes well—in
transforming the input into the desired output. Indeed, one hypothesis for why deep learning
works well is that the complex end-to-end transformation that maps from input to output—
say, from an input image to the output category “giraffe”—is decomposed by the many layers
into the composition of many relatively simple transformations, each of which is fairly easy
to learn by a local updating process.
In the process of forming all these internal transformations, deep networks often discover
meaningful intermediate representations of the data. For example, a network learning to
recognize complex objects in images may form internal layers that detect useful subunits:
edges, corners, ellipses, eyes, faces—cats. Or it may not—deep networks may form internal
layers whose meaning is opaque to humans, even though the output is still correct.
The hidden layers of neural networks are typically less diverse than the output layers.
For the ﬁrst 25 years of research with multilayer networks (roughly 1985–2010), internal
nodes used sigmoid and tanh activation functions almost exclusively. From around 2010
onwards, the ReLU and softplus become more popular, partly because they are believed to
avoid the problem of vanishing gradients mentioned in Section 22.1.2. Experimentation with
increasingly deep networks suggested that, in many cases, better learning was obtained with
deep and relatively narrow networks rather than shallow, wide networks, given a ﬁxed total
number of weights. A typical example of this is shown in Figure 22.7 on page 820.
There are, of course, many other structures to consider for computation graphs, besides
just playing with width and depth. At the time of writing, there is little understanding as
to why some structures seem to work better than others for some particular problem. With
experience, practitioners gain some intuition as to how to design networks and how to ﬁx
them when they don’t work, just as chefs gain intuition for how to design recipes and how
to ﬁx them when they taste unpleasant. For this reason, tools that facilitate rapid exploration
and evaluation of different structures are essential for success in real-world problems.
