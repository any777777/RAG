---
chunk_id: "book-ca4fca8dd8-chunk-1335"
source_id: "book-ca4fca8dd8"
source_file: "book.pdf"
source_type: "pdf"
topics:
  - "References and Textbooks"
chunk_index: 1335
confidence: "first-pass"
extraction_method: "structured-local"
---

Section 22.3
Convolutional Networks
815
dimensional tensor of size 256×256×3×64. Then we apply 96 kernels of size 5×5×3
with a stride of 2 in both x and y directions in the image. This gives an output tensor of size
128×128×96×64. Such a tensor is often called a feature map, since it shows how each
Feature map
feature extracted by a kernel appears across the entire image; in this case it is composed of
96 channels, where each channel carries information from one feature. Notice that unlike the
Channel
input tensor, this feature map no longer has dedicated color channels; nonetheless, the color
information may still be present in the various feature channels if the learning algorithm ﬁnds
color to be useful for the ﬁnal predictions of the network.
22.3.3 Residual networks
Residual networks are a popular and successful approach to building very deep networks
Residual network
that avoid the problem of vanishing gradients.
Typical deep models use layers that learn a new representation at layer i by completely re-
placing the representation at layer i−1. Using the matrix–vector notation that we introduced
in Equation (22.3), with z(i) being the values of the units in layer i, we have
z(i) = f(z(i−1)) = g(i)(W(i)z(i−1)).
Because each layer completely replaces the representation from the preceding layer, all of
the layers must learn to do something useful. Each layer must, at the very least, preserve the
task-relevant information contained in the preceding layer. If we set W(i) = 0 for any layer i,
the entire network ceases to function. If we also set W(i−1) = 0, the network would not even
be able to learn: layer i would not learn because it would observe no variation in its input
from layer i−1, and layer i−1 would not learn because the back-propagated gradient from
layer i would always be zero. Of course, these are extreme examples, but they illustrate the
need for layers to serve as conduits for the signals passing through the network.
The key idea of residual networks is that a layer should perturb the representation from
the previous layer rather than replace it entirely. If the learned perturbation is small, the next
layer is close to being a copy of the previous layer. This is achieved by the following equation
for layer i in terms of layer i−1:
z(i) = g(i)
r (z(i−1) + f(z(i−1))),
(22.10)
where gr denotes the activation functions for the residual layer. Here we think of f as the
residual, perturbing the default behavior of passing layer i−1 through to layer i. The function
Residual
used to compute the residual is typically a neural network with one nonlinear layer combined
with one linear layer:
f(z) = Vg(Wz),
where W and V are learned weight matrices with the usual bias weights added.
Residual networks make it possible to learn signiﬁcantly deeper networks reliably. Con-
sider what happens if we set V=0 for a particular layer in order to disable that layer. Then
the residual f disappears and Equation (22.10) simpliﬁes to
z(i) = gr(z(i−1)).
Now suppose that gr consists of ReLU activation functions and that z(i−1) also applies a ReLU
function to its inputs: z(i−1) =ReLU(in(i−1)). In that case we have
z(i) = gr(z(i−1)) = ReLU(z(i−1)) = ReLU(ReLU(in(i−1))) = ReLU(in(i−1)) = z(i−1) ,
